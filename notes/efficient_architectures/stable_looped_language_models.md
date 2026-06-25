---
layout: page
title: "Stable Looped Language Models"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.12946v1)

# Parcae: Scaling Laws For Stable Looped Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Constrains the spectral norm of injection parameters using discretized negative diagonal parameterization and input normalization to prevent residual stream explosion in recurrent layers.
* **Nuance**: Analytically models looping as a nonlinear time-variant dynamical system, deriving exact divergence conditions via linearization to eliminate the sensitive hyperparameter tuning and post-norm stabilization required by prior recurrent architectures.

#### 💡 Yield
- Achieves up to 6.3% lower validation perplexity over prior looped models and matches downstream quality of Transformers twice its size under fixed parameter/data budgets.
- Derives predictable power laws demonstrating that FLOP-optimal training scales looping and data in tandem, while test-time compute follows a tightly predictable saturating exponential decay.
- Establishes a unified scaling law connecting training depth floors with test-time recurrence ceilings across model sizes (140M to 1.3B).

#### ⚠️ Limitations
- Empirical validation is currently limited to smaller architectures (up to 1.3B parameters), leaving large-scale FLOP budget scalability unverified.
- Increasing mean recurrence depth linearly increases required test-time inference steps, creating latency trade-offs that require future algorithmic mitigation.