---
layout: page
title: "Implicit Dynamics of ICL"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2507.16003v3)

# Learning without training: The implicit dynamics of in-context learning

#### 🚀 Technical Novelty
* **Mechanism**: Introduces "contextual blocks" and derives an exact formula demonstrating how a transformer's self-attention layer dynamically modulates the subsequent MLP layer via a rank-1 weight update derived directly from prompt tokens.
* **Nuance**: Unlike prior theoretical work that relies on restrictive assumptions (e.g., linear attention, single heads, or fixed prompts), this framework applies to general transformer blocks and arbitrary contextual layers without architectural modifications, proving exact equivalence between context processing and dynamic weight modulation.

#### 💡 Yield
- Derives a closed-form expression mapping prompt segments to linear operators, rigorously linking in-context learning to low-rank model editing and steering vectors.
- Empirically validates that implicit weight updates during inference align highly (via normalized Frobenius inner product) with explicit SGD finetuning gradients across varying context lengths.

#### ⚠️ Limitations
- The derived weight updates are inherently dynamic and query-dependent, preventing exact compression into a single static weight matrix without approximation.
- Theoretical focus on generalized contextual blocks leaves practical scaling to massive LLMs and complex multi-step reasoning tasks for future work.