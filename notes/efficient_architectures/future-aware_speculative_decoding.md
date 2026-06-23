---
layout: page
title: "Future-Aware Speculative Decoding"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2603.08899v1)

# ConFu: Contemplate the Future for Better Speculative Sampling

#### 🚀 Technical Novelty
* **Mechanism**: Deploys learnable soft prompts and dynamic Mixture-of-Experts to extract target model reasoning states as auxiliary inputs for draft token generation.
* **Nuance**: Unlike EAGLE which conditions only on the current prefix (causing drift), ConFu explicitly anticipates the target’s semantic trajectory, aligning draft distributions with future states at negligible overhead.

#### 💡 Yield
- Delivers 8–11% average gains in token acceptance rates and generation throughput over EAGLE-3 across Llama-3 3B/8B models on SpecBench.

#### ⚠️ Limitations
- Contemplate token insertion adds compute proportional to draft tree size, requiring future work to minimize overhead for maximal scalability.