---
layout: page
title: "Kimi Linear Architecture"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2510.26692v2)

# Kimi Linear: An Expressive, Efficient Attention Architecture

#### 🚀 Technical Novelty
* **Mechanism**: Introduces Kimi Delta Attention (KDA), a linear attention module featuring channel-wise gating and specialized Diagonal-Plus-Low-Rank (DPLR) transition matrices for hardware-efficient chunkwise parallelization.
* **Nuance**: Unlike prior gated delta networks that use coarse head-wise forgetting, KDA applies fine-grained per-dimension decay rates, while its fixed 3:1 interleaving of linear and global attention layers avoids the routing overhead of intra-layer hybrids.

#### 💡 Yield
- Outperforms full-attention baselines across short-context, long-context (up to 1M tokens), and RL-style post-training tasks under identical training conditions.
- Cuts KV cache memory by up to 75% and delivers up to 6.3× faster decoding throughput at maximum context length.
- Fully open-sourced with optimized KDA kernels, vLLM integration, and pre-trained/instruction-tuned checkpoints.

#### ⚠️ Limitations
- Pure linear attention variants still face theoretical limits in exact copying and fine-grained retrieval for extreme long-context scenarios.
- Hybrid designs remain sensitive to RoPE base frequency shifts when extrapolating context windows beyond training lengths.
- Efficiency gains are heavily dependent on bespoke chunkwise kernel implementations; general DPLR formulations lack comparable speedups.