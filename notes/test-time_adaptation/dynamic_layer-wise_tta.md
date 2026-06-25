---
layout: page
title: "Dynamic Layer-Wise TTA"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.09719v1)

# Unsupervised Layer-Wise Dynamic Test Time Adaptation for LLMs

#### 🚀 Technical Novelty
* **Mechanism**: A prompt-conditioned hypernetwork (SCALENET) predicts non-negative, per-layer and per-step learning rate multipliers to rescale LoRA updates during inference.
* **Nuance**: Replaces brittle fixed or step-wise global learning rates with fine-grained, input-dependent scaling that varies sharply across transformer blocks and adaptation steps, preventing destructive drift while maximizing early-update gains.

#### 💡 Yield
- Consistently outperforms fixed-rate and step-wise baselines on NLL and ROUGE-Lsum across Llama3/Qwen models (3B–70B) and multiple summarization/retrieval datasets.
- Visualization reveals SCALENET learns complex, non-monotonic scaling patterns that differ by projection type (Q/V) and layer depth, with peak update magnitudes naturally decaying after step 1.

#### ⚠️ Limitations
- Prioritizes dataset-tailored, prompt-conditioned adaptation, which may limit transferability across substantially different task distributions without larger training corpora or higher-capacity hypernetworks.