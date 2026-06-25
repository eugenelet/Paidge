---
layout: page
title: "RL-Based Sequential ICL Retrieval"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2305.14502v2)

# RetICL: Sequential Retrieval of In-Context Examples with Reinforcement Learning

#### 🚀 Technical Novelty
* **Mechanism**: Frames sequential ICL example selection as a Markov Decision Process (MDP) and trains a recurrent retriever using RL, incorporating a novel confidence reward based on generated solution perplexity.
* **Nuance**: Unlike prior methods that score examples independently or rely on static heuristics, RetICL dynamically models inter-example dependencies and prompt ordering during the retrieval process itself.

#### 💡 Yield
- Consistently outperforms or matches heuristic and learnable baselines on math word problem (TabMWP, GSM8K) and scientific QA (QASC) tasks while implicitly learning to cluster examples by solution strategy and complexity rather than mere semantic similarity.

#### ⚠️ Limitations
- Relies on a fixed number of in-context examples per prompt; corpus size is highly sensitive; struggles with noise from LLM arithmetic errors during training; currently limited to LSTM architecture without testing on open-ended or real-world educational applications.