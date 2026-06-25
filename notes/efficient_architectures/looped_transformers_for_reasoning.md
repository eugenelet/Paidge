---
layout: page
title: "Looped Transformers For Reasoning"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2502.17416v1)

# REASONING WITH LATENT THOUGHTS: ON THE POWER OF LOOPED TRANSFORMERS

#### 🚀 Technical Novelty
* **Mechanism**: Iteratively applies a fixed k-layer transformer block L times via weight sharing, creating an effective depth of kL while maintaining a constant parameter count.
* **Nuance**: Unlike standard deep models that scale parameters with depth, or explicit CoT prompting that requires external token generation, it generates multiple parallel "latent thoughts" per iteration internally without increasing model size or compute budget.

#### 💡 Yield
- Empirically, (k ⊗ L) looped models match or outperform iso-FLOP non-looped baselines on synthetic and downstream reasoning tasks while using L× fewer parameters.
- Theoretically proves looped transformers can simulate iterative algorithms and exactly replicate T steps of Chain-of-Thought reasoning with minimal architectural overhead.
- Introduces a layer-similarity regularization that transfers the inductive bias toward reasoning to standard models without harming perplexity.

#### ⚠️ Limitations
- Primarily validated on synthetic procedural tasks (addition, p-hop induction) and limited benchmarks; generalization to complex multimodal or open-ended common-sense reasoning is unverified.
- Pretraining perplexity degrades relative to iso-FLOP baselines due to reduced parameters, necessitating task-specific regularization to unlock downstream gains.