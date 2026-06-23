---
layout: page
title: "Deep Learning Generalization Theory"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.01172v1)

# A Theory of Generalization in Deep Learning

#### 🚀 Technical Novelty
* **Mechanism**: Partitions the empirical neural tangent kernel’s output space into a “signal channel” (where SGD accumulates coherent population signal via fast linear drift) and a “reservoir” (where label noise is trapped in test-invisible directions). Derives an exact population-risk objective from a single training run, implemented as an SNR preconditioner on Adam.
* **Nuance**: Unlike frozen-kernel or vacuous capacity bounds, this framework operates in the full feature-learning regime with an evolving kernel (O(1) operator norm drift), mechanistically unifying benign overfitting, double descent, implicit bias, and grokking within a single output-space decomposition.

#### 💡 Yield
- Proves generalization survives full feature learning and maps classical phenomena to signal/reservoir dynamics.
- Derives a validation-free population-risk objective that reduces to an SNR preconditioner adding only one state vector.
- Empirically accelerates grokking by 5×, suppresses memorization in PINNs/INRs (2.36× faster convergence), and improves DPO fine-tuning under noisy preferences (1.13–1.16× accuracy gain, 3× less reward drift).

#### ⚠️ Limitations
- Requires tracking per-example Jacobians and cumulative dissipation Gramian during training, which may scale poorly with extreme model widths or complex architectures.
- Core theoretical derivations rely on squared loss dynamics, though the framework claims broader applicability.
- Empirical validation focuses on PINNs, implicit neural representations, and DPO rather than large-scale language models.