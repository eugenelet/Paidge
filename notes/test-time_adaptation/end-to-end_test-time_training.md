---
layout: page
title: "End-to-End Test-Time Training"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.23675v2)

# End-to-End Test-Time Training for Long Context

#### 🚀 Technical Novelty
* **Mechanism**: Continuously updates model weights during inference via next-token prediction on the input context, initialized through an outer-loop meta-learning optimization that prepares the network specifically for test-time adaptation.
* **Nuance**: Unlike prior dynamic evaluation or TTT methods that decouple training and test objectives, this approach is fully end-to-end differentiable at both stages while maintaining O(1) decode latency, avoiding the quadratic scaling of full attention and the degradation seen in RNN/delta-net baselines beyond 32K context.

#### 💡 Yield
- Maintains loss scaling parity with full-attention Transformers up to 128K context length without performance degradation.
- Achieves constant inference latency regardless of context length, delivering a 2.7× speedup over full attention at 128K on H100 hardware.

#### ⚠️ Limitations
- Requires computing and applying gradients during inference, increasing per-token compute and memory overhead compared to standard autoregressive decoding.
- Extension fine-tuning for sliding-window/RNN baselines suffers from high gradient variance at longer contexts due to fewer sequences per batch, though TTT-E2E mitigates this through its meta-initialized design.
- Relies on careful tuning of the test-time learning rate and meta-initialization hyperparameters to avoid instability during context compression.