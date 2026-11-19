---
name: python-lab
description: Build a pure-Python simulation of a distributed systems algorithm or component (No Docker required).
disable-model-invocation: true
---
Build a clean, self-contained, runnable Python 3 script (using standard library `asyncio`, `socket`, `threading`, `sqlite3`, `hashlib`, `time`, etc.) in the relevant `labs/` directory to simulate the requested distributed system component or algorithm.
Requirements:
1. Include clear docstrings explaining how the code maps to real-world production systems (e.g., how our Python class maps to Envoy, Redis, RocksDB, or Kafka).
2. Include a `if __name__ == "__main__":` simulation block that prints visual metrics (latency, throughput, shard distribution, or failure recovery) to the terminal.
3. Run the script in the terminal to verify it works and ask me a Socratic question about the output.
