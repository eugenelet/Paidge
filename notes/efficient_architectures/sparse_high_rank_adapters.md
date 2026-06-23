---
layout: page
title: "Sparse High Rank Adapters"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2407.16712v1)

# Rapid Switching and Multi-Adapter Fusion via Sparse High Rank Adapters

#### 🚀 Technical Novelty
* **Mechanism**: Directly finetunes 1–2% of pretrained weights using extremely sparse masks (98–99% zeros) during backpropagation, storing adapters as sparse weight-index pairs instead of dense low-rank matrices.
* **Nuance**: Unlike LoRA’s dense matrix addition that overwrites all base weights upon fusion, SHiRA only overwrites a tiny fraction of indices at inference time, eliminating latency spikes and drastically reducing cross-concept interference during multi-adapter use.

#### 💡 Yield
- Achieves up to 2.7% higher average accuracy than LoRA on LLaMA-7B commonsense reasoning tasks while modifying only 1% of parameters.
- Enables up to 10× faster CPU weight loading for rapid adapter switching and significantly reduces concept loss/artifacts in multi-adapter image generation (Stable Diffusion).
- Consumes ~16.6% lower peak GPU memory during training than LoRA and remains fully orthogonal/composable with advanced adapters like DoRA.

#### ⚠️ Limitations
- Structured masking variants (SHiRA-Struct) underperform on complex LLM tasks due to inherent rank limitations.
- Performance heavily depends on mask selection strategy (e.g., SNIP, Grad, or Weight Magnitude), requiring task-specific calibration or ablation.
- Does not address test-time distribution shifts; remains a parameter-efficient fine-tuning method rather than a dynamic adaptation framework.