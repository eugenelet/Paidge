---
layout: page
title: "Context Tuning for ICL"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2507.04221v2)

# Context Tuning for In-Context Optimization

#### 🚀 Technical Novelty
* **Mechanism**: Initializes trainable soft prompts/prefixes directly from few-shot demonstration examples, then optimizes them via gradient descent to iteratively refine the model's internal key-value (KV) cache representation of the task.
* **Nuance**: Unlike standard prompt tuning (which uses random/unrelated initialization) or vanilla ICL (which relies on a single forward pass), it bridges both by optimizing the context itself with linear training complexity, avoiding the quadratic costs of TTT and CT-Prompt.

#### 💡 Yield
- Outperforms standard ICL and prompt-based adaptation across NLP-LR, MMLU, BBH, and ARC benchmarks; achieves competitive accuracy to Test-Time Training (TTT) at a fraction of the computational cost; enables complementary post-hoc refinement when combined with TTT.

#### ⚠️ Limitations
- Prone to overfitting on few-shot examples without Leave-One-Out Masking or Token Dropout; performance degrades on tasks with extremely few demonstrations (<4) where masking reduces context utility; requires task-specific demonstration data for initialization, limiting zero-shot applicability.