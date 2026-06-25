---
layout: page
title: "Training-Free Looped Transformers"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.23872v1)

# Training-Free Looped Transformers

#### 🚀 Technical Novelty
* **Mechanism**: Applies a lightweight, training-free wrapper that iteratively loops a contiguous mid-stack block of frozen transformer layers at inference, using higher-order Runge-Kutta numerical integration to refine the forward pass as an ODE approximation.
* **Nuance**: Unlike prior looped transformers that require end-to-end training with tied weights, this method retrofits recurrence onto off-the-shelf checkpoints purely at test time, avoiding catastrophic degradation by carefully selecting iteration modes (block-mode for dense, layer-mode for MoE) and integration strategies.

#### 💡 Yield
- Achieves consistent accuracy gains (+1.14 to +2.64 pp) across 7 model families (dense, MoE, MLA+MoE) on knowledge-heavy benchmarks like MMLU-Pro and GPQA-Main without any parameter updates or hyperparameter tuning per cell.
- Demonstrates that layer-mode iteration is critical for MoE architectures to prevent expert routing instability during loops, while K-stage Runge-Kutta outperforms naive looping and other fixed-point accelerators.

#### ⚠️ Limitations
- Increases inference latency proportionally to the loop count (K) and window width due to extra forward passes through the looped block.
- Performance gains diminish or become neutral for sub-3B distilled checkpoints on certain knowledge tasks, indicating a size/task-dependent failure boundary.
- Requires careful selection of iteration mode (block vs. layer) based on backbone architecture, with MoE models strictly requiring layer-mode to avoid routing thrashing.