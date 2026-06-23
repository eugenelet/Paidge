---
layout: page
title: "Many-Shot In-Context Learning"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2404.11018v3)

# Many-Shot In-Context Learning

#### 🚀 Technical Novelty
* **Mechanism**: Introduces "Reinforced ICL" (model-generated chain-of-thought rationales filtered by answer correctness) and "Unsupervised ICL" (input-only prompts without solutions) to scale in-context examples from the traditional few-shot regime to hundreds/thousands of shots.
* **Nuance**: Leverages million-token context windows to demonstrate that many-shot ICL fundamentally alters learning dynamics, overriding pretraining biases, learning high-dimensional numerical functions, and rivaling full fine-tuning performance—contrasting sharply with prior work limited to 1-10 shots due to context constraints.

#### 💡 Yield
- Consistent, significant performance gains across diverse tasks (reasoning, translation, classification) when scaling to hundreds/thousands of shots.
- Reinforced and unsupervised variants effectively reduce dependency on human-generated rationales while maintaining high accuracy on complex reasoning tasks.
- Many-shot ICL successfully learns high-dimensional prediction tasks and overrides pretraining biases, performing comparably to full fine-tuning.
- Next-token prediction loss is empirically shown to be an unreliable proxy for downstream in-context learning task performance.

#### ⚠️ Limitations
- Performance is highly sensitive to the ordering of in-context examples, leading to significant fluctuations across different subtasks and requiring careful prompt optimization.
- Unsupervised ICL remains constrained by the availability of high-quality, domain-specific input data without ground-truth solutions.
- Inference runtime scales linearly with the number of shots, necessitating KV caching and substantial computational budgets for extreme scaling regimes.