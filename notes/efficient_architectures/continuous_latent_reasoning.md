---
layout: page
title: "Continuous Latent Reasoning"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2412.06769v3)

# Training Large Language Models to Reason in a Continuous Latent Space

#### 🚀 Technical Novelty
* **Mechanism**: Directly feeds the transformer's last hidden state back as the next input embedding instead of decoding it into discrete word tokens, creating a fully differentiable "continuous thought" loop.
* **Nuance**: Unlike standard CoT or pause-token methods constrained by language space and autoregressive token generation, this approach operates in an unconstrained latent space, allowing superposition of multiple reasoning paths without fluency overhead.

#### 💡 Yield
- Emerges implicit breadth-first search (BFS) behavior for planning without explicit training instructions
- Achieves higher accuracy with significantly fewer generated tokens on logical and mathematical reasoning benchmarks (ProntoQA, ProsQA, GSM8k)
- Demonstrates that continuous states efficiently encode intermediate variables and alternative next steps compared to discrete text

#### ⚠️ Limitations
- Requires a carefully designed multi-stage curriculum guided by language reasoning chains to converge effectively
- Fails to outperform baselines when trained purely via gradient descent on Q&A without curriculum supervision
- Scaling the paradigm to full pretraining and generalizing beyond supervised guidance remains unproven