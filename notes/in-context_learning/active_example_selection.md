---
layout: page
title: "Active Example Selection"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2211.04486v1)

# Active Example Selection for In-Context Learning

#### 🚀 Technical Novelty
* **Mechanism**: Formulates active demonstration selection as a sequential decision problem and trains a reinforcement learning policy to iteratively pick unlabeled examples that maximize in-context accuracy without requiring gold labels during selection.
* **Nuance**: Moves beyond static heuristics like prompt reordering or calibration by learning generalizable selection policies, revealing that optimal example properties often contradict human intuition and exhibit strong scale-dependent behaviors across model sizes.

#### 💡 Yield
- Learned RL policies generalize to unseen tasks with a 5.8% average accuracy gain on GPT-2, while exposing high performance variance across random example sets and demonstrating diminishing returns on larger GPT-3 models due to emerging capabilities.

#### ⚠️ Limitations
- Experiments are constrained to k=4 shots due to context window limits of the tested models, and performance gains vanish on larger GPT-3 architectures, indicating limited direct applicability to state-of-the-art LLMs without further adaptation.