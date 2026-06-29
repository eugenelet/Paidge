---
layout: page
title: "Dynamic Linear Attention"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2606.10650v1)

# Dynamic Linear Attention

#### 🚀 Technical Novelty
* **Mechanism**: Information-Aware Dynamic State Merging and Capacity-Bounded Memory Modeling that dynamically adjusts state granularity based on token-level representation drift while maintaining a fixed-size chronological cache.
* **Nuance**: Unlike prior multi-state linear attention methods (e.g., Log-Linear Attention) that rely on rigid, deterministic temporal schedules for memory compression, DLA adapts on-the-fly to semantic transitions, preventing irreversible information loss and error accumulation in stable sequence regions.

#### 💡 Yield
- Consistently outperforms state-of-the-art multi-state linear attention across 16 datasets, achieving up to 49% relative gains on in-context retrieval tasks and matching full-attention Transformer performance with comparable parameter budgets.
- Delivers higher throughput and lower runtime memory footprint than baselines under varying batch sizes and context lengths, demonstrating superior compute efficiency for long-sequence modeling.

#### ⚠️ Limitations
- Maintaining a cache of multiple summary states inherently increases peak memory usage compared to single-state recurrent models (vanilla SSMs/linear attention), though it remains strictly bounded and more efficient than prior multi-state approaches.