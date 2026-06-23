---
layout: page
title: "FastForward Predictive FFN Sparsity"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.00397v1)

# FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity

#### 🚀 Technical Novelty
* **Mechanism**: Block-wise context-aware FFN sparsity driven by a lightweight expert predictor that proactively selects high-importance neurons, augmented by an error compensation network and layer-wise sparsity scheduler.
* **Nuance**: Unlike prior decoding-focused or static masking methods, it exploits prefill parallelism through proactive, block-level prediction and dynamic compute allocation, avoiding the accuracy collapse of uniform sparsity on long prompts.

#### 💡 Yield
- Delivers up to 1.45× compute-bound speedup at 50% FFN sparsity across LLaMA/Qwen models (1B–8B) with <6% accuracy loss on LongBench, significantly reducing Time-to-First-Token for short-to-moderate context workloads.

#### ⚠️ Limitations
- The error compensator lacks direct signals about which neurons were pruned, limiting its capacity to correct large deviations from suboptimal expert selection; dynamic expert loading remains memory-bandwidth intensive compared to static alternatives.