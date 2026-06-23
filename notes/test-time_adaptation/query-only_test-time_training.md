---
layout: page
title: "Query-Only Test-Time Training"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.13898v1)

# Let’s (not) just put things in Context: Test-Time Training for Long-Context LLMs

#### 🚀 Technical Novelty
* **Mechanism**: Single prefill to cache keys/values followed by targeted gradient updates exclusively on attention query projections, reusing the KV cache.
* **Nuance**: Unlike decoding-based scaling (e.g., chain-of-thought) that generates more tokens with static attention, qTTT dynamically reallocates attention mass to buried evidence without altering model weights or architecture.

#### 💡 Yield
- Theoretically proves "score dilution" limits static attention and derives a logarithmic margin requirement; empirically delivers 12.6–14.1% average gains on LongBench-v2/ZeroScrolls under matched FLOP budgets, outperforming thinking-token baselines.

#### ⚠️ Limitations
- Evaluated only on a single (k, n_TTT) trade-off point; gains are task-dependent (less effective for pure generation/summarization vs. retrieval); future work needed on adaptive compute scheduling and broader inference-time baselines.