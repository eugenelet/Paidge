---
layout: page
title: "Interleaved Head Attention"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.21371v1)

# Interleaved Head Attention

#### 🚀 Technical Novelty
* **Mechanism**: Constructs P pseudo-queries, keys, and values per head as learned linear combinations of all original heads' projections, inducing up to P² attention patterns per head instead of H independent matrices.
* **Nuance**: Unlike prior cross-head mixing methods that operate on attention logits/weights, IHA mixes inputs before the attention operator, preserving standard softmax compatibility with efficient kernels like FlashAttention while achieving quadratic expressivity scaling.

#### 💡 Yield
- Theoretical: Proves strict expressivity gains over MHA; reduces parameter complexity for Polynomial Filters from Θ(kn²) to Θ(√kn²) and cuts required heads for CPM-3 from N_max to ⌈√N_max⌉.
- Empirical: Achieves 10–20% relative improvement on Multi-Key Retrieval (RULER, 4k–16k context) and boosts GSM8K (+5.8%) and MATH-500 (+2.8%) after reasoning-focused fine-tuning under FLOP-matched training.

#### ⚠️ Limitations
- Global IHA can increase attention cost to O(P²N²), mitigated here by a sliding-window schedule; requires future work on adaptive pseudo-head allocation and extension to encoder-decoder/vision architectures.