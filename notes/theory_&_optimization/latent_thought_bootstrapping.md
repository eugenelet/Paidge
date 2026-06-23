---
layout: page
title: "Latent Thought Bootstrapping"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2503.18866v2)

# Reasoning to Learn from Latent Thoughts

#### 🚀 Technical Novelty
* **Mechanism**: Employs an Expectation-Maximization algorithm to iteratively synthesize and train on "latent thoughts" that decompress highly compressed web text, creating a self-improving pretraining loop.
* **Nuance**: Unlike reward-based RL or fixed teacher-student distillation, it frames reasoning as a latent variable optimization problem, enabling scalable, task-agnostic data augmentation without external supervision.

#### 💡 Yield
- A 1B LM successfully bootstraps its performance across three+ iterations using only self-generated latents, achieving 25.4% on MATH versus 5.74% for raw-data baselines.
- Performance gains scale linearly with additional inference compute (Monte Carlo samples) during the E-step, proving inference-time scaling directly boosts pretraining data efficiency.

#### ⚠️ Limitations
- Validated only on a 1B parameter model and reasoning-intensive math text due to strict compute budgets, leaving general-domain scaling unproven.
- Self-bootstrapping may amplify dataset biases or degrade unrelated capabilities (e.g., observed GSM8K few-shot CoT degradation).
- Current autoregressive latent structure is locally myopic and cannot capture hierarchical, long-form planning processes.