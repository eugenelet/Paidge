---
layout: page
title: "Looped Transformers for Reasoning"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2502.17416v1)

# REASONING WITH LATENT THOUGHTS: ON THE POWER OF LOOPED TRANSFORMERS

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a weight-sharing looping mechanism where a k-layer transformer block is iteratively applied L times, creating an effective depth of kL while retaining only k-layer parameters. Also proposes a layer-similarity regularization to amplify this inductive bias during training.
* **Nuance**: Decouples architectural depth from parameter count, contrasting with standard scaling laws that tie depth to model size. Unlike Chain-of-Thought which expands tokens at inference, looped models perform iterative computation internally via shared weights during the forward pass.

#### 💡 Yield
- Looping matches or exceeds iso-FLOP non-looped baselines on synthetic and downstream reasoning tasks despite using L× fewer parameters.
- Theoretical proofs demonstrate looped transformers can simulate iterative algorithms, solve p-hop induction with O(log p) loops, and formally simulate multi-step Chain-of-Thought reasoning via masking and token decoding.
- Downstream accuracy scales logarithmically with effective depth (loops), revealing a strong inductive bias toward compositional reasoning over memorization.

#### ⚠️ Limitations
- Evaluated primarily on synthetic procedural tasks; generalization to complex real-world, multimodal, or common-sense reasoning remains unverified.
- Suffers from higher perplexity compared to parameter-matched baselines due to the inherent trade-off between depth and model capacity.
- Lacks a formalized, unified definition of "reasoning," limiting direct comparison across diverse cognitive benchmarks and leaving broader architectural implications open for future work.