---
layout: page
title: "Intrinsic Reward LLM Training"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2505.19590v3)

# LEARNING TO REASON WITHOUT EXTERNAL REWARDS

#### 🚀 Technical Novelty
* **Mechanism**: Replaces verifiable reward signals in Group Relative Policy Optimization (GRPO) with a model's self-certainty (average KL divergence between its output distribution and a uniform distribution), enabling fully unsupervised policy updates.
* **Nuance**: Unlike RLVR which depends on domain-specific gold solutions or execution test cases, INTUITOR optimizes generation trajectories via intrinsic confidence, completely eliminating the need for external supervision, verifiers, or handcrafted reward functions.

#### 💡 Yield
- Matches GRPO's performance on in-domain mathematical benchmarks (GSM8K, MATH500) without requiring any gold answers or labeled data.
- Achieves superior out-of-domain generalization, yielding a 65% relative improvement on LiveCodeBench and 76% on CRUXEval-O compared to GRPO's negligible gains.
- Enables base models (e.g., Qwen2.5-1.5B) that previously produced repetitive content or scored 0% to develop coherent reasoning chains and well-structured code through intrinsic feedback alone.

#### ⚠️ Limitations
- Relies on the assumption that self-certainty reliably correlates with response quality, which may degrade in highly complex, novel, or ambiguous domains where confidence becomes miscalibrated.
- Lacks explicit outcome verification, creating a risk of confidently generating plausible but incorrect outputs (hallucinations) without external grounding.
- Empirical validation is primarily confined to mathematical reasoning and code generation; broader applicability to open-ended creative, conversational, or multi-step planning tasks remains unverified.