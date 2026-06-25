---
layout: page
title: "Modular Memory Integration"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.15156v2)

# MEMO: Memory as a Model

#### 🚀 Technical Novelty
* **Mechanism**: A five-step reflection synthesis pipeline distills corpora into compositional QA pairs to train a dedicated MEMORY model, which is queried by a frozen EXECUTIVE model via structured multi-turn query decomposition.
* **Nuance**: Eliminates RAG/ICL context-window limits and retrieval noise while avoiding fine-tuning’s catastrophic forgetting and weight-access barriers, achieving constant inference cost independent of corpus size and full black-box LLM compatibility.

#### 💡 Yield
- Strong benchmark performance on BrowseComp-Plus, NarrativeQA, and MuSiQue across diverse settings; empirically validates corpus-independent retrieval costs, robustness to noisy inputs, and seamless plug-and-play integration with both open and proprietary closed-source LLMs without catastrophic forgetting.

#### ⚠️ Limitations
- Performance heavily depends on the accuracy of the reflection synthesis pipeline; complex queries may still fail if sub-query decomposition falls outside the memory model’s trained compositional distribution or requires out-of-distribution reasoning.