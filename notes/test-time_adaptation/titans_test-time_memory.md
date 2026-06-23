---
layout: page
title: "Titans Test-Time Memory"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2501.00663v1)

# Titans: Learning to Memorize at Test Time

#### 🚀 Technical Novelty
* **Mechanism**: A deep neural long-term memory module that adaptively stores historical data into its parameters at test time using gradient-based surprise measures, momentum, and weight decay (forgetting).
* **Nuance**: Unlike standard ICL (which relies on static prompt context) or linear RNNs/Transformers (which compress or cache history in fixed states), Titans explicitly updates weights during inference to memorize "surprising" events, decoupling short-term attention from long-term storage for superior length extrapolation.

#### 💡 Yield
- Outperforms Transformers and modern linear recurrent models (Mamba, HyenaDNA) across language modeling, commonsense reasoning, time series forecasting, and genomics benchmarks.
- Scales to >2M context windows with high accuracy in needle-in-haystack tasks while maintaining fast, parallelizable training via tensorized mini-batch gradient descent.

#### ⚠️ Limitations
- Training throughput is slightly slower than highly optimized kernels like Mamba2 due to the computational overhead of deep memory updates and convolutional operations.
- Architectural variants present a trade-off between expressiveness and speed, requiring careful tuning of decay and momentum hyperparameters for optimal memory management across tasks.