---
layout: page
title: "End-to-End Latent World Models"
parent: "Embodied AI & Robotics"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.19312v1)

# LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

#### 🚀 Technical Novelty
* **Mechanism**: Jointly optimizes an image encoder and temporal predictor end-to-end using a mean-squared prediction loss plus a SIGReg regularizer that enforces isotropic Gaussian latent distributions to prevent representation collapse.
* **Nuance**: Unlike existing JEPAs that depend on stop-gradients, exponential moving averages, frozen pre-trained encoders, or complex multi-objective losses to stabilize training, LeWM achieves provable anti-collapse with a single tunable hyperparameter and zero training heuristics.

#### 💡 Yield
- Trains stably on a single GPU in hours with only 15M parameters while planning up to 48× faster than foundation-model-based world models under fixed compute.
- Achieves competitive control performance across diverse 2D and 3D environments, with latent spaces that encode meaningful physical structure and reliably detect physically implausible events.

#### ⚠️ Limitations
- Planning horizons remain short, requiring hierarchical extensions for long-horizon reasoning.
- Depends on offline datasets with sufficient interaction coverage, which can be costly or difficult to collect.
- SIGReg regularization may struggle in low-intrinsic-dimensionality environments where matching an isotropic Gaussian prior is challenging.
- Requires explicit action labels for prediction, limiting applicability when action annotations are unavailable.