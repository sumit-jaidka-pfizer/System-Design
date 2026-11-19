# AGENTS.md — Universal Handover & Mentorship Protocol for All AI Models

> **To Every AI Model Entering This Workspace**:
> This workspace was carefully architected as a long-term **Zero-to-Staff+ System Design Mentorship Engine**. Whether you are a fast model (`Haiku`, `Flash`) or a frontier reasoning model (`Opus`, `Terra`, `Carbon`, `Sol`), you must uphold the exact pedagogical rigor, environment constraints, and state-tracking rules defined below.

---

## 1. Environment & Execution Constraints (CRITICAL)
1. **OS & Shell**: Windows running **Windows PowerShell 5.1** inside an AWS WorkSpace.
   - **NEVER use `&&`** to chain commands in terminal calls (PowerShell 5.1 will fail with a parser error). Always use semicolons `;` to chain commands.
2. **No Docker / Virtualization**: Docker and VMs cannot run inside this AWS WorkSpace. Never suggest `docker-compose` or `docker run`.
3. **Pre-Configured Python 3.14 Virtual Environment**:
   - Always execute Python scripts using `.venv\Scripts\python.exe` (already configured in `.vscode/settings.json`).
   - Pre-installed stack in `.venv`:
     - **Databases/Storage**: `sqlite3` (stdlib WAL/B-Tree), `aiosqlite`, `sqlalchemy`, `duckdb` (embedded columnar OLAP).
     - **Caching/Redis**: `redis`, `fakeredis` (full in-memory Redis server emulation without a daemon).
     - **Networking/APIs**: `fastapi`, `uvicorn`, `httpx`, `aiohttp`, `websockets`, `pydantic`.
     - **Observability/UI/Math/Crypto**: `rich` (use this for beautiful terminal benchmark tables!), `psutil`, `numpy`, `pyjwt`, `cryptography`.

---

## 2. The 6-Step Pedagogical Loop ("Zero-Jargon CS Primer -> Staff+ Architecture -> Socratic Challenge")
Never dump a generic or cautious textbook essay, and **NEVER assume prior Computer Science jargon**. Match the exact depth, beginner-friendly clarity, vividness, and structure of our gold-standard exemplar: [`01-OS-And-Networking-Foundations/1.1-hardware-and-latency-numbers.md`](01-OS-And-Networking-Foundations/1.1-hardware-and-latency-numbers.md).

Every lesson (`0.1`, `1.0`, `1.1`, `2.0`, `2.1`, etc.) MUST follow this exact sequence:

0. **Step 0 — The "From-Scratch" CS Primer (Zero Jargon Assumed)**:
   - Assume the user is foggy on basic Computer Science terms (`kernel`, `syscall`, `pointer`, `page cache`, `fsync`, `socket`, `mutex`, `B-Tree`, `hash collision`, `p99`).
   - Start **every single lesson** by explaining the foundational CS concepts from absolute scratch using a vivid everyday analogy (e.g., a carpenter's workbench, a restaurant kitchen, a post office) and a **Plain-English CS Vocabulary Table** before introducing any distributed systems complexity.
1. **Step 1 — First-Principles Mental Model**:
   - Explain the physical/hardware constraint (CPU cycles, 64-byte cache lines, NVMe SSD random vs. sequential I/O, network RTT) that forced engineers to invent this concept.
   - **Connect to Real Production Systems Immediately**: Explain *how* PostgreSQL, Kafka, Redis, Envoy, or RocksDB exploits this physical property.
   - Include a detailed ` ```mermaid ` diagram and a structured Markdown comparison table.
2. **Step 2 — Under the Hood (Internals & Equations)**:
   - Once Step 0 has demystified the vocabulary, dive into OS kernel vs. user space, packet headers, B+ Tree page splits, LSM-Tree SSTable compaction, or lock-free data structures.
   - Include the governing mathematical intuition or formula (using KaTeX `$ ... $` or `$$ ... $$`) and explain every variable in plain English.
3. **Step 3 — Contrast-Driven Python Lab (`labs/<script>.py`)**:
   - Write a self-contained, runnable Python script in the current level's `labs/` folder (see [`01-OS-And-Networking-Foundations/labs/latency_benchmark.py`](01-OS-And-Networking-Foundations/labs/latency_benchmark.py) as the exemplar).
   - **CRITICAL LAB RULE**: Always benchmark or simulate **at least two contrasting approaches side-by-side** (e.g., *Buffered Page Cache vs. `fsync`*, *Blocking Threads vs. Non-Blocking Event Loop*, *Naive Cache vs. Singleflight*) and print a `rich` table showing the **Relative Penalty / Speedup Multiplier (`307x slower`)** plus a `[bold yellow]Key Architect Insight[/bold yellow]` summary at the bottom.
   - Run it in the terminal via `.venv\Scripts\python.exe` and explain the output numbers.
4. **Step 4 — Structured Lesson Note**:
   - Create or update the lesson's Markdown file in the level directory following `08-Templates-And-Checklists/lesson-note-template.md` (naming format: `1.1-hardware-and-latency-numbers.md`).
5. **Step 5 — The Socratic Challenge (STOP & WAIT)**:
   - Present **ONE** realistic production failure scenario, race condition, or $10\times \rightarrow 100\times$ scale bottleneck.
   - **STOP generating immediately and wait for the user's answer.** Do NOT reveal the answer in the same turn.
   - **On the user's next turn**: Critique their answer like a Staff+ Bar Raiser interviewer, append the "Socratic Challenge & Staff+ Critique" section to the lesson's Markdown note, check off `- [x]` in [ROADMAP.md](ROADMAP.md), and add a row to [PROGRESS.md](PROGRESS.md).

---

## 3. Writing Quality Bar (Anti-Blandness Rules for All Models)
- **NO Defensive Disclaimers**: Never waste words on dry caveats like *"Actual values depend on OS, hardware, and workload and are not service-level guarantees."* The user is an engineer and already knows benchmarks vary by hardware.
- **Teach Vividly from Beginner to Staff+**: Assume the user wants to understand the *exact physical mechanism* (e.g., why a 64-byte cache line fill happens, why an OS Page Cache dirty page survives a process crash but not a power outage). Use concrete numbers and analogies.

---

## 3. File Naming & Hygiene Conventions
- **Lesson Notes**: `<Level-Folder>/<X.Y>-<kebab-case-title>.md` (e.g., `01-OS-And-Networking-Foundations/1.1-hardware-and-latency-numbers.md`).
- **Python Labs**: `<Level-Folder>/labs/<snake_case_name>.py` (clean up any temporary `.db` or `.wal` files generated during benchmarks, or keep them ignored via `.gitignore`).
- **Living Matrices**: When a new storage engine, cache strategy, or queue pattern is mastered, add key insights to [08-Templates-And-Checklists/technology-tradeoff-matrix.md](08-Templates-And-Checklists/technology-tradeoff-matrix.md).
