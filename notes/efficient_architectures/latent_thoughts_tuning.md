---
layout: page
title: "Latent Thoughts Tuning"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.10229v1)

# Latent Thoughts Tuning: Bridging Context and Reasoning with Fused Information in Latent Tokens

#### 🚀 Technical Novelty
* **Mechanism**: Context-Prediction-Fusion mechanism constructs latent tokens by combining contextual hidden states with probability-weighted vocabulary embeddings, optimized via a progressive three-stage curriculum learning pipeline.
* **Nuance**: Replaces static latent token allocation and external assistant models with dynamic, confidence-driven switching between explicit and latent reasoning, directly resolving distribution mismatch in untied-embedding architectures.

#### 💡 Yield
- Achieves up to 4.3% average accuracy gains over prior latent baselines across 1B–8B parameter models on mathematical reasoning benchmarks while preserving semantic diversity in the latent space.

#### ⚠️ Limitations
- Relies on supervised curriculum learning rather than reinforcement learning for optimization, and empirical validation is currently confined to mathematical reasoning tasks and model scales up to 8B parameters.