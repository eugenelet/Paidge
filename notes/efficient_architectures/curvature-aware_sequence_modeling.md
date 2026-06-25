---
layout: page
title: "Curvature-Aware Sequence Modeling"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.21100v1)

# Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences

#### 🚀 Technical Novelty
* **Mechanism**: Derives exact mathematical equivalences between linear attention and DeltaNet under inverse key Gram preconditioning, then implements a practical diagonal approximation paired with efficient chunkwise parallel algorithms for online least-squares updates.
* **Nuance**: Prior delta-rule models apply uniform decay or ignore loss curvature during online optimization; this method dynamically scales the write key via learned diagonal preconditioners, capturing second-order geometry while preserving sub-quadratic compute and stable parallel training.

#### 💡 Yield
- Theoretical unification proving that exact inverse Gram preconditioning makes linear attention and DeltaNet mathematically equivalent, with stable diagonal approximations enabling efficient chunkwise parallel forms.
- Consistent perplexity and zero-shot accuracy gains across 340M/1B scale language models on commonsense reasoning and in-context retrieval (S-NIAH) benchmarks, with improved write-eigenvalue expressivity for long-context recall.

#### ⚠️ Limitations
- Diagonal approximation discards cross-dimensional curvature information present in the full key Gram matrix, potentially limiting optimization fidelity in high-dimensional feature spaces.
- Evaluations are restricted to 340M/1B scales and synthetic recall tasks; scalability to larger models or extended contexts requires further validation.
- Cross-architectural comparisons (e.g., vs. KDA) are cautioned against due to fixed configuration choices rather than fully optimized baseline tuning.