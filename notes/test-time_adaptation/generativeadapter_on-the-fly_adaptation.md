---
layout: page
title: "GenerativeAdapter On-The-Fly Adaptation"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2411.05877v1)

# GENERATIVE ADAPTER: CONTEXTUALIZING LANGUAGE MODELS IN PARAMETERS WITH A SINGLE FORWARD PASS

#### 🚀 Technical Novelty
* **Mechanism**: Trains a lightweight adapter generator network that projects accumulated context hidden states into layer-wise additive delta weights for a frozen base LM using only forward passes.
* **Nuance**: Bypasses gradient-based fine-tuning and the KV-cache scaling of standard prompting by dynamically updating model parameters on-the-fly with constant inference cost regardless of input length.

#### 💡 Yield
- Achieves 63.5% F1 improvement over supervised fine-tuning on StreamingQA for 32K-token contexts.
- Outperforms base model accuracy on MetaICL in-context learning across 26 diverse tasks.
- Cuts computation and memory costs by 4x compared to full conversation prompting for user personalization.
- Maintains high fact recall on long documents while avoiding the storage overhead of KV caches.

#### ⚠️ Limitations
- Requires extensive self-supervised pretraining of the adapter generator before it can be deployed.
- Performance may degrade on highly dynamic or out-of-distribution streaming contexts not captured during generator training.
- Restricted to updating only linear projection layers, leaving other LM components (e.g., normalization, embeddings) unadapted.