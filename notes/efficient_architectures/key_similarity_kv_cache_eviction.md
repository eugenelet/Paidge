---
layout: page
title: "Key Similarity KV Cache Eviction"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2504.15364v3)

# KEYDIFF: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a training-free, block-wise eviction policy that retains geometrically distinctive keys (minimizing pairwise cosine similarity) to approximate global token importance without computing full attention maps.
* **Nuance**: Unlike prior methods that require full-prompt attention materialization or violate memory bounds during intermediate steps, KEYDIFF operates strictly within fixed cache budgets per block and remains fully compatible with optimized kernels like FlashAttention.

#### 💡 Yield
- Achieves ≤0.04% accuracy drop on LongBench with an 8K cache budget (~23% KV reduction) across Llama 3.1/3.2 models, outperforming SnapKV and TOVA.
- Delivers up to 30% end-to-end inference latency reduction while maintaining near-baseline performance on complex reasoning benchmarks (Math-500).

#### ⚠️ Limitations
- Currently optimized for Grouped Query Attention (GQA) architectures; requires adaptation for other attention variants like Multi-Head Latent Attention.
- Relies on the empirical observation that key diversity strongly proxies importance, which may not generalize uniformly across all model families or specialized domains without further validation.