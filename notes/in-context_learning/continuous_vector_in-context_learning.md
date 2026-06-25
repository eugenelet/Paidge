---
layout: page
title: "Continuous Vector In-Context Learning"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2410.05629v2)

# VECTOR-ICL: IN-CONTEXT LEARNING WITH CONTINUOUS VECTOR REPRESENTATIONS

#### 🚀 Technical Novelty
* **Mechanism**: A lightweight, trainable projector maps arbitrary encoder embeddings into the LLM's native text embedding space, allowing continuous vectors to function as direct in-context demonstrations.
* **Nuance**: Unlike standard ICL that relies on discrete tokenization or natural language prompts, Vector-ICL bypasses lexical constraints entirely, enabling seamless cross-modal few-shot adaptation without modifying the base LLM weights.

#### 💡 Yield
- Achieves competitive or superior few-shot performance across text classification, summarization, numerical function regression, time-series, graph classification, and fMRI decoding compared to standard ICL and domain-specific tuned models.
- Demonstrates that pretraining projectors on general language modeling objectives is sufficient to unlock Vector-ICL, while task-specific fine-tuning further amplifies accuracy without retraining the decoder.

#### ⚠️ Limitations
- Strictly dependent on external black-box encoders to generate initial embeddings; performance is bounded by the quality and alignment of those source representations.
- Cross-modal tasks often require non-linear projectors rather than simple linear mappings, increasing architectural complexity and training overhead for heterogeneous data types.