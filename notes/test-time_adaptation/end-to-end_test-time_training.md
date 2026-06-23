---
layout: page
title: "End-to-End Test-Time Training"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.23675v2)

# End-to-End Test-Time Training for Long Context

#### 🚀 Technical Novelty
* **Mechanism**: Sequentially updates model weights during inference using next-token prediction gradients, initialized via meta-learning to optimize the weight state specifically for test-time learning dynamics.
* **Nuance**: Fully end-to-end differentiable across both training and inference phases; directly optimizes the final test loss via outer-loop meta-gradients rather than relying on heuristic dynamic evaluation or fixed update rules like prior TTT methods.

#### 💡 Yield
- Matches full-attention Transformer scaling curves up to 128K context while maintaining O(1) decode latency.
- Achieves a 2.7× inference speedup over standard full attention on H100 hardware without perplexity degradation.
- Demonstrates that long-context modeling can be framed as continual learning rather than architectural redesign.

#### ⚠️ Limitations
- Inference-time gradient steps increase memory bandwidth pressure and require careful per-context learning rate scheduling.
- Relies on next-token prediction loss at test time, which may degrade under distribution shifts or non-stationary contexts.
- Evaluated primarily on standard language modeling; instruction-tuning, multi-domain generalization, and real-world deployment remain unexplored.