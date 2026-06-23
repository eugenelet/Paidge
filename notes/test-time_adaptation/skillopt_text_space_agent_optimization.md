---
layout: page
title: "SkillOpt Text Space Agent Optimization"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.23904v2)

# SkillOpt: Executive Strategy for Self-Evolving Agent Skills

#### 🚀 Technical Novelty
* **Mechanism**: Deploys a separate optimizer model to generate bounded add/delete/replace edits on a skill document, guided by trajectory feedback, textual learning rates, and a held-out validation gate.
* **Nuance**: Unlike prompt tuning or one-shot skill generation, it applies deep-learning-style optimization controls (validation gating, rejected-edit buffers, epoch-wise slow updates) to stabilize text-space editing without modifying model weights.

#### 💡 Yield
- Achieves best or tied-best performance across all 52 evaluated (model, benchmark, harness) cells; lifts GPT-5.5 accuracy by +19.1 to +24.8 points across direct chat and agentic loops; demonstrates strong cross-model, cross-harness, and cross-benchmark transferability of optimized skills.

#### ⚠️ Limitations
- Optimization phase requires an auxiliary frontier model and multiple rollout/validation cycles; skill capacity is constrained by token limits (~300–2k tokens) and depends heavily on the reliability of the external scoring function.