---
layout: page
title: "CAOTE Token Eviction"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2504.14051v6)

# CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based Token Eviction

#### 🚀 Technical Novelty
* **Mechanism**: Computes token eviction error in closed-form by mathematically combining attention scores (query-key alignment) and value vectors to quantify each cached token's exact contribution to the final attention output.
* **Nuance**: Unlike prior eviction methods that rely exclusively on attention scores as a proxy for importance, CAOTE explicitly models value vector contributions and functions as a model-agnostic meta-heuristic that seamlessly plugs into existing score-based strategies (e.g., H2O, SnapKV) for consistent performance gains.

#### 💡 Yield
- Consistently improves accuracy across LongBench, Needle-in-Haystack retrieval, and perplexity benchmarks on LLaMA3 and Qwen2.5 families when integrated with state-of-the-art eviction baselines.
- Enables block-wise prompt processing and dynamic KV cache budgeting, effectively mitigating memory/compute bottlenecks for long-context inference on resource-constrained hardware without requiring model retraining or fine-tuning.

#### ⚠️ Limitations
- Relies on a heuristic closed-form approximation rather than learned parameters; performance may vary across non-standard attention mechanisms or highly specialized architectures.
- Primarily evaluated on decoder-only LLMs; generalization to multimodal, encoder-decoder, or hybrid models is not explicitly demonstrated.
- The per-token computational overhead of calculating the CAOTE score during autoregressive generation must be carefully balanced against memory savings in ultra-low-latency deployment scenarios.