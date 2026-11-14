# Latency, Powers of 2 & Capacity Estimation Cheatsheet

## 1. Numbers Every Architect Must Know (2026 Calibrated)

| Operation | Latency | Order of Magnitude | Human Scale Analogy ($1\text{ ns} = 1\text{ sec}$) |
| :--- | :--- | :--- | :--- |
| **L1 Cache Reference** | $0.5\text{ ns}$ | Nanoseconds | $0.5\text{ seconds}$ (A heartbeat) |
| **Branch Mispredict** | $5\text{ ns}$ | Nanoseconds | $5\text{ seconds}$ |
| **L2 Cache Reference** | $7\text{ ns}$ | Nanoseconds | $7\text{ seconds}$ |
| **Mutex Lock / Unlock** | $25\text{ ns}$ | Nanoseconds | $25\text{ seconds}$ |
| **Main Memory (RAM) Reference** | $100\text{ ns}$ | Nanoseconds | $1.5\text{ minutes}$ |
| **Compress 1KB with Zstd/LZ4** | $2,000\text{ ns}$ ($2\ \mu\text{s}$) | Microseconds | $33\text{ minutes}$ |
| **NVMe SSD Random Read (4KB)** | $16,000\text{ ns}$ ($16\ \mu\text{s}$) | Microseconds | $4.4\text{ hours}$ |
| **Same-AZ Network Round Trip** | $250,000\text{ ns}$ ($0.25\text{ ms}$) | Sub-Millisecond | $2.9\text{ days}$ |
| **Cross-AZ Network Round Trip (Same Region)** | $1,000,000\text{ ns}$ ($1\text{ ms}$) | Milliseconds | $11.5\text{ days}$ |
| **Read 1 MB Sequentially from NVMe SSD** | $300\ \mu\text{s} - 1\text{ ms}$ | Milliseconds | $3.5 - 11.5\text{ days}$ |
| **HDD Disk Seek (Legacy / Cold Storage)** | $10\text{ ms}$ | Milliseconds | $3.8\text{ months}$ |
| **Cross-Continent RTT (US-East $\leftrightarrow$ EU-West)** | $75\text{ ms}$ | Milliseconds | $2.4\text{ years}$ |
| **Global Opposite RTT (US $\leftrightarrow$ Singapore)** | $180\text{ ms}$ | Milliseconds | $5.7\text{ years}$ |

---

## 2. Powers of 2 & Data Volume Shortcuts

| Power | Exact Value | Approximation | System Design Unit |
| :--- | :--- | :--- | :--- |
| $2^{10}$ | $1,024$ | $10^3$ ($1\text{ Thousand}$) | **1 KB** (Kilobyte) |
| $2^{20}$ | $1,048,576$ | $10^6$ ($1\text{ Million}$) | **1 MB** (Megabyte) |
| $2^{30}$ | $1,073,741,824$ | $10^9$ ($1\text{ Billion}$) | **1 GB** (Gigabyte) |
| $2^{40}$ | $1.099 \times 10^{12}$ | $10^{12}$ ($1\text{ Trillion}$) | **1 TB** (Terabyte) |
| $2^{50}$ | $1.125 \times 10^{15}$ | $10^{15}$ ($1\text{ Quadrillion}$) | **1 PB** (Petabyte) |

---

## 3. Back-of-the-Envelope Shortcuts

- **Time Conversions**:
  - $1\text{ Day} = 86,400\text{ sec} \approx 10^5\text{ seconds}$
  - $1\text{ Month} \approx 2.5 \times 10^6\text{ seconds}$
  - $1\text{ Year} \approx 3.15 \times 10^7\text{ seconds} \approx \pi \times 10^7\text{ seconds}$
- **Quick QPS Rule of Thumb**:
  - $1\text{M requests/day} \approx 12\text{ RPS}$ (avg) $\rightarrow 30-60\text{ RPS}$ (peak)
  - $100\text{M requests/day} \approx 1,200\text{ RPS}$ (avg) $\rightarrow 3,000-6,000\text{ RPS}$ (peak)
  - $1\text{B requests/day} \approx 12,000\text{ RPS}$ (avg) $\rightarrow 30,000-60,000\text{ RPS}$ (peak)
- **Single-Node Practical Ceilings (Commodity 16–32 vCPU Cloud Instance)**:
  - **PostgreSQL / MySQL (Primary)**: $\sim 5\text{k} - 15\text{k}$ writes/sec; $\sim 20\text{k} - 50\text{k}$ simple indexed reads/sec.
  - **Redis (Single Core / Shard)**: $\sim 80\text{k} - 120\text{k}$ ops/sec.
  - **Kafka Broker**: $\sim 200\text{ MB/sec} - 500\text{ MB/sec}$ sequential disk throughput.
  - **L7 Reverse Proxy (NGINX / Envoy)**: $\sim 50\text{k} - 150\text{k}$ RPS per node.
