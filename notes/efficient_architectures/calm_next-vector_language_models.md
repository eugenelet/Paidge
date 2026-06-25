---
layout: page
title: "CALM: Next-Vector Language Models"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2510.27688v1)

# CONTINUOUS AUTOREGRESSIVE LANGUAGE MODELS

#### 🚀 Technical Novelty
* **Mechanism**: Compresses chunks of K discrete tokens into a single dense continuous vector via a lightweight autoencoder, enabling next-vector prediction instead of next-token prediction.
* **Nuance**: Differs from prior SOTA by abandoning softmax over massive vocabularies in favor of a likelihood-free framework using Energy Transformers and BrierLM evaluation, scaling semantic bandwidth per step rather than parameter count.

#### 💡 Yield
- Achieves >99.9% token reconstruction accuracy with K=4; establishes BrierLM as a strictly proper, likelihood-free evaluation metric; demonstrates superior performance-compute trade-offs compared to discrete baselines at equivalent quality levels.

#### ⚠️ Limitations
- Current autoencoder focuses heavily on reconstruction rather than semantic structure, leading to brittle latent spaces; performance gap remains between CALM (K=1) and standard Transformers; context-aware autoencoders and semantically grounded latent spaces are left for future work.