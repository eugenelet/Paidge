---
layout: page
title: "Context-to-Weight Equivalence"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2511.17864v1)

# Equivalence of Context and Parameter Updates in Modern Transformer Blocks

#### 🚀 Technical Novelty
* **Mechanism**: Derives exact analytical formulas for rank-1 weight patches and RMSNorm scale updates that mathematically absorb context into a Gemma-style transformer block, generalizing via input/output controllability properties.
* **Nuance**: Extends prior vanilla transformer proofs to modern architectures lacking biases by incorporating gating (SwiGLU), RMSNorm, and multi-layer induction, proving perfect equivalence rather than approximation.

#### 💡 Yield
- Provides a constructive proof and algorithm for computing implicit weight patches across multi-layer modern LLMs; experimentally validates near-perfect logit matching and identical token generation on Gemma 3 1B without context vs. original with context.

#### ⚠️ Limitations
- Updates are strictly token-dependent and must be recomputed at every inference step; framework is descriptive/theoretical rather than a prescriptive algorithm for efficient inference or global context absorption.