---
layout: page
title: "Global Regression KV Cache"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.31105v1)

# GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs

#### 🚀 Technical Novelty
* **Mechanism**: Formulates KV-cache merging as a global ridge-regression optimization problem that directly minimizes the attention-output discrepancy between compressed and full caches, distributing recovered information across all retained tokens.
* **Nuance**: Unlike prior local or key-similarity heuristics that funnel merges onto a few span-boundary tokens (causing over-merging and semantic blurring), GRKV treats every retained token as an active carrier and applies ridge regularization to prevent over-smoothing.

#### 💡 Yield
- Achieves the highest overall performance across 16 LongBench and 13 RULER tasks when paired with modern span-based eviction methods (SnapKV, CriticalKV), outperforming prior merging baselines that typically degrade retrieval and QA accuracy due to information loss.

#### ⚠️ Limitations
- Optimization is sensitive to hyperparameters; increasing update steps or surrogate window sizes beyond defaults degrades performance by overfitting the local attention surrogate.
- Relies on a fixed fraction of high-attention tokens as anchors, which may limit adaptability in highly dynamic or non-stationary context distributions.