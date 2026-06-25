---
layout: page
title: "Kimi Linear Architecture"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2510.26692v2)

# KIMILINEAR: AN EXPRESSIVE, EFFICIENT ATTENTION ARCHITECTURE

#### 🚀 Technical Novelty
* **Mechanism**: Introduces Kimi Delta Attention (KDA), a linear attention module that replaces coarse head-wise forgetting with channel-wise gating and parameterizes transition dynamics via a specialized Diagonal-Plus-Low-Rank (DPLR) matrix, enabling hardware-efficient chunkwise parallelization.
* **Nuance**: Unlike prior hybrid or purely linear models that rely on scalar decay or standard DPLR formulations, KDA’s per-dimension forgetting rates provide finer-grained memory control while maintaining the parallelizable structure of classical delta rules, bridging the expressivity-efficiency gap without architectural overhead.

#### 💡 Yield
- Outperforms full Multi-Head Latent Attention (MLA) baselines across short-context, long-context, and RL-style post-training tasks using identical training recipes.
- Cuts KV cache footprint by up to 75% and achieves up to 6.3× faster decoding throughput at 1M context length while maintaining stable Time Per Output Token (TPOT).
- Delivers drop-in vLLM integration and open-sourced KDA kernels, enabling seamless deployment without modifying existing caching or scheduling interfaces.

#### ⚠️ Limitations
- Pure linear attention still struggles with exact copying and fine-grained retrieval in extreme long-context scenarios, necessitating hybrid interleaving rather than full replacement.
- Hybrid designs remain sensitive to RoPE base frequency adjustments, complicating context window extrapolation unless paired with NoPE-based full attention layers.
- Empirical validation is primarily focused on language modeling; broader modality robustness or specialized domain generalization remains unexplored.