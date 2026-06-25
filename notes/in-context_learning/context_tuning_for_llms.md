---
layout: page
title: "Context Tuning for LLMs"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2507.04221v2)

# Context Tuning for In-Context Optimization

#### 🚀 Technical Novelty
* **Mechanism**: Initializes trainable soft prompts or KV cache prefixes directly from task-specific demonstration pairs, then optimizes them via gradient descent at inference time to refine the model's context representation.
* **Nuance**: Unlike traditional prompt tuning that uses random or unrelated tokens, it bootstraps from actual few-shot examples to leverage ICL's inherent capabilities. It bridges zero-shot prompting and test-time training, offering linear complexity (CT-KV) compared to quadratic costs of prior methods while avoiding full weight updates.

#### 💡 Yield
- CT-KV achieves competitive accuracy with Test-Time Training but with significantly lower computational cost and linear time complexity.
- Outperforms standard ICL, Prompt Tuning, and Prefix Tuning across multiple NLP and reasoning benchmarks (MMLU, BBH, ARC).
- Demonstrates complementarity: applying CT-KV post-hoc to TTT yields additional performance gains.

#### ⚠️ Limitations
- CT-Prompt suffers from quadratic training-time complexity relative to the number of examples.
- Requires careful hyperparameter tuning (e.g., Leave-One-Out Masking, Token Dropout) to prevent overfitting or memorization of demonstration pairs.
- Performance on ARC drops if masking is removed due to very few-shot setups, indicating sensitivity to demonstration count.