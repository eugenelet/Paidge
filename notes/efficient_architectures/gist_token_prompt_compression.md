---
layout: page
title: "Gist Token Prompt Compression"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2304.08467v3)

# Learning to Compress Prompts with Gist Tokens

#### 🚀 Technical Novelty
* **Mechanism**: Inserts virtual "gist" tokens between the prompt and input, then modifies Transformer attention masks to force the model to compress all prompt information into these tokens before processing the actual input.
* **Nuance**: Replaces per-task gradient-based prefix tuning with a zero-shot meta-learning approach that predicts gist activations for unseen tasks, amortizing distillation costs across a task distribution without retraining or storing task-specific weights.

#### 💡 Yield
- Achieves up to 26x prompt compression and ~40% FLOPs reduction on LLaMA-7B and FLAN-T5-XXL while maintaining human-evaluated output quality comparable to full prompts.
- Enables caching and reuse of compressed activations, drastically reducing memory/storage overhead compared to traditional prompt caching strategies.

#### ⚠️ Limitations
- Training relies on noisy synthetic instruction data (Alpaca+), which may not fully capture real-world prompt distributions.
- Compression effectiveness is tightly coupled to the number of gist tokens; aggressive compression can degrade output quality.
- Generalization to highly specialized, domain-specific, or out-of-distribution prompts beyond the training distribution remains unverified.