---
layout: page
title: "Visual In-Context Learning"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2402.11574v1)

# Visual In-Context Learning for Large Vision-Language Models

#### 🚀 Technical Novelty
* **Mechanism**: A three-stage pipeline (Visual Demonstration Retrieval, Intent-Oriented Image Summarization, and Composition) that extracts task-specific visual parsing via an LVLM and converts image demonstrations into concise text summaries to bypass cross-modal interaction bottlenecks.
* **Nuance**: Unlike standard ICL that concatenates raw images (suffering from representation disparities and token limits), VICL shifts the demonstration modality entirely to language while preserving visual intent, relying solely on intra-LLM interactions for context utilization.

#### 💡 Yield
- Validated across five visual reasoning datasets with improved ICL performance; information flow analysis confirms effective knowledge transfer; demonstrates viable in-context unlearning for resetting model knowledge without retraining.

#### ⚠️ Limitations
- Depends on external pre-trained encoders (ViT, CLIP) for retrieval and reranking, increasing inference overhead; in-context unlearning is presented as a promising preliminary capability requiring broader empirical validation.