---
layout: page
title: "Tandem S2S-LLM Architecture"
parent: "Multimodal & Vision"
---

**🔗 Source:** [arXiv](https://arxiv.org/abs/2510.02327v2)

# KAME: TANDEM ARCHITECTURE FOR ENHANCING KNOWLEDGE IN REAL-TIME SPEECH-TO-SPEECH CONVERSATIONAL AI

#### 🚀 Technical Novelty
* **Mechanism**: Asynchronously streams partial transcripts to a back-end LLM, which feeds evolving "oracle" tokens back to a front-end S2S transformer to guide real-time speech generation.
* **Nuance**: Unlike cascaded systems that wait for full utterances or monolithic S2S models with limited knowledge capacity, KAME decouples audio and text modalities to enable immediate responses continuously refined by external reasoning without latency penalties.

#### 💡 Yield
- Achieves MT-Bench scores of 6.23–6.43 (approaching cascaded systems' ~7.70) while maintaining zero initial response latency, proving back-end LLM agnosticism and flexible knowledge infusion.

#### ⚠️ Limitations
- Premature response generation causes minor quality degradation compared to fully cascaded systems due to incomplete context at inference start, and training relies on simulated oracle augmentation that may not perfectly capture real-time LLM dynamics or natural conversational pauses.