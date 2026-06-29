---
layout: page
title: "Gist Sparse Attention"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.20920v1)

# Forget, Then Recall: Learnable Compression and Selective Unfolding via Gist Sparse Attention

#### 🚀 Technical Novelty
* **Mechanism**: Interleaved learnable gist tokens compress raw contexts into dense summaries, serving as differentiable routing signals to selectively unfold and attend only to the most relevant raw token chunks.
* **Nuance**: Bridges compression and training-time sparsity end-to-end within standard Transformers, avoiding the architectural modifications of NSA, external indexers of DSA, and non-differentiable pooling gates of MoBA.

#### 💡 Yield
- Achieves log-linear per-step decoding complexity O(log n) via recursive gist-of-gist construction.
- Consistently outperforms compression baselines and inference-time sparse attention on LongBench/RAG benchmarks, delivering 8–12 point gains after fine-tuning under identical token budgets (8× to 32× compression).

#### ⚠️ Limitations
- Selective finetuning requires position-dependent sparse masks that may necessitate custom CUDA kernels for efficient implementation.
- Hierarchical depth and chunking parameters require careful tuning to balance compression ratio against retrieval fidelity, and the coarse-to-fine routing assumes structured context dependencies rather than uniformly dense ones.