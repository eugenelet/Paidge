---
layout: page
title: "Dynamic Layer-Wise TTA"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.09719v1)

# Unsupervised Layer-Wise Dynamic Test Time Adaptation for LLMs

#### 🚀 Technical Novelty
* **Mechanism**: Introduces SCALENET, a lightweight hypernetwork that predicts non-negative, per-layer and per-step learning rate multipliers for LoRA parameters during inference, conditioned on the input prompt.
* **Nuance**: Unlike prior TTA methods relying on fixed global rates or static schedules, this approach learns fine-grained, prompt-dependent scaling patterns across transformer layers and adaptation steps, preventing destructive drift while maximizing early-update gains.

#### 💡 Yield
- Consistently reduces negative log-likelihood (NLL) and improves ROUGE-Lsum across Llama3/Qwen models on summarization and QA benchmarks compared to fixed-rate and step-wise TTA baselines.
- Empirically validates that optimal unsupervised TTA requires aggressive initial updates followed by rapid damping, with highly non-uniform scaling needs even between adjacent query/value projections.
- Enables efficient training via a first-order approximation that avoids expensive second-order derivatives while unrolling the inference-time adaptation process.

#### ⚠️ Limitations
- Prioritizes dataset-tailored, prompt-conditioned adaptation, which may limit transferability across substantially different task distributions or out-of-distribution prompts.
- Relies on a shallow MLP hypernetwork; scaling to more complex distribution shifts may require higher-capacity architectures and broader training corpora.