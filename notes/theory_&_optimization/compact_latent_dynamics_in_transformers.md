---
layout: page
title: "Compact Latent Dynamics in Transformers"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2511.05963v4)

# Next-Latent Prediction Transformers Learn Compact World Models

#### 🚀 Technical Novelty
* **Mechanism**: Extends standard next-token prediction with an auxiliary self-supervised objective that trains a lightweight dynamics model to predict the transformer’s next latent state given the current latent state and new token.
* **Nuance**: Unlike hybrid architectures or token-space methods, NextLat leaves the transformer architecture intact, using only an outer-loop auxiliary loss to enforce temporal consistency during fully parallel training without sequential computation overhead.

#### 💡 Yield
- Theoretically proves that latent representations provably converge to sufficient-statistic belief states for future prediction under the proposed objective.
- Empirically demonstrates superior length generalization on NC1-complete state-tracking tasks (A5 word problem) compared to standard GPT baselines, with a co-trained RNN extrapolating far beyond the transformer's expressivity limits.
- Enables variable-length self-speculative decoding, accelerating language modeling inference by up to 3.3× without requiring separate draft models or multi-token prediction heads.

#### ⚠️ Limitations
- Experiments restricted to simple MLP latent dynamics models; broader architectural search for the dynamics model remains unexplored.
- Objective design (stop-gradients, KL distillation, loss functions) relies on small-scale ablations; necessity of specific components at larger model/data scales is unverified.
- Computational constraints prevented evaluation of hidden layer width effects in the dynamics bottleneck or full scaling studies across diverse domains.