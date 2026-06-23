---
layout: page
title: "Stable Looped Language Models"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.12946v1)

# Parcae: Scaling Laws For Stable Looped Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Constrains the spectral norm of injection parameters using negative diagonal discretization and input normalization to prevent residual stream explosion in recurrent layers.
* **Nuance**: Replaces fragile hyperparameter tuning and post-norm tricks with a control-theoretic dynamical systems framework, treating looping as an orthogonal compute-scaling axis rather than a fixed-depth approximation.

#### 💡 Yield
- Derives unified scaling laws showing training FLOPs should scale looping and data via power laws, while test-time compute follows a predictable saturating exponential decay.
- Achieves up to 6.3% lower validation perplexity than prior looped models and matches Transformer quality at twice the parameter count under fixed budgets.

#### ⚠️ Limitations
- Empirical validation is limited to smaller scales (up to 1.3B parameters); large-scale FLOP extrapolation remains unverified.
- Test-time quality gains saturate at training recurrence depth, necessitating more inference steps for marginal improvements.