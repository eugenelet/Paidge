---
layout: page
title: "Hierarchical Vision LLM Pretraining"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.00086v1)

# Hierarchical Pre-Training of Vision Encoders with Large Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Multi-layer cross-attention that projects hierarchical vision encoder features directly into the LLM’s input space, preserving spatial and semantic gradients across network depths.
* **Nuance**: Diverges from late-fusion or frozen-Q-former paradigms by explicitly pre-training the vision encoder via a progressive three-stage pipeline to enable dynamic, structured cross-modal alignment rather than shallow embedding injection.

#### 💡 Yield
- Achieves superior performance on classification and vision-language benchmarks (MME, GQA, OK-VQA, ScienceQA) while delivering a 3× per-epoch training speedup and 55% peak GPU memory reduction through compute-optimal hierarchical connections.

#### ⚠️ Limitations
- Relies on qualitative gradient/attention visualizations rather than quantitative stability metrics; connection density was fixed at 25% without exhaustive ablation; scalability to temporal modalities (video) remains unexplored.