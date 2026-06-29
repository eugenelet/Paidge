---
layout: page
title: "Hierarchical Dynamic Prompt Compression"
parent: "Efficient Architectures"
---

# Hierarchical and Dynamic Prompt Compression for Efficient Zero-shot API Usage

#### 🚀 Technical Novelty
* **Mechanism**: Introduces "HD-Gist tokens" (Gistarg for arguments, Gistvalue for categorical values) paired with dynamic attention masking that selectively unmask value-level tokens only when needed, alongside a reconstruction loss to preserve compressed information.
* **Nuance**: Differs from prior static gist-token compression by using hierarchical granularity and dynamic zoom-in/out capabilities, avoiding the severe accuracy drop of fixed-compression methods while maintaining KV-cache efficiency without external encoders.

#### 💡 Yield
- Achieves 56.68% joint-goal accuracy on SGD (vs ~41% for static gist) and outperforms uncompressed LLaMA baseline by 4.5% on paraphrased SGD-X test set, demonstrating compression acts as a regularization bottleneck that improves out-of-domain generalization.
- Reduces inference memory by ~32.5%, compute by ~30%, and cuts average attended documentation tokens from ~109 to ~5 while maintaining comparable CUDA decoding time to static gist caching.

#### ⚠️ Limitations
- Speedup is inherently limited because Transformer FLOPs are dominated by feed-forward layers during decoding, not just attention computation with cached keys/values.
- Requires structured hierarchical formatting and ground-truth labels during training to supervise the reconstruction objective and dynamic masking scheme.
- Generalization to highly unstructured free-text compression is theoretically proposed but not empirically validated in this work.