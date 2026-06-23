---
layout: page
title: "Temporal Derivative Learning"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2606.08720v1)

# This is how the Neocortex Learns

#### 🚀 Technical Novelty
* **Mechanism**: Error-driven predictive learning via temporal derivatives (recirculation/GeneRec), where backpropagated gradients are implicitly computed as phase-based temporal differences between prediction and outcome activation states rather than explicit error populations.
* **Nuance**: Eliminates the need for segregated feedforward/feedback pathways or dedicated error-coding neurons required by standard predictive coding and biologically-inspired backprop approximations, instead leveraging bidirectional excitatory connectivity and thalamocortical loops to approximate gradients while strictly adhering to known neurochemical plasticity constraints.

#### 💡 Yield
- Provides a unified computational, algorithmic, and implementational framework that satisfies Marr’s three levels of analysis for neocortical learning.
- Resolves the temporal credit assignment problem through behavioral timescale synaptic plasticity (BTSP) and eligibility traces that bridge delayed reinforcement signals with earlier state representations.
- Demonstrates via spiking neural simulations that this mechanism scales to complex, cognitively motivated tasks without sacrificing biological plausibility or requiring non-local weight transport.

#### ⚠️ Limitations
- Relies heavily on theoretical synthesis and computational modeling rather than direct empirical benchmarking against competing neurobiological datasets.
- Leaves unresolved the precise identity, routing, and neuromodulatory integration of target signals for layer 5 neocortical output neurons.
- Computational scaling to massive cortical-scale networks remains constrained by current spiking simulation frameworks and hardware efficiency limitations.