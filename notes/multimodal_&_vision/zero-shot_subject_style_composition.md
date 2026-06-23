---
layout: page
title: "Zero-Shot Subject Style Composition"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2502.19673v1)

# SubZero: Composing Subject, Style, and Action via Zero-Shot Personalization

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a Disentangled Stochastic Optimal Controller for latent modulation combined with Orthogonal Temporal Aggregation (OTA) in cross-attention blocks to fuse subject, style, and text conditioning without fine-tuning.
* **Nuance**: Unlike ControlNet or IP-Adapter pipelines that suffer from rigid conditioning or content/style leakage, SubZero uses zero-order optimization and custom-trained projectors to explicitly disentangle features, enabling flexible action prompts and diverse outputs while remaining inference-only.

#### 💡 Yield
- Establishes new state-of-the-art on face and object stylization benchmarks, outperforming RB-Modulation and IP-Adapter by 2–4% in average similarity scores.
- Achieves 64–74% human preference rates for identity preservation and style alignment without requiring helper prompts or per-concept adapter training.
- Demonstrates strong compatibility with fast diffusion backbones (e.g., SDXL-Lightning, Wurstchen) and low compute overhead suitable for on-device deployment.

#### ⚠️ Limitations
- Requires initial offline training of custom subject/style projectors despite offering zero-shot inference capabilities.
- Stochastic latent optimization introduces additional inference steps compared to purely feed-forward adapters, potentially limiting real-time throughput on highly constrained hardware.
- Performance remains dependent on the quality and domain alignment of the underlying text-to-image backbone model.