# The 45-Minute Staff+ System Design Interview Framework

## Phase 1: Requirements & Scope (Minutes 0–5)
1. **Functional Requirements (FRs)**: Top 3–4 core user actions ("Users can post X, view Y"). Explicitly state what is *out of scope*.
2. **Non-Functional Requirements (NFRs)**:
   - **Scale**: DAU, Peak QPS, Read:Write ratio.
   - **Latency**: e.g., $p99 < 200\text{ms}$ for reads.
   - **Consistency vs. Availability**: CP (banking, ticket booking) or AP (social feed, likes)?
   - **Durability**: Zero data loss?

## Phase 2: Back-of-the-Envelope Estimations (Minutes 5–8)
- **Seconds in a day**: $86,400 \approx 10^5\text{ seconds}$.
- **Average QPS**: $\frac{\text{Daily Requests}}{10^5}$ | **Peak QPS**: $2 \times \text{ to } 5 \times \text{Average QPS}$.
- **Storage (1 Year)**: $\text{Writes/sec} \times 10^5 \times 365 \times \text{Record Size}$.
- *Rule*: Only calculate numbers that directly influence an architectural decision (e.g., "Do we need sharding?" or "Will the working set fit in Redis RAM?").

## Phase 3: API Contract & Core Data Model (Minutes 8–15)
- Define 2–3 core REST/gRPC/WebSocket endpoints (include pagination tokens, idempotency keys, auth headers).
- Sketch the core schema and justify the **Database Choice** (Relational vs. Document vs. Wide-Column) and **Primary/Partition Keys**.

## Phase 4: High-Level Architecture (Minutes 15–25)
- Draw the end-to-end Read Path and Write Path using ` ```mermaid `.
- Client $\rightarrow$ DNS/CDN $\rightarrow$ L7 API Gateway $\rightarrow$ Stateless Services $\rightarrow$ Cache / Queue $\rightarrow$ Database.

## Phase 5: Deep Dive, Bottlenecks & Failure Modes (Minutes 25–42)
*Staff+ differentiation happens here. Proactively address:*
1. **Data Layer**: How do we shard? How do we handle hot keys / celebrity users?
2. **Cache Layer**: What happens on a Cache Stampede or Redis node crash?
3. **Failure Modes**: What if a downstream service is slow (Circuit Breaker, DLQ, Backpressure)? What if two users book the exact same seat simultaneously (Distributed Lock / DB MVCC / Conditional Update)?
4. **Multi-Region & Observability**: Active-Active conflict resolution, key SLIs/SLOs.
