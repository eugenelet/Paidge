---
layout: page
title: "Growing Memory RNNs"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.24281v1)

# MEMORYCACHING: RNNS WITH GROWING MEMORY

#### 🚀 Technical Novelty
* **Mechanism**: Segments input sequences and caches compressed hidden states at segment boundaries, enabling subsequent tokens to directly attend to historical memory checkpoints rather than relying solely on a fixed-size recurrent state.
* **Nuance**: Interpolates between fixed O(L) RNN compression and growing O(L²) Transformer KV-caches via controllable aggregation strategies (e.g., gated residual connections, sparse selective routing), avoiding full quadratic attention costs while mitigating RNN memory overflow.

#### 💡 Yield
- Achieves competitive accuracy on long-context understanding and in-context recall tasks, closely matching Transformers while outperforming state-of-the-art RNNs like Titans and Atlas.
- Delivers significantly higher training throughput and lower memory overhead than Transformers as sequence length scales, with sparse variants adding minimal computational overhead to base models.

#### ⚠️ Limitations
- Design choices were intentionally simplified for demonstration; more expressive pooling or routing mechanisms could further boost performance in future iterations.
- Effective complexity scales with the number of cached segments (O(NL)) rather than strictly O(L), requiring careful segment-size tuning to balance memory retention and computational speed.