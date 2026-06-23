---
layout: page
title: "Spiffy Accelerates Diffusion LLMs"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2509.18085v3)

# Spiffy: Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding

#### 🚀 Technical Novelty
* **Mechanism**: Auto-speculative drafting using the dLLM's own distribution to generate candidate states, verified via a novel directed draft graph that respects bidirectional token dependencies.
* **Nuance**: Eliminates auxiliary draft model overhead and adapts speculative decoding to block-wise, bidirectional unmasking, enabling parallel verification with provable distribution preservation unlike AR-LLM tree-based methods.

#### 💡 Yield
- Achieves 2.8–3.1× standalone speedup and up to 7.9× when combined with parallel decoding schemes while maintaining exact output quality across GSM8K, HumanEval, MBPP, and MATH; offline calibration converges with just 20–50 samples.

#### ⚠️ Limitations
- Requires a fixed offline calibration phase and static graph structures during generation, limiting dynamic adaptation to highly variable prompt complexities; standalone speedups plateau without complementary optimizations like KV-caching.