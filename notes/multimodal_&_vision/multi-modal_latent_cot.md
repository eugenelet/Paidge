---
layout: page
title: "Multi-Modal Latent CoT"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2312.08762v1)

# Multi-modal Latent Space Learning for Chain-of-Thought Reasoning in Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Replaces static off-the-shelf vision extractors with a diffusion-based latent space learning module that iteratively aligns visual features with textual reasoning steps via noise prediction and denoising.
* **Nuance**: Unlike prior SOTA methods that fuse shallow, fixed CLIP/DETR features via attention, this approach captures high-level semantic dependencies through iterative transformations, enabling deeper cross-modal understanding specifically tailored for complex logical inference.

#### 💡 Yield
- Achieves state-of-the-art performance on ScienceQA (90.97% base / 93.35% large), surpassing ChatGPT by 18.18% with under 1B parameters.
- Demonstrates strong cross-task generalization, significantly boosting multi-modal machine translation BLEU scores across multiple benchmarks.
- Ablation studies confirm that fine-tuning the VAE and UNet components during CoT training is essential for generating reasoning-aligned visual latents over static pre-training.

#### ⚠️ Limitations
- Relies on a sequential two-stage pipeline (rationale generation followed by answer inference), making it vulnerable to error propagation if initial rationales are flawed.
- Requires careful input masking for image-less questions (preferring zero tensors over blank images) to prevent diffusion noise from introducing misleading visual priors.
- The iterative diffusion process increases computational overhead during training and inference compared to single-pass feature extraction baselines.