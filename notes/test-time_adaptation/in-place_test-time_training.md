---
layout: page
title: "In-Place Test-Time Training"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.06169v1)

# In-Place Test-Time Training

#### 🚀 Technical Novelty
* **Mechanism**: Repurposes the final projection matrix of standard MLP blocks as adaptable "fast weights," updated via a parallelizable chunk-wise rule and an objective explicitly aligned with Next-Token Prediction.
* **Nuance**: Unlike prior TTT methods that require specialized recurrent layers, costly from-scratch pretraining, or inefficient sequential per-token updates, this approach acts as a seamless "drop-in" enhancement that complements attention mechanisms while maintaining high accelerator throughput.

#### 💡 Yield
- Enables a 4B-parameter LLM to effectively process contexts up to 128k with negligible memory/throughput overhead.
- Consistently outperforms competitive TTT baselines when pretrained from scratch, validating the architectural merit of MLP-based fast weights.
- Ablations confirm optimal chunk sizes (512–1024) and prove that both convolutional future-token masking and projection transformations are essential for the LM-aligned objective.

#### ⚠️ Limitations
- Integration with alternative efficient long-context backbones (e.g., State-Space Models or sparse attention variants) is explicitly deferred to future work.
- Chunk-wise updates inherently present a performance-efficiency trade-off, requiring careful tuning of chunk granularity to balance parallelism and adaptation fidelity.