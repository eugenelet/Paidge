---
layout: page
title: "In-Place Test-Time Training"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.06169v1)

# In-Place Test-Time Training

#### 🚀 Technical Novelty
* **Mechanism**: Treats the final projection matrix of existing MLP blocks as adaptable "fast weights," updating them in-place during inference via a chunk-wise rule and an objective explicitly aligned with next-token prediction.
* **Nuance**: Eliminates the need for specialized TTT layers or scratch pretraining by acting as a complementary, drop-in enhancement to attention; replaces inefficient sequential per-token updates with highly parallelizable chunk-wise processing tailored for autoregressive modeling.

#### 💡 Yield
- Enables a 4B-parameter model to effectively process contexts up to 128k while maintaining negligible throughput/memory overhead; consistently outperforms competitive TTT baselines in both drop-in fine-tuning and full pretraining settings.

#### ⚠️ Limitations
- Requires careful tuning of chunk size to balance performance and efficiency gains; currently validated on standard Transformer architectures, with integration into alternative efficient long-context backbones (e.g., SSMs) deferred to future work.