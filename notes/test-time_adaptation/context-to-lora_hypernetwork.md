---
layout: page
title: "Context-to-LoRA Hypernetwork"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.06358v1)

# SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass

#### 🚀 Technical Novelty
* **Mechanism**: Extracts multi-layer memory states from the backbone LLM and processes them through a lightweight, bidirectional M2P Transformer to generate full-rank LoRA adapters in one pass.
* **Nuance**: Eliminates the restrictive MLP bottlenecks and subset-layer generation of prior hypernetworks by leveraging global self-attention across all layers, fully exploiting the LLM’s pre-trained inductive bias for coherent weight coordination.

#### 💡 Yield
- Achieves performance parity with In-Context Learning and surpasses SFT baselines on multi-hop QA tasks while reducing amortizable generation time to ~0.3s.
- Demonstrates consistent scaling across backbone LLM sizes and hypernetwork parameters without capacity saturation, trained on 6B tokens.

#### ⚠️ Limitations
- Performance degrades on multi-turn conversations as the original context is discarded after adapter generation, limiting long-context reasoning during extended interactions.
- Requires extensive pretraining (6B tokens) and curated instruction-tuning data, posing high upfront computational costs for deployment.