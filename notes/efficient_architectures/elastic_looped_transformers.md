---
layout: page
title: "Elastic Looped Transformers"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.09168v2)

# ELT: Elastic Looped Transformers for Visual Generation

#### 🚀 Technical Novelty
* **Mechanism**: Introduces Intra-Loop Self Distillation (ILSD), which trains intermediate recurrent loop states to mimic the final teacher trajectory, allowing weight-shared transformer blocks to produce high-fidelity outputs at any iteration count.
* **Nuance**: Unlike vanilla looped transformers that only converge coherently at a fixed training depth, ELT forces progressive refinement across all loops, transforming a rigid recurrent architecture into an elastic system with dynamic test-time compute scaling.

#### 💡 Yield
- Achieves a 4× parameter reduction compared to MaskGIT and MAGVIT baselines while matching or improving FID (2.0) on ImageNet256×256 and FVD (72.8) on UCF-101 under iso-inference-compute settings.
- Enables true any-time inference, allowing real-time traversal of the quality-compute Pareto frontier without retraining across both diffusion and masked generative transformer frameworks.

#### ⚠️ Limitations
- Quality-compute trade-offs require careful loop-count selection; suboptimal exit points may still yield marginal degradation despite distillation.
- Training stability depends on precise alignment between student (intermediate) and teacher (full-loop) trajectories, which can be sensitive to hyperparameter scheduling.
- Evaluated primarily on class-conditional image/video synthesis; generalization to unconditional generation, complex multi-modal tasks, or non-vision domains is not yet demonstrated.