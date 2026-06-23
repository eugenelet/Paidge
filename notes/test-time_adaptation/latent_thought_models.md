---
layout: page
title: "Latent Thought Models"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2502.01567v2)

# Latent Thought Models with Variational Bayes Inference-Time Computation

#### 🚀 Technical Novelty
* **Mechanism**: Explicit layered latent thought vectors are dynamically inferred via fast variational Bayes posterior updates during generation, cross-attending to each Transformer decoder layer.
* **Nuance**: Departs from static parameter LLMs and iterative diffusion by treating inference-time compute as a primary scaling axis; performance scales with both model size and the number of latent optimization steps per token.

#### 💡 Yield
- Achieves GPT-2-Large level perplexity with only ~7% of parameters and significantly reduced training FLOPs per token, establishing new sample/compute efficiency frontiers.
- Demonstrates emergent few-shot arithmetic reasoning and competitive conditional/unconditional text generation at smaller scales, outperforming autoregressive and diffusion baselines on MAUVE and generative perplexity.
- Reveals that increasing inference steps improves both sample and compute efficiency, decoupling performance gains from traditional parameter scaling laws.

#### ⚠️ Limitations
- Relies on a simple isotropic Gaussian prior for latent vectors rather than a learnable, structured prior model.
- Lacks an explicit reward or verifier model in the latent space to guide optimization for complex reasoning tasks.
- Empirical validation is currently limited to GPT-2 scale; scaling behavior beyond this regime remains unexplored.