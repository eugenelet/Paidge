---
layout: page
title: "Asynchronous RAG for Speech"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.12928v3)

# Moshi RAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Triggers a special `<ret>` token during autoregressive speech generation to asynchronously invoke an external knowledge retrieval system, exploiting the natural temporal gap between response onset and key informational content.
* **Nuance**: Dynamically activates back-end retrieval only when context demands it within a strict ~2-second window, avoiding the fixed-interval calls, synchronous processing bottlenecks, or heavy retraining required by prior full-duplex RAG approaches.

#### 💡 Yield
- Achieves factuality parity with top publicly released non-duplex speech LMs while preserving real-time interactivity metrics on full-duplex benchmarks.
- Enables plug-and-play integration of diverse retrieval backends (e.g., web search, LLMs) at inference time without retraining the base model.
- Demonstrates strong zero-shot generalization to out-of-domain mathematical reasoning tasks by effectively leveraging external tools for complex problem-solving.

#### ⚠️ Limitations
- Relies on a separate streaming ASR module for text transcription, introducing potential error propagation and added pipeline complexity.
- Strict ~2-second retrieval delay constraint may bottleneck highly complex queries requiring extended multi-step reasoning or slower external backends.
- Performance remains tightly coupled to the quality, latency, and availability of external knowledge sources, limiting robustness in offline or restricted-network environments.