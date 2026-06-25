---
layout: page
title: "SkillOpt Text-Space Optimizer"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.23904v2)

# SkillOpt: Executive Strategy for Self-Evolving Agent Skills

#### 🚀 Technical Novelty
* **Mechanism**: A dedicated optimizer model proposes bounded add/delete/replace edits to a skill document, which are aggregated under a textual learning-rate budget and accepted only through a held-out validation gate, with rejected edits preserved as negative feedback.
* **Nuance**: Unlike ad-hoc prompt tuning or uncontrolled skill evolution, SkillOpt imposes deep-learning-style optimization discipline (scheduled learning rates, momentum-like slow updates, strict validation gating) onto textual artifacts, ensuring stable, auditable, and reproducible refinement without touching model weights.

#### 💡 Yield
- Achieves best-or-tied performance across all 52 evaluated (model, benchmark, harness) cells on six diverse benchmarks, delivering +19.1 to +24.8 average accuracy gains over no-skill baselines.
- Demonstrates robust cross-model, cross-harness, and cross-benchmark transferability, producing compact (300–2,000 token), inspectable skill artifacts that require zero additional inference calls at deployment.

#### ⚠️ Limitations
- Requires a separate frontier optimizer model during the training phase, introducing computational overhead for the optimization loop itself.
- Optimized skills are procedural/textual artifacts; performance gains depend on the quality of the held-out validation split and may degrade if the target domain or execution harness diverges significantly from the optimization trajectory.
- Focuses exclusively on text-based skill documents rather than continuous control spaces or weight-space adaptation, limiting direct applicability to low-level robotic or multimodal policy learning.