---
layout: page
title: "RL-Guided In-Context Learning"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2211.04486v1)

# Active Example Selection for In-Context Learning

#### 🚀 Technical Novelty
* **Mechanism**: Formulates demonstration example selection as a sequential decision problem solved via reinforcement learning to iteratively query and incorporate unlabeled examples that maximize in-context task performance.
* **Nuance**: Shifts from static prompt engineering (random sampling, reordering, or calibration) to active, policy-driven search, revealing that ICL stability is highly dependent on demonstration composition rather than just ordering or scaling.

#### 💡 Yield
- RL-derived policies achieve a 5.8% average accuracy gain on unseen tasks and 12.1% on seen tasks for GPT-2 compared to max-entropy active learning baselines.
- Empirically proves that ICL performance variance is driven by example selection quality, with optimal demonstration properties (e.g., label balance, coverage) often contradicting human intuition.
- Establishes a clear scaling trajectory: selection gains are substantial for GPT-2 and GPT-3 Ada but diminish significantly on larger models due to emerging robustness capabilities.

#### ⚠️ Limitations
- Experiments constrained to 4-shot classification tasks due to context window limits and diminishing returns from additional examples.
- Performance improvements fade substantially as model scale increases, limiting practical utility for state-of-the-art large language models.
- Evaluated exclusively on text classification; generalization to complex reasoning, generation, or multi-modal domains remains unverified.