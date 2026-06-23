---
layout: page
title: "Recursive Context Scaling"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.24601v1)

# RECURSIVE LANGUAGE MODELS

#### 🚀 Technical Novelty
* **Mechanism**: Exposes the input prompt as a manipulable variable in an external REPL environment, allowing the LLM to programmatically chunk, filter, and recursively invoke itself over sub-snippets via generated code.
* **Nuance**: Replaces lossy context compaction or fixed retrieval scaffolds with dynamic, inference-time recursion that scales effective context through selective state interaction rather than architectural modifications or training.

#### 💡 Yield
- Handles inputs up to 10M+ tokens while outperforming base LLMs and compaction baselines by double-digit margins across dense reasoning, multi-hop QA, and code understanding tasks; median inference costs remain comparable to or cheaper than direct calls due to selective context viewing.

#### ⚠️ Limitations
- Slight performance degradation on shorter prompts compared to direct base model calls, indicating a deployment trade-off point; high variance in cost/runtime due to unpredictable trajectory lengths; heavy reliance on the underlying LLM's code generation and sub-call management capabilities, leading to model-dependent behavior.