---
layout: page
title: "Vector In-Context Learning"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2410.05629v2)

# VECTOR-ICL: IN-CONTEXT LEARNING WITH CONTINUOUS VECTOR REPRESENTATIONS

#### 🚀 Technical Novelty
* **Mechanism**: Compresses arbitrary input data via black-box encoders, then aligns the resulting embeddings to the LLM's space using lightweight projectors (linear or non-linear), treating them as discrete "box tokens" for in-context demonstrations.
* **Nuance**: Eliminates the need for linguistic tokenization or weight updates by bridging continuous data directly into the LLM's context window, contrasting with standard few-shot ICL which is constrained to text-based demonstrations and domain-specific adapters.

#### 💡 Yield
- Surpasses few-shot ICL and domain-specific tuned models across text reconstruction, numerical function regression, classification, summarization, molecule captioning, time-series, graph classification, and fMRI decoding.
- Enables precise arithmetic and large-number function approximation where token-based LLMs typically fail due to discretization artifacts.
- Demonstrates that pretraining projectors with general next-token prediction is sufficient to unlock Vector-ICL, while task-specific fine-tuning yields further gains.

#### ⚠️ Limitations
- Depends on external pre-trained encoders for initial vector extraction, and cross-modal alignment may require complex non-linear projectors rather than simple linear mappings. (Note: Formal limitations section not fully provided in the excerpt, but these constraints are explicitly noted in the methodology).