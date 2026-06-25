---
layout: page
title: "Entropy-Based Draft Stopping"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2410.18351v1)

# AdaEDL: Early Draft Stopping for Speculative Decoding of Large Language Models via an Entropy-based Lower Bound on Token Acceptance Probability

#### 🚀 Technical Novelty
* **Mechanism**: Dynamically terminates the token drafting phase during speculative decoding by computing a lower bound on expected acceptance probability using draft model logits' entropy.
* **Nuance**: Unlike prior adaptive methods that rely on static confidence thresholds or require training task-specific predictors, AdaEDL is entirely training-free and leverages distributional uncertainty (entropy) for robust, plug-and-play acceleration.

#### 💡 Yield
- Achieves 10%-57% inference speedups over static draft-length speculative decoding and up to 10% gains over other training-free baselines across multiple datasets and model pairs.
- Maintains consistent performance gains even at high sampling temperatures where traditional speculative decoding collapses below autoregressive baselines.
- Eliminates the need for dataset-specific fine-tuning or hyperparameter search, enabling seamless integration into existing LLM inference pipelines.

#### ⚠️ Limitations
- Sensitive to the initial stopping threshold (λ), particularly for short-generation tasks where insufficient drafting rounds hinder dynamic threshold convergence.
- Relies on a fixed entropy scaling factor (γ ≈ 0.2) in current implementations; optimal γ may vary across models and requires further investigation.
- Efficiency gains are inherently bounded by the draft model's computational cost and alignment with the target model, limiting absolute speedups in highly mismatched setups.