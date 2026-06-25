---
layout: page
title: "Instant Context Internalization"
parent: "In-Context Learning"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2602.15902v1)

# Doc-to-LoRA: Learning to Instantly Internalize Contexts

#### 🚀 Technical Novelty
* **Mechanism**: Meta-trains a Perceiver-based hypernetwork to map variable-length context activations directly to layer-wise LoRA adapter weights via a single forward pass.
* **Nuance**: Replaces the slow, iterative backpropagation of traditional Context Distillation with one-shot inference, eliminating KV-cache bloat and enabling per-prompt adaptation without retraining.

#### 💡 Yield
- Achieves near-perfect zero-shot accuracy on Needle-in-a-Haystack tasks for contexts exceeding the base LLM's native window by 4×.
- Outperforms standard Context Distillation under limited compute budgets while drastically cutting internalization latency and peak memory usage.
- Demonstrates zero-shot generalization to unseen document lengths and effective cross-modal transfer (visual information to text-only LLMs).

#### ⚠️ Limitations
- Requires access to the frozen target LLM's internal activations during hypernetwork training, limiting deployment flexibility for closed-source or black-box models.
- Relies on synthetic query generation pipelines that may not fully cover domain-specific edge cases or highly specialized knowledge distributions.
- Performance may degrade on highly complex reasoning tasks where simple parameter internalization cannot capture nuanced contextual dependencies or multi-step logic.