---
layout: page
title: "Optical Direct Feedback Training"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2409.12965v2)

# Streamlined optical training of large-scale modern deep learning architectures with direct feedback alignment

#### 🚀 Technical Novelty
* **Mechanism**: Implements Direct Feedback Alignment (DFA) on a hybrid electronic-photonic platform where an Optical Processing Unit (OPU) passively executes large-scale random matrix multiplications in parallel at up to 1500 TeraOPS under 30W.
* **Nuance**: Replaces the sequential, backward-locking nature of backpropagation with fully parallel layer updates via optical random projections, decoupling training time from electronic compute/memory bottlenecks and enabling superior scaling for ultra-deep/wide networks.

#### 💡 Yield
- Successfully trained >1B parameter Transformers and Diffusion models across language, vision, and generative tasks; demonstrated ODFA surpasses backpropagation in wall-clock training time at extreme scales (~2.7B parameters) while maintaining high energy efficiency.

#### ⚠️ Limitations
- Current optical projection dimensions (10³ × 10³) significantly underutilize the hardware's maximum capacity (10⁶ × 10⁶); GPU memory constraints still limit forward passes and parameter updates for massive models, requiring offloading techniques; smaller networks initially train slower due to fixed optical frame rate limits.