---
layout: page
title: "EAGLE Speculative Sampling"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2401.15077v3)

# EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty

#### 🚀 Technical Novelty
* **Mechanism**: Autoregressively predicts second-to-top-layer hidden states using a lightweight draft model, conditioned on the target LLM's features plus the next-step sampled token to eliminate feature ambiguity.
* **Nuance**: Unlike Medusa or Lookahead which predict tokens directly or rely on n-grams/Jacobi iteration, EAGLE operates at the continuous feature level and explicitly injects shifted tokens to resolve sampling-induced uncertainty, boosting acceptance rates to ~0.8 without any backbone fine-tuning.

#### 💡 Yield
- Delivers 2.7x–3.5x latency speedup and doubles throughput across LLaMA2/Vicuna/Mixtral series while provably preserving the original output distribution for both greedy and non-greedy decoding.
- Requires minimal training overhead (2–4B tokens, 1–2 days on consumer GPUs) and generalizes zero-shot across dialogue, code, math, and instruction tasks with negligible amortized cost.

#### ⚠️ Limitations
- Acceleration gains degrade as batch size increases due to memory-bound verification bottlenecks and reduced GPU compute availability per token.
- Draft model performance is optimized for its fixed training domain (ShareGPT); while sensitivity is low, deployment in highly out-of-distribution domains may slightly reduce acceptance rates without retraining.