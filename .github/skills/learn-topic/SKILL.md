---
name: learn-topic
description: "Learn a System Design topic using First Principles, Internals, Python Lab, and a Socratic Challenge."
disable-model-invocation: true
---
Look up the requested topic number or name in [ROADMAP.md](../../ROADMAP.md), [PROGRESS.md](../../PROGRESS.md), and [AGENTS.md](../../AGENTS.md). Match the exact Staff+ depth and vividness of our gold-standard exemplar ([01-OS-And-Networking-Foundations/1.1-hardware-and-latency-numbers.md](../../01-OS-And-Networking-Foundations/1.1-hardware-and-latency-numbers.md)):
1. **First-Principles Mental Model**: Why it exists, what hardware/network bottleneck it solves, how real systems (Postgres/Kafka/Redis/Envoy) use it, a detailed ` ```mermaid ` diagram, and a comparison matrix. Zero dry disclaimers!
2. **Under the Hood (Internals)**: Concrete OS, network, or storage engine mechanics + governing equations in KaTeX (`$$`).
3. **Contrast-Driven Python Lab (No Docker)**: Create a runnable Python script in the module's `labs/` folder that compares at least two contrasting designs side-by-side (e.g., naive vs. optimized) using `rich` tables with relative speedup/penalty multipliers, and run it with `.venv\Scripts\python.exe`.
4. **Create/Update Note**: Document the core concepts cleanly in the module's Markdown file structured according to [08-Templates-And-Checklists/lesson-note-template.md](../../08-Templates-And-Checklists/lesson-note-template.md).
5. **The Socratic Challenge**: End with ONE realistic production failure scenario or 100x scale bottleneck question. **Stop and wait for my response** before critiquing, logging the takeaway in [PROGRESS.md](../../PROGRESS.md) and [ROADMAP.md](../../ROADMAP.md), and completing the lesson.
