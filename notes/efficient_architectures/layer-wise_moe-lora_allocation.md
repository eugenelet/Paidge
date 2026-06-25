---
layout: page
title: "Layer-Wise MoE-LoRA Allocation"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2402.08562v1)

# Higher Layers Need More LoRA Experts

#### 🚀 Technical Novelty
* **Mechanism**: Integrates LoRA adapters into a Mixture-of-Experts framework with flexible layer-wise allocation, allowing each Transformer block to use a distinct number of trainable low-rank matrices instead of a fixed count.
* **Nuance**: Departs from uniform expert distribution in prior LoRA-MoE methods by empirically proving and implementing asymmetric allocation, assigning more experts to deeper layers where representational redundancy is lowest and abstract feature learning is highest.

#### 💡 Yield
- Achieves superior performance across six NLP/commonsense QA benchmarks with fewer trainable parameters than all PEFT baselines; layer-wise Frobenius norm analysis confirms lower layers suffer higher expert redundancy, validating the asymmetric design.
- Demonstrates strong continuous learning capabilities, significantly reducing domain knowledge forgetting compared to standard LoRA during sequential fine-tuning.

#### ⚠️ Limitations
- Relies on static, pre-defined layer-wise expert counts rather than fully dynamic per-input routing during training or inference.
- Primarily validated on decoder-only LLMs for text-based tasks; multimodal, vision, or cross-architecture generalization remains unexplored.