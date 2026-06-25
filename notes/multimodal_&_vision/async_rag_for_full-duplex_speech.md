---
layout: page
title: "Async RAG for Full-Duplex Speech"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2604.12928v3)

# Moshi RAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Trains a learned `<ret>` trigger token to dynamically invoke an asynchronous retrieval back-end during speech generation, exploiting the natural temporal gap between response onset and key informational content.
* **Nuance**: Unlike prior streaming RAG methods that rely on fixed-interval calls or pre-indexed corpora, Moshi RAG conditionally triggers retrieval only when knowledge-intensive queries are detected and guarantees completion within a strict ≤2-second window, preserving real-time interactivity while remaining backend-agnostic.

#### 💡 Yield
- Achieves factuality on QA benchmarks comparable to the best publicly released non-duplex speech language models while maintaining full-duplex conversational metrics.
- Enables plug-and-play integration of external retrieval backends (e.g., LLM-based or web search) without retraining, demonstrating strong generalization to out-of-domain mathematical reasoning tasks.

#### ⚠️ Limitations
- Relies on a separate streaming ASR module for text conversion, adding pipeline complexity and potential error propagation from transcription inaccuracies.
- Retrieval delay is hard-constrained to ≤2 seconds, which may limit the depth of queries or effectiveness with large-scale, slow-to-index corpora.
- Performance remains dependent on external retrieval backend quality and latency; not a fully self-contained reasoning architecture.