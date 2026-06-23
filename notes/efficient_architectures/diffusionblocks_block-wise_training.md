---
layout: page
title: "DiffusionBlocks Block-Wise Training"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2506.14202v3)

# DIFFUSIONBLOCKS: BLOCK-WISE NEURAL NETWORK TRAINING VIA DIFFUSION INTERPRETATION

#### 🚀 Technical Novelty
* **Mechanism**: Maps sequential residual updates to Euler discretization steps of a continuous-time reverse diffusion process, allowing each block to be trained independently via score matching over assigned noise ranges.
* **Nuance**: Replaces ad-hoc local objectives with a principled diffusion-theoretic foundation and equi-probability partitioning, enabling scalable block-wise training across modern generative architectures rather than just classification tasks.

#### 💡 Yield
- Reduces training memory linearly by the number of blocks (B× reduction) since gradients are computed for only one block per step.
- Matches or surpasses end-to-end backpropagation accuracy/FID on CIFAR-10/100 and ImageNet across vision, diffusion, autoregressive, and recurrent-depth models.
- Eliminates iterative training overhead in recurrent-depth models by converting K-pass optimization into a single-pass process (up to K-fold speedup).

#### ⚠️ Limitations
- Requires identical input/output dimensions per block, restricting direct application to architectures with mismatched skip connections like standard U-Nets.
- Validated primarily on models trained from scratch; efficient conversion of pre-trained large models via fine-tuning remains unproven.
- Optimal partitioning granularity and the theoretical basis for performance gains at moderate block counts require further investigation.