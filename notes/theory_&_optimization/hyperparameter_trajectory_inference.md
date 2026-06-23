---
layout: page
title: "Hyperparameter Trajectory Inference"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.01771v3)

# HYPERPARAMETER TRAJECTORY INFERENCE WITH CONDITIONAL LAGRANGIAN OPTIMAL TRANSPORT

#### 🚀 Technical Novelty
* **Mechanism**: Learns kinetic and potential energy terms via conditional Lagrangian optimal transport to infer geodesic paths between sparse anchor distributions of network outputs.
* **Nuance**: Extends standard trajectory inference by embedding least-action principles and manifold geometry into the cost function, overcoming the non-linear, non-Euclidean dynamics that break conventional flow-matching or linear interpolation.

#### 💡 Yield
- Empirically outperforms direct interpolation and conditional flow matching in reconstructing conditional probability paths across sparse hyperparameter spectra in reinforcement learning and quantile regression tasks.

#### ⚠️ Limitations
- Primarily targets single continuous hyperparameters rather than high-dimensional spaces; performance degrades under extreme data sparsity, though it remains more robust than baselines.