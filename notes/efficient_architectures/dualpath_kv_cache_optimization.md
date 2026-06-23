---
layout: page
title: "DualPath KV Cache Optimization"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.21548v2)

# DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference

#### 🚀 Technical Novelty
* **Mechanism**: Introduces dual-path KV-Cache loading that routes data from persistent storage directly to either prefill or decode engines, then leverages high-speed RDMA to transfer cache between them, bypassing single-NIC saturation.
* **Nuance**: Unlike prior systems that only optimize the storage-to-prefill path or rely on expensive DRAM pools, DualPath exploits underutilized decode-side storage bandwidth and dynamically balances I/O load without increasing memory overhead.

#### 💡 Yield
- Achieves up to 1.87× offline inference throughput and 1.96× average online serving throughput on realistic agentic workloads while strictly maintaining latency SLOs.
- Reduces average trajectory completion time (JCT) by ~45% compared to baseline disaggregated systems through NIC-centric traffic isolation and workload-aware scheduling.
- Demonstrates near-linear scalability across up to 1,152 GPUs with negligible scheduler overhead (<10 CPU cores).

#### ⚠️ Limitations
- Evaluations assume zero inter-arrival time and tool-call latency, which likely overestimates real-world working set sizes and system capacity under production conditions.
- Scheduling algorithm and prefill/decode ratio configurations require further adaptation for highly dynamic, bursty enterprise workloads.
- Performance gains from layering a DRAM cache on top of DualPath are marginal, limiting the effectiveness of hybrid memory-tier optimizations.