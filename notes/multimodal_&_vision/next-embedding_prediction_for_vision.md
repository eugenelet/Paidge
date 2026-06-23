---
layout: page
title: "Next-Embedding Prediction for Vision"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.16922v2)

# Next-Embedding Prediction Makes Strong Vision Learners

#### 🚀 Technical Novelty
* **Mechanism**: Causal Transformer predicts the next patch embedding conditioned on previous ones using a stop-gradient similarity loss, operating entirely in continuous embedding space.
* **Nuance**: Eliminates momentum encoders, discrete tokenizers, pixel decoders, and contrastive losses required by prior SOTA (e.g., JEPA, MAE), relying solely on a single predictive objective within a standard causal architecture.

#### 💡 Yield
- Achieves 83.8% top-1 accuracy on ImageNet-1K with ViT-B and 85.3% with ViT-L after fine-tuning; transfers effectively to semantic segmentation on ADE20K; proves generative pretraining from embeddings is a scalable alternative to representation learning.

#### ⚠️ Limitations
- Poor linear probing performance due to shallow output features; struggles with complex physical reasoning (reflections, shading, shadows) and dense/overlapping objects; current scale limited by ImageNet-1K dataset diversity.