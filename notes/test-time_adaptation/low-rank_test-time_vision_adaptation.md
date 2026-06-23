---
layout: page
title: "Low-Rank Test-Time Vision Adaptation"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2502.02069v1)

# LoRA-TTT: Low-Rank Test-Time Training for Vision-Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Injects trainable low-rank matrices into the deeper layers of the VLM's image encoder during inference, optimizing them via a combined marginal entropy and masked image reconstruction loss.
* **Nuance**: Shifts adaptation focus from text prompts to vision parameters, precomputes text features to eliminate the text encoder bottleneck, and preserves base model generalization by freezing original weights while updating only low-rank deltas.

#### 💡 Yield
- Achieves state-of-the-art zero-shot classification across 15 datasets (avg +5.79% OOD, +1.36% fine-grained) while drastically cutting memory/runtime overhead compared to TPT; demonstrates superior calibration via MAE loss and maintains full prompt interchangeability without external caches or teacher models.

#### ⚠️ Limitations
- Performance is sensitive to LoRA rank/scale hyperparameters and layer selection; pure entropy minimization induces model overconfidence requiring reconstruction loss mitigation; evaluated primarily on zero-shot classification rather than complex downstream vision tasks.