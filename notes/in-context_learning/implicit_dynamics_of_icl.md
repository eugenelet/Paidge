---
layout: page
title: "Implicit Dynamics of ICL"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2507.16003v3)

# Learning without training: The implicit dynamics of in-context learning

#### 🚀 Technical Novelty
* **Mechanism**: Introduces "contextual blocks" and derives an exact closed-form formula demonstrating that a prompt context is mathematically equivalent to a rank-1 weight update applied directly to the first MLP layer's weights.
* **Nuance**: Unlike prior theoretical works that rely on restrictive assumptions (e.g., linear attention, single heads, or specific prompt structures), this framework applies to general transformer blocks and arbitrary contextual layers without architectural modifications.

#### 💡 Yield
- Proves exact equivalence between in-context learning dynamics and implicit gradient descent, showing high alignment with actual SGD finetuning updates across varying context lengths.
- Unifies disparate mechanistic interpretability concepts by demonstrating that steering vectors and low-rank factual model edits naturally emerge from the same underlying mechanism of context-induced weight modulation.

#### ⚠️ Limitations
- The derived implicit weight updates are inherently dynamic and query-dependent, meaning they cannot be compressed into a single static weight update for all inputs without approximation.
- Focuses strictly on mechanistic theory and mathematical derivation rather than proposing new training algorithms or architectural optimizations for practical deployment.