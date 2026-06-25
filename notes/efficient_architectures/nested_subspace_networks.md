---
layout: page
title: "Nested Subspace Networks"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2509.17874v2)

# Deep Hierarchical Learning with Nested Subspace Networks for Large Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Re-parameterizes linear layers into rank-trainable components using shared factor matrices (A, B), where effective weights at rank r are formed by prefixing these matrices to satisfy a strict nested subspace property.
* **Nuance**: Unlike static compression or discrete dynamic networks, NSNs provide a smooth, continuous spectrum of compute budgets at inference time while remaining architecturally agnostic and applicable post-hoc to frozen pre-trained LLMs.

#### 💡 Yield
- Achieves up to 50% FLOPs reduction with only ~5% accuracy drop across multiple LLMs (Pythia, GPT-Neo, Gemma, Qwen).
- Provides theoretical guarantees for granular budget control and a predictable compute-performance Pareto frontier.
- Successfully adapts pre-trained foundation models without training from scratch or modifying network interfaces.

#### ⚠️ Limitations
- Currently applies uniform rank reduction/augmentation across all layers rather than layer-specific adaptive compute.
- Requires solving the nontrivial problem of correlating problem-specific information with layer-specific representational capacity for future fine-grained control.
- Training relies on an uncertainty-aware objective that may introduce complexity compared to standard fine-tuning pipelines.