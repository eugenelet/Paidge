---
layout: page
title: "OpenVLA Generalist Robot Policy"
parent: "Embodied AI & Robotics"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2406.09246v3)

# OpenVLA: An Open-Source Vision-Language-Action Model

#### 🚀 Technical Novelty
* **Mechanism**: Fuses multi-granularity visual features (DINOv2 + SigLIP) with a Llama-2 backbone, directly fine-tuned on 970k real-world robot episodes to predict actions as language tokens. Integrates LoRA for parameter-efficient adaptation and int4 quantization for low-memory inference.
* **Nuance**: Replaces closed, massive VLAs (e.g., RT-2-X at 55B) and modular architectures with a streamlined, end-to-end token-fusion pipeline that achieves higher success rates with 7x fewer parameters while enabling commodity-GPU deployment.

#### 💡 Yield
- Surpasses RT-2-X by 16.5% absolute task success rate across 29 tasks and multiple robot embodiments.
- Matches full fine-tuning performance using only 1.4% of trainable parameters via LoRA, cutting training compute by 8x.
- Achieves bfloat16-level accuracy with int4 quantization, halving VRAM requirements while maintaining viable control frequencies (~3Hz).

#### ⚠️ Limitations
- Restricted to single-image observations; lacks support for multi-view, proprioceptive history, or heterogeneous sensory inputs.
- Inference throughput remains insufficient for high-frequency control setups (e.g., 50Hz ALOHA systems).
- Peak success rates rarely exceed 90%, highlighting reliability gaps in complex real-world scenarios.
- Compute constraints left foundational design questions (e.g., base VLM scaling, internet-scale co-training benefits) unexplored.