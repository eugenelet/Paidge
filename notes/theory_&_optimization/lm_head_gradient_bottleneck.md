---
layout: page
title: "LM Head Gradient Bottleneck"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.10145v1)

# Lost in Backpropagation: The LM Head is a Gradient Bottleneck

#### 🚀 Technical Novelty
* **Mechanism**: Rigorous theoretical and empirical analysis demonstrating that backpropagating high-dimensional logit gradients through a low-rank linear head causes severe lossy compression, misaligning the effective update direction with the optimal gradient.
* **Nuance**: Reframes the classical softmax bottleneck from an expressivity limitation to a fundamental optimization flaw, proving it degrades training dynamics independently of the underlying transformer backbone architecture.

#### 💡 Yield
- Theoretical proof that logit update rank is strictly bounded by 2D, causing massive misalignment with the first-order optimal gradient direction.
- Empirical validation across GPT-2, Llama-3, Qwen-3, and Pythia families showing 95–99% gradient norm suppression and up to ×16 slower convergence in controlled bottleneck experiments.

#### ⚠️ Limitations
- Focuses exclusively on pretraining dynamics and theoretical bounds; does not yet propose or benchmark a concrete architectural solution for the LM head.
- Theoretical expressivity assumptions rely on deterministic, sufficiently expressive hidden states, which may not fully capture real-world representation degeneration during early training phases.