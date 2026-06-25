---
layout: page
title: "VocabTrim Vocabulary Pruning"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2506.22694v2)

# VOCABTRIM: Vocabulary Pruning for Efficient Speculative Decoding in LLMs

#### 🚀 Technical Novelty
* **Mechanism**: Trims the drafter model's LM head by retaining only the top-K most frequently sampled tokens from a calibration dataset, drastically reducing output dimensionality and inference compute.
* **Nuance**: Unlike prior SOTA methods that require shared vocabularies or architectural modifications to drafters, VOCABTRIM is entirely training-free and bypasses vocabulary alignment constraints by focusing solely on pruning the drafting stage's memory bottleneck.

#### 💡 Yield
- Reduces drafter LM head size by up to 75% with negligible block efficiency drop (1–5%).
- Achieves 14–19% improvement in memory-bound speed-up (MBSU) on Llama-3 models across Spec-Bench tasks.
- Target-generated calibration datasets consistently outperform raw text or draft-generated data for optimal speed-accuracy trade-offs.

#### ⚠️ Limitations
- Requires a representative calibration dataset to compute token frequencies; performance may degrade on domains with low vocabulary overlap (e.g., coding vs. general text).
- Employs a static Top-K trimming strategy, limiting adaptability to dynamic or highly specialized downstream tasks without re-calibration.