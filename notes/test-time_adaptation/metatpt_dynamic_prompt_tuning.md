---
layout: page
title: "MetaTPT Dynamic Prompt Tuning"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.12268v1)

# MetaTPT: Meta Test-time Prompt Tuning for Vision-Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Dual-loop meta-adaptation framework that jointly optimizes differentiable, self-supervised parameterized augmentations and learnable prompts on a per-sample basis during inference.
* **Nuance**: Replaces TPT's static, handcrafted data augmentations with dynamically learned affine transformations that adapt to each test sample's domain-specific features, preventing information loss in challenging shifts.

#### 💡 Yield
- Achieves state-of-the-art zero-shot generalization across multiple VLMs (CLIP, CoOp, MaPLe, MMRL) on cross-dataset and domain generalization benchmarks; ablations confirm online dual-loop optimization significantly outperforms one-stage joint training and offline augmentation strategies.

#### ⚠️ Limitations
- The online per-sample meta-adaptation strategy increases inference latency compared to fixed-augmentation baselines, prioritizing robustness over computational efficiency without explicit acceleration mechanisms.