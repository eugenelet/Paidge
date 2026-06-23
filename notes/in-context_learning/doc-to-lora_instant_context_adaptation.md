---
layout: page
title: "Doc-to-LoRA Instant Context Adaptation"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.15902v1)

# Doc-to-LoRA: Learning to Instantly Internalize Contexts

#### 🚀 Technical Novelty
* **Mechanism**: Meta-trains a Perceiver-style hypernetwork to map variable-length context activations directly into layer-wise LoRA adapter weights via a single forward pass.
* **Nuance**: Replaces iterative, per-prompt backpropagation used in traditional Context Distillation with a learned amortized mapping, enabling real-time parameter generation instead of slow fine-tuning cycles.

#### 💡 Yield
- Achieves near-perfect zero-shot accuracy on Needle-in-a-Haystack tasks for contexts exceeding the base LLM's native window by 4×.
- Significantly reduces peak memory consumption and internalization latency compared to standard Context Distillation under limited compute budgets.
- Demonstrates robust zero-shot generalization to unseen document lengths and effective cross-modal knowledge transfer (visual-to-text).

#### ⚠️ Limitations
- Performance is inherently bound to the frozen base LLM's activation quality and capacity.
- Requires extensive, diverse context-query-response datasets for hypernetwork training, risking poor generalization on highly specialized or out-of-distribution domains.
- Chunking mechanism introduces architectural complexity that may limit adapter rank scaling efficiency for extremely long sequences.