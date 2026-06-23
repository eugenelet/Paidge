---
layout: page
title: "Latent Reasoning via Fused Tokens"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.10229v1)

# Latent Thoughts Tuning: Bridging Context and Reasoning with Fused Information in Latent Tokens

#### 🚀 Technical Novelty
* **Mechanism**: Introduces a Context-Prediction-Fusion mechanism that constructs latent tokens by combining recurrent hidden states with probability-weighted vocabulary embeddings, trained via a progressive three-stage curriculum learning pipeline.
* **Nuance**: Unlike prior latent methods that suffer from feature collapse (Coconut) or discard context (Soft-Thinking), LT-Tuning dynamically switches between explicit CoT and latent reasoning based on prediction confidence, bridging the distribution gap between input embeddings and output hidden states without external assistants.

#### 💡 Yield
- Outperforms existing latent reasoning baselines by up to 4.3% average accuracy across mathematical benchmarks (1B-8B models).
- Successfully mitigates feature collapse in larger models with untied embeddings, demonstrating robust scaling behavior where prior methods degrade.
- Enables confidence-driven dynamic allocation of computation, reducing unnecessary inference steps on trivial problems while providing deeper reasoning for complex ones.

#### ⚠️ Limitations
- Requires a three-stage post-training curriculum pipeline, adding complexity to the fine-tuning process compared to standard prompting or simple SFT.
- Performance gains are evaluated primarily on mathematical reasoning benchmarks; generalization to other domains (e.g., code, open-ended generation) is not extensively tested.
- Relies on threshold-based confidence triggering, which may require careful hyperparameter tuning across different model scales and tasks.