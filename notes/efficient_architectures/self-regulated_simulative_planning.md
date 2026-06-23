---
layout: page
title: "Self-Regulated Simulative Planning"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.22138v1)

# Efficient Agentic Reasoning Through Self-Regulated Simulative Planning

#### 🚀 Technical Novelty
* **Mechanism**: Decomposes agentic decision-making into three distinct, learnable stages: a configurator (System III) that dynamically decides when to plan, a simulative planner (System II) that uses the LLM as an in-language world model to predict future states, and reactive execution (System I) for direct action.
* **Nuance**: Unlike unconstrained chain-of-thought or rigid always-on planners, this architecture explicitly controls planning presence and horizon via a learned regulator, preventing inefficient token bloat while preserving structured, verifiable deliberation across diverse tasks without per-domain engineering.

#### 💡 Yield
- SR2AM-v1.0-30B achieves Pass@1 performance competitive with 685B–1T parameter agentic models across math, science, tabular, and web reasoning tasks.
- Reduces reasoning token consumption by 25.8–95.3% compared to similarly scaled competitors.
- RL training shifts the model's strategy from planning more often (+2.0%) to planning further ahead (+22.8% horizon), optimizing efficiency without sacrificing accuracy.

#### ⚠️ Limitations
- Supervised data construction relies on reconstructing plans from pretrained LLM traces or multi-module prompting, which may not perfectly capture optimal planning trajectories.
- RL training requires careful trajectory filtering to prevent format collapse and depends on accurate LLM-judge rewards for answer correctness.
- Currently validated on language-based interactive reasoning and tool-use environments rather than physical embodiment or highly dynamic real-world settings.