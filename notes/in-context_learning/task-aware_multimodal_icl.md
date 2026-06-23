---
layout: page
title: "Task-Aware Multimodal ICL"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2503.04839v2)

# ADVANCING MULTIMODAL IN-CONTEXT LEARNING IN LARGE VISION-LANGUAGE MODELS WITH TASK-AWARE DEMONSTRATIONS

#### 🚀 Technical Novelty
* **Mechanism**: SabER deploys a lightweight decoder-only transformer with task-aware attention to autoregressively select and order in-context demonstrations (ICDs), iteratively refining cross-modal feature extraction and explicit task mapping.
* **Nuance**: Unlike prior heuristic or similarity-based retrieval methods that treat selection and ordering as disjoint steps, SabER jointly optimizes ICD configuration end-to-end using explicit task-specific queries and hierarchical masking to resolve modality misalignment and complex input-output mappings.

#### 💡 Yield
- Consistently outperforms SOTA across 5 LVLMs and 9 benchmarks (gains of +2.00% to 9.26%), with the largest improvements on complex VQA tasks (+8.41% on VizWiz).
- Empirically proves Task Recognition (TR) dominates Task Learning (TL) in LVLMs, and that explicit task semantics (queries) are more critical than ground-truth labels for guiding ICL.
- Ablations confirm hierarchical layer interaction and binary gating modules are optimal for cross-modal grounding without overfitting or feature loss.

#### ⚠️ Limitations
- Trade-off exists between instruction detail and task recognition accuracy; overly verbose prompts can skew semantics and hinder model convergence.
- Performance gains are more modest on simpler tasks (e.g., image captioning) compared to complex, composition-heavy benchmarks.
- Relies on fixed pre-trained CLIP encoders for initial embedding generation, which may limit adaptability to novel visual domains without re-encoding or adapter fine-tuning.