---
layout: page
title: "TurboQuant Online Vector Quantization"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2504.19874v1)

# TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate

#### 🚀 Technical Novelty
* **Mechanism**: Randomly rotates high-dimensional inputs to induce a concentrated Beta distribution on coordinates, applies optimal scalar Lloyd-Max quantizers per coordinate, and appends a 1-bit Quantized Johnson-Lindenstrauss transform on the residual for unbiased inner-product estimation.
* **Nuance**: Unlike codebook-dependent methods like Product Quantization, TurboQuant is data-oblivious and online, eliminating training/storage overhead while achieving provably near-optimal distortion rates within a small constant factor across all bit-widths.

#### 💡 Yield
- Achieves absolute quality neutrality at 3.5 bits/channel and marginal degradation at 2.5 bits/channel for LLM KV cache compression without accuracy loss.
- Delivers superior nearest-neighbor search recall compared to PQ and RabitQ while reducing quantization and indexing time to virtually zero seconds.
- Provides formal information-theoretic lower bounds on distortion rate, proving TurboQuant closely matches theoretical limits.

#### ⚠️ Limitations
- Relies on high-dimensional geometric concentration properties; performance may degrade in low-dimensional spaces where coordinate independence breaks down.
- Uses randomized quantization, introducing stochasticity that requires careful handling or averaging in strictly deterministic deployment pipelines.