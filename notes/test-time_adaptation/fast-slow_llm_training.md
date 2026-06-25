---
layout: page
title: "Fast-Slow LLM Training"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.12484v2)

# Learning, Fast and Slow: Towards LLMs That Adapt Continually

#### 🚀 Technical Novelty
* **Mechanism**: Introduces Fast-Slow Training (FST), which co-evolves slow parametric weights via verifiable-reward RL and fast textual weights via reflective prompt optimization (GEPA) in an interleaved feedback loop.
* **Nuance**: Unlike traditional pipelines that treat parameter updates and prompt tuning as sequential or disjoint, FST distributes adaptation across both channels simultaneously, allowing context to absorb transient task signals while parameters retain general reasoning capabilities.

#### 💡 Yield
- Achieves up to 3× sample efficiency compared to RL-only training while reaching higher performance ceilings on math, code, and reasoning tasks.
- Reduces KL divergence from the base model by up to 70%, significantly mitigating catastrophic forgetting and preserving plasticity for subsequent tasks.
- Demonstrates robust continual learning capabilities, successfully adapting to sequentially changing task domains where parameter-only RL stalls or collapses.

#### ⚠️ Limitations
- Initial exploration of fast-to-slow distillation shows it cannot fully replace joint reward optimization, indicating both channels must be trained together for optimal performance.
- Computational efficiency and trajectory reuse across prompt/weight updates remain open challenges requiring further optimization.
- Framework generality depends on the choice of underlying optimizers (e.g., GEPA for prompts, RLVR for weights), which may vary in stability or cost.