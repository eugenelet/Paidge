---
layout: page
title: "One-Step Drifting Generation"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.04770v2)

# Generative Modeling via Drifting

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a "drifting field" that computes attraction/repulsion forces between real and generated samples, driving the pushforward distribution toward the data distribution during training via a fixed-point loss.
* **Nuance**: Unlike diffusion/flow models that iterate at inference time or GANs that use adversarial optimization, this method evolves the distribution inherently through standard parameter updates (SGD) and minimizes drift directly without adversarial dynamics or iterative sampling.

#### 💡 Yield
- Achieves 1.54 FID on ImageNet 256×256 (latent) and 1.61 FID (pixel) with single-step inference, outperforming prior one-step methods.
- Theoretically proves equilibrium when distributions match; successfully transfers to robotic control matching multi-step diffusion policies.

#### ⚠️ Limitations
- Theoretical converse (V=0 implies q=p) does not generally hold in theory.
- Requires a strong feature encoder; fails to work effectively on raw pixel space without it.
- Design of drifting field kernels and architecture remains suboptimal and open for future exploration.