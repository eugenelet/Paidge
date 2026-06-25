---
layout: page
title: "RL-Conductor Agent Orchestration"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.04388v4)

# Learning to Orchestrate Agents in Natural Language with the Conductor

#### 🚀 Technical Novelty
* **Mechanism**: Trains a 7B LLM via GRPO reinforcement learning to output natural-language agentic workflows (subtasks, agent assignments, and access lists) that dynamically coordinate worker models at inference.
* **Nuance**: Replaces static multi-agent scaffolds and manual prompting with end-to-end RL reward maximization, allowing flexible coordination topologies and prompt engineering to emerge naturally while adapting to arbitrary agent pools at runtime.

#### 💡 Yield
- Achieves state-of-the-art results on LiveCodeBench and GPQA Diamond with a 7B model, surpassing costly multi-agent baselines using fewer API calls.
- Generalizes across diverse math, coding, and science domains by training with randomized agent pools.
- Introduces recursive topologies where the Conductor calls itself, enabling tunable inference-time scaling through online iterative adaptation.

#### ⚠️ Limitations
- Performance gains come at the cost of increased test-time compute and latency due to iterative multi-agent coordination.
- Effectiveness is contingent on the capabilities and diversity of the available worker agent pool, despite randomization during training.