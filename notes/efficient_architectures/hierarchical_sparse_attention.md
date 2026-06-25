---
layout: page
title: "Hierarchical Sparse Attention"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.05191v1)

# Double-P: Hierarchical Top-P Sparse Attention for Long-Context LLMs

#### 🚀 Technical Novelty
* **Mechanism**: Two-stage hierarchical estimation that first approximates attention mass at the cluster level using size-weighted centroids, then adaptively refines to token-level computation only when necessary, accelerated via custom CUDA kernels.
* **Nuance**: Replaces rigid top-k budgets and costly single-stage top-p sorting with dynamic, probability-driven compute allocation that guarantees exact attention mass preservation across heterogeneous heads, layers, and decoding steps without linear selection overhead.

#### 💡 Yield
- Near-zero accuracy drop on RULER and LongBench benchmarks up to 128K context lengths compared to full attention.
- Up to 1.78× attention-level speedup and 1.26× end-to-end decoding speedup over state-of-the-art sparse baselines (Quest, RetroInfer).
- Eliminates >60% of top-p estimation overhead by replacing token-level sorting with efficient cluster-level approximation and adaptive budget allocation.

#### ⚠️ Limitations
- Requires manual tuning of dual thresholds (p1, p2) to balance accuracy and latency across different model architectures.
- Evaluated primarily on GQA-based LLaMA-3.1-8B and Qwen-3-8B; cross-architecture generalization and non-GQA variants lack explicit validation.
- GPU kernel optimizations are hardware-specific (CUDA 12.8/PyTorch 2.8 on H100), requiring porting effort for alternative accelerators or memory-constrained deployments.