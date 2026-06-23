---
layout: page
title: "Hierarchical Vision-LLM Fusion"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.00086v1)

# Hierarchical Pre-Training of Vision Encoders with Large Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a hierarchical cross-attention framework that injects multi-level visual features from a vision encoder into an LLM across multiple layers, stabilized by a three-stage progressive training pipeline (projector alignment → joint optimization → end-to-end fine-tuning).
* **Nuance**: Differs from standard late-fusion or frozen-LLM paradigms (e.g., BLIP-2, Flamingo) by explicitly pre-training the vision encoder through structured cross-modal gradient flow, preserving fine-grained spatial hierarchies rather than collapsing embeddings into a single flattened vector.

#### 💡 Yield
- Consistently outperforms self-attention baselines on image classification (ImageNet, CIFAR) and complex vision-language reasoning benchmarks (MME, GQA, OK-VQA, ScienceQA).
- Delivers a 3× speedup in per-epoch training time and reduces peak GPU memory consumption by 55% while enabling granular gradient propagation into early encoder layers.

#### ⚠️ Limitations
- Connection density ablations were minimal ("without extensive ablations"), leaving optimal integration sparsity less rigorously quantified.
- Currently validated only on static images and specific LLM scales, with explicit extensions to video modalities and dynamic layer selection deferred to future work.