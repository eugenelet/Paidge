---
layout: page
title: "Efficient Context Compression"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.03784v4)

# Fix the Structural Bottleneck: Context Compression via Explicit Information Transmission

#### 🚀 Technical Novelty
* **Mechanism**: Treats a frozen LLM as a feature extractor and decomposes compression into two stages: a widthwise optimal-transport-based global allocation plan to distribute information across compression slots, and a depthwise weighted shortcut mechanism to aggregate features across layers.
* **Nuance**: Differs from prior SOTA by decoupling compression from the LLM's trainable self-attention mechanism, explicitly solving the "lack of allocation" and "information dilution" bottlenecks inherent in standard LLM-as-a-compressor paradigms.

#### 💡 Yield
- Consistently outperforms strong soft-compression baselines across 12 datasets, improving average F1 by up to 18.5% while adding only ~1% trainable parameters and achieving >2× faster compression latency.
- Maintains performance close to uncompressed baselines even at high compression ratios (×8, ×16) and scales effectively to larger models (Llama-3.1-8B) and longer contexts (8k).

#### ⚠️ Limitations
- Performance slightly lags on very short-context tasks (e.g., RelationExtraction with ~30 tokens) where fixed compression budgets constrain the effective ratio.
- Relies on a frozen LLM as a feature extractor, meaning it cannot dynamically adapt its internal representations during the compression phase itself.