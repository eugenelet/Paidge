---
layout: page
title: "Supervised Memory Training"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2606.06479v1)

# Pretraining Recurrent Networks without Recurrence

#### 🚀 Technical Novelty
* **Mechanism**: Decouples memory representation (learned via a parallel Transformer encoder predicting future states) from memory dynamics (trained via one-step supervised transitions), eliminating recurrent unrolling and BPTT.
* **Nuance**: Unlike linear RNNs or iterative parallel solvers that approximate BPTT, SMT achieves true O(1) gradient paths by treating memory encoding as a permutation-invariant set problem, avoiding both sequential bottlenecks and the expressivity limits of linear transitions.

#### 💡 Yield
- Outperforms BPTT on language modeling and pixel sequence tasks for long-range dependency learning.
- Enables fully time-parallel RNN pretraining with fixed-size memory inference.
- Provides theoretical grounding linking predictive state representations to sufficient statistics for future prediction.

#### ⚠️ Limitations
- Teacher Transformer's parallel architecture imposes circuit depth limits, potentially restricting ultimate expressivity compared to full BPTT.
- Requires lightweight post-training/fine-tuning to correct memory drift and adapt to specific downstream tasks.
- Current implementation trains only a single memory state per sequence; scaling to all timesteps may differ.