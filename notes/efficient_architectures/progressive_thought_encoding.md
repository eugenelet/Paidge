---
layout: page
title: "Progressive Thought Encoding"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.16839v1)

# Training Large Reasoning Models Efficiently via Progressive Thought Encoding

#### 🚀 Technical Novelty
* **Mechanism**: Dynamically compresses information from evicted KV cache tokens into fixed-size vector representations during RL rollouts, then folds these representations into lightweight LoRA adapters to preserve long-range context.
* **Nuance**: Unlike sliding-window caches that permanently discard early tokens and degrade reasoning, or full-cache approaches that exhaust VRAM, this method maintains a constant memory footprint while continuously updating model weights with compressed historical states, enabling longer reasoning trajectories without architectural overhauls.

#### 💡 Yield
- Achieves up to +23.4% accuracy gains on AIME benchmarks under tight cache budgets compared to vanilla RL training and LoRA baselines.
- Reduces peak GPU memory usage by nearly 50% during GRPO post-training while enabling scalable rollouts up to 64K tokens within a fixed 1K context window.
- Demonstrates consistent performance scaling across Qwen2.5 (3B/7B) and DeepSeek-R1-Distill-Llama-8B models on six mathematical reasoning benchmarks.

#### ⚠️ Limitations
- Relies on standard sliding-window token eviction, which treats all evicted tokens equally without importance weighting (advanced dropping strategies noted as future work).
- Evaluated exclusively on mathematical reasoning tasks; generalization to other domains or non-mathematical complex reasoning remains unverified.
- Performance can degrade with excessive global token counts (e.g., #Global-64 underperforms #Global-32 at highly constrained cache sizes), indicating a sensitivity to adapter capacity tuning.