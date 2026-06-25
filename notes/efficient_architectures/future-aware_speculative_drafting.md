---
layout: page
title: "Future-Aware Speculative Drafting"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.08899v1)

# ConFu: Contemplate the Future for Better Speculative Sampling

#### 🚀 Technical Novelty
* **Mechanism**: Introduces learnable soft prompts and a dynamic Mixture-of-Experts (MoE) mechanism to generate "contemplate tokens" that capture the frozen target model's intermediate reasoning trajectory, feeding these future-oriented signals into the draft model at negligible inference cost.
* **Nuance**: Unlike prior SOTA methods like EAGLE-3 that condition draft generation solely on the current prefix (leading to distribution drift and error accumulation), ConFu explicitly bridges speculative decoding with continuous latent reasoning tokens to anticipate semantic trajectories before committing to specific token choices.

#### 💡 Yield
- Achieves an 8–11% improvement in both token acceptance rates and generation speed over EAGLE-3 across Llama-3 3B/8B models on SpecBench, with consistent gains across varying temperatures (0.0, 0.7, 1.0) and draft tree budgets (30/60 nodes).
- Ablation studies confirm that both the MoE-based dynamic contemplate tokens and the future prediction replication training strategy are critical for robust performance, outperforming static token baselines.

#### ⚠️ Limitations
- The insertion of contemplate tokens introduces additional computation proportional to the draft tree budget, requiring careful trade-offs between lookahead depth and latency.
- Relies on a frozen target model; cannot fine-tune the base LLM weights, limiting direct adaptation to specialized downstream domains without external prompting or retrieval augmentation.
- Anticipation accuracy naturally degrades at higher sampling temperatures where the target model's future trajectory becomes less deterministic and harder to predict.