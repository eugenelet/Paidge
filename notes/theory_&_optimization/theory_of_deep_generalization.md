---
layout: page
title: "Theory of Deep Generalization"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.01172v1)

# A Theory of Generalization in Deep Learning

#### 🚀 Technical Novelty
* **Mechanism**: Partitions output space via cumulative dissipation Gramian into a signal channel (where loss dissipates) and a reservoir (where noise is trapped), enabling exact population-risk estimation from a single training run.
* **Nuance**: Extends frozen-kernel NTK theory to the full feature-learning regime with an evolving kernel, mechanistically unifying benign overfitting, double descent, implicit bias, and grokking within a single bias-variance decomposition.

#### 💡 Yield
- Derives an exact population-risk objective computable from per-example Jacobians during training, requiring only one extra state vector in Adam.
- Empirically accelerates grokking by 5×, suppresses memorization in PINNs/INRs, and improves DPO fine-tuning under noisy preferences while staying closer to the reference policy.

#### ⚠️ Limitations
- Relies on squared loss assumptions for the core signal/reservoir decomposition (though claims broader applicability).
- Requires computing per-example Jacobians and maintaining a cumulative dissipation Gramian, which may scale poorly with extremely large batch sizes or memory-constrained setups.
- Theoretical guarantees assume C² parameterization and specific gradient flow/SGD dynamics; practical performance depends on the SNR threshold condition (μ_k² > σ_k²/(b-1)).