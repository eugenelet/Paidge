---
layout: page
title: "Multi-Image VLM Analysis"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2601.07812v1)

# More Images, More Problems? A Controlled Analysis of VLM Failure Modes.

#### 🚀 Technical Novelty
* **Mechanism**: Procedural multi-image data synthesis from single-image annotations combined with layer-wise causal attention masking to restrict unnecessary cross-image token interactions during fine-tuning.
* **Nuance**: Unlike prior benchmarks that repurpose existing datasets, MIMIC isolates unitary reasoning dimensions (e.g., information distribution, distractor robustness) to pinpoint exact failure modes, while the masking strategy specifically targets deeper transformer layers to enforce cleaner intra-image representations without full architectural overhaul.

#### 💡 Yield
- Achieves state-of-the-art performance across multiple multi-image benchmarks (MuirBench, Blink, NLVR2, etc.) with significant gains on counting and common-object tasks.
- Reduces computational cost by ~81% FLOPs compared to vanilla attention while outperforming full fine-tuning baselines.
- Reveals that SOTA VLMs fundamentally exhibit "single-image behavior," struggling with multi-concept tracking and cross-image aggregation under controlled conditions.

#### ⚠️ Limitations
- Benchmark relies on MS-COCO, limiting direct applicability to specialized domains like dense documents or medical imaging without adaptation.
- Focuses on semantic understanding and counting; pixel-perfect perception of extremely small details may require adaptive resolution strategies not explored here.
- Validated primarily on open-weight models; closed-source model behavior under similar constraints remains unverified.