---
layout: page
title: "Latent Thought Models"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2502.01567v2)

# Latent Thought Models with Variational Bayes Inference-Time Computation

#### 🚀 Technical Novelty
* **Mechanism**: Dual-rate variational Bayes optimization that rapidly adapts instance-specific latent thought vectors during inference while slowly updating global decoder weights via cross-attention.
* **Nuance**: Introduces inference steps and latent dimensionality as independent scaling axes, decoupling sample efficiency from fixed model parameter counts unlike traditional autoregressive or diffusion models that rely solely on static weights.

#### 💡 Yield
- Matches GPT-2-Large validation perplexity with only 6.7% of parameters and equivalent training compute (trFLOPs/tok).
- Proves performance scales along inference steps and latent size, demonstrating compute-per-token can substitute for data/model scaling.
- Exhibits emergent few-shot arithmetic reasoning at scales where baseline LLMs fail, while maintaining competitive unconditional/conditional generation speed and quality.

#### ⚠️ Limitations
- Relies on a simplistic isotropic Gaussian prior rather than structured or learnable prior models for richer latent representations.
- Lacks reward/verifier models in the latent space to guide optimization toward complex reasoning or planning tasks.
- Empirical validation is currently confined to GPT-2 scale; larger-scale architectural and scaling law validations remain unexplored.