---
layout: page
title: "Continuous Latent Reasoning"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2412.06769v3)

# Training Large Language Models to Reason in a Continuous Latent Space

#### 🚀 Technical Novelty
* **Mechanism**: Directly feeds the LLM's last hidden state (a "continuous thought") back as the next input embedding instead of decoding to discrete tokens, trained via a multi-stage curriculum.
* **Nuance**: Differs from prior SOTA by eliminating language-space constraints entirely during reasoning, allowing superposition of multiple reasoning paths and implicit breadth-first search without explicit tree-search algorithms or pause tokens.

#### 💡 Yield
- Outperforms standard CoT on logical reasoning tasks (ProntoQA, ProsQA) with significantly fewer generated tokens.
- Achieves a superior accuracy-efficiency trade-off on math reasoning (GSM8k) by effectively chaining continuous thoughts.
- Emerges with implicit BFS-like planning capabilities without explicit training objectives for search.

#### ⚠️ Limitations
- Requires a multi-stage curriculum guided by language CoT data; struggles to learn latent reasoning purely from end-to-end gradient descent on Q&A pairs.
- Performance gap remains compared to carefully tuned iCoT baselines, indicating room for improved training strategies.
- Generalization to pretraining and broader reasoning challenges needs further exploration.