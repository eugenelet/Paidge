---
layout: page
title: "Test-Time LLM Adaptation"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2505.20633v1)

# Test-Time Learning for Large Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Formulates inference-time adaptation as input perplexity minimization, actively weighting high-perplexity samples for backpropagation, and applying lightweight LoRA updates to preserve pre-trained knowledge.
* **Nuance**: Replaces standard TTA's entropy minimization with autoregressive-aware input perplexity optimization, eliminating the need for external retrieval or labeled data while mitigating catastrophic forgetting via parameter-efficient updates.

#### 💡 Yield
- Achieves ≥20% performance gains on domain adaptation benchmarks; reduces online backward passes by ~69.7%; establishes AdaptEval benchmark for rigorous TTL evaluation.

#### ⚠️ Limitations
- Sensitive to the perplexity threshold hyperparameter (P0); relies on greedy decoding which may limit output diversity; requires careful calibration to avoid overfitting on noisy test streams.