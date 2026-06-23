---
layout: page
title: "Elastic Looped Transformers"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.09168v2)

# ELT: Elastic Looped Transformers for Visual Generation

#### 🚀 Technical Novelty
* **Mechanism**: Intra-Loop Self Distillation (ILSD) trains intermediate loop states to match the final teacher trajectory, forcing progressive refinement so any early exit yields high-fidelity outputs.
* **Nuance**: Unlike vanilla weight-tied recurrent models where only the fixed training depth converges to a valid solution, ELT decouples parameter count from computational depth, enabling true Any-Time inference without retraining or architectural changes.

#### 💡 Yield
- Achieves competitive FID of 2.0 on ImageNet-256 and FVD of 72.8 on UCF-101 with a 4× parameter reduction under iso-inference-compute settings compared to MaskGIT/MAGVIT baselines.
- Enables dynamic scaling between latency-critical on-device generation and high-fidelity cloud rendering from a single trained model, effectively shifting the efficiency frontier for visual synthesis.

#### ⚠️ Limitations
- Generation quality remains strictly bound to the chosen inference loop count, requiring manual compute-quality trade-offs at deployment rather than automatic adaptation.
- Evaluated primarily on class-conditional generation tasks; scalability and stability for unconditional or complex multi-modal scenarios remain open questions.