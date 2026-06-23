---
layout: page
title: "Stable End-to-End World Models"
parent: "Embodied AI & Robotics"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.19312v1)

# LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a JEPA that jointly optimizes an encoder and predictor end-to-end from raw pixels using only an MSE prediction loss and a SIGReg regularizer enforcing isotropic Gaussian latent distributions to prevent representation collapse.
* **Nuance**: Eliminates reliance on heuristic stabilization tricks (stop-gradients, EMA), frozen foundation encoders, or multi-objective losses used by prior JEPA methods, replacing them with a provably anti-collapse Gaussian prior and a single tunable hyperparameter.

#### 💡 Yield
- Achieves stable training on a single GPU in hours with only 15M parameters, outperforming existing end-to-end JEPAs while matching foundation-model-based world models at a fraction of the cost.
- Enables planning up to 48× faster than DINO-WM under fixed compute budgets across diverse 2D and 3D control tasks (PushT, OGBench-Cube, Two Room).
- Latent representations encode interpretable physical structure and reliably detect physically implausible events through surprise quantification.

#### ⚠️ Limitations
- Planning horizons remain short; long-horizon reasoning requires hierarchical extensions not yet implemented.
- Performance degrades in low-data-diversity environments where matching a high-dimensional isotropic Gaussian prior becomes challenging.
- Requires explicit action labels for future state prediction, which are costly to collect and may be mitigated by inverse dynamics modeling in future work.