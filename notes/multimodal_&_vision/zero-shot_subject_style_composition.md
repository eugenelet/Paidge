---
layout: page
title: "Zero-Shot Subject Style Composition"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2502.19673v1)

# SubZero: Composing Subject, Style, and Action via Zero-Shot Personalization

#### 🚀 Technical Novelty
* **Mechanism**: Disentangled Stochastic Optimal Controller for iterative latent modulation combined with Orthogonal Temporal Aggregation (OTA) in cross-attention blocks to fuse text, subject, and style features without fine-tuning.
* **Nuance**: Replaces rigid ControlNet pipelines and per-concept adapter training with zero-order latent optimization and orthogonal feature blending, enabling flexible action prompting and single-reference generalization while strictly decoupling content/style leakage.

#### 💡 Yield
- Establishes new state-of-the-art on face/object-style composition benchmarks (e.g., +4–6% average similarity over RB-Modulation/IP-Adapter) and achieves 64–75% human preference scores while maintaining strict subject/style fidelity without helper prompts.

#### ⚠️ Limitations
- Iterative latent optimization during inference increases computational overhead compared to single-pass methods, potentially constraining ultra-low-latency real-time deployment; performance remains dependent on the quality of pre-trained subject/style projectors.