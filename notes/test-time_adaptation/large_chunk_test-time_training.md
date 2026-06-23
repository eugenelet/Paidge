---
layout: page
title: "Large Chunk Test-Time Training"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2505.23884v1)

# Test-Time Training Done Right

#### 🚀 Technical Novelty
* **Mechanism**: Introduces Large Chunk Test-Time Training (LaCT), updating fast weights over massive chunks (2K–1M tokens) instead of per-token, integrated with sliding window attention and advanced optimizers like Muon.
* **Nuance**: Reverses the conventional TTT assumption that tiny mini-batches are optimal; by treating large chunks as unordered sets, it achieves high parallelism and >70% GPU utilization using pure PyTorch, enabling nonlinear state scaling up to 40% of model parameters.

#### 💡 Yield
- Achieves orders-of-magnitude higher hardware efficiency (up to 70% peak FLOPS) without custom CUDA kernels.
- Scales nonlinear fast weights significantly, outperforming per-token recurrence baselines (e.g., Mamba-2, GLA) in novel view synthesis and language modeling tasks.
- Successfully processes extreme sequence lengths: up to 1M tokens for novel view synthesis and 56K tokens for autoregressive video diffusion.

#### ⚠️ Limitations
- Performance gains are most pronounced when data naturally aligns with chunk structures (e.g., images, video frames); language tasks require additional architectural adjustments like window attention.
- Relies on standard PyTorch compilation rather than hand-optimized custom kernels, which may limit absolute peak throughput compared to highly specialized implementations.
- Validation is concentrated on specific long-context benchmarks; broader generalization across diverse hardware or out-of-distribution sequence types remains unexplored.