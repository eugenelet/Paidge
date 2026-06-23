---
layout: page
title: "Dynamic Draft Trees for LLMs"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2406.16858v2)

# EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees

#### 🚀 Technical Novelty
* **Mechanism**: Dynamically adjusts the speculative draft tree structure during generation by using the draft model's confidence scores as real-time proxies for token acceptance rates, expanding branches only where contextual complexity warrants it.
* **Nuance**: Unlike prior SOTA methods (e.g., EAGLE-1, Medusa) that rely on fixed, position-dependent draft trees or relaxed acceptance conditions, EAGLE-2 adapts in real-time to context difficulty while strictly preserving the original LLM's output distribution without extra training.

#### 💡 Yield
- Achieves 3.05x–4.26x average speedup (up to 5x on code generation) across Vicuna and LLaMA model families, increasing average acceptance length to ~4–5.5 tokens per drafting-verification cycle.
- Delivers lossless acceleration with zero additional training overhead or parameter modifications to the base LLM or draft model.

#### ⚠️ Limitations
- Performance drops on world-knowledge QA and summarization tasks because the draft models are trained exclusively on SFT data rather than large-scale pretraining corpora.
- Speedup ratios are hardware-dependent, and the method's efficacy relies heavily on the draft model's calibration quality across different architectures.