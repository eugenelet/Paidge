---
layout: page
title: "Recursive Long Context Scaling"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.24601v1)

# RECURSIVE LANGUAGE MODELS

#### 🚀 Technical Novelty
* **Mechanism**: Exposes the input prompt as a variable in an external REPL environment, allowing the LLM to write code that programmatically peeks into, chunks, and recursively invokes itself over sub-snippets of the context.
* **Nuance**: Differs from prior context compaction or retrieval scaffolds by avoiding lossy summarization/truncation; instead, it preserves full information density through dynamic, model-driven recursive decomposition and selective context loading during inference.

#### 💡 Yield
- Successfully processes inputs up to 10M+ tokens (two orders of magnitude beyond standard context windows) with minimal performance degradation across dense reasoning tasks like OOLONG and BrowseComp-Plus.
- Outperforms direct LLM calls, context compaction, and retrieval agents by double-digit percentage gains while maintaining comparable or lower median inference costs per query.
- Demonstrates emergent, model-driven context management behaviors including regex-based filtering, uniform chunking for sub-calls, and variable-stitched long-output generation without explicit training.

#### ⚠️ Limitations
- Performance slightly degrades on shorter prompts compared to base models, indicating a tradeoff point where direct inference is preferable.
- High variance in inference cost and runtime due to unpredictable trajectory lengths; outlier runs can be significantly more expensive than base model queries.
- Behavior and success rates vary substantially across different base models (e.g., GPT-5 vs. Qwen3-Coder) without task-specific prompt tuning or system prompt adjustments.