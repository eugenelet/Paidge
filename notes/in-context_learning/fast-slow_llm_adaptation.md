---
layout: page
title: "Fast-Slow LLM Adaptation"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.12484v2)

# Learning, Fast and Slow: Towards LLMs That Adapt Continually

#### 🚀 Technical Novelty
* **Mechanism**: Treats optimized prompts/context as trainable “fast weights” that co-evolve in real-time with slow parametric updates via RL, distributing adaptation across both channels.
* **Nuance**: Breaks the traditional sequential pipeline of fine-tuning followed by prompt tuning by jointly optimizing textual scaffolds and model parameters against verifiable rewards simultaneously, rather than treating them as disjoint or post-hoc steps.

#### 💡 Yield
- Achieves up to 3× sample efficiency gains over RL-only training on math, code, and reasoning tasks while reaching higher performance ceilings.
- Reduces KL divergence from the base model by up to 70%, effectively mitigating catastrophic forgetting and preserving plasticity for downstream task shifts.
- Demonstrates robust continual learning capabilities, successfully adapting to sequential domain changes where parameter-only RL stalls or collapses.

#### ⚠️ Limitations
- Computational overhead stems from maintaining a diverse population of candidate prompts and running interleaved optimization loops.
- Fast-to-slow distillation alone cannot replicate joint reward optimization, confirming that both channels must be actively trained together for peak performance.
- Relies on specific instantiations (GEPA for prompts, CISPO/RLVR for weights); broader optimizer ablations and efficiency improvements are deferred to future work.