---
layout: page
title: "Tandem S2S-LLM Architecture"
parent: "Efficient Architectures"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2510.02327v2)

# KAME: TANDEM ARCHITECTURE FOR ENHANCING KNOWLEDGE IN REAL-TIME SPEECH-TO-SPEECH CONVERSATIONAL AI

#### 🚀 Technical Novelty
* **Mechanism**: Asynchronous "oracle stream" that feeds evolving text responses from a back-end LLM into the front-end S2S transformer for real-time conditioning.
* **Nuance**: Bridges monolithic S2S and cascaded paradigms by decoupling inference cycles, enabling immediate low-latency responses while continuously refining output with external knowledge, unlike rigid layered or sequential systems.

#### 💡 Yield
- MT-Bench score of 6.43 (vs 2.05 for baseline S2S) with zero median latency; demonstrates back-end agnosticism allowing LLM swaps without front-end retraining.

#### ⚠️ Limitations
- Premature generation causes minor quality gaps vs cascaded systems due to incomplete initial context; relies on simulated oracle data that may not perfectly mirror live LLM behavior; performance plateaus without long-pause training examples.