---
layout: page
title: "Interleaved Head Attention"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.21371v1)

# Interleaved Head Attention

#### 🚀 Technical Novelty
* **Mechanism**: Constructs P pseudo-queries, keys, and values per head as learned linear combinations of all original heads' projections, enabling up to P² cross-head attention patterns within each head.
* **Nuance**: Unlike prior head-mixing methods that operate on attention logits post-computation, IHA mixes inputs before the standard softmax operator, preserving compatibility with optimized kernels like FlashAttention while fundamentally altering information flow across heads.

#### 💡 Yield
- Theoretical proof of superior parameter efficiency for polynomial filters (Θ(√kn²) vs Θ(kn²)) and order-sensitive tasks (⌈√N_max⌉ heads vs N_max).
- Empirical gains: 10–20% improvement in multi-key retrieval on RULER (4k–16k context), +5.8% on GSM8K and +2.8% on MATH-500 after reasoning fine-tuning, all under FLOP-matched training.

#### ⚠️ Limitations
- Global IHA increases attention cost to O(P²N²), requiring sliding-window schedules or adaptive pseudo-head allocation to remain practical.
- Current validation is limited to decoder-only LLMs; extensions to encoder-decoder and vision architectures are noted as future work.