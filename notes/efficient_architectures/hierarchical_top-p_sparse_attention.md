---
layout: page
title: "Hierarchical Top-P Sparse Attention"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.05191v1)

# Double-P: Hierarchical Top-P Sparse Attention for Long-Context LLMs

#### 🚀 Technical Novelty
* **Mechanism**: A hierarchical two-stage top-p framework that performs coarse cluster-level attention mass estimation followed by adaptive token-level refinement, paired with GPU-optimized kernels to minimize selection overhead.
* **Nuance**: Replaces rigid fixed-budget (top-k) or single-stage top-p selection with dynamic, step-wise budget allocation that guarantees preserved attention mass while eliminating the linear selection overhead and constraint violations of prior methods.

#### 💡 Yield
- Achieves near-zero accuracy drop on RULER and LongBench benchmarks up to 128K context lengths compared to full attention.
- Delivers up to 1.78× attention-level speedup and 1.26× end-to-end decoding speedup over state-of-the-art sparse baselines (Quest, RetroInfer).
- Eliminates target mass violation rates inherent in fixed-budget methods across heterogeneous heads and layers.

#### ⚠️ Limitations
- Requires empirical tuning of hierarchical thresholds (p1, p2) to balance accuracy and latency per model/task.
- Evaluated primarily on LLaMA3.1-8B and Qwen3-8B; generalization to other architectures or training paradigms is not explicitly validated.