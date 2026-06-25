---
layout: page
title: "Dynamic Draft Tree Acceleration"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2406.16858v2)

# EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees

#### 🚀 Technical Novelty
* **Mechanism**: Replaces static draft trees in speculative sampling with context-aware dynamic structures that expand or contract per token based on the draft model's confidence scores.
* **Nuance**: Unlike prior SOTA methods that assume position-dependent acceptance rates, EAGLE-2 exploits the draft model's inherent calibration to approximate real-time acceptance probabilities, enabling adaptive tree shaping without relaxing acceptance conditions or retraining.

#### 💡 Yield
- Achieves 3.05x–4.26x speedup over vanilla autoregressive decoding and 20%–40% faster than EAGLE-1 across Vicuna, LLaMA2, and LLaMA3 models on six diverse tasks while guaranteeing exact output distribution parity.

#### ⚠️ Limitations
- Performance degrades on knowledge-heavy QA/summarization tasks due to draft model training data bias (SFT-only vs. pretraining), and speedup metrics remain hardware-dependent with unisolated draft-model forward overhead.