---
layout: page
title: "EAGLE Speculative Sampling"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2401.15077v3)

# EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a lightweight draft model that autoregressively predicts second-to-top-layer features instead of discrete tokens, incorporating a one-step-ahead token sequence to explicitly resolve sampling-induced feature ambiguity.
* **Nuance**: Unlike Medusa or Lookahead which predict spaced tokens or rely on n-grams/Jacobi iteration with lower acceptance accuracy (~0.6), EAGLE operates at the continuous feature level with shifted-token conditioning, achieving ~0.8 acceptance accuracy without fine-tuning the backbone model.

#### 💡 Yield
- Achieves 2.7x-3.5x latency speedup and doubles throughput across LLaMA2/Vicuna/Mixtral models while theoretically guaranteeing exact output distribution preservation for both greedy and non-greedy decoding.

#### ⚠️ Limitations
- Speedup ratio diminishes as batch size increases due to GPU memory/compute constraints; requires a small amount of training data (2-4B tokens or fixed ShareGPT subset) for the draft model, though amortized cost becomes negligible over time.