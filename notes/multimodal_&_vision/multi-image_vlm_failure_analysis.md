---
layout: page
title: "Multi-Image VLM Failure Analysis"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2601.07812v1)

# More Images, More Problems? A Controlled Analysis of VLM Failure Modes.

#### 🚀 Technical Novelty
* **Mechanism**: Procedural synthetic data generation combined with layer-wise causal attention masking that restricts vision tokens to intra-image attention during fine-tuning.
* **Nuance**: Unlike prior works that repurpose existing datasets, this approach isolates unitary reasoning failures (aggregation, tracking, distractors) via a controlled testbed and explicitly modifies the optimization landscape to curb spurious cross-image interactions.

#### 💡 Yield
- Establishes new state-of-the-art across MuirBench, Blink, MMIU, and MIMIC benchmarks; reduces computational cost by ~81% FLOPs while significantly boosting multi-concept tracking and information aggregation capabilities.

#### ⚠️ Limitations
- Benchmark domain restricted to MS-COCO for controlled variable isolation; adaptive resolution strategies for fine-grained pixel tasks are unexplored; validation primarily focuses on open-weight architectures.