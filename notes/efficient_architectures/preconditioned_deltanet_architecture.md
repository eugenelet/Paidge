---
layout: page
title: "Preconditioned DeltaNet Architecture"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.21100v1)

# Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences

#### 🚀 Technical Novelty
* **Mechanism**: Derives an exact equivalence between linear attention and delta-rule updates under inverse key Gram preconditioning, then implements a practical diagonal approximation alongside efficient chunkwise parallel algorithms.
* **Nuance**: Unlike prior first-order delta-rule approximations that treat all key-value associations uniformly, this method incorporates second-order loss curvature via a learnable diagonal preconditioner while preserving sub-quadratic complexity and GPU-friendly intra-chunk parallelism.

#### 💡 Yield
- Consistent performance improvements across synthetic recall (S-NIAH) and language modeling benchmarks at 340M/1B scales.
- Introduces the DGPS taxonomy, cleanly decoupling decay, gain, preconditioner, and solve axes to unify and guide linear recurrence design.
- Demonstrates that query/key-side preconditioning dynamically modulates write eigenvalues, enhancing long-context memory dynamics without sacrificing training throughput.

#### ⚠️ Limitations
- Diagonal approximation may fail to capture complex cross-dimensional key-key correlations compared to exact inverse Gram computation.
- Evaluations are restricted to 340M/1B scales with fixed architectural configurations; authors explicitly caution against direct cross-architecture comparisons (e.g., GDN vs KDA).
- Chunkwise parallelism introduces a context-length hyperparameter (chunk size C) that forces a trade-off between sequential recurrence fidelity and intra-chunk parallel compute overhead.