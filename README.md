# System Design Mastery: Zero to Staff+ & AI-Native Architect (2026+)

An interactive, Socratic, **Python-lab-driven** System Design workspace engineered for **FAANG/Staff+ Interviews**, **Real-World Production Architecture**, **Deep Distributed Systems Internals**, and **Modern AI-Native System Design**.

---

## Quick Start (How to Use This Workspace in VS Code)

1. **Always Start a Fresh Chat Per Lesson (`Ctrl+N`)**
   - Keeps your context window small, fast, and 50–80% cheaper in token usage.
2. **Use Your Built-In Slash Commands in Copilot Chat (Agent Mode)**:
   - `/learn-topic 1.1` — Starts any lesson from [ROADMAP.md](ROADMAP.md) using the 5-step **First Principles $\rightarrow$ Internals $\rightarrow$ Python Lab $\rightarrow$ Note $\rightarrow$ Socratic Challenge** cycle.
   - `/boss-fight 1.6` — Launches the end-of-level **Spiral Capstone Boss Fight** (evolves an architecture from 100 users to 100M users).
   - `/python-lab <topic>` — Builds and benchmarks a pure-Python distributed systems simulation in `labs/`.
   - `/review-drill` — Runs a 3-question Staff+ active recall & production outage drill from your completed modules in [PROGRESS.md](PROGRESS.md).
   - `/mock-interview <topic>` — Runs a realistic 45-minute Staff+ Bar Raiser mock interview and logs your scorecard in [08-Templates-And-Checklists/mock-interview-log.md](08-Templates-And-Checklists/mock-interview-log.md).

---

## Model Selection Guide (High-ROI Token Strategy)

| Task Type | Recommended Models | Reasoning Effort |
| :--- | :--- | :--- |
| **Daily Lessons (`/learn-topic`), Python Labs, Active Recall (`/review-drill`)** | `Auto (10% discount)`, `Claude Haiku 5.5`, `Gemini 3.8 Flash`, or `Claude Sonnet 5.5` | **Low / Medium** |
| **Spiral Capstone Boss Fights (`/boss-fight`), Complex Trade-Offs** | `Claude Sonnet 5.5`, `Gemini 4 Carbon / Argon`, `GPT-6.1 Sol` | **Medium** |
| **45-Min Staff+ Mock Interviews (`/mock-interview`), Deep Consensus Critiques** | `Claude Opus 5.5`, `GPT-6.1 Terra` | **High** |

---

## Workspace Architecture

| Path | Purpose |
| :--- | :--- |
| [ROADMAP.md](ROADMAP.md) | 8-Level curriculum from OS/Networking physics to AI-Native System Design |
| [PROGRESS.md](PROGRESS.md) | Living tracker of completed lessons, Python labs, and Socratic Challenge takeaways |
| [AGENTS.md](AGENTS.md) | Universal handover instructions & quality bar for all AI models in this workspace |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Automatic workspace system prompt for GitHub Copilot |
| `.github/prompts/*.prompt.md` | Reusable slash-command workflows (`/learn-topic`, `/boss-fight`, `/python-lab`, `/review-drill`, `/mock-interview`) |
| `01` through `07` folders | Modular topic notes + runnable `labs/*.py` simulations (Zero Docker required) |
| [08-Templates-And-Checklists/](08-Templates-And-Checklists/) | Interview framework, 2026 latency numbers, trade-off matrices, lesson note template, and mock interview scorecards |

---

## Local Environment Setup (If Cloned on a New Machine)

```powershell
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
```
