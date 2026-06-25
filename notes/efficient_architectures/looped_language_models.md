---
layout: page
title: "Looped Language Models"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2510.25741v4)

# Scaling Latent Reasoning via Looped Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Introduces the LoopLM architecture, which recursively applies a shared weight-tied transformer block during the forward pass, coupled with an entropy-regularized exit gate that dynamically allocates recurrent depth per input.
* **Nuance**: Unlike standard scaling or inference-time Chain-of-Thought (which expands output sequences and context windows), LoopLM deepens its internal computational graph via parameter sharing, decoupling compute depth from model size while preserving causal faithfulness and reducing post-hoc rationalization.

#### 💡 Yield
- Ouro 1.4B and 2.6B models match or exceed 4B–8B standard transformers across math, science, and reasoning benchmarks after scaling to 7.7T tokens.
- Recurrence dramatically improves knowledge manipulation and multi-hop composition without increasing raw knowledge storage capacity (~2 bits/parameter).
- Adaptive latent updates yield safer outputs and reasoning traces more tightly aligned with final predictions than explicit CoT.

#### ⚠️ Limitations
- Entropy-regularized gating requires careful hyperparameter tuning to prevent collapse to extreme depths or premature shallow exits.
- Recurrent architectures inherently trade parallelization efficiency for parameter efficiency, potentially impacting raw inference throughput compared to standard transformers.
- Scaling laws and saturation behaviors are newly characterized; long-term stability across diverse domains remains an open empirical question.