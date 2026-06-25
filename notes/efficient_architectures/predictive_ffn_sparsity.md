---
layout: page
title: "Predictive FFN Sparsity"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.00397v1)

# FASTFORWARD: ACCELERATING LLM PREFILL WITH PREDICTIVE FFN SPARSITY

#### 🚀 Technical Novelty
* **Mechanism**: Block-wise context-aware FFN sparsity driven by a lightweight expert predictor, an auxiliary error compensation network, and a layer-wise compute scheduler.
* **Nuance**: Unlike decoding-focused or static masking methods that break prefill parallelism or require unavailable prompt statistics, it proactively predicts neuron importance per block while dynamically allocating fidelity based on token-mixing importance.

#### 💡 Yield
- Achieves up to 1.45× compute-bound speedup at 50% sparsity with <6% accuracy drop across LLaMA/Qwen models (1B–8B) on LongBench.
- Proves FFNs dominate prefill FLOPs for contexts up to ~28K tokens, making targeted sparsity the most impactful lever for TTFT reduction.

#### ⚠️ Limitations
- The error compensator lacks direct signals about selected/pruned experts, limiting correction magnitude for suboptimal selections.
- Current dynamic expert loading remains memory-bandwidth intensive; full efficiency requires future static expert integration.