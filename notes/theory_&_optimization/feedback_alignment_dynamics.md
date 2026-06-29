---
layout: page
title: "Feedback Alignment Dynamics"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2011.12428v2)

# Align, then memorise: the dynamics of learning with feedback alignment

#### 🚀 Technical Novelty
* **Mechanism**: Identifies a sequential "align-then-memorize" dynamic where forward weights first adapt to random feedback weights to approximate true gradients, then shift focus to data fitting.
* **Nuance**: Moves beyond static alignment assumptions by quantifying how matrix conditioning and layer-wise progression dictate success on Transformers versus failure on CNNs, introducing a "degeneracy breaking" convergence property absent in prior analyses.

#### 💡 Yield
- Proves DFA naturally converges to solutions maximizing gradient alignment; derives that well-conditioned error statistics are necessary for learning; empirically validates bottom-to-top layer-wise alignment progression on MNIST and CIFAR10.

#### ⚠️ Limitations
- Theoretical derivations rely on the infinite-data online learning limit and linear network assumptions; empirical validation is confined to standard vision benchmarks without large-scale architectural scaling tests; performance degrades with correlated targets or label noise.