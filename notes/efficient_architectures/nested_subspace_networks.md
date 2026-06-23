---
layout: page
title: "Nested Subspace Networks"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2509.17874v2)

# Deep Hierarchical Learning with Nested Subspace Networks for Large Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Re-parameterizes linear layers using shared low-rank factor matrices (A, B) to construct a nested hierarchy of effective weights at varying ranks, optimized jointly via an uncertainty-aware objective that balances contributions across the hierarchy.
* **Nuance**: Unlike static compression or discrete dynamic networks, NSNs provide a continuous, smooth compute-performance frontier post-hoc on frozen pre-trained models without altering tensor shapes or requiring specialized from-scratch training schemes.

#### 💡 Yield
- Achieves up to 50% FLOPs reduction with only ~5% accuracy drop across multiple LLMs (Pythia, GPT-Neo, Gemma, Qwen).
- Provides theoretical guarantees for granular budget control and smooth Pareto frontiers at inference.
- Simultaneously satisfies instant test-time adaptability, post-hoc applicability to any foundation model, and architectural agnosticism.

#### ⚠️ Limitations
- Currently applies uniform rank scaling across all layers rather than layer-specific adaptive compute.
- Requires future work to correlate problem-specific information with layer-specific representational capacity for fine-grained control.
- FLOPs reduction is bounded by a dimension-dependent break-even point, limiting gains for certain layer sizes or specific input/output configurations.