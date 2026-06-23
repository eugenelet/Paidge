---
layout: page
title: "Looped Language Models"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2510.25741v4)

# Scaling Latent Reasoning via Looped Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a weight-tied recurrent transformer stack (LoopLM) that iteratively updates latent states, coupled with an entropy-regularized gating mechanism that dynamically allocates computational depth via learned early-exit probabilities.
* **Nuance**: Unlike standard transformers that scale via parameter count or explicit token generation (CoT), LoopLM decouples compute depth from model size through architectural recurrence, avoiding context-length bloat while enabling input-adaptive latent reasoning.

#### 💡 Yield
- Ouro 1.4B and 2.6B models match or exceed 4B–8B standard LLMs across math, science, and language benchmarks after scaling to 7.7T training tokens.
- Recurrence dramatically improves knowledge manipulation and multi-hop composition without increasing raw knowledge storage capacity (~2 bits/parameter).
- Latent iterative updates yield reasoning traces with higher causal faithfulness and improved safety alignment compared to explicit CoT methods.

#### ⚠️ Limitations
- Requires careful calibration of exit thresholds and entropy regularization coefficients to prevent early-exit collapse or over-computation on simple inputs.
- Gains stem from architectural compute allocation rather than expanded knowledge capacity, limiting direct transferability to tasks requiring massive factual recall without complementary scaling.