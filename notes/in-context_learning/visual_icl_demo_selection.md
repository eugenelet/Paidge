---
layout: page
title: "Visual ICL Demo Selection"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.26775v1)

# Learning to Select Visual In-Context Demonstrations

#### 🚀 Technical Novelty
* **Mechanism**: A Dueling DQN agent equipped with a query-centric Transformer Decoder sequentially constructs demonstration sets by optimizing for downstream MLLM accuracy (negative MAE reward).
* **Nuance**: Shifts from static, similarity-first kNN retrieval to a dynamic RL policy that explicitly trades visual redundancy for label-space diversity and regression boundary coverage.

#### 💡 Yield
- LSD significantly outperforms kNN on objective visual regression benchmarks (e.g., UTKFace, KADID-10k) while kNN remains optimal for subjective preference tasks.
- The learned policy generalizes across unseen MLLMs (Gemma, Qwen, Phi) and exhibits emergent label-awareness despite receiving no explicit label supervision during training.
- Empirical analysis confirms the *set* of selected demonstrations matters far more than their sequential order for downstream performance.

#### ⚠️ Limitations
- The diversity-seeking policy can introduce unnecessary variance for subjective preference tasks, where strict visual similarity (kNN) remains superior.
- Performance gains are task-dependent, requiring careful reward design to avoid over-optimizing for specific regression boundaries rather than general ICL robustness.