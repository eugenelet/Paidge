---
layout: page
title: "Compact Test-Time Memory"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.12357v1)

# δ-mem: Efficient Online Memory for Large Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Compresses sequential token history into a fixed-size online associative memory state (OSAM) using delta-rule learning with dimension-wise gating, then injects low-rank query/output corrections directly into the frozen backbone's attention computation during generation.
* **Nuance**: Unlike prior methods that rely on explicit context extension, external retrieval modules, or static parametric adapters, δ-mem tightly couples a dynamically evolving matrix directly with the backbone's forward pass, enabling continuous test-time state updates without full fine-tuning or architectural replacement.

#### 💡 Yield
- Achieves 1.10× average score improvement over the frozen backbone and 1.15× over the strongest non-δ-mem baseline using only an 8×8 memory state.
- Delivers substantial gains on memory-heavy benchmarks (1.31× on MemoryAgentBench, 1.20× on LoCoMo) while largely preserving general reasoning capabilities.
- Demonstrates that effective long-term context reuse can be realized through compact online state coupling rather than scaling context windows or external storage.

#### ⚠️ Limitations
- Fixed small state dimensionality (8×8) may cap capacity for highly complex, dense, or multi-hop long-term dependencies requiring richer associative representations.
- Performance is sensitive to delta-rule learning hyperparameters (write/retention gates) and may require careful tuning across different model scales or domains.
- Evaluated primarily on text-based QA and agent benchmarks; real-world deployment overhead, state persistence across sessions, and integration with external tool-use pipelines remain unexplored.