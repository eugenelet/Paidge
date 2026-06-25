---
layout: page
title: "One-Step Generative Drifting"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.04770v2)

# Generative Modeling via Drifting

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a "drifting field" that governs sample movement during training by balancing attraction to real data and repulsion from generated samples, minimizing drift via a fixed-point loss with stop-gradient updates.
* **Nuance**: Unlike diffusion/flow models that decompose generation into iterative inference steps or rely on distillation, Drifting Models evolve the pushforward distribution natively during optimization, enabling direct one-step (1-NFE) generation from scratch.

#### 💡 Yield
- Achieves state-of-the-art 1-NFE FID scores on ImageNet 256x256 (1.54 in latent space, 1.61 in pixel space), outperforming prior single-step methods and competing with multi-step diffusion models.
- Successfully transfers to robotic control tasks, matching or exceeding 100-NFE Diffusion Policies with a single inference step.

#### ⚠️ Limitations
- Theoretical gap: While $q=p \Rightarrow V=0$ is proven, the converse ($V=0 \Rightarrow q=p$) does not generally hold, leaving equilibrium conditions theoretically unproven for arbitrary fields.
- Heavy reliance on high-quality feature encoders (e.g., latent-MAE) and struggles without them; pixel-space training requires careful kernel design to avoid vanishing similarities.
- Design choices for the drifting field, kernels, and architecture remain suboptimal and open for future exploration.