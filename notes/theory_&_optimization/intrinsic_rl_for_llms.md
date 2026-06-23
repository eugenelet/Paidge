---
layout: page
title: "Intrinsic RL for LLMs"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2505.19590v3)

# Learning to Reason Without External Rewards

#### 🚀 Technical Novelty
* **Mechanism**: Replaces verifiable rewards in Group Relative Policy Optimization (GRPO) with a model's self-certainty (average KL divergence between its output distribution and a uniform distribution) as the sole intrinsic reward signal.
* **Nuance**: Eliminates dependency on gold solutions, test cases, or domain-specific verifiers by optimizing process-oriented internal feedback rather than outcome-based external rewards, enabling training purely on unlabeled queries.

#### 💡 Yield
- Matches GRPO performance on in-domain mathematical benchmarks (GSM8K, MATH500) without any labeled data or ground truth.
- Achieves superior out-of-domain generalization, notably a 65% relative improvement on LiveCodeBench versus zero gain for GRPO, and a 76% gain on CRUXEval-O.
- Enables base LLMs to spontaneously generate coherent reasoning chains and structured code from purely unlabeled data, demonstrating emergent instruction-following capabilities.

#### ⚠️ Limitations
- Relies entirely on the calibration accuracy of self-certainty as a correctness proxy, which may not perfectly align with task success in ambiguous or poorly calibrated regimes.
- Lacks explicit verification guarantees, potentially allowing suboptimal but highly confident trajectories to be reinforced during training without external correction.