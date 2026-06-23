---
layout: page
title: "Compact Test-Time Memory"
parent: "Test-Time Adaptation"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2605.12357v1)

# δ-mem: Efficient Online Memory for Large Language Models

#### 🚀 Technical Novelty
* **Mechanism**: Compresses historical tokens into a fixed-size 8×8 online associative memory state updated via delta-rule learning during generation, injecting low-rank query/output corrections directly into the frozen backbone's attention.
* **Nuance**: Bypasses explicit context expansion and external retrieval by tightly coupling a dynamically evolving, test-time-updated state with attention computation, maintaining backbone parameters completely frozen while adapting to new inputs on-the-fly.

#### 💡 Yield
- Achieves 1.10× average score improvement over the frozen backbone and 1.15× over the strongest non-δ-mem baseline, with gains exceeding 1.31× on MemoryAgentBench and 1.20× on LoCoMo.
- Demonstrates that effective long-term memory can be realized through a compact online state coupled directly with attention, preserving general capabilities without full fine-tuning or architectural replacement.

#### ⚠️ Limitations
- Fixed 8×8 state capacity inherently caps the volume and complexity of retainable historical information, potentially limiting performance on ultra-long-range or highly dense dependency tasks.
- Online delta-rule updates require careful gate tuning to prevent state drift or noise accumulation across extended interaction horizons.