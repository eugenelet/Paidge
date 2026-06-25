---
layout: page
title: "AutoCompressor Long Context Compression"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2305.14788v2)

# Adapting Language Models to Compress Contexts

#### 🚀 Technical Novelty
* **Mechanism**: Recursive generation of summary vectors from segmented text, concatenated as soft prompts for subsequent segments (summary accumulation), trained via unsupervised next-token prediction on randomized segment lengths.
* **Nuance**: Unlike prompt compression methods that optimize per-context or require distillation, AutoCompressors learn a generalizable compression function during fine-tuning, enabling direct knowledge transfer across variable-length contexts and eliminating per-query optimization overhead.

#### 💡 Yield
- Fine-tuned OPT-2.7B/Llama-2-7B models handle up to 30,720 tokens; summary vectors outperform few-shot ICL on 8/11 classification tasks while reducing inference costs.
- Fused summaries in retrieval-augmented modeling achieve 1.5× perplexity gains over plain-text baselines with higher throughput and lower storage overhead.

#### ⚠️ Limitations
- Potential domain mismatch during fine-tuning can degrade zero-shot accuracy on specific tasks.
- Summary vector length grows linearly with document length, potentially impacting memory at extreme scales.
- Performance still lags behind full-context retrieval methods (e.g., REPLUG top-10) in certain settings, indicating room for higher-fidelity compression.