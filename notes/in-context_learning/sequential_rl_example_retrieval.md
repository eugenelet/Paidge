---
layout: page
title: "Sequential RL Example Retrieval"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2305.14502v2)

# RetICL: Sequential Retrieval of In-Context Examples with Reinforcement Learning

#### 🚀 Technical Novelty
* **Mechanism**: Models ICL example selection as a Markov Decision Process (MDP) and trains an LSTM-based retriever via reinforcement learning to sequentially pick examples, incorporating a novel confidence reward based on generated solution perplexity.
* **Nuance**: Unlike prior methods that score examples independently or rely on static semantic similarity, RetICL dynamically conditions each selection on previously chosen examples and their ordering, implicitly capturing inter-example dependencies and reasoning strategies.

#### 💡 Yield
- Consistently outperforms or matches heuristic and learnable baselines across math word problem (TabMWP, GSM8K) and scientific QA (QASC) benchmarks.
- Qualitative latent space analysis reveals the model clusters examples by solution complexity and reasoning steps rather than superficial semantic features.

#### ⚠️ Limitations
- Uses a fixed number of in-context examples, preventing dynamic prompt length adaptation during inference.
- Training rewards rely on LLM-generated solutions, which can introduce noise from arithmetic errors or flawed logic.
- Primarily validated on structured math/QA tasks; generalization to open-ended generation or real-world educational settings remains unproven.