---
layout: page
title: "Global Regression KV Cache"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.31105v1)

# GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs

#### 🚀 Technical Novelty
* **Mechanism**: Formulates KV-cache merging as a global ridge-regression problem that directly minimizes the attention-output discrepancy between compressed and full caches, distributing evicted token information across all retained tokens.
* **Nuance**: Replaces prior local/heuristic matching strategies that funnel merges onto sparse span-boundary carriers; GRKV treats all retained tokens as active carriers and applies ridge regularization to prevent semantic blurring and over-smoothing.

#### 💡 Yield
- Only KV-cache merging method to consistently improve overall performance across 16 LongBench and 13 RULER tasks when paired with modern span-based eviction methods (e.g., SnapKV, CriticalKV).
- Delivers substantial memory reduction and decoding latency savings (~42% at 64K context) while maintaining plug-and-play compatibility with diverse eviction backbones without requiring model retraining.

#### ⚠️ Limitations
- Relies on a fixed surrogate window for regression optimization, which may constrain generalization to highly dynamic or out-of-distribution long-context scenarios.
- Introduces moderate prefill overhead compared to pure eviction methods, though remains significantly faster than heavier merging baselines like AsymKV.