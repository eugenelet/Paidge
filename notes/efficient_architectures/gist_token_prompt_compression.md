---
layout: page
title: "Gist Token Prompt Compression"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2304.08467v3)

# Learning to Compress Prompts with Gist Tokens

#### 🚀 Technical Novelty
* **Mechanism**: Modifies Transformer attention masks during instruction tuning to force prompt information into a small set of learnable "gist" tokens, enabling zero-shot prediction and caching of compressed activations.
* **Nuance**: Differs from prefix-tuning (which requires per-task gradient descent) and standard context distillation by using a meta-learning approach that predicts gist prefixes zero-shot for unseen tasks, amortizing training costs across a task distribution rather than optimizing for single prompts.

#### 💡 Yield
- Achieves up to 26x prompt compression on LLaMA-7B and FLAN-T5-XXL while maintaining human-evaluated output quality comparable to uncompressed models.
- Reduces inference FLOPs by up to 40% and wall time by 4.2%, requiring only ~10 lines of code change to standard instruction tuning pipelines.

#### ⚠️ Limitations
- Training relies on noisy, synthetic instruction data sampled from GPT-3 variants, which may limit real-world generalization beyond instruction-following tasks.
- Compression efficacy and quality trade-offs are sensitive to the number of gist tokens (k), with extreme compression potentially degrading performance on complex reasoning or long-context generation.