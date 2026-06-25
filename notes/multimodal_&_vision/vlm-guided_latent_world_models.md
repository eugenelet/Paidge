---
layout: page
title: "VLM-Guided Latent World Models"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.22281v1)

# ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model

#### 🚀 Technical Novelty
* **Mechanism**: Dual-temporal architecture pairing a dense-frame JEPA predictor with a uniformly sampled VLM-thinker branch, connected via a hierarchical pyramid feature extractor that distills multi-layer VLM representations into FiLM modulation signals for the latent predictor.
* **Nuance**: Avoids the language-output bottleneck and compute sparsity of standalone VLMs by treating them purely as semantic/knowledge guides, while overcoming JEPA's limited temporal context through long-horizon knowledge injection rather than extended dense observation windows.

#### 💡 Yield
- Surpasses both V-JEPA and Qwen3-VL baselines on EgoDex and EgoExo4D trajectory prediction metrics (ADE/FDE) and latent forecasting quality (FD, SL1, CD).
- Enables stable long-horizon recursive rollouts (up to 32 steps) with significantly improved semantic grounding and physical consistency in egocentric manipulation tasks.

#### ⚠️ Limitations
- Inherently constrained by the quadratic attention cost and memory footprint of large VLMs, limiting real-time deployment scalability.
- Sensitive to temporal stride alignment between dense JEPA frames and sparse VLM sampling, requiring careful architectural tuning to prevent feature misalignment.
- Evaluated primarily on egocentric manipulation/human activity datasets, with generalization to broader robotic control or open-world environments unverified.