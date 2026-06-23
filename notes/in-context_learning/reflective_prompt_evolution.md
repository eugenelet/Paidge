---
layout: page
title: "Reflective Prompt Evolution"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2507.19457v2)

# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

#### 🚀 Technical Novelty
* **Mechanism**: Iteratively mutates compound AI system prompts by analyzing serialized natural language trajectories, applying multi-objective evolutionary search to maintain a Pareto front of diverse candidate prompts.
* **Nuance**: Bypasses GRPO's reliance on thousands of scalar reward rollouts by leveraging LLMs' native language priors for high-level rule extraction, avoiding greedy local optima through stochastic diversity maintenance rather than single-path gradient updates.

#### 💡 Yield
- Achieves up to 20% higher accuracy than GRPO (avg +6%) across six benchmarks while using up to 35× fewer rollouts and surpassing MIPROv2 by >10%.
- Demonstrates strong sample efficiency, requiring only dozens of reflection LLM calls per task to converge on robust, generalizable prompt instructions.

#### ⚠️ Limitations
- Optimization phase depends on external reflection LLM calls, introducing computational latency and API costs during the prompt tuning stage.
- Primarily validated on text-heavy reasoning and instruction-following workflows; scalability to highly parameterized or non-textual domains remains untested.