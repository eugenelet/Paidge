---
layout: page
title: "Bootstrapping Latent Thoughts"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2503.18866v2)

# Reasoning to Learn from Latent Thoughts

#### 🚀 Technical Novelty
* **Mechanism**: Frames pretraining as a latent variable problem where the model infers underlying "thoughts" (Z) from observed text (X), using Monte Carlo sampling within an Expectation-Maximization loop to generate and train on synthetic thought-augmented data.
* **Nuance**: Unlike teacher-student distillation or reward-based RL methods, this approach requires no external supervision or verifiable rewards; it creates a self-contained bootstrapping loop where the model progressively improves its own latent generator and training corpus using only inference compute.

#### 💡 Yield
- A 1B LM successfully bootstrapped across three iterations, achieving 25.4% on MATH (vs. 5.74% raw data baseline) without task-specific labels, with performance scaling predictably as Monte Carlo samples increase during the E-step.

#### ⚠️ Limitations
- Experiments are constrained to a 1B parameter model and reasoning-heavy math text due to compute limits; lacks exploration of hierarchical latent structures, efficient sampling variants, and potential bias amplification from prolonged self-bootstrapping.