---
layout: page
title: Reading List
permalink: /reading-list/
---

# 📚 Centralized Reading List & Field Advancements

Select a research vector below to isolate the literature and view its trend.

<div class="topic-filter-container" style="display: flex; gap: 8px; flex-wrap: wrap; margin: 1.5rem 0 2rem 0;">
<button class="topic-pill active" onclick="filterTopic('all', this)">🌟 All Advancements</button>
<button class="topic-pill" onclick="filterTopic('test-time_adaptation', this)">🔄 Test-Time Adaptation</button>
<button class="topic-pill" onclick="filterTopic('in-context_learning', this)">🧠 In-Context Learning</button>
<button class="topic-pill" onclick="filterTopic('efficient_architectures', this)">⚡ Efficient Architectures</button>
<button class="topic-pill" onclick="filterTopic('multimodal_&_vision', this)">👁️ Multimodal & Vision</button>
<button class="topic-pill" onclick="filterTopic('embodied_ai_&_robotics', this)">🤖 Embodied AI & Robotics</button>
<button class="topic-pill" onclick="filterTopic('theory_&_optimization', this)">📐 Theory & Optimization</button>
</div>

<style>
  .topic-pill { padding: 6px 14px; background: #f8fafc; border: 1px solid #cbd5e1; color: #475569; border-radius: 20px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.2s; }
  .topic-pill.active { background: #3253DC; color: white; border-color: #6382f2; box-shadow: 0 0 8px rgba(50, 83, 220, 0.4); }
  .topic-pill:hover:not(.active) { background: #e2e8f0; color: #0f172a; }
  
  .timeline-container { border-left: 2px solid #3253DC; margin-left: 12px; padding-left: 24px; position: relative; margin-top: 2rem; margin-bottom: 3rem; }
  .timeline-item { position: relative; margin-bottom: 2.5rem; }
  .timeline-node { position: absolute; left: -30px; top: 6px; width: 10px; height: 10px; background: #3253DC; border-radius: 50%; box-shadow: 0 0 8px rgba(99, 130, 242, 0.4); border: 2px solid #ffffff; z-index: 10;}
  .timeline-date { background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-size: 0.8rem; letter-spacing: 0.5px; }
  .paper-link { color: #0f172a; font-weight: 700; font-size: 1.05rem; text-decoration: none; transition: color 0.2s; }
  .paper-link:hover { color: #3253DC; }
  .full-title-sub { font-size: 0.8rem; color: #64748b; font-style: italic; margin-top: 4px; margin-bottom: 4px; padding-left: 2px; }
  .takeaway-text { color: #334155; font-size: 0.95rem; line-height: 1.5; margin-top: 8px; }
  
  /* Citation Badge for Light Theme */
  .citation-badge { display: inline-block; font-size: 0.7rem; font-family: monospace; background: #eff6ff; color: #3253DC; border: 1px solid #bfdbfe; padding: 2px 6px; border-radius: 4px; text-decoration: none; vertical-align: middle; margin: 0 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); transition: all 0.2s; position: relative; top: -1px;}
  .citation-badge:hover { background: #3253DC; color: #ffffff; box-shadow: 0 0 6px rgba(50, 83, 220, 0.4); }
</style>

<script>
  function filterTopic(slug, btnEl) {
    document.querySelectorAll('.topic-pill').forEach(b => b.classList.remove('active'));
    btnEl.classList.add('active');
    document.querySelectorAll('.topic-section-group').forEach(group => {
      group.style.display = (slug === 'all' || group.getAttribute('data-topic') === slug) ? 'block' : 'none';
    });
  }
</script>

<div class="topic-section-group" data-topic="test-time_adaptation" markdown="1">

## 🔄 Test-Time Adaptation

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0; color: #e2e8f0; font-size: 0.95rem; line-height: 1.6;" markdown="1">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 1.1rem;">🧭</span>
<strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
</div>

The field is converging on a paradigm shift from static prompting to dynamic, inference-time parameterization where frozen weights are continuously compressed into low-rank fast weights, hypernetwork-generated adapters, and latent state matrices via unsupervised gradient optimization <a href="/notes/test-time_adaptation/in-place_test-time_training.html" class="citation-badge">In-Place Test-Time Training</a> <a href="/notes/test-time_adaptation/context-to-lora_hypernetwork.html" class="citation-badge">Context-to-LoRA Hypernetwork</a> <a href="/notes/test-time_adaptation/latent_thought_models.html" class="citation-badge">Latent Thought Models</a> <a href="/notes/test-time_adaptation/compact_test-time_memory.html" class="citation-badge">Compact Test-Time Memory</a> <a href="/notes/test-time_adaptation/generativeadapter_test-time_adaptation.html" class="citation-badge">GenerativeAdapter Test-Time Adaptation</a> <a href="/notes/test-time_adaptation/end-to-end_test-time_training.html" class="citation-badge">End-to-End Test-Time Training</a>. This mathematical trajectory directly circumvents the quadratic context-scaling bottleneck of standard attention by routing inference compute toward lightweight, per-step weight updates and dynamic memory allocation, enabling constant-latency long-context modeling and self-directed adaptation without architectural modification or iterative fine-tuning <a href="/notes/test-time_adaptation/large_chunk_test-time_training.html" class="citation-badge">Large Chunk Test-Time Training</a> <a href="/notes/test-time_adaptation/titans_test-time_memory.html" class="citation-badge">Titans Test-Time Memory</a> <a href="/notes/test-time_adaptation/dynamic_layer-wise_tta.html" class="citation-badge">Dynamic Layer-Wise TTA</a> <a href="/notes/test-time_adaptation/test-time_llm_adaptation.html" class="citation-badge">Test-Time LLM Adaptation</a> <a href="/notes/test-time_adaptation/self-adapting_llm_framework.html" class="citation-badge">Self-Adapting LLM Framework</a>.

</div>

<div class="timeline-container">
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/test-time_adaptation/compact_test-time_memory.html" class="paper-link">Compact Test-Time Memory</a>
</div>
<div class="full-title-sub">δ-mem: Efficient Online Memory for Large Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> δ-mem enables frozen LLMs to dynamically accumulate and reuse long-term context via a compact 8×8 state matrix updated at test-time, bypassing costly context expansion.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/test-time_adaptation/fast-slow_llm_training.html" class="paper-link">Fast-Slow LLM Training</a>
</div>
<div class="full-title-sub">Learning, Fast and Slow: Towards LLMs That Adapt Continually</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Interleaving prompt optimization with reinforcement learning enables rapid task adaptation while preserving model plasticity and preventing catastrophic forgetting.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/test-time_adaptation/training-free_looped_transformers.html" class="paper-link">Training-Free Looped Transformers</a>
</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Retrofitting frozen LLMs with inference-time layer looping and numerical integration yields consistent accuracy gains without training or architectural changes.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-04</span>
<a href="/notes/test-time_adaptation/in-place_test-time_training.html" class="paper-link">In-Place Test-Time Training</a>
</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Repurposes standard MLP projection matrices as dynamic fast weights to enable scalable, drop-in test-time adaptation for LLMs without costly retraining.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/test-time_adaptation/dynamic_layer-wise_tta.html" class="paper-link">Dynamic Layer-Wise TTA</a>
</div>
<div class="full-title-sub">Unsupervised Layer-Wise Dynamic Test Time Adaptation for LLMs</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A lightweight hypernetwork dynamically predicts per-layer, per-step learning rate multipliers to stabilize unsupervised inference-time parameter updates in LLMs.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/test-time_adaptation/context-to-lora_hypernetwork.html" class="paper-link">Context-to-LoRA Hypernetwork</a>
</div>
<div class="full-title-sub">SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Instantly converts diverse text contexts into high-quality LoRA adapters via a single-pass hypernetwork, bypassing iterative fine-tuning and long-context latency.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-12</span>
<a href="/notes/test-time_adaptation/query-only_test-time_training.html" class="paper-link">Query-Only Test-Time Training</a>
</div>
<div class="full-title-sub">Let’s (not) just put things in Context: Test-Time Training for Long-Context LLMs</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Redirecting inference compute from generating thinking tokens to lightweight query-gradient updates dramatically improves long-context retrieval and reasoning.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-12</span>
<a href="/notes/test-time_adaptation/end-to-end_test-time_training.html" class="paper-link">End-to-End Test-Time Training</a>
</div>
<div class="full-title-sub">End-to-End Test-Time Training for Long Context</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Compressing long contexts into model weights via test-time gradient updates and meta-initialized initialization enables constant-latency scaling that rivals full-attention Transformers.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-12</span>
<a href="/notes/test-time_adaptation/metatpt_adaptive_prompt_tuning.html" class="paper-link">MetaTPT Adaptive Prompt Tuning</a>
</div>
<div class="full-title-sub">MetaTPT: Meta Test-time Prompt Tuning for Vision-Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Dynamically learns sample-specific augmentations via dual-loop meta-optimization to robustly adapt vision-language models to unseen domains during inference.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-12</span>
<a href="/notes/test-time_adaptation/rl-conductor_agent_orchestration.html" class="paper-link">RL-Conductor Agent Orchestration</a>
</div>
<div class="full-title-sub">Learning to Orchestrate Agents in Natural Language with the Conductor</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A 7B RL-trained model dynamically orchestrates and scales worker LLMs at inference time, achieving state-of-the-art reasoning performance through adaptive test-time coordination.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-06</span>
<a href="/notes/test-time_adaptation/self-adapting_llm_framework.html" class="paper-link">Self-Adapting LLM Framework</a>
</div>
<div class="full-title-sub">Self-Adapting Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> SEAL trains LLMs via reinforcement learning to autonomously generate synthetic data and optimization directives, enabling persistent, self-directed weight updates for novel tasks without external supervision.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-06</span>
<a href="/notes/test-time_adaptation/text-to-lora_instant_adaptation.html" class="paper-link">Text-to-LoRA Instant Adaptation</a>
</div>
<div class="full-title-sub">Text-to-LoRA: Instant Transformer Adaption</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A hypernetwork generates task-specific LoRA adapters on-the-fly from natural language prompts, enabling zero-shot model adaptation without retraining.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-05</span>
<a href="/notes/test-time_adaptation/large_chunk_test-time_training.html" class="paper-link">Large Chunk Test-Time Training</a>
</div>
<div class="full-title-sub">Test-Time Training Done Right</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> LaCT scales fast-weight updates to millions of tokens, boosting GPU utilization by orders of magnitude and enabling scalable long-context modeling across diverse modalities.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-05</span>
<a href="/notes/test-time_adaptation/test-time_llm_adaptation.html" class="paper-link">Test-Time LLM Adaptation</a>
</div>
<div class="full-title-sub">Test-Time Learning for Large Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Minimizing input perplexity on unlabeled test data via LoRA and high-perplexity sampling enables efficient, label-free adaptation of LLMs to new domains.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-02</span>
<a href="/notes/test-time_adaptation/latent_thought_models.html" class="paper-link">Latent Thought Models</a>
</div>
<div class="full-title-sub">Latent Thought Models with Variational Bayes Inference-Time Computation</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> LTMs leverage inference-time optimization of explicit latent thought vectors to achieve superior sample efficiency and emergent reasoning with drastically fewer parameters than standard LLMs.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-02</span>
<a href="/notes/test-time_adaptation/low-rank_test-time_adaptation.html" class="paper-link">Low-Rank Test-Time Adaptation</a>
</div>
<div class="full-title-sub">LoRA-TTT: Low-Rank Test-Time Training for Vision-Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Replaces computationally heavy test-time prompt tuning with lightweight low-rank image encoder updates, enabling fast, memory-efficient domain adaptation for vision-language models.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-01</span>
<a href="/notes/test-time_adaptation/titans_test-time_memory.html" class="paper-link">Titans Test-Time Memory</a>
</div>
<div class="full-title-sub">Titans: Learning to Memorize at Test Time</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A novel architecture that dynamically memorizes surprising context at inference time, enabling efficient scaling beyond 2M tokens while outperforming Transformers and linear RNNs.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-11</span>
<a href="/notes/test-time_adaptation/generativeadapter_test-time_adaptation.html" class="paper-link">GenerativeAdapter Test-Time Adaptation</a>
</div>
<div class="full-title-sub">GENERATIVE ADAPTER: CONTEXTUALIZING LANGUAGE MODELS IN PARAMETERS WITH A SINGLE FORWARD PASS</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Dynamically converts streaming text contexts into low-rank parameter updates via a single forward pass, enabling efficient test-time adaptation without fine-tuning or inference overhead.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-11</span>
<a href="/notes/test-time_adaptation/test-time_training_for_llms.html" class="paper-link">Test-Time Training for LLMs</a>
</div>
<div class="full-title-sub">The Surprising Effectiveness of Test-Time Training for Few-Shot Learning</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Dynamically updating model weights during inference using few-shot examples drastically improves reasoning and generalization on novel tasks compared to static prompting.

</div>
</div>
</div>

</div>

<div class="topic-section-group" data-topic="in-context_learning" markdown="1">

## 🧠 In-Context Learning

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0; color: #e2e8f0; font-size: 0.95rem; line-height: 1.6;" markdown="1">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 1.1rem;">🧭</span>
<strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
</div>

The field is undergoing a fundamental paradigm shift from static prompt composition to treating in-context demonstrations as dynamic computational substrates that execute token-dependent rank-1 implicit weight updates on MLP layers <a href="/notes/in-context_learning/context-to-weight_equivalence.html" class="citation-badge">Context-to-Weight Equivalence</a> <a href="/notes/in-context_learning/implicit_dynamics_of_icl.html" class="citation-badge">Implicit Dynamics of ICL</a>. This mathematical unification with gradient descent establishes a collective trajectory toward optimizing demonstration retrieval via reinforcement learning <a href="/notes/in-context_learning/active_example_selection.html" class="citation-badge">Active Example Selection</a> <a href="/notes/in-context_learning/rl-based_sequential_icl_retrieval.html" class="citation-badge">RL-Based Sequential ICL Retrieval</a>, compressing long contexts through meta-learned hypernetworks <a href="/notes/in-context_learning/instant_context_internalization.html" class="citation-badge">Instant Context Internalization</a>, and aligning cross-modal representations to bypass the computational bottlenecks of raw sequence scaling.

</div>

<div class="timeline-container">
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-03</span>
<a href="/notes/in-context_learning/visual_icl_demo_selection.html" class="paper-link">Visual ICL Demo Selection</a>
</div>
<div class="full-title-sub">Learning to Select Visual In-Context Demonstrations</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Reframes demonstration selection as a reinforcement learning problem to dynamically balance visual relevance and diversity, outperforming kNN on objective visual regression tasks.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/in-context_learning/instant_context_internalization.html" class="paper-link">Instant Context Internalization</a>
</div>
<div class="full-title-sub">Doc-to-LoRA: Learning to Instantly Internalize Contexts</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A meta-learned hypernetwork instantly converts long document contexts into lightweight LoRA adapters, enabling fast, memory-efficient in-context learning without iterative fine-tuning.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-12</span>
<a href="/notes/in-context_learning/recursive_long_context_scaling.html" class="paper-link">Recursive Long Context Scaling</a>
</div>
<div class="full-title-sub">RECURSIVE LANGUAGE MODELS</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A model-agnostic inference strategy that treats prompts as an external environment, enabling LLMs to recursively decompose and process arbitrarily long contexts without architectural changes or context rot.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-11</span>
<a href="/notes/in-context_learning/context-to-weight_equivalence.html" class="paper-link">Context-to-Weight Equivalence</a>
</div>
<div class="full-title-sub">Equivalence of Context and Parameter Updates in Modern Transformer Blocks</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Proves that the computational effect of context in modern LLMs can be perfectly mapped to token-dependent rank-1 patches on MLP weights and normalization layers.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-07</span>
<a href="/notes/in-context_learning/context_tuning_for_llms.html" class="paper-link">Context Tuning for LLMs</a>
</div>
<div class="full-title-sub">Context Tuning for In-Context Optimization</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Gradient-optimized context initialization from few-shot examples significantly boosts LLM few-shot performance without parameter updates.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-07</span>
<a href="/notes/in-context_learning/implicit_dynamics_of_icl.html" class="paper-link">Implicit Dynamics of ICL</a>
</div>
<div class="full-title-sub">Learning without training: The implicit dynamics of in-context learning</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Mathematically proves that transformer prompts act as exact rank-1 implicit weight updates to MLP layers, unifying in-context learning with gradient descent dynamics.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-03</span>
<a href="/notes/in-context_learning/task-aware_icd_configuration.html" class="paper-link">Task-Aware ICD Configuration</a>
</div>
<div class="full-title-sub">ADVANCING MULTIMODAL IN-CONTEXT LEARNING IN LARGE VISION-LANGUAGE MODELS WITH TASK-AWARE DEMONSTRATIONS</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A lightweight transformer with task-aware attention dynamically optimizes in-context demonstration sequences to significantly boost multimodal ICL performance.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-10</span>
<a href="/notes/in-context_learning/continuous_vector_in-context_learning.html" class="paper-link">Continuous Vector In-Context Learning</a>
</div>
<div class="full-title-sub">VECTOR-ICL: IN-CONTEXT LEARNING WITH CONTINUOUS VECTOR REPRESENTATIONS</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> LLMs can effectively perform in-context learning on diverse continuous data modalities by aligning them to their embedding space via lightweight projectors.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-04</span>
<a href="/notes/in-context_learning/many-shot_in-context_learning.html" class="paper-link">Many-Shot In-Context Learning</a>
</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Scaling in-context examples to hundreds or thousands dramatically boosts LLM reasoning and generation, often matching fine-tuning while bypassing the need for human-labeled rationales.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-02</span>
<a href="/notes/in-context_learning/visual_in-context_learning.html" class="paper-link">Visual In-Context Learning</a>
</div>
<div class="full-title-sub">Visual In-Context Learning for Large Vision-Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Replaces visual demonstrations with intent-oriented text summaries to bridge cross-modal gaps and significantly boost ICL in large vision-language models.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2023-05</span>
<a href="/notes/in-context_learning/rl-based_sequential_icl_retrieval.html" class="paper-link">RL-Based Sequential ICL Retrieval</a>
</div>
<div class="full-title-sub">RetICL: Sequential Retrieval of In-Context Examples with Reinforcement Learning</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> RetICL leverages reinforcement learning to sequentially retrieve and order in-context examples, dynamically optimizing prompt composition for superior LLM reasoning.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2022-11</span>
<a href="/notes/in-context_learning/active_example_selection.html" class="paper-link">Active Example Selection</a>
</div>
<div class="full-title-sub">Active Example Selection for In-Context Learning</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Reinforcement learning optimizes demonstration example selection to stabilize and boost in-context learning performance, particularly for smaller language models.

</div>
</div>
</div>

</div>

<div class="topic-section-group" data-topic="efficient_architectures" markdown="1">

## ⚡ Efficient Architectures

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0; color: #e2e8f0; font-size: 0.95rem; line-height: 1.6;" markdown="1">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 1.1rem;">🧭</span>
<strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
</div>

The field is rapidly abandoning dense autoregressive decoding in favor of linear functional state-spaces and sparse adaptive routing to bypass the quadratic attention scaling and KV-cache I/O bottlenecks that constrain long-context and agentic inference. This transition is mathematically realized through constrained manifold projections <a href="/notes/efficient_architectures/manifold-constrained_hyper-connections.html" class="citation-badge">Manifold-Constrained Hyper-Connections</a>, regression-aligned cache compression <a href="/notes/efficient_architectures/global_regression_kv_cache.html" class="citation-badge">Global Regression KV Cache</a> <a href="/notes/efficient_architectures/caote_token_eviction.html" class="citation-badge">CAOTE Token Eviction</a>, and continuous latent feedback loops <a href="/notes/efficient_architectures/continuous_latent_reasoning.html" class="citation-badge">Continuous Latent Reasoning</a> <a href="/notes/efficient_architectures/calm_next-vector_language_models.html" class="citation-badge">CALM: Next-Vector Language Models</a> that decouple parameter count from compute depth while preserving representational fidelity.

</div>

<div class="timeline-container">
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/efficient_architectures/functional_attention_architecture.html" class="paper-link">Functional Attention Architecture</a>
</div>
<div class="full-title-sub">Functional Attention: From Pairwise Affinities to Functional Correspondences</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Replaces quadratic token-wise attention with linear functional operators to enable resolution-invariant, geometry-aware operator learning.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/efficient_architectures/self-regulated_simulative_planning.html" class="paper-link">Self-Regulated Simulative Planning</a>
</div>
<div class="full-title-sub">Efficient Agentic Reasoning Through Self-Regulated Simulative Planning</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Decomposing agentic reasoning into a dynamically gated configurator and simulative planner slashes token consumption by up to 95% while matching trillion-parameter model accuracy.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/efficient_architectures/modular_memory_integration.html" class="paper-link">Modular Memory Integration</a>
</div>
<div class="full-title-sub">MEMO: Memory as a Model</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> MEMO replaces brittle retrieval with a plug-and-play modular memory model, enabling efficient, noise-robust knowledge integration without retraining or modifying the base LLM.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/efficient_architectures/global_regression_kv_cache.html" class="paper-link">Global Regression KV Cache</a>
</div>
<div class="full-title-sub">GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> GRKV eliminates over-merging in long-context LLMs by using training-free global ridge regression to align compressed and full KV caches, boosting performance with minimal memory overhead.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/efficient_architectures/weight-compiled_agentic_workflows.html" class="paper-link">Weight-Compiled Agentic Workflows</a>
</div>
<div class="full-title-sub">Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Internalizing agentic routing logic directly into small model weights delivers near-frontier procedural quality at two orders of magnitude lower inference cost than external orchestration.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-04</span>
<a href="/notes/efficient_architectures/curvature-aware_sequence_modeling.html" class="paper-link">Curvature-Aware Sequence Modeling</a>
</div>
<div class="full-title-sub">Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Diagonal preconditioning of linear recurrences captures second-order optimization curvature, enabling efficient chunkwise parallel architectures that consistently improve long-context retrieval and language modeling.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-04</span>
<a href="/notes/efficient_architectures/stable_looped_language_models.html" class="paper-link">Stable Looped Language Models</a>
</div>
<div class="full-title-sub">Parcae: Scaling Laws For Stable Looped Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Parcae stabilizes looped transformers via spectral norm constraints, enabling predictable training and test-time compute scaling that matches larger Transformer baselines.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-04</span>
<a href="/notes/efficient_architectures/latent_condensed_attention.html" class="paper-link">Latent Condensed Attention</a>
</div>
<div class="full-title-sub">Latent-Condensed Transformer for Efficient Long Context Modeling</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> LCA natively condenses compressed latent representations to slash KV cache and compute by up to 90% without adding parameters or sacrificing accuracy.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-04</span>
<a href="/notes/efficient_architectures/elastic_looped_transformers.html" class="paper-link">Elastic Looped Transformers</a>
</div>
<div class="full-title-sub">ELT: Elastic Looped Transformers for Visual Generation</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> ELT decouples parameter count from compute depth via recurrent weight-sharing and intra-loop distillation, enabling any-time visual generation with a 4× efficiency gain.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-03</span>
<a href="/notes/efficient_architectures/inference_layer_skipping.html" class="paper-link">Inference Layer Skipping</a>
</div>
<div class="full-title-sub">Skip the Good Part: Representation Structure & Inference-Time Layer Skipping in Diffusion vs. Autoregressive LLMs</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Native diffusion LLMs exhibit hierarchical representational redundancy that enables aggressive, static inference-time layer skipping for significant FLOPs reduction without performance degradation.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-03</span>
<a href="/notes/efficient_architectures/sparse_efficient_llm_kernels.html" class="paper-link">Sparse Efficient LLM Kernels</a>
</div>
<div class="full-title-sub">Sparser, Faster, Lighter Transformer Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Novel CUDA kernels and sparse packing formats unlock >99% unstructured sparsity in LLMs, yielding major throughput and memory gains with minimal accuracy trade-offs.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-03</span>
<a href="/notes/efficient_architectures/future-aware_speculative_drafting.html" class="paper-link">Future-Aware Speculative Drafting</a>
</div>
<div class="full-title-sub">ConFu: Contemplate the Future for Better Speculative Sampling</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> ConFu accelerates LLM inference by equipping draft models with dynamic, future-oriented contemplate tokens that mitigate error accumulation and boost token acceptance rates over SOTA baselines.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/efficient_architectures/predictive_ffn_sparsity.html" class="paper-link">Predictive FFN Sparsity</a>
</div>
<div class="full-title-sub">FASTFORWARD: ACCELERATING LLM PREFILL WITH PREDICTIVE FFN SPARSITY</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> FastForward slashes prefill latency via block-wise predictive FFN sparsity and error compensation, delivering up to 1.45× speedup with minimal accuracy loss on constrained hardware.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/efficient_architectures/dualpath_kv_cache_optimization.html" class="paper-link">DualPath KV Cache Optimization</a>
</div>
<div class="full-title-sub">DualPath: Breaking the Storage Bandwidth Bottleneck in Agentic LLM Inference</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> DualPath eliminates KV-cache I/O bottlenecks in agentic LLM inference by dynamically routing cache loads across prefill and decode engines, boosting throughput nearly 2×.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/efficient_architectures/one-step_generative_drifting.html" class="paper-link">One-Step Generative Drifting</a>
</div>
<div class="full-title-sub">Generative Modeling via Drifting</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A novel training-time distribution evolution framework that enables high-quality, single-step image generation without iterative inference or distillation.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/efficient_architectures/latent_thoughts_tuning.html" class="paper-link">Latent Thoughts Tuning</a>
</div>
<div class="full-title-sub">Latent Thoughts Tuning: Bridging Context and Reasoning with Fused Information in Latent Tokens</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Introduces a confidence-driven latent reasoning framework that fuses contextual hidden states with predictive vocabulary embeddings to eliminate feature collapse and reduce inference latency in LLMs.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/efficient_architectures/interleaved_head_attention.html" class="paper-link">Interleaved Head Attention</a>
</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> IHA overcomes multi-head attention's linear scaling bottleneck by enabling cross-head mixing via pseudo-projections, drastically improving parameter efficiency and multi-step reasoning performance.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/efficient_architectures/hierarchical_sparse_attention.html" class="paper-link">Hierarchical Sparse Attention</a>
</div>
<div class="full-title-sub">Double-P: Hierarchical Top-P Sparse Attention for Long-Context LLMs</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Adaptive hierarchical top-p sparse attention eliminates fixed-budget constraints to deliver near-zero accuracy loss with up to 2.23× decoding speedup for long-context LLMs.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/efficient_architectures/progressive_thought_encoding.html" class="paper-link">Progressive Thought Encoding</a>
</div>
<div class="full-title-sub">Training Large Reasoning Models Efficiently via Progressive Thought Encoding</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Compressing evicted KV cache tokens into LoRA adapters enables memory-efficient RL training and long-context reasoning under strict hardware constraints.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/efficient_architectures/query-oriented-sparse-attention.html" class="paper-link">query-oriented-sparse-attention</a>
</div>
<div class="full-title-sub">QUOKA: QUERY-ORIENTED KV SELECTION FOR EFFICIENT LLM PREFILL</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> QUOKA accelerates LLM prefill latency by up to 7× through a training-free, hardware-agnostic sparse attention mechanism that dynamically selects representative queries and aligned KV pairs.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/efficient_architectures/memory_caching_for_rnns.html" class="paper-link">Memory Caching for RNNs</a>
</div>
<div class="full-title-sub">MEMORYCACHING: RNNS WITH GROWING MEMORY</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Caching intermediate RNN memory states enables linear-complexity models to scale context length without quadratic overhead.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-12</span>
<a href="/notes/efficient_architectures/manifold-constrained_hyper-connections.html" class="paper-link">Manifold-Constrained Hyper-Connections</a>
</div>
<div class="full-title-sub">mHC: Manifold-Constrained Hyper-Connections</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Projects unconstrained hyper-connections onto a constrained manifold to restore identity mapping, enabling stable and efficient large-scale LLM training.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-10</span>
<a href="/notes/efficient_architectures/kimi_linear_architecture.html" class="paper-link">Kimi Linear Architecture</a>
</div>
<div class="full-title-sub">KIMILINEAR: AN EXPRESSIVE, EFFICIENT ATTENTION ARCHITECTURE</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A hybrid linear attention design that slashes KV cache by 75% and boosts decoding speed up to 6× while surpassing full-attention baselines.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-10</span>
<a href="/notes/efficient_architectures/calm_next-vector_language_models.html" class="paper-link">CALM: Next-Vector Language Models</a>
</div>
<div class="full-title-sub">CONTINUOUS AUTOREGRESSIVE LANGUAGE MODELS</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> CALM replaces discrete token prediction with continuous vector generation, cutting autoregressive steps by K and significantly improving the performance-compute trade-off for LLMs.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-10</span>
<a href="/notes/efficient_architectures/looped_language_models.html" class="paper-link">Looped Language Models</a>
</div>
<div class="full-title-sub">Scaling Latent Reasoning via Looped Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> LoopLM replaces explicit chain-of-thought with iterative latent computation and adaptive early-exit gating, delivering 2–3× parameter efficiency at frontier scale.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-09</span>
<a href="/notes/efficient_architectures/accelerating_diffusion_llm_inference.html" class="paper-link">Accelerating Diffusion LLM Inference</a>
</div>
<div class="full-title-sub">Spiffy: Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Spiffy introduces lossless speculative decoding with directed draft graphs to accelerate diffusion LLM inference by up to 7.9× without training auxiliary models.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-09</span>
<a href="/notes/efficient_architectures/nested_subspace_networks.html" class="paper-link">Nested Subspace Networks</a>
</div>
<div class="full-title-sub">Deep Hierarchical Learning with Nested Subspace Networks for Large Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> NSNs enable post-hoc, continuous compute-performance trade-offs in pre-trained LLMs via nested low-rank factorization without retraining.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-06</span>
<a href="/notes/efficient_architectures/vocabtrim_vocabulary_pruning.html" class="paper-link">VocabTrim Vocabulary Pruning</a>
</div>
<div class="full-title-sub">VOCABTRIM: Vocabulary Pruning for Efficient Speculative Decoding in LLMs</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Pruning the drafter's language modeling head to frequent tokens eliminates memory-bound drafting overhead, boosting speculative decoding speed without training.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-06</span>
<a href="/notes/efficient_architectures/fisher-guided_sparse_lora.html" class="paper-link">Fisher-Guided Sparse LoRA</a>
</div>
<div class="full-title-sub">FLoE: Fisher-Based Layer Selection for Efficient Sparse Adaptation of Low-Rank Experts</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> FLoE slashes PEFT memory and compute by using Fisher information to sparsely activate only critical transformer layers for MoE-based LoRA adaptation.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-06</span>
<a href="/notes/efficient_architectures/block-wise_diffusion_training.html" class="paper-link">Block-Wise Diffusion Training</a>
</div>
<div class="full-title-sub">DIFFUSIONBLOCKS: BLOCK-WISE NEURAL NETWORK TRAINING VIA DIFFUSION INTERPRETATION</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Transforms residual networks into independently trainable blocks via diffusion theory, slashing training memory by a factor of B while matching end-to-end performance.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-04</span>
<a href="/notes/efficient_architectures/key_similarity_kv_cache_eviction.html" class="paper-link">Key Similarity KV Cache Eviction</a>
</div>
<div class="full-title-sub">KEYDIFF: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> KEYDIFF enables memory-constrained long-context LLM inference by evicting KV cache tokens based on key diversity rather than attention scores, cutting latency up to 30% with near-baseline accuracy.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-04</span>
<a href="/notes/efficient_architectures/key_similarity_kv_cache_eviction.html" class="paper-link">Key Similarity KV Cache Eviction</a>
</div>
<div class="full-title-sub">KEYDIFF: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> KEYDIFF enables memory-constrained long-context LLM inference by evicting KV cache entries based on key diversity rather than attention scores, cutting latency up to 30% with negligible accuracy loss.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-04</span>
<a href="/notes/efficient_architectures/caote_token_eviction.html" class="paper-link">CAOTE Token Eviction</a>
</div>
<div class="full-title-sub">CAOTE: KV Cache Selection for LLMs via Attention Output Error-Based Token Eviction</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> CAOTE minimizes long-context inference bottlenecks by introducing a closed-form token eviction metric that directly optimizes attention output error through key-value integration, boosting accuracy without retraining.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-04</span>
<a href="/notes/efficient_architectures/turboquant_online_vector_quantization.html" class="paper-link">TurboQuant Online Vector Quantization</a>
</div>
<div class="full-title-sub">TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> TurboQuant achieves near-optimal online vector quantization via random rotation and residual transforms, enabling lossless LLM KV caching and instant nearest-neighbor search.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-02</span>
<a href="/notes/efficient_architectures/looped_transformers_for_reasoning.html" class="paper-link">Looped Transformers For Reasoning</a>
</div>
<div class="full-title-sub">REASONING WITH LATENT THOUGHTS: ON THE POWER OF LOOPED TRANSFORMERS</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Weight-sharing looped transformers achieve deep-network reasoning performance with a fraction of parameters by implicitly simulating chain-of-thought steps.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-12</span>
<a href="/notes/efficient_architectures/continuous_latent_reasoning.html" class="paper-link">Continuous Latent Reasoning</a>
</div>
<div class="full-title-sub">Training Large Language Models to Reason in a Continuous Latent Space</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Coconut replaces discrete chain-of-thought with continuous latent feedback, enabling efficient breadth-first search reasoning and significantly reducing token costs while boosting accuracy.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-12</span>
<a href="/notes/efficient_architectures/hardware-efficient_gated_delta_networks.html" class="paper-link">Hardware-Efficient Gated Delta Networks</a>
</div>
<div class="full-title-sub">GATED DELTA NETWORKS : IMPROVING MAMBA 2 WITH DELTA RULE</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Unifies data-dependent gating and delta rules into a hardware-efficient linear attention mechanism that enables precise memory control and outperforms prior SOTA across long-context benchmarks.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-10</span>
<a href="/notes/efficient_architectures/entropy-based_draft_stopping.html" class="paper-link">Entropy-Based Draft Stopping</a>
</div>
<div class="full-title-sub">AdaEDL: Early Draft Stopping for Speculative Decoding of Large Language Models via an Entropy-based Lower Bound on Token Acceptance Probability</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> AdaEDL dynamically optimizes speculative decoding draft lengths using entropy-based bounds, boosting inference speed by up to 57% without training.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-07</span>
<a href="/notes/efficient_architectures/sparse_high_rank_adapters.html" class="paper-link">Sparse High Rank Adapters</a>
</div>
<div class="full-title-sub">Rapid Switching and Multi-Adapter Fusion via Sparse High Rank Adapters</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Modifying just 1–2% of base weights via sparse masking enables instant adapter switching and eliminates concept interference during multi-adapter fusion, outperforming LoRA.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-06</span>
<a href="/notes/efficient_architectures/dynamic_draft_tree_acceleration.html" class="paper-link">Dynamic Draft Tree Acceleration</a>
</div>
<div class="full-title-sub">EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> EAGLE-2 dynamically adjusts speculative draft trees using confidence scores to achieve lossless, up to 4.26x inference speedups without extra training.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-02</span>
<a href="/notes/efficient_architectures/layer-wise_moe-lora_allocation.html" class="paper-link">Layer-Wise MoE-LoRA Allocation</a>
</div>
<div class="full-title-sub">Higher Layers Need More LoRA Experts</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> MoLA dynamically allocates more LoRA experts to higher Transformer layers, boosting PEFT performance while eliminating redundant parameters.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-01</span>
<a href="/notes/efficient_architectures/eagle_speculative_sampling.html" class="paper-link">EAGLE Speculative Sampling</a>
</div>
<div class="full-title-sub">EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> EAGLE accelerates LLM inference up to 3.5x by predicting second-to-top-layer features and resolving sampling ambiguity via shifted token inputs.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2023-05</span>
<a href="/notes/efficient_architectures/autocompressor_long_context_compression.html" class="paper-link">AutoCompressor Long Context Compression</a>
</div>
<div class="full-title-sub">Adapting Language Models to Compress Contexts</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> AutoCompressors recursively compress long texts into reusable soft prompts, enabling efficient long-window reasoning and accelerated inference without architectural overhauls.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2023-04</span>
<a href="/notes/efficient_architectures/gist_token_prompt_compression.html" class="paper-link">Gist Token Prompt Compression</a>
</div>
<div class="full-title-sub">Learning to Compress Prompts with Gist Tokens</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Compresses arbitrary prompts into cached gist tokens via modified attention masks, cutting inference FLOPs by up to 40% with minimal quality loss.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2019-06</span>
<a href="/notes/efficient_architectures/swiftnet_efficient_nas.html" class="paper-link">SwiftNet Efficient NAS</a>
</div>
<div class="full-title-sub">SwiftNet: Using Graph Propagation as Meta-knowledge to Search Highly Representative Neural Architectures</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> GRAM leverages graph propagation to efficiently search flexible neural architectures, yielding SwiftNet models with state-of-the-art accuracy-density and latency for edge deployment.

</div>
</div>
</div>

</div>

<div class="topic-section-group" data-topic="multimodal_&_vision" markdown="1">

## 👁️ Multimodal & Vision

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0; color: #e2e8f0; font-size: 0.95rem; line-height: 1.6;" markdown="1">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 1.1rem;">🧭</span>
<strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
</div>

The field is converging on a predictive latent-space paradigm that replaces flat reconstruction and contrastive objectives with hierarchical feature fusion and dynamic cross-modal alignment to enable structured semantic reasoning without heavy tuning <a href="/notes/multimodal_&_vision/hierarchical_vision_llm_pretraining.html" class="citation-badge">Hierarchical Vision LLM Pretraining</a> <a href="/notes/multimodal_&_vision/next-embedding_predictive_autoregression.html" class="citation-badge">Next-Embedding Predictive Autoregression</a> <a href="/notes/multimodal_&_vision/multi-modal_latent_cot.html" class="citation-badge">Multi-Modal Latent CoT</a>. This trajectory directly addresses the latency-quality and cross-image aggregation bottlenecks in real-time multimodal pipelines by injecting asynchronous retrieval <a href="/notes/multimodal_&_vision/async_rag_for_full-duplex_speech.html" class="citation-badge">Async RAG for Full-Duplex Speech</a> and orthogonal attention mechanisms <a href="/notes/multimodal_&_vision/zero-shot_subject_style_composition.html" class="citation-badge">Zero-Shot Subject Style Composition</a> into frozen latent predictors <a href="/notes/multimodal_&_vision/vlm-guided_latent_world_models.html" class="citation-badge">VLM-Guided Latent World Models</a> <a href="/notes/multimodal_&_vision/latentlens_interpretable_visual_tokens.html" class="citation-badge">LatentLens Interpretable Visual Tokens</a> <a href="/notes/multimodal_&_vision/multi-image_vlm_analysis.html" class="citation-badge">Multi-Image VLM Analysis</a> <a href="/notes/multimodal_&_vision/tandem_s2s-llm_architecture.html" class="citation-badge">Tandem S2S-LLM Architecture</a>.

</div>

<div class="timeline-container">
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-04</span>
<a href="/notes/multimodal_&_vision/async_rag_for_full-duplex_speech.html" class="paper-link">Async RAG for Full-Duplex Speech</a>
</div>
<div class="full-title-sub">Moshi RAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Introduces an asynchronous retrieval mechanism that boosts factuality in real-time full-duplex speech models without compromising conversational latency.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-04</span>
<a href="/notes/multimodal_&_vision/hierarchical_vision_llm_pretraining.html" class="paper-link">Hierarchical Vision LLM Pretraining</a>
</div>
<div class="full-title-sub">Hierarchical Pre-Training of Vision Encoders with Large Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> HIVE replaces flattened vision embeddings with multi-layer cross-attention, enabling structured hierarchical feature fusion that boosts multimodal alignment and cuts training costs by half.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-03</span>
<a href="/notes/multimodal_&_vision/vlm-guided_latent_world_models.html" class="paper-link">VLM-Guided Latent World Models</a>
</div>
<div class="full-title-sub">ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Bridges dense visual dynamics and long-horizon semantic reasoning by injecting hierarchical VLM features into JEPA latent predictors for robust trajectory forecasting.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/multimodal_&_vision/latentlens_interpretable_visual_tokens.html" class="paper-link">LatentLens Interpretable Visual Tokens</a>
</div>
<div class="full-title-sub">LATENTLENS: Revealing Highly Interpretable Visual Tokens in LLMs</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> LATENTLENS demonstrates that visual tokens in frozen LLMs are highly interpretable by matching them to contextualized text embeddings, fundamentally challenging prior methods that underestimated cross-modal semantic alignment.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-01</span>
<a href="/notes/multimodal_&_vision/multi-image_vlm_analysis.html" class="paper-link">Multi-Image VLM Analysis</a>
</div>
<div class="full-title-sub">More Images, More Problems? A Controlled Analysis of VLM Failure Modes.</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Resolves critical cross-image aggregation failures in VLMs through a controlled benchmark, synthetic data generation, and targeted attention masking.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-12</span>
<a href="/notes/multimodal_&_vision/next-embedding_predictive_autoregression.html" class="paper-link">Next-Embedding Predictive Autoregression</a>
</div>
<div class="full-title-sub">Next-Embedding Prediction Makes Strong Vision Learners</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A minimalist causal transformer trained to predict future patch embeddings achieves state-of-the-art self-supervised vision learning without reconstruction or contrastive losses.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-10</span>
<a href="/notes/multimodal_&_vision/tandem_s2s-llm_architecture.html" class="paper-link">Tandem S2S-LLM Architecture</a>
</div>
<div class="full-title-sub">KAME: TANDEM ARCHITECTURE FOR ENHANCING KNOWLEDGE IN REAL-TIME SPEECH-TO-SPEECH CONVERSATIONAL AI</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> A tandem architecture injects real-time LLM reasoning into a speech-to-speech model, bridging the latency-quality gap in conversational AI.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-02</span>
<a href="/notes/multimodal_&_vision/zero-shot_subject_style_composition.html" class="paper-link">Zero-Shot Subject Style Composition</a>
</div>
<div class="full-title-sub">SubZero: Composing Subject, Style, and Action via Zero-Shot Personalization</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> SubZero enables tuning-free subject and style composition in diffusion models via orthogonal attention and latent optimization, eliminating content leakage for efficient edge deployment.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2023-12</span>
<a href="/notes/multimodal_&_vision/multi-modal_latent_cot.html" class="paper-link">Multi-Modal Latent CoT</a>
</div>
<div class="full-title-sub">Multi-modal Latent Space Learning for Chain-of-Thought Reasoning in Language Models</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Introduces a diffusion-based latent space learning framework that dynamically aligns visual and textual features to significantly boost multi-modal chain-of-thought reasoning.

</div>
</div>
</div>

</div>

<div class="topic-section-group" data-topic="embodied_ai_&_robotics" markdown="1">

## 🤖 Embodied AI & Robotics

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0; color: #e2e8f0; font-size: 0.95rem; line-height: 1.6;" markdown="1">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 1.1rem;">🧭</span>
<strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
</div>

The field is converging on unified differentiable mappings from raw pixel observations to continuous motor commands, where cross-embodiment generalization is achieved by scaling vision-language priors through efficient fine-tuning <a href="/notes/embodied_ai_&_robotics/openvla_generalist_robot_policy.html" class="citation-badge">OpenVLA Generalist Robot Policy</a> and stabilizing latent dynamics with minimal loss formulations that eliminate heuristic collapse prevention <a href="/notes/embodied_ai_&_robotics/end-to-end_latent_world_models.html" class="citation-badge">End-to-End Latent World Models</a>. This trajectory replaces modular control pipelines with end-to-end trainable architectures that couple flow-matched action generation <a href="/notes/embodied_ai_&_robotics/generalist_robot_control_model.html" class="citation-badge">Generalist Robot Control Model</a> with predictive world modeling, establishing a scalable mathematical framework where high-frequency dexterous manipulation emerges directly from large-scale multimodal demonstrations without task-specific architectural inductive biases.

</div>

<div class="timeline-container">
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-03</span>
<a href="/notes/embodied_ai_&_robotics/end-to-end_latent_world_models.html" class="paper-link">End-to-End Latent World Models</a>
</div>
<div class="full-title-sub">LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> LeWorldModel enables stable, end-to-end training of latent world models from raw pixels using only two loss terms, eliminating heuristic collapse-prevention tricks while enabling fast planning and physical understanding.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-10</span>
<a href="/notes/embodied_ai_&_robotics/generalist_robot_control_model.html" class="paper-link">Generalist Robot Control Model</a>
</div>
<div class="full-title-sub">π0: A Vision-Language-Action Flow Model for General Robot Control</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Merges pre-trained vision-language models with flow matching to enable high-frequency, dexterous robot control across diverse embodiments using a massive 10k-hour dataset.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2024-06</span>
<a href="/notes/embodied_ai_&_robotics/openvla_generalist_robot_policy.html" class="paper-link">OpenVLA Generalist Robot Policy</a>
</div>
<div class="full-title-sub">OpenVLA: An Open-Source Vision-Language-Action Model</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> OpenVLA sets a new SOTA for generalist robot control by efficiently fine-tuning a 7B vision-language model on diverse real-world demonstrations.

</div>
</div>
</div>

</div>

<div class="topic-section-group" data-topic="theory_&_optimization" markdown="1">

## 📐 Theory & Optimization

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0; color: #e2e8f0; font-size: 0.95rem; line-height: 1.6;" markdown="1">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="font-size: 1.1rem;">🧭</span>
<strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
</div>

The current frontier resolves the collective bottleneck of gradient compression in linear projections and unstable recurrent unrolling by abandoning static weight updates in favor of dynamic, self-supervised adaptation governed by continuous latent supervision and intrinsic predictive signals <a href="/notes/theory_&_optimization/lm_head_gradient_bottleneck.html" class="citation-badge">LM Head Gradient Bottleneck</a> <a href="/notes/theory_&_optimization/supervised_memory_training.html" class="citation-badge">Supervised Memory Training</a>. This mathematical trajectory formalizes optimization as a time-parallel, validation-free process that prevents representation collapse through temporal derivative learning <a href="/notes/theory_&_optimization/neocortical_learning_theory.html" class="citation-badge">Neocortical Learning Theory</a>, certitude-driven unsupervised reasoning <a href="/notes/theory_&_optimization/intrinsic_reward_llm_training.html" class="citation-badge">Intrinsic Reward LLM Training</a>, and optimal transport interpolation <a href="/notes/theory_&_optimization/hyperparameter_trajectory_inference.html" class="citation-badge">Hyperparameter Trajectory Inference</a> to enable weight-free procedural refinement <a href="/notes/theory_&_optimization/skillopt_text-space_optimizer.html" class="citation-badge">SkillOpt Text-Space Optimizer</a> and synthetic latent bootstrapping <a href="/notes/theory_&_optimization/bootstrapping_latent_thoughts.html" class="citation-badge">Bootstrapping Latent Thoughts</a>.

</div>

<div class="timeline-container">
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-06</span>
<a href="/notes/theory_&_optimization/neocortical_learning_theory.html" class="paper-link">Neocortical Learning Theory</a>
</div>
<div class="full-title-sub">This is how the Neocortex Learns</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Proposes temporal derivative predictive learning as the biologically plausible foundation for neocortical intelligence, bridging error backpropagation with synaptic plasticity mechanisms.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-06</span>
<a href="/notes/theory_&_optimization/supervised_memory_training.html" class="paper-link">Supervised Memory Training</a>
</div>
<div class="full-title-sub">Pretraining Recurrent Networks without Recurrence</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> SMT replaces unstable BPTT with time-parallel supervised learning on Transformer-generated memory states, enabling stable O(1) gradient paths for long-range RNN training.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/theory_&_optimization/skillopt_text-space_optimizer.html" class="paper-link">SkillOpt Text-Space Optimizer</a>
</div>
<div class="full-title-sub">SkillOpt: Executive Strategy for Self-Evolving Agent Skills</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> SkillOpt treats agent skills as trainable external states, using a structured text-space optimizer with learning rates, validation gates, and momentum to reliably improve procedural performance without weight updates.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/theory_&_optimization/next_implicit_token_prediction.html" class="paper-link">Next Implicit Token Prediction</a>
</div>
<div class="full-title-sub">NITP: Next Implicit Token Prediction for LLM Pre-training</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Augmenting discrete token prediction with continuous latent-space supervision prevents representation collapse and consistently boosts LLM generalization.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-05</span>
<a href="/notes/theory_&_optimization/theory_of_deep_generalization.html" class="paper-link">Theory of Deep Generalization</a>
</div>
<div class="full-title-sub">A Theory of Generalization in Deep Learning</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Derives a practical population-risk objective from training dynamics that explains generalization phenomena and accelerates optimization without validation data.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-03</span>
<a href="/notes/theory_&_optimization/lm_head_gradient_bottleneck.html" class="paper-link">LM Head Gradient Bottleneck</a>
</div>
<div class="full-title-sub">Lost in Backpropagation: The LM Head is a Gradient Bottleneck</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Backpropagating through a standard linear LM head compresses 95–99% of gradients, fundamentally degrading training efficiency and convergence.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-03</span>
<a href="/notes/theory_&_optimization/hyperparameter_trajectory_inference.html" class="paper-link">Hyperparameter Trajectory Inference</a>
</div>
<div class="full-title-sub">HYPERPARAMETER TRAJECTORY INFERENCE WITH CONDITIONAL LAGRANGIAN OPTIMAL TRANSPORT</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Leverages conditional Lagrangian optimal transport to interpolate neural network outputs across unobserved hyperparameter settings, enabling dynamic inference-time adaptation without retraining.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2026-02</span>
<a href="/notes/theory_&_optimization/superhuman_adaptable_intelligence.html" class="paper-link">Superhuman Adaptable Intelligence</a>
</div>
<div class="full-title-sub">AI Must Embrace Specialization via Superhuman Adaptable Intelligence</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Shifts the AI research paradigm from anthropocentric AGI to measurable adaptation speed and specialization, advocating for self-supervised world models over homogeneous autoregressive architectures.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-07</span>
<a href="/notes/theory_&_optimization/reflective_prompt_evolution.html" class="paper-link">Reflective Prompt Evolution</a>
</div>
<div class="full-title-sub">GEPA: REFLECTIVE PROMPT EVOLUTION CAN OUTPERFORM REINFORCEMENT LEARNING</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> GEPA replaces sparse RL gradients with dense natural language reflection and evolutionary search, optimizing LLM prompts with up to 35x fewer rollouts while surpassing prior SOTA.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-05</span>
<a href="/notes/theory_&_optimization/intrinsic_reward_llm_training.html" class="paper-link">Intrinsic Reward LLM Training</a>
</div>
<div class="full-title-sub">LEARNING TO REASON WITHOUT EXTERNAL REWARDS</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> INTUITOR replaces external rewards with self-certainty scores, enabling fully unsupervised LLM reasoning that matches supervised RL while generalizing better across domains.

</div>
</div>
<div class="timeline-item">
<div class="timeline-node"></div>
<div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
<span class="timeline-date">2025-03</span>
<a href="/notes/theory_&_optimization/bootstrapping_latent_thoughts.html" class="paper-link">Bootstrapping Latent Thoughts</a>
</div>
<div class="full-title-sub">Reasoning to Learn from Latent Thoughts</div>
<div class="takeaway-text" markdown="1">

<span style="color: #64748b; font-family: monospace; font-weight: bold;">└─</span> Models can iteratively bootstrap their own data efficiency by inferring and training on synthetic latent reasoning thoughts via an EM algorithm.

</div>
</div>
</div>

</div>

