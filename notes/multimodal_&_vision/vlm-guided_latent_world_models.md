---
layout: page
title: "VLM-Guided Latent World Models"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.22281v1)

# ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a dual-temporal pathway that pairs a dense-frame JEPA predictor for fine-grained motion with a uniformly sampled VLM-thinker branch, linked by a hierarchical pyramid representation extraction module that aggregates multi-layer VLM features into JEPA-compatible guidance via FiLM modulation.
* **Nuance**: Unlike prior SOTA that either rely solely on dense visual predictors (missing semantic context) or use VLMs as standalone dense predictors (suffering from language-output bottlenecks and compute-driven sparsity), ThinkJEPA strictly positions the VLM as a semantic/knowledge guide while preserving high-FPS physical dynamics through the JEPA branch.

#### 💡 Yield
- Achieves superior trajectory prediction accuracy and latent forecasting quality on EgoDex and EgoExo4D benchmarks, with notably stable long-horizon recursive rollout behavior compared to both V-JEPA and Qwen3-VL baselines.

#### ⚠️ Limitations
- Dual-branch architecture incurs significant computational overhead, limiting real-time deployment potential; effective guidance requires careful multi-layer feature alignment that may necessitate domain-specific fine-tuning to avoid catastrophic forgetting or representation mismatch on small action-conditioned datasets.