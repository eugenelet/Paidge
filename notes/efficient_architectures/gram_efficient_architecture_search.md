---
layout: page
title: "GRAM Efficient Architecture Search"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/1906.08305v2)

# SwiftNet: Using Graph Propagation as Meta-knowledge to Search Highly Representative Neural Architectures

#### 🚀 Technical Novelty
* **Mechanism**: GRAM represents network operations as nodes in a Directed Acyclic Graph (DAG) and accumulates learned structural knowledge into a meta-graph via node-wise search and Gibbs sampling.
* **Nuance**: Unlike prior cell-based NAS methods that rely on rigid blocks and width multipliers (causing accuracy drops when downsizing), GRAM enables flexible, fine-grained structure-level pruning directly on the meta-graph to remove redundant edges without retraining.

#### 💡 Yield
- SwiftNet achieves 2.15× higher accuracy density than MobileNet-V2 and reduces search cost by 26× compared to FBNet, reaching 63.28% top-1 ImageNet accuracy with only 53M MACs and 2.07M parameters (19.09ms latency on Pixel 1).

#### ⚠️ Limitations
- The meta-graph convergence relies on Gibbs sampling, which lacks a strict theoretical upper bound guarantee for the number of iterations required to converge; rigorous convergence analysis is deferred to future work.