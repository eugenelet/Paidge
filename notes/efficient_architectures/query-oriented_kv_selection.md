---
layout: page
title: "Query-Oriented KV Selection"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.08722v1)

# QUOKA: QUERY-ORIENTED KV SELECTION FOR EFFICIENT LLM PREFILL

#### 🚀 Technical Novelty
* **Mechanism**: Uses cosine dissimilarity to isolate a small set of geometrically diverse representative queries, then subselects the most aligned keys/values through standard linear algebra operations during chunked prefill.
* **Nuance**: Unlike pattern-based sparse attention that demands custom hardware kernels or generation-centric query-dependent methods that degrade under multi-query prefill, QUOKA is training-free, hardware-agnostic, and explicitly models query geometry to sustain accuracy at high sparsity budgets.

#### 💡 Yield
- Maintains near-dense accuracy across LongBench, RULER, and Math500 while utilizing only ~12% of the original KV cache budget.
- Delivers up to 5× standalone attention speedup and 3× time-to-first-token (TTFT) reduction on NVIDIA GPUs, scaling to 7× on Intel CPUs.
- Demonstrates robust generalization across diverse LLM families (Llama3, Qwen3, SmolLM) and hardware architectures with minimal hyperparameter sensitivity.

#### ⚠️ Limitations
- The $\bar{Q}K^\top$ aggregation step is acknowledged as a potential computational bottleneck that could benefit from channel sparsity or learned low-dimensional projections.
- Does not integrate with KV cache eviction policies, which the authors explicitly note as a complementary direction for future work.