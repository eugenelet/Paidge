---
layout: page
title: "Key Similarity KV Cache Eviction"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2504.15364v3)

# KEYDIFF: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a training-free, block-wise KV cache eviction policy that retains keys exhibiting low pairwise cosine similarity (high geometric diversity) as a proxy for token importance, completely bypassing explicit attention weight computation.
* **Nuance**: Unlike prior eviction methods that require full-prompt attention materialization (which violates strict memory bounds during prefill or demands heavy compute), KEYDIFF operates within fixed per-block memory budgets and remains fully compatible with optimized attention backends like FlashAttention.

#### 💡 Yield
- Achieves ≤0.04% accuracy drop on LongBench with an 8K cache budget (~23% KV reduction) across Llama 3.1/3.2 model families, outperforming SOTA eviction baselines.
- Delivers up to 30% end-to-end inference latency reduction by eliminating attention score materialization overhead and enabling FlashAttention integration.
- Maintains near non-evicting baseline performance on complex reasoning tasks (Math-500) under tight memory constraints, validating its efficacy for long-horizon generation.

#### ⚠️ Limitations
- Primarily designed and empirically validated for Grouped Query Attention (GQA) architectures; requires architectural adaptation to support other attention variants like Multi-Head Latent Attention.
- Block-wise processing introduces a dependency on block size tuning, which may impact optimal throughput/memory trade-offs across heterogeneous edge hardware configurations.