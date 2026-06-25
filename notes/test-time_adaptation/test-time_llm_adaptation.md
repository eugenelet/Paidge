---
layout: page
title: "Test-Time LLM Adaptation"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2505.20633v1)

# Test-Time Learning for Large Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Formulates test-time updates as input perplexity minimization, guided by a sample-efficient strategy that prioritizes high-perplexity samples and applies lightweight LoRA updates.
* **Nuance**: Replaces prior TTA methods' reliance on output entropy minimization with autoregressive-aware input perplexity optimization, preventing degradation of generative dynamics while mitigating catastrophic forgetting through parameter-efficient fine-tuning.

#### 💡 Yield
- Delivers ≥20% relative performance gains over base LLMs and outperforms SOTA TTA baselines (Tent, EATA, COME) across domain knowledge, instruction-following, and reasoning benchmarks; cuts online backward passes by ~70% via selective sample weighting.

#### ⚠️ Limitations
- Adaptation performance is sensitive to the perplexity threshold hyperparameter (P0); greedy decoding is enforced during updates which may limit response diversity; and online stability requires batching updates every 100 samples rather than per-step.