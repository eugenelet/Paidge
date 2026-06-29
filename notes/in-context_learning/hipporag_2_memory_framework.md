---
layout: page
title: "HippoRAG 2 Memory Framework"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2502.14802v2)

# From RAG to Memory: Non-Parametric Continual Learning for Large Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Combines Personalized PageRank over an automatically constructed knowledge graph with query-to-triple linking and dynamically weighted passage nodes during retrieval.
* **Nuance**: Unlike prior structure-augmented RAG methods that sacrifice factual recall for complex reasoning, it balances multi-hop associativity with baseline factual memory by optimizing reset probabilities and filtering irrelevant triples online.

#### 💡 Yield
- Achieves a 7% average improvement over standard RAG on associative tasks while maintaining factual/sense-making performance; demonstrates consistent robustness across growing corpora and varying dense retrievers.

#### ⚠️ Limitations
- Performance on complex associative tasks degrades as corpus size increases; higher computational overhead (tokens/time/memory) compared to standard dense retrieval; relies on LLM-generated KG triples that may introduce noise if the base model is weak.