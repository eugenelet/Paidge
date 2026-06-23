---
layout: page
title: "Modular Memory Architecture"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.15156v2)

# MEMO: Memory as a Model

#### 🚀 Technical Novelty
* **Mechanism**: A five-step data synthesis pipeline distills target corpora into compositional "reflections" to train a dedicated MEMORY model, which is queried via a structured multi-turn protocol by a frozen EXECUTIVE model.
* **Nuance**: Decouples knowledge storage from reasoning, eliminating context-window limits and retrieval noise inherent in RAG/ICL while avoiding catastrophic forgetting and computational costs of parametric fine-tuning.

#### 💡 Yield
- Achieves strong benchmark performance (BrowseComp-Plus, NarrativeQA, MuSiQue) against parametric and non-parametric baselines.
- Maintains constant retrieval cost independent of corpus size at inference time.
- Ensures plug-and-play compatibility with any LLM (open or proprietary) without accessing weights or logits.

#### ⚠️ Limitations
- Training pipeline relies on a GENERATOR model to synthesize reflections, potentially introducing synthesis bias or computational overhead.
- The fixed reflection interface and multi-turn protocol may struggle with highly novel query formulations not aligned with the synthesized knowledge structure.