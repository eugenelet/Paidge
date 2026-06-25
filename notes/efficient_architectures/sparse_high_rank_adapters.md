---
layout: page
title: "Sparse High Rank Adapters"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2407.16712v1)

# Rapid Switching and Multi-Adapter Fusion via Sparse High Rank Adapters

#### 🚀 Technical Novelty
* **Mechanism**: Applies extreme gradient-masking during backpropagation to freeze 98–99% of base weights, training only a sparse subset (1–2%) that is stored as weight-value/index pairs for direct inference-time overwriting.
* **Nuance**: Unlike LoRA which fuses dense low-rank matrices and overwrites nearly all base parameters (blocking rapid switching), SHiRA preserves the original weight tensor structure, enabling instant adapter swapping on edge devices and naturally orthogonal multi-adapter fusion with minimal cross-concept interference.

#### 💡 Yield
- Achieves up to 2.7% higher average accuracy than LoRA on LLaMA-7B commonsense reasoning tasks while changing only 1% of parameters at inference time.
- Reduces peak GPU training memory by ~16.6% compared to standard LoRA while maintaining comparable training speed, and integrates seamlessly with advanced adapters like DoRA.
- Eliminates concept loss/artifacts in multi-adapter fusion, delivering up to 6.69% higher fused accuracy on LLMs and superior image quality (HPSv2) on Stable Diffusion style-transfer tasks.

#### ⚠️ Limitations
- Mask design sensitivity: Structured masks (SHiRA-Struct) underperform on complex LLM tasks, requiring task-aware mask selection (e.g., SNIP, Grad, WM).
- Evaluated primarily on LLaMA-7B/2-7B and Stable Diffusion; broader generalization to larger-scale foundation models or novel architectures remains unverified.
- Relies on calibration sets for gradient-based masking strategies, introducing a minor pre-training overhead not present in zero-shot PEFT methods.