---
mode: agent
description: Run a Spiral Capstone Boss Fight (1.6, 2.6, 3.7, 4.6) to evolve an end-to-end architecture and benchmark it.
---
Consult [ROADMAP.md](../../ROADMAP.md), [PROGRESS.md](../../PROGRESS.md), and [AGENTS.md](../../AGENTS.md) for the requested Spiral Capstone Boss Fight (`1.6`, `2.6`, `3.7`, or `4.6`).

Run this interactive 3-stage Boss Fight:
1. **Stage 1 — The Production Crisis Brief**:
   - Present a concrete startup scenario hitting a wall as traffic scales $100\times$ (include current RPS, payload sizes, SLA requirements, and symptoms like $p99$ latency spikes or DB lock contention).
   - Ask me to propose my architectural redesign using the concepts from this Level. **Stop and wait for my design.**
2. **Stage 2 — Chaos Injection & Staff+ Pushback**:
   - Critique my initial design, inject a realistic chaos event (e.g., hot shard/celebrity key, network partition, retry storm, or WAL fsync bottleneck), and ask how I modify the architecture to survive it.
3. **Stage 3 — Python Benchmark Proof & Scorecard**:
   - Build and run a capstone Python simulation in the level's `labs/` folder (using `.venv\Scripts\python.exe` and `rich`) proving the "Before vs. After" throughput/latency improvement.
   - Document the capstone architecture in the level folder and mark the Boss Fight complete in [ROADMAP.md](../../ROADMAP.md) and [PROGRESS.md](../../PROGRESS.md).
