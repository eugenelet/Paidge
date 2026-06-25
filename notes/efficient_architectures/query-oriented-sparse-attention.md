---
layout: page
title: "query-oriented-sparse-attention"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.08722v1)

# QUOKA: QUERY-ORIENTED KV SELECTION FOR EFFICIENT LLM PREFILL

#### 🚀 Technical Novelty
* **Mechanism**: Training-free query-oriented KV selection using cosine dissimilarity to identify representative queries, followed by cosine similarity scoring to subselect the most relevant keys/values for chunked prefill.
* **Nuance**: Differs from prior SOTA by explicitly accounting for query geometry during multi-query prefill chunks, avoiding homogeneous averaging that degrades accuracy, and remaining fully compatible with standard dense kernels without custom hardware dependencies.

#### 💡 Yield
- Near-baseline accuracy on LongBench, RULER, Needle-in-a-Haystack, and Math500 benchmarks while using 88% fewer KV pairs.
- Up to 3× reduction in time-to-first-token (TTFT) and up to 7× attention speedup across Nvidia GPUs, Intel CPUs, and consumer hardware.
- Robust performance across diverse LLM families (Llama3, Qwen3, SmolLM, GPT-OSS) with gradual accuracy degradation under increasing sparsity.

#### ⚠️ Limitations
- Accuracy gradually degrades as sparsity budget increases (though remains stable within ~3% drop for <12% tokens used).
- Computation of the aggregated query-key matrix ($\bar{Q}K^\top$) could be further optimized; authors note potential for exploiting channel sparsity or learned projections.
- Primarily validated on decoder-only LLMs and chunked prefill settings; KV cache eviction integration is left for future work.