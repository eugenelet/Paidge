---
layout: page
title: "Task-Aware ICD Configuration"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2503.04839v2)

# ADVANCING MULTIMODAL IN-CONTEXT LEARNING IN LARGE VISION-LANGUAGE MODELS WITH TASK-AWARE DEMONSTRATIONS

#### 🚀 Technical Novelty
* **Mechanism**: SabER employs a lightweight decoder-only transformer with task-aware attention and hierarchical gating to autoregressively select and order in-context demonstrations (ICDs) using unified image-query-result triplets.
* **Nuance**: Moves beyond coarse-grained similarity retrieval by explicitly modeling Task Recognition (TR) and Task Learning (TL) dynamics, resolving cross-modal misalignment through end-to-end task semantics refinement rather than heuristic matching.

#### 💡 Yield
- Achieves 2.00%–9.26% performance gains across five LVLMs and nine benchmarks; empirically proves TR dominates TL in multimodal ICL and that explicit task queries (Q) outweigh ground-truth labels (R) for robust sequence configuration.

#### ⚠️ Limitations
- Gains plateau on simpler tasks; instruction length requires careful balancing to prevent task recognition skew; performance remains dependent on the base LVLM's architectural capacity and CLIP encoder quality.