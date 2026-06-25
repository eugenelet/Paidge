---
layout: page
title: "Fisher-Guided Sparse LoRA"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2506.00495v1)

# FLoE: Fisher-Based Layer Selection for Efficient Sparse Adaptation of Low-Rank Experts

#### 🚀 Technical Novelty
* **Mechanism**: Fisher information-guided importance scoring dynamically identifies task-critical transformer layers, paired with Bayesian optimization to automatically allocate optimal LoRA ranks without exhaustive grid search.
* **Nuance**: Replaces uniform full-layer MoE-LoRA deployment with sparse, context-aware adapter placement, eliminating redundant parameter allocation and mitigating domain interference across mixed tasks.

#### 💡 Yield
- Retains 93.1% of full fine-tuning accuracy while adapting just 25% of layers; achieves up to 7.0% relative gain over full-layer PEFT in mixed-domain benchmarks; significantly cuts GPU memory and training runtime.

#### ⚠️ Limitations
- Restricts each LoRA module to a fixed number of low-rank experts; requires an initial full-layer MoE-LoRA fine-tuning phase on sampled data for layer/rank selection; primarily validated on LLaMA2, Gemma2, and Mistral families.