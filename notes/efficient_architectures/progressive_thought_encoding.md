---
layout: page
title: "Progressive Thought Encoding"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.16839v1)

# Training Large Reasoning Models Efficiently via Progressive Thought Encoding

#### 🚀 Technical Novelty
* **Mechanism**: Dynamically encodes information from evicted KV cache tokens into fixed-size vector representations that are continuously folded into lightweight LoRA adapters during RL rollouts, preserving long-range context without expanding cache size.
* **Nuance**: Unlike sliding-window or dynamic pruning strategies that permanently discard intermediate reasoning steps, this method maintains constant memory overhead while allowing the model to retain global reasoning signals through online parameter updates rather than token retention.

#### 💡 Yield
- Achieves +19.3% accuracy gain over LoRA-based fine-tuning and +29.9% over untuned LRMs across six mathematical benchmarks under tight cache budgets, with up to +23.4% improvement on AIME2024/2025.
- Reduces peak GPU memory by ~50% during GRPO training while enabling stable scaling to 64K token generation lengths within a fixed 1K context window without performance plateauing.

#### ⚠️ Limitations
- Relies on standard sliding-window eviction rather than advanced, compute-heavy token-dropping strategies (e.g., HeadKV, PyramidKV) due to significant runtime overhead during rollout.
- Primarily validated on mathematical reasoning tasks; generalization to other long-context domains or non-mathematical symbolic manipulation remains untested.