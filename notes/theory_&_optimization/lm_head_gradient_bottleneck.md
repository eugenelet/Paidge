---
layout: page
title: "LM Head Gradient Bottleneck"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.10145v1)

# Lost in Backpropagation: The LM Head is a Gradient Bottleneck

#### 🚀 Technical Novelty
* **Mechanism**: Demonstrates that backpropagating V-dimensional logits through a rank-D linear head (where D≪V) causes unavoidable lossy compression, destroying the majority of gradient norm and misaligning update directions.
* **Nuance**: Reframes the softmax bottleneck from a purely expressivity limitation to a fundamental optimization/gradient flow problem, proving it harms training dynamics independently of backbone architecture.

#### 💡 Yield
- Theoretical proof that logit updates are rank-constrained to 2D, fundamentally misaligned with optimal gradient directions when D≪V.
- Empirical validation across GPT-2, Llama-3, Qwen-3, and Pythia families showing 95–99% gradient norm suppression and up to ×16 slower convergence in controlled bottleneck experiments.
- Identification of a trivial synthetic language task where expressivity isn't the issue, but gradient compression makes learning impossible.

#### ⚠️ Limitations
- Focuses on standard autoregressive LMs with linear softmax heads; does not yet propose or test concrete architectural replacements in large-scale frontier settings.
- Theoretical analysis assumes deterministic, sufficiently expressive hidden representations (φθ), abstracting away potential representation degeneration effects.
- Empirical bottleneck tests use controlled 2B parameter models rather than full-scale frontier LLMs.