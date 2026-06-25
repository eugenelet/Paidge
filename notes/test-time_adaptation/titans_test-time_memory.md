---
layout: page
title: "Titans Test-Time Memory"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2501.00663v1)

# Titans: Learning to Memorize at Test Time

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a deep neural long-term memory module that uses gradient-based "surprise" metrics and adaptive decay to continuously update its parameters during inference, operating in parallel with short-term attention.
* **Nuance**: Unlike standard ICL or fixed-weight models, Titans actively adapts its internal state at test time via a meta-optimization process mathematically equivalent to mini-batch gradient descent with momentum and weight decay, decoupling long-term storage from the context window.

#### 💡 Yield
- Scales effectively to >2M context windows with high needle-in-haystack accuracy; outperforms Transformers and modern linear recurrent models (e.g., Mamba, Hyena) across language modeling, commonsense reasoning, time series forecasting, and genomics benchmarks.

#### ⚠️ Limitations
- The deep memory variant incurs slightly lower training throughput than highly optimized kernels like Mamba2 due to complex transition processes; architectural trade-offs exist between expressive memory design (MAC/MAG variants) and raw training speed (MAL variant).