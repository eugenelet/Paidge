---
layout: page
title: "Inference Layer Skipping"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.07475v1)

# Skip the Good Part: Representation Structure & Inference-Time Layer Skipping in Diffusion vs. Autoregressive LLMs

#### 🚀 Technical Novelty
* **Mechanism**: Static, task-agnostic inference-time layer skipping that bypasses high-similarity early layers in native diffusion LLMs without KV-cache sharing or architectural modifications.
* **Nuance**: Exploits objective-induced hierarchical abstraction and representational redundancy rather than cache-centric optimizations, while revealing persistent initialization bias when AR models are adapted to diffusion training.

#### 💡 Yield
- Native dLLMs achieve up to 18.75% FLOPs reduction while retaining >90% performance on reasoning and code benchmarks, whereas AR models degrade sharply under comparable skipping.
- First systematic layer- and token-wise analysis proving diffusion objectives induce global abstraction with minimal recency bias, contrasting with AR's incremental, depth-dependent refinement.

#### ⚠️ Limitations
- Autoregressive and AR-initialized models exhibit brittle performance drops when layers are skipped, limiting cross-architecture applicability.
- Aggressive consecutive layer skipping causes steeper accuracy degradation, and safety/out-of-distribution behaviors remain unverified beyond standard benchmarks.