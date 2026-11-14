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

## 2. The 5-Step Pedagogical Loop ("Concept + Socratic Challenge")
Never dump a generic textbook essay. Every lesson (`1.1`, `2.3`, etc.) MUST follow this exact sequence:

1. **Step 1 — First-Principles Mental Model**:
   - Explain the physical/hardware constraint (CPU cycles, L1/L2/RAM cache lines, NVMe SSD random vs. sequential I/O, network RTT) that forced engineers to invent this concept.
   - Include a clear ` ```mermaid ` diagram and a structured Markdown comparison table.
2. **Step 2 — Under the Hood (Internals)**:
   - Dive into OS kernel vs. user space, packet headers, B+ Tree page splits, LSM-Tree SSTable compaction, or lock-free data structures.
3. **Step 3 — Runnable Python Lab (`labs/<script>.py`)**:
   - Write a self-contained, runnable Python script in the current level's `labs/` folder that proves the concept empirically (using `rich` tables/console output so the user sees latency, throughput, or failure behavior clearly).
   - Run it in the terminal via `.venv\Scripts\python.exe` and explain the output numbers.
4. **Step 4 — Structured Lesson Note**:
   - Create or update the lesson's Markdown file in the level directory following `08-Templates-And-Checklists/lesson-note-template.md` (naming format: `1.1-hardware-and-latency-numbers.md`).
5. **Step 5 — The Socratic Challenge (STOP & WAIT)**:
   - Present **ONE** realistic production failure scenario, race condition, or $10\times \rightarrow 100\times$ scale bottleneck.
   - **STOP generating immediately and wait for the user's answer.** Do NOT reveal the answer in the same turn.
   - **On the user's next turn**: Critique their answer like a Staff+ Bar Raiser interviewer, append the "Socratic Challenge & Staff+ Critique" section to the lesson's Markdown note, check off `- [x]` in [ROADMAP.md](ROADMAP.md), and add a row to [PROGRESS.md](PROGRESS.md).

---

## 3. File Naming & Hygiene Conventions
- **Lesson Notes**: `<Level-Folder>/<X.Y>-<kebab-case-title>.md` (e.g., `01-OS-And-Networking-Foundations/1.1-hardware-and-latency-numbers.md`).
- **Python Labs**: `<Level-Folder>/labs/<snake_case_name>.py` (clean up any temporary `.db` or `.wal` files generated during benchmarks, or keep them ignored via `.gitignore`).
- **Living Matrices**: When a new storage engine, cache strategy, or queue pattern is mastered, add key insights to [08-Templates-And-Checklists/technology-tradeoff-matrix.md](08-Templates-And-Checklists/technology-tradeoff-matrix.md).
