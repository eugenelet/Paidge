---
layout: page
title: "Layer-Wise LoRA Expert Allocation"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2402.08562v1)

# Higher Layers Need More LoRA Experts

#### 🚀 Technical Novelty
* **Mechanism**: Introduces MoLA, a PEFT framework that replaces uniform LoRA-MoE distributions with flexible, layer-wise expert allocation across Transformer blocks.
* **Nuance**: Departs from prior SOTA by empirically proving lower layers suffer representational collapse/redundancy, enabling targeted expert specialization in higher layers rather than fixed per-layer counts.

#### 💡 Yield
- Achieves equal or superior performance on six NLP/commonsense QA benchmarks compared to all PEFT baselines using fewer total parameters.
- Demonstrates that asymmetric allocation (e.g., 2-4-6-8 experts) significantly outperforms uniform configurations by mitigating lower-layer redundancy.
- Exhibits strong continuous learning capabilities, minimizing domain knowledge forgetting during sequential fine-tuning across multiple subjects.

#### ⚠️ Limitations
- Relies on static, pre-defined layer-wise expert configurations rather than fully dynamic, input-aware allocation during training.
- Computational overhead of maintaining multiple routers and expert pairs per layer is not explicitly optimized or compared against standard LoRA inference latency.
- Validation is limited to decoder-only LLMs and instruction-tuning benchmarks, leaving encoder-decoder and multimodal extensions unexplored.