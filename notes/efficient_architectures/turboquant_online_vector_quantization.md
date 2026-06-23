---
layout: page
title: "TurboQuant Online Vector Quantization"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2504.19874v1)

# TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate

#### 🚀 Technical Novelty
* **Mechanism**: Randomly rotates high-dimensional input vectors to induce a concentrated Beta distribution on coordinates, applies optimal scalar quantizers per coordinate, and combines them with a 1-bit Quantized Johnson-Lindenstrauss (QJL) transform on the residual to produce an unbiased inner-product estimator.
* **Nuance**: Unlike product quantization or learned schemes that require heavy codebook storage or offline training, TurboQuant is data-oblivious, online-capable, and provably matches information-theoretic distortion bounds across all bit-widths without sacrificing accelerator vectorization compatibility.

#### 💡 Yield
- Proves information-theoretic lower bounds on achievable distortion rate, demonstrating TurboQuant closely matches them within a ~2.7x constant factor.
- Empirically achieves absolute quality neutrality at 3.5 bits/channel for LLM KV cache compression and outperforms Product Quantization/RabitQ in nearest-neighbor recall while reducing indexing time to virtually zero.

#### ⚠️ Limitations
- Optimized for worst-case/general data distributions rather than dataset-specific adaptations, potentially leaving gains on the table for highly structured inputs.
- Theoretical distortion guarantees differ by a small constant factor from absolute information-theoretic limits, and the two-stage residual pipeline introduces minor computational overhead compared to single-pass scalar quantization.