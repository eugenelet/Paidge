---
layout: page
title: "Efficient Long Context Compression"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2305.14788v2)

# Adapting Language Models to Compress Contexts

#### 🚀 Technical Novelty
* **Mechanism**: Introduces "summary accumulation" paired with randomized segment training to recursively generate compact summary vectors that act as dynamic soft prompts for subsequent text segments.
* **Nuance**: Unlike prior compression methods that only retain the most recent summary or require per-context optimization, AutoCompressors concatenate all historical summaries and learn a unified compression policy via unsupervised language modeling objectives, avoiding expensive distillation loops.

#### 💡 Yield
- Extends effective context windows up to 30,720 tokens while preserving pre-trained capabilities on standard benchmarks.
- Compressed in-context demonstrations outperform plain-text few-shot prompting on 8/11 classification tasks with significantly lower inference costs.
- Fused summary vectors achieve superior perplexity gains and 1.7× throughput improvements over full-passage retrieval-augmented baselines like REPLUG.

#### ⚠️ Limitations
- Fine-tuning induces domain mismatch, causing zero-shot accuracy degradation on certain Llama-2 tasks compared to the base model.
- Summary vector sequence length grows linearly with document length, potentially impacting memory overhead for extremely long inputs.
- Still underperforms full-context retrieval methods in complex multi-passage reasoning scenarios where higher-fidelity compression is needed.