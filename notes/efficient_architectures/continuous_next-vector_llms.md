---
layout: page
title: "Continuous Next-Vector LLMs"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2510.27688v1)

# CONTINUOUS AUTOREGRESSIVE LANGUAGE MODELS

#### 🚀 Technical Novelty
* **Mechanism**: Compresses chunks of K discrete tokens into a single dense continuous vector via a lightweight autoencoder, enabling next-vector prediction instead of next-token prediction.
* **Nuance**: Abandons the softmax vocabulary bottleneck entirely by adopting a likelihood-free energy-based framework and BrierLM metric, avoiding iterative diffusion/flow sampling while maintaining controllable temperature sampling.

#### 💡 Yield
- Achieves >99.9% token reconstruction with K=4 using only 10 latent dimensions; establishes BrierLM as a strictly proper likelihood-free evaluation metric; demonstrates superior performance-compute trade-offs compared to discrete baselines at equivalent quality.

#### ⚠️ Limitations
- Current autoencoder lacks semantic grounding in the latent space (focuses only on reconstruction); performance gap remains between CALM (K=1) and standard Transformers; context-aware autoencoders and semantically rich latent spaces are left for future work.