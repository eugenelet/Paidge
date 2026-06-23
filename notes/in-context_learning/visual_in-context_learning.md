---
layout: page
title: "Visual In-Context Learning"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2402.11574v1)

# Visual In-Context Learning for Large Vision-Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Implements a three-stage pipeline: visual demonstration retrieval via ViT, cross-modal reranking with CLIP, and intent-oriented image summarization that converts visual examples into concise, task-specific text descriptions for language-only prompt composition.
* **Nuance**: Unlike standard LVLM ICL that concatenates raw images (causing token bloat and cross-modal representation mismatches), VICL fully translates demonstrations into language, leveraging the LLM's native reasoning pathways while introducing in-context unlearning capabilities.

#### 💡 Yield
- Achieves consistent performance gains across five visual reasoning datasets by aligning demonstration semantics with task intent.
- Information flow analysis confirms that text-only demonstrations improve cross-modal interaction efficiency and reduce representation disparity.
- Demonstrates viable in-context unlearning, allowing models to selectively discard or reset specific knowledge via prompt engineering without parameter updates.

#### ⚠️ Limitations
- Relies heavily on the quality of external retrieval (ViT/CLIP) and the LVLM's own captioning accuracy for intent summarization.
- In-context unlearning is presented as a promising exploratory finding rather than a rigorously validated standalone technique.
- Still subject to standard LLM context window constraints, albeit mitigated by reduced token counts per demonstration.