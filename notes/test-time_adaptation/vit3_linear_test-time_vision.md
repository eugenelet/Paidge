---
layout: page
title: "ViT3 Linear Test-Time Vision"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.01643v2)

# ViT3: Unlocking Test-Time Training in Vision

#### 🚀 Technical Novelty
* **Mechanism**: Reformulates self-attention into an online learning problem where key-value pairs dynamically train a compact inner module (e.g., gated linear units + depthwise convolutions) at test time to update weights via gradient steps.
* **Nuance**: Unlike fixed linear attention or Mamba that compress KV into static states, ViT3 uses flexible, learnable inner modules with online updates, enabling richer non-linear representations without quadratic complexity.

#### 💡 Yield
- Distills six practical design principles for visual TTT (e.g., full-batch single-epoch training with LR=1.0 is optimal; convolutional inner models suit vision tasks). Achieves competitive or superior performance to Mamba and linear attention variants on ImageNet, COCO detection/segmentation, ADE20K, and ImageNet generation, while delivering ~4.6x speedup and 90% memory reduction at high resolutions.

#### ⚠️ Limitations
- Deep inner models suffer from optimization difficulties in current TTT settings; performance still lags slightly behind highly optimized O(N^2) vision Transformers (e.g., TransNeXt) on segmentation, indicating a need for deeper/more expressive inner modules.