---
layout: page
title: "Weight-Compiled Agentic Workflows"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.22502v1)

# Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost

#### 🚀 Technical Novelty
* **Mechanism**: Fine-tuning a base LLM on synthetic, flowchart-derived conversations to embed decision trees and tool-use protocols directly into parameters.
* **Nuance**: Replaces transient, prompt-heavy external orchestrators with persistent "subterranean agents," decoupling workflow complexity from context window consumption and runtime latency.

#### 💡 Yield
- 8B compiled models reach 87–98% of frontier in-context quality; cuts per-conversation costs by 128–462× and latency by 2.8×; enables 30–50 minute workflow recompilation cycles.

#### ⚠️ Limitations
- Slightly lower naturalness/graceful handling scores than frontier baselines (~82% for 3B); requires synthetic data generation via a larger model during training; workflow updates demand full recompile rather than instant prompt edits.