---
layout: page
title: "Multi-Modal Latent CoT"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2312.08762v1)

# Multi-modal Latent Space Learning for Chain-of-Thought Reasoning in Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Employs a diffusion process (VAE + UNet) to iteratively denoise and align image representations with text, creating a dynamic multi-modal latent space optimized for reasoning.
* **Nuance**: Replaces static, shallow off-the-shelf vision encoders (e.g., CLIP/DETR) fused via attention with a generative alignment process that captures deeper semantic dependencies tailored to language thoughts.

#### 💡 Yield
- Achieves state-of-the-art accuracy on ScienceQA (90.97% base, 93.35% large), surpassing ChatGPT by 18.18% with under 1B parameters.
- Sets new SOTA in multi-modal machine translation (EN-DE/EN-FR) and demonstrates that diffusion-enhanced latent spaces yield more coherent rationales than fixed visual features.

#### ⚠️ Limitations
- Relies heavily on pre-trained stable diffusion components for optimal initialization; random initialization, while helpful, requires significant training to match performance.
- Handling image-less questions introduces sensitivity to input representation (zero tensors outperform blank images to avoid misleading diffusion noise).
- Operates on a two-stage pipeline (rationale generation followed by answer inference), which may increase computational overhead compared to single-pass architectures.