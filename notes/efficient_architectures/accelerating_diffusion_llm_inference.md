---
layout: page
title: "Accelerating Diffusion LLM Inference"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2509.18085v3)

# Spiffy: Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding

#### 🚀 Technical Novelty
* **Mechanism**: Auto-speculative decoding that samples draft states directly from the dLLM's own distribution and structures them as a directed draft graph, verified in parallel via lossless rejection sampling.
* **Nuance**: Unlike AR-LLM speculative decoding which relies on trees or auxiliary drafters, Spiffy respects the bidirectional, block-wise nature of diffusion generation, eliminating drafting overhead while mathematically guaranteeing distribution preservation.

#### 💡 Yield
- Achieves 2.8–3.1× standalone speedup across open-source dLLMs (LLaDA variants), scaling to up to 7.9× when multiplied with parallel decoding techniques like KV-caching and multi-token unmasking.
- Proves losslessness theoretically and empirically, maintaining exact accuracy on GSM8K, HumanEval, MATH, and MBPP benchmarks across varying draft block counts.
- Offline graph calibration converges rapidly (<30 mins, 20–50 samples) and generalizes stably across tasks without retraining.

#### ⚠️ Limitations
- Requires a one-time offline calibration step to determine optimal directed graph configurations before deployment.
- Speedup scaling behavior may differ between compute-bound and memory-bound hardware architectures.
- Current auto-speculation implementation depends on the target dLLM's distribution; future efficiency gains are contingent on the availability of smaller auxiliary draft models.