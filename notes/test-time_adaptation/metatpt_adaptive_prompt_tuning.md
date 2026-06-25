---
layout: page
title: "MetaTPT Adaptive Prompt Tuning"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.12268v1)

# MetaTPT: Meta Test-time Prompt Tuning for Vision-Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Dual-loop meta-learning framework that jointly optimizes a self-supervised auxiliary task for dynamic, parameterized affine augmentations and learnable prompts via cross-view consistency enforcement.
* **Nuance**: Replaces the fixed, handcrafted data augmentations used in prior TTA methods (like TPT) with differentiable, sample-specific transformations that adapt online to capture nuanced domain features.

#### 💡 Yield
- Achieves state-of-the-art performance on cross-dataset and domain generalization benchmarks across multiple VLMs (CLIP, CoOp, MaPLe, MMRL).
- Ablations confirm learnable augmentations consistently outperform fixed ones, dual-loop optimization surpasses one-stage joint training, and online adaptation beats offline variants.

#### ⚠️ Limitations
- Online per-sample meta-adaptation inherently increases inference latency and memory overhead compared to static augmentation methods; computational trade-offs are not explicitly quantified in the provided text.