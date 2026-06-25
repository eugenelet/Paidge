---
layout: page
title: "Neocortical Learning Theory"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2606.08720v1)

# This is how the Neocortex Learns

#### 🚀 Technical Novelty
* **Mechanism**: Error-driven predictive learning via temporal derivatives (phase-difference activation) combined with corticothalamic circuits and competitive kinase synaptic plasticity, implemented in the Axon spiking neural framework.
* **Nuance**: Replaces explicit error pathways and segregated feedforward/feedback channels with bidirectional excitatory networks that implicitly encode gradients as temporal activity differences, aligning with known neocortical microcircuitry rather than artificial backpropagation architectures.

#### 💡 Yield
- Demonstrates that temporal derivative algorithms mathematically approximate error backpropagation while satisfying computational, algorithmic, and implementational criteria for biological plausibility.
- Integrates behavioral timescale synaptic plasticity (BTSP) and eligibility traces to resolve the temporal credit assignment problem in deep layered networks without requiring instantaneous gradient signals.

#### ⚠️ Limitations
- The precise driving target signal for layer 5 neocortical plasticity remains empirically unresolved.
- Relies on theoretical mapping between abstract algorithms and complex neurochemical processes, requiring further in vivo validation.
- Focuses on computational neuroscience theory rather than large-scale AI engineering benchmarks or architectural innovations.