---
layout: page
title: "Visual ICL Demo Selection"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.26775v1)

# Learning to Select Visual In-Context Demonstrations

#### 🚀 Technical Novelty
* **Mechanism**: A Dueling DQN agent paired with a query-centric Transformer Decoder that sequentially constructs demonstration sets by maximizing downstream MLLM accuracy via a reward signal derived from prediction error (MAE).
* **Nuance**: Replaces static, similarity-first kNN retrieval with a dynamic, task-aware RL policy that actively balances visual relevance with label-space diversity, explicitly avoiding the redundant "boundary" examples that plague unsupervised baselines.

#### 💡 Yield
- LSD significantly outperforms kNN on objective visual regression benchmarks (UTKFace, KADID-10k, etc.) by learning to select diverse boundary examples that better define regression spaces.
- Reveals a fundamental task-dependent dichotomy: kNN remains optimal for subjective preference tasks, but learned selection is strictly necessary for objective/factual tasks.
- Demonstrates strong cross-MLLM generalization, with the frozen RL policy maintaining performance advantages on unseen architectures (Qwen 2.5, Phi-3.5) without retraining.

#### ⚠️ Limitations
- The diversity-seeking policy introduces unnecessary variance for subjective preference tasks, making it suboptimal where strict visual similarity (kNN) is preferred.
- Relies on pre-computed embeddings (SigLIP) and MLLM feedback for rewards, limiting direct applicability to domains lacking clear regression metrics or accessible reward signals.
- Sequential selection adds computational overhead compared to static retrieval, though it scales via FAISS-based approximate nearest-neighbor search.