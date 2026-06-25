---
layout: page
title: "Query-Only Test-Time Training"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2512.13898v1)

# Let’s (not) just put things in Context: Test-Time Training for Long-Context LLMs

#### 🚀 Technical Novelty
* **Mechanism**: Performs a single prefill to cache keys/values, then applies targeted gradient updates exclusively to attention query projection matrices during inference while reusing the KV cache.
* **Nuance**: Directly counteracts static self-attention's "score dilution" by increasing target-distractor logit margins at test time, unlike decoding-based scaling strategies that merely generate more text with fixed attention weights.

#### 💡 Yield
- Theoretically proves a logarithmic margin requirement for long contexts and shows qTTT provably meets it; empirically delivers >12% average accuracy gains on LongBench-v2/ZeroScrolls under FLOP-matched budgets, consistently outperforming chain-of-thought baselines across model sizes.

#### ⚠️ Limitations
- Gains are task-dependent (minimal for pure summarization/generation where retrieval isn't the bottleneck), evaluated only at a single compute budget point, and lacks automated predictors for when to deploy qTTT versus decoding-based scaling.