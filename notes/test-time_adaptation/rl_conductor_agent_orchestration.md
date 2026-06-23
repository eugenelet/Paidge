---
layout: page
title: "RL Conductor Agent Orchestration"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.04388v4)

# LEARNING TO ORCHESTRATE AGENTS IN NATURAL LANGUAGE WITH THE CONDUCTOR

#### 🚀 Technical Novelty
* **Mechanism**: Trained via GRPO reinforcement learning, the Conductor outputs natural-language agentic workflows that dynamically partition problems, assign subtasks to specific worker LLMs, and define flexible communication topologies.
* **Nuance**: Unlike static multi-agent scaffolds or manual prompting, it learns coordination end-to-end through pure reward maximization, enabling seamless generalization to arbitrary open/closed-source agent pools and recursive self-referential inference loops.

#### 💡 Yield
- A 7B Conductor surpasses individual worker models and costly multi-agent baselines on LiveCodeBench and GPQA Diamond benchmarks.
- Randomized agent pool training enables robust adaptation to diverse, user-specified model sets without expensive API calls.
- Recursive topologies introduce a novel, tunable axis of dynamic test-time scaling that elevates reasoning performance through online iterative adaptation.

#### ⚠️ Limitations
- Performance depends on verifiable correctness rewards for RL alignment, limiting direct application to purely subjective or unverified tasks.
- Recursive inference loops inherently increase test-time compute and latency, trading efficiency for peak accuracy.