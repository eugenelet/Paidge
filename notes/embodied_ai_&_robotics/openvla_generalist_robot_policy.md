---
layout: page
title: "OpenVLA Generalist Robot Policy"
parent: "Embodied AI & Robotics"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2406.09246v3)

# OpenVLA: An Open-Source Vision-Language-Action Model

#### 🚀 Technical Novelty
* **Mechanism**: Fuses DINOv2 and SigLIP visual encoders with a Llama 2 backbone, directly tokenizing robot actions into the VLM vocabulary and fine-tuning on 970k real-world episodes. Leverages LoRA for parameter-efficient adaptation and int4 quantization for low-memory inference.
* **Nuance**: Unlike closed VLAs or modular generalist policies that stitch components together, OpenVLA adopts an end-to-end tokenization approach for actions, enabling out-of-the-box cross-embodiment control and open-source accessibility while matching full fine-tuning performance with only 1.4% trainable parameters.

#### 💡 Yield
- Outperforms the closed 55B-parameter RT-2-X model by 16.5% absolute success rate across 29 tasks using 7x fewer parameters.
- LoRA fine-tuning matches full fine-tuning accuracy while reducing trainable parameters to 1.4% and cutting compute time by 8x on consumer GPUs.
- int4 quantization halves VRAM requirements without sacrificing task success rates, enabling deployment on hardware with <16GB memory.

#### ⚠️ Limitations
- Restricted to single-image observations, lacking support for multi-view cameras, proprioceptive history, or heterogeneous sensory inputs.
- Inference throughput is insufficient for high-frequency control setups (e.g., 50Hz), limiting applicability to dexterous or bi-manual tasks.
- Achieves <90% success rates on tested tasks, indicating reliability gaps, with many architectural and training design questions left unexplored due to compute constraints.