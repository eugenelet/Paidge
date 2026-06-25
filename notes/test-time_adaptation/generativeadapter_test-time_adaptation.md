---
layout: page
title: "GenerativeAdapter Test-Time Adaptation"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2411.05877v1)

# GENERATIVE ADAPTER: CONTEXTUALIZING LANGUAGE MODELS IN PARAMETERS WITH A SINGLE FORWARD PASS

#### 🚀 Technical Novelty
* **Mechanism**: A lightweight adapter generator network encodes streaming context hidden states from a frozen base LM and produces layer-wise additive delta weights in a single forward pass, which are directly added to the base model for inference.
* **Nuance**: Unlike prompting (which suffers from quadratic attention overhead with long contexts) or fine-tuning/continual pretraining (which requires expensive gradient-based updates), this method achieves on-the-fly parameter adaptation using only forward passes, decoupling context length from inference cost.

#### 💡 Yield
- Achieves a 63.5% F1 score improvement over supervised fine-tuning on StreamingQA for 32K-token contexts.
- Outperforms the base model's in-context learning capability on MetaICL (44.9% average accuracy across 26 tasks).
- Reduces computation and memory costs by 4x compared to full conversation history prompting in user personalization scenarios.

#### ⚠️ Limitations
- Evaluated primarily on 7B-scale models (Mistral-7B-Instruct, Llama2-7B-Chat), leaving scalability to larger architectures unverified.
- Adapter generation is restricted to linear projection layers (attention and FFN down/up projections) rather than full network parameter updates.
- Performance heavily depends on the self-supervised pretraining data quality of the adapter generator, potentially limiting zero-shot generalization to highly specialized domains without instruction tuning.