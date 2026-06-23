---
layout: page
title: "KV Cache Token Eviction"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2504.14051v6)

# CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based Token Eviction

#### 🚀 Technical Novelty
* **Mechanism**: Derives a closed-form eviction score that minimizes the mean squared error of the attention output by jointly weighting query-key alignment and value vector contributions.
* **Nuance**: Moves beyond pure attention-score heuristics by explicitly modeling how each cached token's value impacts the final hidden state, enabling it to function as a model-agnostic meta-heuristic atop existing eviction methods.

#### 💡 Yield
- Consistently improves accuracy across LongBench, Needle-in-Haystack, and perplexity benchmarks when integrated with SOTA eviction strategies (H2O, TOVA, SnapKV) on LLaMA3 and Qwen2.5 families.
- Provides a theoretically grounded, post-training optimization that alleviates quadratic attention compute and KV cache memory bottlenecks for long-context inference.

#### ⚠️ Limitations
- Adds minor computational overhead during inference compared to pure attention-score methods (addressed via the proposed FastCAOTE approximation).
- Validated exclusively on decoder-only LLMs; generalization to non-Transformer or multimodal architectures remains unexplored.
- Operates strictly as a post-training eviction heuristic without modifying model weights or training objectives.