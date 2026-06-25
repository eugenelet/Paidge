---
layout: page
title: "Manifold-Constrained Hyper-Connections"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.24880v1)

# mHC: Manifold-Constrained Hyper-Connections

#### 🚀 Technical Novelty
* **Mechanism**: Projects learnable residual stream mixing matrices onto a doubly stochastic manifold via iterative Sinkhorn-Knopp optimization to enforce bounded forward/backward signal propagation.
* **Nuance**: Unlike standard HC that suffers from unbounded gradient explosion, identity mapping loss, and memory overhead across layers, mHC mathematically constrains the connection space while fusing kernels and overlapping communication for infrastructure efficiency.

#### 💡 Yield
- Consistent performance gains over baseline and unconstrained HC on 27B LLM benchmarks (e.g., +2.1% BBH, +2.3% DROP) with robust scaling across compute and token budgets.
- Reduces maximum propagation gain magnitude by three orders of magnitude, ensuring stable signal flow without sacrificing FLOP efficiency or topological expressivity.

#### ⚠️ Limitations
- Manifold projection relies on truncated Sinkhorn-Knopp iterations (20 steps for speed), causing slight deviations from perfect doubly stochastic constraints.
- Full efficiency gains depend on custom infrastructure implementations (kernel fusion, DualPipe overlap); naive deployment may incur overhead from added architectural complexity.