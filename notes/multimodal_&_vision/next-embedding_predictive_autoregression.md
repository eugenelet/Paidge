---
layout: page
title: "Next-Embedding Predictive Autoregression"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.16922v2)

# Next-Embedding Prediction Makes Strong Vision Learners

#### 🚀 Technical Novelty
* **Mechanism**: Trains a Vision Transformer autoregressively to predict the next patch embedding in continuous space using causal masking and stop-gradient, directly mirroring next-token prediction in LLMs.
* **Nuance**: Eliminates the need for pixel decoders, discrete tokenizers, contrastive pairs, momentum encoders, or task-specific heads, relying purely on a single predictive objective over continuous embeddings rather than representation extraction.

#### 💡 Yield
- Achieves 83.8% (ViT-B) and 85.3% (ViT-L) top-1 accuracy on ImageNet-1K after standard fine-tuning.
- Transfers effectively to dense prediction tasks, delivering strong semantic segmentation performance on ADE20K.
- Proves that generative pretraining principles from NLP can be directly applied to vision via continuous embedding prediction, yielding a scalable, architecturally simple self-supervised paradigm.

#### ⚠️ Limitations
- Performs poorly under standard linear probing because the final autoregressive output remains shallow and closely tied to the initial patch embeddings.
- Struggles with complex physical reasoning tasks like interpreting reflections, shading, shadows, and dense overlapping objects, likely due to ImageNet-1k dataset limitations rather than architectural flaws.
- Current validation is limited to ImageNet-1K; scalability and robustness on more diverse, large-scale vision datasets remain untested.