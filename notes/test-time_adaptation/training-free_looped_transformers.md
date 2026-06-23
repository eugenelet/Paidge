---
layout: page
title: "Training-Free Looped Transformers"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.23872v1)

# Training-Free Looped Transformers

#### 🚀 Technical Novelty
* **Mechanism**: Wraps a frozen checkpoint's contiguous mid-stack layers in an iterative loop at inference, modeling each pre-norm block as a forward Euler step on an implicit ODE and refining it via higher-order solvers (e.g., K-stage Runge-Kutta).
* **Nuance**: Eliminates the end-to-end training and weight-tied architecture required by prior recurrent transformers; introduces "layer-mode" iteration to stabilize expert routing in MoE models during inference, which block-mode fails to do.

#### 💡 Yield
- Delivers consistent +1.14–2.64 pp accuracy gains across 7 model families (dense, MoE, MLA+MoE) on knowledge-heavy benchmarks without per-cell hyperparameter tuning or parameter updates.
- Demonstrates that naive looping degrades performance by pushing activations out of the trained regime, while ODE-inspired sub-stepping strategies stabilize inference and extract latent reasoning capacity from frozen weights.

#### ⚠️ Limitations
- Increases inference latency proportionally to the loop count K due to extra forward passes through the window.
- Provides diminishing returns (3–4× smaller gains) for MLA-based MoE models and shows instability on sub-3B distilled checkpoints for certain knowledge tasks.