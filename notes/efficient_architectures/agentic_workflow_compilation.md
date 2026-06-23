---
layout: page
title: "Agentic Workflow Compilation"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.22502v1)

# Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost

#### 🚀 Technical Novelty
* **Mechanism**: Generates synthetic conversational trajectories from directed flowchart graphs and performs full-parameter fine-tuning on small LLMs (3B/8B) to internalize routing logic, creating a "subterranean agent" that self-orchestrates at runtime without external prompts or orchestrators.
* **Nuance**: Replaces transient context-window injection and external orchestration layers with persistent weight-based procedural knowledge, enabling constant-size prompts regardless of workflow depth and eliminating per-turn instruction parsing overhead.

#### 💡 Yield
- 8B compiled models achieve 87–98% of frontier in-context quality across complex domains (travel booking, Zoom support, insurance claims)
- Reduces per-conversation inference costs by 128–462× via self-hosting and constant-size prompts, with cost advantage scaling alongside procedure complexity
- Lowers failure rates significantly (e.g., 5.5% vs. 24% in travel booking) while enabling rapid 30–50 minute recompile cycles compatible with CI/CD pipelines

#### ⚠️ Limitations
- Smaller models (3B) still trail frontier baselines on nuanced metrics like graceful handling and naturalness (~82% parity)
- Quality is tightly coupled to the fidelity and coverage of synthetic trajectory generation during training
- Requires production-grade hardware for recompilation, though cycles remain short and deployment-compatible