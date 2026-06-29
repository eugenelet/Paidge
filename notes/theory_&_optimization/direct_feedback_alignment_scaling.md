---
layout: page
title: "Direct Feedback Alignment Scaling"
parent: "Theory & Optimization"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2006.12878v2)

# Direct Feedback Alignment Scales to Modern Deep Learning Tasks and Architectures

#### 🚀 Technical Novelty
* **Mechanism**: Replaces backpropagation’s transposed weight matrix with a fixed random projection of the global error to each layer, enabling parallel credit assignment under synaptic asymmetry.
* **Nuance**: Overcomes prior limitations that confined DFA to simple fully-connected networks by demonstrating its viability across complex, modern architectures (Transformers, Graph Convolutions, NeRFs) in diverse domains.

#### 💡 Yield
- Achieves backpropagation-parity performance across 8 tasks and 11 architectures; proves challenging tasks are solvable without weight transport when optimizer hyperparameters (e.g., Adam’s β2, LR schedules) are carefully adapted.

#### ⚠️ Limitations
- Still requires an implausible global feedback pathway; maintains a performance gap with BP in complex settings like Transformers without extensive fine-tuning; retains minimal weight transport for embeddings and attention matrices.