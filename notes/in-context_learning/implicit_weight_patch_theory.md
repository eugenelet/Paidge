---
layout: page
title: "Implicit Weight Patch Theory"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2511.17864v1)

# Equivalence of Context and Parameter Updates in Modern Transformer Blocks

#### 🚀 Technical Novelty
* **Mechanism**: Derives a constructive proof and algorithm showing that the entire computational effect of a prompt can be exactly absorbed into rank-1 patches on MLP weights and RMSNorm scales, unified under "input controllability" and "output controllability" properties.
* **Nuance**: Extends prior vanilla-transformer proofs to bias-free modern architectures (Gemma/Llama), multi-layer networks, gating, normalization, and MoE blocks, eliminating the historical reliance on bias terms for context absorption.

#### 💡 Yield
- Establishes a unified theorem proving implicit weight updates exist across diverse modern LLM architectures.
- Empirically validates near-perfect logit matching and identical token generation between patched models (without context) and original models (with context) on Gemma 3.

#### ⚠️ Limitations
- Derived parameter updates are strictly token-dependent and require recomputation at every generation step.
- Serves as a descriptive theoretical framework for understanding ICL rather than a prescriptive method for efficient inference or cross-step patch reusability.