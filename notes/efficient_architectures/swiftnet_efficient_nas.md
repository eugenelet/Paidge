---
layout: page
title: "SwiftNet Efficient NAS"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/1906.08305v2)

# SwiftNet: Using Graph Propagation as Meta-knowledge to Search Highly Representative Neural Architectures

#### 🚀 Technical Novelty
* **Mechanism**: GRAM employs a node-wise search over a complete Directed Acyclic Graph (DAG) to continuously accumulate architectural knowledge into a meta-graph, combined with a novel structure-level pruning method that removes low-weight edges to extract resource-aware models.
* **Nuance**: Unlike cell-based NAS approaches that rely on rigid predefined blocks and width multipliers (which discard useful feature maps and drop accuracy), GRAM explores a vastly larger, unconstrained search space and preserves structural redundancy information through graph-based pruning rather than channel scaling.

#### 💡 Yield
- SwiftNet achieves 2.15× higher accuracy density than MobileNet-V2 and reduces FBNet's search cost by 26×, reaching 63.28% top-1 ImageNet accuracy with only 53M MACs and 2.07M parameters while delivering up to 2.42× faster inference latency on mobile hardware.

#### ⚠️ Limitations
- The convergence of the meta-graph relies on Gibbs Sampling, which does not provide a strict theoretical guarantee on the upper bound of iterations required before convergence.