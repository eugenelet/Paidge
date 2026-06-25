---
layout: page
title: "Hyperparameter Trajectory Inference"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.01771v3)

# HYPERPARAMETER TRAJECTORY INFERENCE WITH CONDITIONAL LAGRANGIAN OPTIMAL TRANSPORT

#### 🚀 Technical Novelty
* **Mechanism**: Learns a data-dependent conditional Lagrangian (kinetic & potential energy terms) to model non-linear hyperparameter-induced dynamics, using optimal transport maps and geodesics to construct a continuous surrogate probability path.
* **Nuance**: Differs from standard Euclidean interpolation or conditional flow matching by embedding least-action principles and manifold inductive biases into the cost function, ensuring feasible, physically meaningful trajectories across sparse, high-dimensional hyperparameter spectra.

#### 💡 Yield
- Empirically outperforms direct interpolation and conditional flow matching baselines in reconstructing conditional probability paths under sparse anchor distributions.
- Successfully enables inference-time hyperparameter adjustment for reinforcement learning policies (cancer treatment reward balancing) and quantile regression uncertainty bounds without retraining.

#### ⚠️ Limitations
- Performance degrades with increasing data sparsity, though it degrades less than baselines; requires careful selection of anchor distributions across the hyperparameter spectrum.
- Currently restricted to single continuous hyperparameters and relies on neural approximations for optimal transport maps, which may face scalability challenges in extremely high-dimensional output spaces.