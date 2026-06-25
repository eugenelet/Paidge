---
layout: page
title: "Self-Regulated Simulative Planning"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.22138v1)

# Efficient Agentic Reasoning Through Self-Regulated Simulative Planning

#### 🚀 Technical Novelty
* **Mechanism**: Decomposes agentic decision-making into three distinct, learnable stages: a reactive actor (System I), a simulative planner that uses the LLM as an implicit language-space world model (System II), and a learned configurator (System III) that dynamically gates whether to plan, continue planning, or act directly at each turn.
* **Nuance**: Unlike unconstrained chain-of-thought or always-on planning paradigms, it explicitly decouples the *decision to plan* from the *planning process itself*, using RL to shift behavior toward longer simulation horizons rather than increased planning frequency, thereby eliminating token bloat without sacrificing deliberation depth.

#### 💡 Yield
- SR2AM-v1.0-30B achieves Pass@1 performance competitive with 685B–1T parameter agentic LLMs while consuming 25.8–95.3% fewer reasoning tokens across math, science, tabular, and web-reasoning benchmarks.
- RL training increases the average planning horizon by 22.8% while growing planning frequency by only 2.0%, empirically proving that extended forward simulation is more efficient than frequent short deliberation for agentic tasks.

#### ⚠️ Limitations
- Relies on the LLM itself as an implicit language-space world model rather than a dedicated, trained simulator, which may limit accuracy in highly dynamic, non-textual, or physically grounded environments.
- The scalable v1.0 data pipeline reconstructs structured plans from pretrained LLM traces via an annotator model, potentially inheriting reasoning biases, hallucinations, or structural errors from the source models.