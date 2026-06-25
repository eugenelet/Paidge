---
layout: page
title: "DualPath KV Cache Optimization"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.21548v2)

# DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference

#### 🚀 Technical Novelty
* **Mechanism**: Introduces dual-path KV-Cache loading that routes data from storage to decoding engines first, then transfers it to prefill engines via RDMA, paired with a global scheduler that dynamically balances compute and network load.
* **Nuance**: Unlike prior systems that saturate prefill-side storage NICs or rely on memory-constrained DRAM pools, DualPath exploits idle storage bandwidth on decode engines while isolating KV-Cache traffic from latency-critical model execution communications.

#### 💡 Yield
- Increases offline inference throughput by up to 1.87× and online serving throughput by an average of 1.96× without violating SLOs.
- Reduces average job completion time by ~45% compared to baseline disaggregated architectures through workload-aware scheduling and NIC load balancing.

#### ⚠️ Limitations
- Assumes specific high-bandwidth hardware (e.g., 400Gbps storage/compute NICs) and RDMA support, limiting direct applicability to legacy clusters.
- Optimal prefill-to-decode ratios and parallelism settings require costly empirical tuning; the scheduler still faces challenges under highly dynamic or bursty online workloads.
- Real-world working sets may exceed available memory due to non-zero inter-arrival times and tool-call latencies, potentially reducing cache hit rates in production.