from __future__ import annotations

import hashlib
import math
import os
import socket
import statistics
import tempfile
import threading
import time
from collections.abc import Callable
from contextlib import contextmanager

from rich.console import Console
from rich.table import Table


def read_exact(connection: socket.socket, size: int) -> bytes:
    chunks = bytearray()
    while len(chunks) < size:
        chunk = connection.recv(size - len(chunks))
        if not chunk:
            raise ConnectionError("localhost echo server closed the connection")
        chunks.extend(chunk)
    return bytes(chunks)


@contextmanager
def localhost_echo() -> socket.socket:
    payload_size = 64
    stop_payload = b"\xff" * payload_size
    server_errors: list[OSError] = []
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)

    def serve() -> None:
        try:
            connection, _ = listener.accept()
            with connection:
                while True:
                    payload = read_exact(connection, payload_size)
                    if payload == stop_payload:
                        return
                    connection.sendall(payload)
        except OSError as error:
            server_errors.append(error)
        finally:
            listener.close()

    server = threading.Thread(target=serve, name="localhost-echo", daemon=True)
    server.start()
    try:
        client = socket.create_connection(listener.getsockname(), timeout=5)
    except OSError:
        listener.close()
        server.join(timeout=5)
        raise
    client.settimeout(5)
    try:
        yield client
    finally:
        cleanup_error: OSError | None = None
        try:
            client.sendall(stop_payload)
        except OSError as error:
            cleanup_error = error
        client.close()
        server.join(timeout=5)
        if server.is_alive():
            raise TimeoutError("localhost echo server did not stop")
        if server_errors:
            raise RuntimeError("localhost echo server failed") from server_errors[0]
        if cleanup_error:
            raise RuntimeError("could not stop localhost echo server") from cleanup_error


def measure(
    operation: Callable[[], object],
    iterations: int,
    repeats: int = 5,
) -> tuple[float, float]:
    operation()
    batch_averages_ns: list[float] = []
    for _ in range(repeats):
        started = time.perf_counter_ns()
        for _ in range(iterations):
            operation()
        elapsed_ns = time.perf_counter_ns() - started
        batch_averages_ns.append(elapsed_ns / iterations)

    ordered = sorted(batch_averages_ns)
    p95_index = max(0, math.ceil(0.95 * len(ordered)) - 1)
    return statistics.median(ordered), ordered[p95_index]


def format_latency(nanoseconds: float) -> str:
    if nanoseconds >= 1_000_000:
        return f"{nanoseconds / 1_000_000:.3f} ms"
    if nanoseconds >= 1_000:
        return f"{nanoseconds / 1_000:.3f} us"
    return f"{nanoseconds:.1f} ns"


def main() -> None:
    console = Console()
    results: list[tuple[str, int, float, float, str]] = []

    values = list(range(1024))
    index = 0

    def read_python_list() -> int:
        nonlocal index
        index = (index + 1) & 1023
        return values[index]

    results.append(
        (
            "1. RAM Lookup (Python list index)",
            100_000,
            *measure(read_python_list, 100_000),
            "Baseline (1.0x)",
        )
    )
    baseline_ns = results[0][2]

    hash_payload = b"x" * 4096
    med_hash, p95_hash = measure(lambda: hashlib.sha256(hash_payload).digest(), 5_000)
    results.append(
        (
            "2. CPU Compute (SHA-256 on 4 KiB)",
            5_000,
            med_hash,
            p95_hash,
            f"{med_hash / baseline_ns:,.1f}x slower",
        )
    )

    with tempfile.TemporaryDirectory(prefix="latency-lab-") as directory:
        buffered_path = os.path.join(directory, "page-cache-benchmark.bin")
        with open(buffered_path, "wb", buffering=0) as buffered_file:
            def write_page_cache_only() -> None:
                buffered_file.seek(0)
                buffered_file.write(b"x" * 128)

            med_buf, p95_buf = measure(write_page_cache_only, 5_000)
            results.append(
                (
                    "3. OS Page Cache Write (No fsync)",
                    5_000,
                    med_buf,
                    p95_buf,
                    f"{med_buf / baseline_ns:,.1f}x slower",
                )
            )

        payload = b"l" * 64
        with localhost_echo() as client:

            def localhost_round_trip() -> None:
                client.sendall(payload)
                if read_exact(client, len(payload)) != payload:
                    raise RuntimeError("localhost echo returned an unexpected payload")

            med_tcp, p95_tcp = measure(localhost_round_trip, 1_000)
            results.append(
                (
                    "4. TCP Loopback RTT (64 B)",
                    1_000,
                    med_tcp,
                    p95_tcp,
                    f"{med_tcp / baseline_ns:,.1f}x slower",
                )
            )

        file_path = os.path.join(directory, "fsync-benchmark.bin")
        with open(file_path, "wb", buffering=0) as file:
            def write_and_fsync() -> None:
                file.seek(0)
                file.write(b"x" * 128)
                os.fsync(file.fileno())

            med_fsync, p95_fsync = measure(write_and_fsync, 30)
            results.append(
                (
                    "5. Durable Disk Write (write + fsync)",
                    30,
                    med_fsync,
                    p95_fsync,
                    f"{med_fsync / baseline_ns:,.0f}x slower",
                )
            )

    table = Table(title="Lesson 1.1 Empirical Hardware & OS Boundary Benchmark")
    table.add_column("Operation / Boundary Crossed", style="cyan")
    table.add_column("Iterations", justify="right")
    table.add_column("Median Latency", justify="right", style="bold green")
    table.add_column("P95 Batch Latency", justify="right", style="yellow")
    table.add_column("Serial Ceiling (ops/s)", justify="right", style="bold magenta")
    table.add_column("Relative Penalty", justify="right", style="red")

    for name, iterations, median_ns, p95_ns, penalty in results:
        throughput = 1_000_000_000 / median_ns
        table.add_row(
            name,
            f"{iterations:,}",
            format_latency(median_ns),
            format_latency(p95_ns),
            f"{throughput:,.0f}",
            penalty,
        )

    console.print(table)
    console.print(
        f"\n[bold yellow]Key Architect Insight:[/bold yellow] Writing to the OS Page Cache took "
        f"[bold green]{format_latency(med_buf)}[/bold green], whereas forcing durability via "
        f"[bold red]os.fsync()[/bold red] took [bold red]{format_latency(med_fsync)}[/bold red] "
        f"([bold]{med_fsync / med_buf:,.0f}x slower![/bold]). This is why databases use "
        f"Group Commit and why Kafka relies on OS Page Cache + replication instead of per-message fsync."
    )


if __name__ == "__main__":
    main()
