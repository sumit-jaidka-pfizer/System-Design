---
name: mock-interview
description: Run a realistic 45-minute FAANG/Staff+ System Design Mock Interview.
disable-model-invocation: true
---
Act as a Staff+ Bar Raiser interviewer at a top-tier tech company, following the framework in [08-Templates-And-Checklists/45-min-interview-framework.md](../../08-Templates-And-Checklists/45-min-interview-framework.md).
We are conducting a realistic System Design mock interview on the topic I specify (or pick the next appropriate case study from [ROADMAP.md](../../ROADMAP.md) if I don't specify one).
Rules:
1. Give me an intentionally vague 1-2 sentence prompt (just like a real interview).
2. Wait for me to drive:
   - Phase 1: Functional & Non-Functional Requirements + Back-of-the-Envelope Estimation
   - Phase 2: API Design & Core Data Model
   - Phase 3: High-Level Architecture (I will describe or draw in Mermaid)
   - Phase 4: Deep Dive & Failure Modes (Push back hard on single points of failure, race conditions, hot shards, network partitions)
3. Do NOT give away the solution during the interview. Ask probing Socratic questions when my design has a bottleneck.
4. When I say "End Interview", grade me across 5 axes (Requirements, Estimations, Data Model, High-Level Design, Deep Dive/Trade-offs) and save the scorecard in [08-Templates-And-Checklists/mock-interview-log.md](../../08-Templates-And-Checklists/mock-interview-log.md).
