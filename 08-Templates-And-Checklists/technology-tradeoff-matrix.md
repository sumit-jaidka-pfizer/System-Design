# Staff+ Technology Trade-Off Matrix ("When to Choose X vs. Y")

> *As we complete each module, we will expand this living decision matrix with concrete failure modes we observe in our labs.*

## 1. Storage Engines: B+ Tree vs. LSM-Tree

| Dimension | B+ Tree (PostgreSQL, MySQL InnoDB, SQLite) | LSM-Tree (RocksDB, Cassandra, ScyllaDB) |
| :--- | :--- | :--- |
| **Core Mechanism** | Fixed-size pages ($4\text{KB}-16\text{KB}$) updated in-place on disk + WAL | Append-only WAL + In-memory `MemTable` flushed to immutable `SSTables` + Compaction |
| **Read Latency ($p99$)** | **Winner**: Predictable $O(\log_B N)$ page lookups | Slower unless cached; may check MemTable + multiple SSTables (mitigated by **Bloom Filters**) |
| **Write Throughput** | Limited by random disk I/O & page splits | **Winner**: Every write is sequential memory + WAL append |
| **Write Amplification** | High on small random updates (writes entire $16\text{KB}$ page) | High during background **Compaction** (Leveled vs. Size-Tiered) |
| **Use When...** | High read-to-write ratio, strict ACID transactions, low $p99$ point/range reads | Massive write ingestion (IoT, chat messages, event logs, time-series) |

---

## 2. Messaging: Message Queue (RabbitMQ/SQS) vs. Commit Log Stream (Kafka)

| Dimension | Traditional Message Queue (RabbitMQ / AWS SQS) | Distributed Commit Log (Apache Kafka / Redpanda) |
| :--- | :--- | :--- |
| **Data Retention** | Deleted immediately after consumer `ACK` | Retained on disk for days/weeks (or tiered to S3) regardless of consumption |
| **Replayability** | **No** (once acked, message is gone) | **Yes** (consumers can rewind offset to reprocess historical events) |
| **Routing Logic** | Smart broker, dumb consumer (Exchanges, per-message routing, task queues) | Dumb broker, smart consumer (Sequential partition offsets) |
| **Ordering Guarantee** | Weak / best-effort (breaks under retries or multiple workers) | **Strict ordering within a single Partition Key** |
| **Use When...** | Background job queues (sending emails, video transcoding workers, per-task retries) | Event sourcing, CDC pipelines, high-throughput log aggregation, multi-consumer event streams |

---

## 3. Caching Patterns: Cache-Aside vs. Write-Through vs. Write-Behind

| Pattern | How It Works | Pros | Cons / Failure Mode |
| :--- | :--- | :--- | :--- |
| **Cache-Aside (Lazy Loading)** | App checks Cache; on miss, reads DB and populates Cache. Writes go to DB then *invalidate* (delete) Cache. | Resilient to cache failure; only caches requested data. | Cold-start latency; **Cache Stampede** on hot key expiry; subtle race condition if `Write` happens instead of `Delete`. |
| **Read/Write-Through** | App talks to Cache as main store; Cache synchronously writes to DB. | Cache is always consistent with DB; no cold reads after write. | Higher write latency (2 synchronous hops); caches data that may never be read again. |
| **Write-Behind (Write-Back)** | App writes *only* to Cache; Cache flushes asynchronously in batches to DB. | **Extreme write throughput** & write coalescing (e.g., like/view counters). | **Data loss risk** if cache node crashes before flushing to DB. |
