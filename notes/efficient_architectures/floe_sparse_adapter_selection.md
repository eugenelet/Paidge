---
layout: page
title: "FLoE Sparse Adapter Selection"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2506.00495v1)

# FLoE: Fisher-Based Layer Selection for Efficient Sparse Adaptation of Low-Rank Experts

#### 🚀 Technical Novelty
* **Mechanism**: Fisher information-guided importance scoring dynamically identifies task-critical transformer layers, paired with Bayesian optimization to automatically allocate optimal LoRA ranks without exhaustive grid search.
* **Nuance**: Breaks from the uniform adapter deployment paradigm of prior PEFT methods (e.g., HydraLoRA) by sparsely activating only a fraction of layers, eliminating redundant parameter allocation and mitigating cross-domain interference.

#### 💡 Yield
- Retains 93.1% of full fine-tuning accuracy on MMLU while adapting just 25% of layers; delivers a 7.0% relative performance gain over full-layer PEFT in mixed-domain tasks; significantly cuts GPU memory footprint and inference latency.

#### ⚠️ Limitations
- Restricts each LoRA module to a fixed number of low-rank experts rather than dynamically scaling expert counts per layer.
- Requires an initial full-layer fine-tuning phase on a sampled dataset to compute importance scores before final sparse adaptation.