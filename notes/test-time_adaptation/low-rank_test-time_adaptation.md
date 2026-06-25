---
layout: page
title: "Low-Rank Test-Time Adaptation"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2502.02069v1)

# LoRA-TTT: Low-Rank Test-Time Training for Vision-Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Injects trainable low-rank matrices into the deeper layers of the VLM's image encoder during inference, optimizing them via a combined marginal entropy and masked autoencoder (MAE) reconstruction loss on augmented test instances.
* **Nuance**: Shifts adaptation focus from text prompts to vision parameters, precomputes and caches text features to eliminate the text encoder at test time, and preserves base model generalization by freezing original weights while updating only low-rank deltas.

#### 💡 Yield
- Achieves state-of-the-art zero-shot classification across 15 datasets, improving CLIP-ViT-B/16 accuracy by +5.79% (OOD) and +1.36% (fine-grained) without external models or caching.
- Significantly reduces memory footprint and inference runtime compared to test-time prompt tuning (TPT), making it viable for real-time edge deployment.
- The MAE-based reconstruction loss mitigates the overconfidence problem inherent in entropy-only TTT, yielding superior Expected Calibration Error (ECE) comparable to specialized calibration methods.

#### ⚠️ Limitations
- Performance sensitivity to LoRA rank and scale hyperparameters, though stability improves with smaller ranks (e.g., rank 4).
- Marginal entropy loss alone can cause domain-specific performance drops (e.g., EuroSAT), necessitating loss combination for robust cross-domain generalization.
- Primary evaluation focuses on zero-shot image classification; broader downstream task adaptation (e.g., segmentation, detection) is not extensively validated in the provided text.