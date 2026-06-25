---
layout: page
title: "Large Chunk Test-Time Training"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2505.23884v1)

# Test-Time Training Done Right

#### 🚀 Technical Novelty
* **Mechanism**: Updates model "fast weights" using massive unordered chunks (2K–1M tokens) combined with sliding window attention, replacing per-token or tiny-batch recurrence.
* **Nuance**: Prior TTT methods use <64 token updates causing <5% GPU utilization and limited state scaling; LaCT achieves ~70% FLOPS utilization via pure PyTorch, scales nonlinear states to 40% of parameters, and supports advanced optimizers like Muon without custom kernels.

#### 💡 Yield
- Reaches up to 70% peak GPU throughput on A100s while scaling fast-weight memory capacity an order of magnitude beyond prior work.
- Sets new benchmarks in novel view synthesis (1M+ context), language modeling, and autoregressive video diffusion (56K tokens) without hardware-specific code.

#### ⚠️ Limitations
- Chunk structure must be manually aligned with data topology (e.g., grouping image patches or video frames), limiting direct applicability to inherently sequential data like raw text.
- Linear large-chunk variants underperform on unstructured sequences unless paired with nonlinear states and specialized optimizers.
- Extremely long contexts still face inherent memory bandwidth constraints despite compute efficiency gains.