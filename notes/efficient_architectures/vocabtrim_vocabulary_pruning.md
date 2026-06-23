---
layout: page
title: "VocabTrim Vocabulary Pruning"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2506.22694v2)

# VOCABTRIM: Vocabulary Pruning for Efficient Speculative Decoding in LLMs

#### 🚀 Technical Novelty
* **Mechanism**: Trims the drafter model's language modeling head to retain only the top-K most frequently sampled tokens from a calibration dataset, eliminating unnecessary logit computations over rare vocabulary items.
* **Nuance**: Unlike prior SOTA methods that require task-specific drafter retraining or force shared vocabularies, this approach is entirely training-free and specifically targets the memory-bound drafting bottleneck to maximize speed-up without architectural modifications.

#### 💡 Yield
- Delivers 14–19% improvement in memory-bound speed-up (MBSU) across Llama-3 models on Spec-Bench with only a 1–5% drop in block efficiency/acceptance rate.
- Demonstrates that calibration using target-model-generated completions yields superior vocabulary selection compared to raw text or draft-generated data, maximizing the speed-accuracy tradeoff.

#### ⚠️ Limitations
- Requires task-specific recalibration for domains with low vocabulary overlap (e.g., coding), as a single trimmed set degrades performance on mismatched tasks.
- Fixed top-K pruning strategy may not optimally balance speed and accuracy across varying hardware memory constraints or draft tree depths without further hyperparameter tuning.