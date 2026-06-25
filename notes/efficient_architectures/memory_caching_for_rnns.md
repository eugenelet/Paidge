---
layout: page
title: "Memory Caching for RNNs"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.24281v1)

# MEMORYCACHING: RNNS WITH GROWING MEMORY

#### 🚀 Technical Novelty
* **Mechanism**: Segments input sequences and caches compressed hidden/memory states at boundaries, enabling subsequent tokens to attend to a growing set of past checkpoints via controllable aggregation functions.
* **Nuance**: Interpolates between fixed-memory RNNs (O(L)) and full-attention Transformers (O(L²)) by dynamically scaling memory capacity with sequence length, avoiding KV-caching bottlenecks while preserving recurrence efficiency.

#### 💡 Yield
- Achieves competitive long-context QA and recall performance against Transformers on LongBench; delivers significant training throughput gains over attention-based models at scale across linear attention and deep memory architectures.

#### ⚠️ Limitations
- Simplified pooling/routing choices were used to isolate the MC effect, leaving room for more expressive aggregation mechanisms; complexity scales with cached segments (O(NL)) rather than strictly O(L).