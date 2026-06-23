---
layout: page
title: "Entropy-Based Adaptive Speculative Decoding"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2410.18351v1)

# AdaEDL: Early Draft Stopping for Speculative Decoding of Large Language Models via an Entropy-based Lower Bound on Token Acceptance Probability

#### 🚀 Technical Novelty
* **Mechanism**: Uses the draft model's output entropy to approximate a lower bound on token acceptance probability, enabling dynamic, on-the-fly early stopping of the drafting process.
* **Nuance**: Replaces static draft lengths and max-confidence thresholds by evaluating the full probability distribution via entropy, eliminating the need for training task-specific predictors while maintaining robustness across varying sampling temperatures.

#### 💡 Yield
- Outperforms static draft-length speculative decoding by 10%-57% and other training-free methods by up to 10% across multiple datasets and model pairs.
- Maintains inference speed gains even at high sampling temperatures (up to 1.7) where baseline speculative decoding collapses below autoregressive speeds.
- Requires zero training or dataset-specific fine-tuning, acting as a plug-and-play acceleration layer for existing LLM systems.

#### ⚠️ Limitations
- Sensitive to the initial stopping threshold (λ), particularly for short generations where insufficient drafting rounds prevent dynamic threshold convergence.
- Relies on the draft model's distributional alignment with the target; performance gains diminish if the draft model is poorly correlated or untrained.
- Entropy scaling factor (γ) was fixed at 0.2 in experiments, leaving room for dataset-specific tuning or dynamic adaptation in future work.