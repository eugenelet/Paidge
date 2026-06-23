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
  /* Button Styles */
  .topic-pill { padding: 6px 14px; background: #1a202c; border: 1px solid #4a5568; color: #a0aec0; border-radius: 20px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.2s; }
  .topic-pill.active { background: #3253DC; color: white; border-color: #6382f2; box-shadow: 0 0 8px rgba(50, 83, 220, 0.4); }
  .topic-pill:hover:not(.active) { background: #2d3748; color: white; }
  
  /* Epistemic Step-Function (Timeline) Styles */
  .timeline-container { border-left: 2px solid #3253DC; margin-left: 12px; padding-left: 24px; position: relative; margin-top: 2rem; margin-bottom: 3rem; }
  .timeline-item { position: relative; margin-bottom: 2rem; }
  .timeline-node { position: absolute; left: -30px; top: 6px; width: 10px; height: 10px; background: #3253DC; border-radius: 50%; box-shadow: 0 0 8px rgba(99, 130, 242, 0.8); border: 2px solid #16181d; z-index: 10;}
  .timeline-date { background: #2d3748; color: #cbd5e0; padding: 2px 8px; border-radius: 4px; font-family: monospace; font-size: 0.8rem; letter-spacing: 0.5px; }
  .paper-link { color: #e2e8f0; font-weight: 600; font-size: 1.05rem; text-decoration: none; transition: color 0.2s; }
  .paper-link:hover { color: #6382f2; }
  .takeaway-text { color: #a0aec0; font-size: 0.95rem; line-height: 1.5; margin-top: 6px; }
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

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The field converges on a paradigm of inference-time parameterization where frozen base models are dynamically augmented via fast weights, low-rank adapters, or external memory structures optimized through online gradients, hypernetworks, or meta-optimization loops, effectively transforming adaptation into a continuous, input-conditioned optimization process that expands effective capacity and context retention without architectural modification. This trajectory addresses the static weight bottleneck by treating model behavior as a differentiable function of the test distribution, enabling scalable, unsupervised personalization where instance-specific latent updates or recursive orchestration continuously recalibrate attention and memory dynamics to achieve persistent reasoning gains and long-context scaling within constant latency constraints.</p>
</div>

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/test-time_adaptation/skillopt_text_space_agent_optimization.html" class="paper-link">SkillOpt Text Space Agent Optimization</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Treats agent skills as trainable external state optimized via text-space gradients, enabling weight-free procedural adaptation across models and harnesses."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/test-time_adaptation/compact_test-time_memory.html" class="paper-link">Compact Test-Time Memory</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"An 8×8 online memory matrix dynamically updates during inference, enabling frozen LLMs to efficiently retain long-term context without fine-tuning or context expansion."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/test-time_adaptation/training-free_looped_transformers.html" class="paper-link">Training-Free Looped Transformers</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Retrofitting frozen LLMs with inference-time layer looping and numerical integration yields significant accuracy gains without any training or architectural changes."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-04</span>
      <a href="/notes/test-time_adaptation/in-place_test-time_training.html" class="paper-link">In-Place Test-Time Training</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Repurposes existing MLP projection matrices as dynamic fast weights to enable scalable, drop-in test-time adaptation for LLMs without costly retraining."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/test-time_adaptation/dynamic_layer-wise_tta.html" class="paper-link">Dynamic Layer-Wise TTA</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A lightweight hypernetwork dynamically scales per-layer inference-time updates, stabilizing unsupervised prompt-specific adaptation without external supervision."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/test-time_adaptation/context-to-lora_hypernetwork.html" class="paper-link">Context-to-LoRA Hypernetwork</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A bottleneck-free hypernetwork converts diverse contexts into high-quality LoRA adapters in a single forward pass, enabling instant, compute-efficient LLM adaptation without iterative fine-tuning."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-12</span>
      <a href="/notes/test-time_adaptation/rl_conductor_agent_orchestration.html" class="paper-link">RL Conductor Agent Orchestration</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A 7B RL-trained model dynamically orchestrates and recursively scales worker LLMs at inference time to achieve state-of-the-art reasoning performance."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-12</span>
      <a href="/notes/test-time_adaptation/metatpt_dynamic_prompt_tuning.html" class="paper-link">MetaTPT Dynamic Prompt Tuning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"MetaTPT dynamically learns sample-specific augmentations via dual-loop meta-optimization to robustly adapt vision-language models at test time."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-12</span>
      <a href="/notes/test-time_adaptation/query-only_test-time_training.html" class="paper-link">Query-Only Test-Time Training</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Applying lightweight gradient updates to query projections during inference dynamically reallocates attention mass, outperforming static in-context learning and thinking tokens for long-context retrieval."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-12</span>
      <a href="/notes/test-time_adaptation/end-to-end_test-time_training.html" class="paper-link">End-to-End Test-Time Training</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Compressing long contexts into model weights via inference-time gradient updates enables full-attention scaling with constant latency."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-06</span>
      <a href="/notes/test-time_adaptation/text-driven_lora_generation.html" class="paper-link">Text-Driven LoRA Generation</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A hypernetwork dynamically generates task-specific LoRA adapters from natural language at inference, enabling zero-shot adaptation without retraining."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-06</span>
      <a href="/notes/test-time_adaptation/self-adapting_llms.html" class="paper-link">Self-Adapting LLMs</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"SEAL enables LLMs to autonomously generate and apply their own finetuning directives via reinforcement learning, achieving persistent weight updates for new tasks without external supervision."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-05</span>
      <a href="/notes/test-time_adaptation/large_chunk_test-time_training.html" class="paper-link">Large Chunk Test-Time Training</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Large-chunk online weight updates drastically boost GPU utilization and enable scalable test-time memory for long-context modeling."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-05</span>
      <a href="/notes/test-time_adaptation/test-time_llm_adaptation.html" class="paper-link">Test-Time LLM Adaptation</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Minimizes input perplexity on unlabeled test data with LoRA updates to dynamically adapt LLMs without labeled data or catastrophic forgetting."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-02</span>
      <a href="/notes/test-time_adaptation/latent_thought_models.html" class="paper-link">Latent Thought Models</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Introduces a novel architecture that dynamically optimizes instance-specific latent vectors during inference, unlocking new scaling dimensions for superior sample and parameter efficiency."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-02</span>
      <a href="/notes/test-time_adaptation/low-rank_test-time_vision_adaptation.html" class="paper-link">Low-Rank Test-Time Vision Adaptation</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Replaces computationally heavy test-time prompt tuning with low-rank image encoder updates, enabling faster, memory-efficient domain adaptation for vision-language models."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-01</span>
      <a href="/notes/test-time_adaptation/titans_test-time_memory.html" class="paper-link">Titans Test-Time Memory</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Dynamically updates model parameters during inference to memorize surprising context, enabling efficient scaling beyond 2M tokens."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-11</span>
      <a href="/notes/test-time_adaptation/generativeadapter_on-the-fly_adaptation.html" class="paper-link">GenerativeAdapter On-The-Fly Adaptation</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Compresses streaming context into low-rank parameter updates via a single forward pass, enabling efficient test-time adaptation without fine-tuning or inference overhead."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-11</span>
      <a href="/notes/test-time_adaptation/test-time_training_for_llms.html" class="paper-link">Test-Time Training for LLMs</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Gradient-based parameter updates during inference using in-context examples drastically improve language models' reasoning and few-shot generalization on novel tasks."</em>
    </div>
  </div>
</div>

</div>

<div class="topic-section-group" data-topic="in-context_learning" markdown="1">

## 🧠 In-Context Learning

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The field converges on a mathematical unification positing that in-context learning operates as implicit gradient descent mediated by rank-1 weight patches, catalyzing a paradigm shift from static retrieval to the dynamic optimization of demonstration manifolds via reinforcement learning and evolutionary strategies to maximize input-output controllability. This trajectory identifies the collective bottleneck as the efficient utilization of context, resolved by scaling example counts and optimizing their selection or projection into task-aware latent spaces, thereby enabling frozen models to replicate fine-tuning performance without weight updates by treating prompts as parameter-free, infinitely extensible adapters governed by the same optimization dynamics as explicit training.</p>
</div>

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/in-context_learning/fast-slow_llm_adaptation.html" class="paper-link">Fast-Slow LLM Adaptation</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Interleaving prompt optimization with reinforcement learning enables rapid task adaptation while preserving model plasticity and preventing catastrophic forgetting."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-03</span>
      <a href="/notes/in-context_learning/visual_icl_demo_selection.html" class="paper-link">Visual ICL Demo Selection</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"RL-driven demonstration selection outperforms kNN on objective visual ICL by actively balancing visual relevance with task-specific diversity."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/in-context_learning/doc-to-lora_instant_context_adaptation.html" class="paper-link">Doc-to-LoRA Instant Context Adaptation</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A lightweight hypernetwork instantly converts long prompts into LoRA adapters, eliminating KV-cache overhead while preserving in-context learning performance."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-12</span>
      <a href="/notes/in-context_learning/recursive_context_scaling.html" class="paper-link">Recursive Context Scaling</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"An inference-time scaffolding strategy that treats long prompts as an external environment, enabling LLMs to recursively decompose and process inputs orders of magnitude beyond their native context windows without architectural changes."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-11</span>
      <a href="/notes/in-context_learning/implicit_weight_patch_theory.html" class="paper-link">Implicit Weight Patch Theory</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Context effects in modern LLMs are mathematically equivalent to rank-1 MLP weight patches governed by input/output controllability."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-07</span>
      <a href="/notes/in-context_learning/reflective_prompt_evolution.html" class="paper-link">Reflective Prompt Evolution</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"GEPA replaces sparse RL gradients with iterative natural language reflection and evolutionary search to optimize LLM prompts with drastically higher sample efficiency."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-07</span>
      <a href="/notes/in-context_learning/context_tuning_for_icl.html" class="paper-link">Context Tuning for ICL</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Gradient-optimizing in-context demonstrations and KV caches significantly boosts few-shot LLM adaptation without weight updates."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-07</span>
      <a href="/notes/in-context_learning/implicit_dynamics_of_icl.html" class="paper-link">Implicit Dynamics of ICL</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Proves that transformer blocks mathematically convert prompt context into rank-1 weight updates, unifying in-context learning with implicit gradient descent."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-03</span>
      <a href="/notes/in-context_learning/task-aware_multimodal_icl.html" class="paper-link">Task-Aware Multimodal ICL</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A lightweight transformer with task-aware attention dynamically optimizes demonstration sequences, substantially boosting multimodal in-context learning performance."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-10</span>
      <a href="/notes/in-context_learning/vector_in-context_learning.html" class="paper-link">Vector In-Context Learning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Lightweight embedding projectors enable frozen LLMs to perform in-context learning directly on continuous vectors across diverse modalities."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-04</span>
      <a href="/notes/in-context_learning/many-shot_in-context_learning.html" class="paper-link">Many-Shot In-Context Learning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Scaling in-context learning to hundreds or thousands of examples dramatically boosts performance on complex reasoning and low-resource tasks, often matching fine-tuning without weight updates."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-02</span>
      <a href="/notes/in-context_learning/visual_in-context_learning.html" class="paper-link">Visual In-Context Learning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Replaces visual ICL demonstrations with intent-driven text summaries to bypass cross-modal gaps and boost LVLM reasoning without retraining."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2023-05</span>
      <a href="/notes/in-context_learning/sequential_rl_example_retrieval.html" class="paper-link">Sequential RL Example Retrieval</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Frames in-context example selection as a sequential reinforcement learning problem to capture inter-example dependencies and boost LLM reasoning."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2022-11</span>
      <a href="/notes/in-context_learning/rl-guided_in-context_learning.html" class="paper-link">RL-Guided In-Context Learning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Reinforcement learning optimizes demonstration example selection to stabilize and boost in-context learning performance, particularly for smaller language models."</em>
    </div>
  </div>
</div>

</div>

<div class="topic-section-group" data-topic="efficient_architectures" markdown="1">

## ⚡ Efficient Architectures

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The field exhibits a fundamental convergence toward continuous latent manifolds where discrete token dynamics are supplanted by functional representations and structured linear recurrences, mathematically resolving the quadratic attention scaling bottleneck via resolution-invariant operator learning and low-rank KV condensation while maintaining long-context fidelity through curvature-aware geometry. Concurrently, inference architectures are evolving from static computation graphs to adaptive, context-aware control systems that dynamically allocate compute via entropy-driven routing, speculative draft topologies, and sparse activation manifolds, enabling lossless compression of memory states and agentic workflows with sub-quadratic complexity and parameter-efficient generalization.</p>
</div>

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/efficient_architectures/functional_attention_architecture.html" class="paper-link">Functional Attention Architecture</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Lifts attention from discrete tokens to functional spaces via structured linear operators for efficient, resolution-invariant operator learning."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/efficient_architectures/global_regression_kv_cache.html" class="paper-link">Global Regression KV Cache</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Training-free global ridge regression aligns compressed KV caches with full-cache attention, eliminating over-merging while preserving long-context performance."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/efficient_architectures/self-regulated_simulative_planning.html" class="paper-link">Self-Regulated Simulative Planning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Decomposing agentic reasoning into a self-regulated configurator and simulative planner slashes token consumption by up to 95% while matching trillion-parameter model performance."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/efficient_architectures/modular_memory_architecture.html" class="paper-link">Modular Memory Architecture</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Plug-and-play modular memory enables efficient, noise-robust knowledge integration in frozen LLMs without retraining or context expansion."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/efficient_architectures/agentic_workflow_compilation.html" class="paper-link">Agentic Workflow Compilation</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Fine-tuning small LLMs to internalize agentic workflows cuts inference costs by two orders of magnitude while maintaining near-frontier quality."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-04</span>
      <a href="/notes/efficient_architectures/latent_condensed_attention.html" class="paper-link">Latent Condensed Attention</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"LCA natively condenses context within MLA’s latent space, slashing KV cache by 90% and accelerating prefilling by 2.5× without extra parameters."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-04</span>
      <a href="/notes/efficient_architectures/preconditioned_deltanet_architecture.html" class="paper-link">Preconditioned DeltaNet Architecture</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Diagonal preconditioning injects curvature-aware geometry into delta-rule recurrences, enabling exact online least-squares solutions with efficient parallel training and consistent long-context gains."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-04</span>
      <a href="/notes/efficient_architectures/stable_looped_language_models.html" class="paper-link">Stable Looped Language Models</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Stabilizes looped transformers via spectral norm constraints to scale compute predictably without inflating parameter counts."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-04</span>
      <a href="/notes/efficient_architectures/elastic_looped_transformers.html" class="paper-link">Elastic Looped Transformers</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Weight-shared recurrent transformer blocks enable parameter-efficient visual generation with flexible test-time compute via intra-loop self-distillation."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-03</span>
      <a href="/notes/efficient_architectures/efficient_sparse_llm_kernels.html" class="paper-link">Efficient Sparse LLM Kernels</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Custom CUDA kernels and sparse packing formats unlock >99% unstructured sparsity in LLMs for major throughput and memory gains with negligible accuracy loss."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-03</span>
      <a href="/notes/efficient_architectures/inference_layer_skipping.html" class="paper-link">Inference Layer Skipping</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Native diffusion LLMs develop redundant early layers that enable aggressive inference-time skipping with minimal accuracy loss, outperforming brittle autoregressive counterparts."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-03</span>
      <a href="/notes/efficient_architectures/future-aware_speculative_decoding.html" class="paper-link">Future-Aware Speculative Decoding</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Equips draft models with future-oriented contemplate tokens to slash inference latency while preserving output quality."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/efficient_architectures/dualpath_kv_cache_optimization.html" class="paper-link">DualPath KV Cache Optimization</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"DualPath eliminates KV-cache I/O bottlenecks in agentic LLM inference by dynamically routing cache loads across prefill and decode engines to double system throughput."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/efficient_architectures/progressive_thought_encoding.html" class="paper-link">Progressive Thought Encoding</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Encodes evicted KV cache tokens into LoRA adapters, enabling large reasoning models to train and infer under strict memory constraints without sacrificing accuracy."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/efficient_architectures/fastforward_predictive_ffn_sparsity.html" class="paper-link">FastForward Predictive FFN Sparsity</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"FastForward slashes LLM prefill latency via block-wise predictive FFN sparsity and error compensation, preserving accuracy while cutting compute costs."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/efficient_architectures/latent_reasoning_via_fused_tokens.html" class="paper-link">Latent Reasoning via Fused Tokens</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Fuses contextual hidden states with predictive vocabulary embeddings to enable stable, dynamic latent reasoning without verbose text chains."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/efficient_architectures/interleaved_head_attention.html" class="paper-link">Interleaved Head Attention</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"IHA breaks MHA's linear scaling limit by enabling cross-head mixing via pseudo-projections, boosting long-context retrieval and reasoning with minimal parameter overhead."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/efficient_architectures/hierarchical_top-p_sparse_attention.html" class="paper-link">Hierarchical Top-P Sparse Attention</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A two-stage hierarchical top-p mechanism adaptively allocates compute to deliver near-lossless, high-speed long-context LLM inference."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/efficient_architectures/query-oriented_kv_selection.html" class="paper-link">Query-Oriented KV Selection</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"QUOKA slashes LLM prefill latency by up to 7× via a training-free, query-aware sparse attention mechanism that preserves near-baseline accuracy."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/efficient_architectures/growing_memory_rnns.html" class="paper-link">Growing Memory RNNs</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Caching recurrent memory checkpoints scales effective context length while preserving sub-quadratic inference efficiency."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-12</span>
      <a href="/notes/efficient_architectures/manifold-constrained_hyper-connections.html" class="paper-link">Manifold-Constrained Hyper-Connections</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Constrains expanded residual connectivity on a doubly stochastic manifold to restore identity mapping, enabling stable and scalable large-scale LLM training."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-10</span>
      <a href="/notes/efficient_architectures/tandem_s2s-llm_architecture.html" class="paper-link">Tandem S2S-LLM Architecture</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A tandem architecture injects real-time LLM knowledge into a speech-to-speech model via oracle tokens, achieving cascaded-system quality without latency penalties."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-10</span>
      <a href="/notes/efficient_architectures/kimi_linear_architecture.html" class="paper-link">Kimi Linear Architecture</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A hybrid linear attention design that slashes KV cache by 75%, accelerates decoding sixfold, and surpasses full-attention performance."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-10</span>
      <a href="/notes/efficient_architectures/continuous_next-vector_llms.html" class="paper-link">Continuous Next-Vector LLMs</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"CALM replaces discrete token prediction with continuous vector generation, cutting autoregressive steps by K and significantly improving the performance-compute trade-off."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-10</span>
      <a href="/notes/efficient_architectures/looped_language_models.html" class="paper-link">Looped Language Models</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"LoopLM replaces explicit chain-of-thought with adaptive latent recurrence, delivering 2–3× parameter efficiency while matching larger frontier models."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-09</span>
      <a href="/notes/efficient_architectures/nested_subspace_networks.html" class="paper-link">Nested Subspace Networks</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"NSNs enable dynamic, granular compute adjustment at inference time for pre-trained LLMs via low-rank factorization, achieving smooth performance-efficiency trade-offs without retraining."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-09</span>
      <a href="/notes/efficient_architectures/spiffy_accelerates_diffusion_llms.html" class="paper-link">Spiffy Accelerates Diffusion LLMs</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Spiffy introduces lossless speculative decoding with directed draft graphs to accelerate diffusion LLM inference up to 7.9× without training auxiliary models."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-06</span>
      <a href="/notes/efficient_architectures/diffusionblocks_block-wise_training.html" class="paper-link">DiffusionBlocks Block-Wise Training</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Recasting residual networks as diffusion processes enables memory-efficient, independent block training that matches end-to-end performance."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-06</span>
      <a href="/notes/efficient_architectures/floe_sparse_adapter_selection.html" class="paper-link">FLoE Sparse Adapter Selection</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"FLoE slashes LLM fine-tuning costs by using Fisher information to sparsely activate only critical transformer layers for MoE-based LoRA adaptation."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-06</span>
      <a href="/notes/efficient_architectures/vocabtrim_vocabulary_pruning.html" class="paper-link">VocabTrim Vocabulary Pruning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Training-free pruning of drafter LM heads slashes memory-bound drafting latency by up to 19% with negligible acceptance rate loss."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-04</span>
      <a href="/notes/efficient_architectures/turboquant_online_vector_quantization.html" class="paper-link">TurboQuant Online Vector Quantization</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"TurboQuant achieves near-optimal, accelerator-friendly vector quantization via random rotation and residual transforms, enabling quality-neutral KV cache compression with near-zero indexing latency."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-04</span>
      <a href="/notes/efficient_architectures/key_similarity_kv_cache_eviction.html" class="paper-link">Key Similarity KV Cache Eviction</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"KEYDIFF enables memory-constrained long-context LLM inference by evicting redundant KV cache entries via key similarity, cutting latency up to 30% with negligible accuracy loss."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-04</span>
      <a href="/notes/efficient_architectures/key_similarity_kv_cache_eviction.html" class="paper-link">Key Similarity KV Cache Eviction</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"KEYDIFF enables memory-constrained long-context LLM inference by evicting KV cache tokens based on key diversity rather than attention scores, cutting latency by up to 30% with negligible accuracy loss."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-04</span>
      <a href="/notes/efficient_architectures/kv_cache_token_eviction.html" class="paper-link">KV Cache Token Eviction</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"CAOTE minimizes inference memory bottlenecks by computing closed-form token importance via attention output error, boosting long-context accuracy without retraining."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-02</span>
      <a href="/notes/efficient_architectures/looped_transformers_for_reasoning.html" class="paper-link">Looped Transformers for Reasoning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Iterative weight-sharing enables deep reasoning capabilities at a fraction of the parameter cost of standard architectures."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-12</span>
      <a href="/notes/efficient_architectures/continuous_latent_reasoning.html" class="paper-link">Continuous Latent Reasoning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Replacing discrete chain-of-thought tokens with continuous hidden states enables efficient, multi-path latent reasoning in LLMs."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-12</span>
      <a href="/notes/efficient_architectures/gated_deltanet_architecture.html" class="paper-link">Gated DeltaNet Architecture</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Unifies gating and delta rules to enable hardware-efficient parallel training and precise long-context memory control in linear transformers."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-10</span>
      <a href="/notes/efficient_architectures/entropy-based_adaptive_speculative_decoding.html" class="paper-link">Entropy-Based Adaptive Speculative Decoding</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"A training-free, entropy-driven early stopping mechanism that dynamically optimizes speculative decoding draft lengths to boost LLM inference speed by up to 57% without accuracy loss."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-07</span>
      <a href="/notes/efficient_architectures/sparse_high_rank_adapters.html" class="paper-link">Sparse High Rank Adapters</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Modifying just 1–2% of base weights via sparse high-rank adapters enables rapid switching and multi-concept fusion with zero inference overhead."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-06</span>
      <a href="/notes/efficient_architectures/dynamic_draft_trees_for_llms.html" class="paper-link">Dynamic Draft Trees for LLMs</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"EAGLE-2 achieves lossless 3x-5x LLM inference speedups by dynamically adjusting draft tree structures based on context-aware confidence scores."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-02</span>
      <a href="/notes/efficient_architectures/layer-wise_lora_expert_allocation.html" class="paper-link">Layer-Wise LoRA Expert Allocation</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Strategically distributing more LoRA experts to higher Transformer layers drastically reduces parameter-efficient fine-tuning redundancy while boosting performance."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-01</span>
      <a href="/notes/efficient_architectures/eagle_speculative_sampling.html" class="paper-link">EAGLE Speculative Sampling</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"EAGLE accelerates LLM inference up to 3.5x by predicting second-to-top-layer features and resolving sampling uncertainty with shifted tokens."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2023-05</span>
      <a href="/notes/efficient_architectures/efficient_long_context_compression.html" class="paper-link">Efficient Long Context Compression</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Teaching LMs to recursively compress long contexts into accumulated soft prompts enables efficient window extension and faster inference without architectural overhaul."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2023-04</span>
      <a href="/notes/efficient_architectures/gist_token_prompt_compression.html" class="paper-link">Gist Token Prompt Compression</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Compresses arbitrary LLM prompts into cached gist tokens via modified attention masks, slashing inference compute by up to 40% with minimal quality loss."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2019-06</span>
      <a href="/notes/efficient_architectures/gram_efficient_architecture_search.html" class="paper-link">GRAM Efficient Architecture Search</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"GRAM leverages graph propagation to efficiently search compact neural architectures, delivering SwiftNet models with unmatched accuracy-density and latency for edge deployment."</em>
    </div>
  </div>
</div>

</div>

<div class="topic-section-group" data-topic="multimodal_&_vision" markdown="1">

## 👁️ Multimodal & Vision

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The field is transitioning from discrete, static multimodal alignment to a unified framework of continuous, disentangled latent dynamics where cross-modal integration is mediated by structured attention and predictive constraints, thereby resolving fundamental trade-offs between real-time latency, computational efficiency, and semantic fidelity. This trajectory advances through hierarchical feature coupling and orthogonal optimization in unquantized spaces, enabling autoregressive reasoning and robust compositionality while eliminating content leakage and aggregation artifacts inherent to rigid tokenization schemes.</p>
</div>

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-04</span>
      <a href="/notes/multimodal_&_vision/asynchronous_rag_for_speech.html" class="paper-link">Asynchronous RAG for Speech</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Integrates asynchronous retrieval into full-duplex speech models to boost factuality without sacrificing real-time conversational latency."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-04</span>
      <a href="/notes/multimodal_&_vision/hierarchical_vision-llm_fusion.html" class="paper-link">Hierarchical Vision-LLM Fusion</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"HIVE fuses multi-layer vision features directly into LLMs via cross-attention, boosting multimodal alignment and cutting training costs."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-03</span>
      <a href="/notes/multimodal_&_vision/vlm-guided_latent_world_models.html" class="paper-link">VLM-Guided Latent World Models</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Merges dense JEPA dynamics with long-horizon VLM reasoning via hierarchical feature alignment to boost trajectory forecasting."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/multimodal_&_vision/latentlens_visual_token_interpretability.html" class="paper-link">LATENTLENS Visual Token Interpretability</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"LATENTLENS demonstrates that visual tokens in frozen LLMs are highly interpretable through contextual text matching, overturning prior assumptions about cross-modal alignment."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-01</span>
      <a href="/notes/multimodal_&_vision/multi-image_vlm_failure_analysis.html" class="paper-link">Multi-Image VLM Failure Analysis</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Resolves cross-image aggregation failures in vision-language models through a controlled benchmark and targeted attention masking."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-12</span>
      <a href="/notes/multimodal_&_vision/next-embedding_prediction_for_vision.html" class="paper-link">Next-Embedding Prediction for Vision</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Training Vision Transformers to autoregressively predict future patch embeddings directly in continuous space yields strong self-supervised visual learners without reconstruction or discrete tokenizers."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-02</span>
      <a href="/notes/multimodal_&_vision/zero-shot_subject_style_composition.html" class="paper-link">Zero-Shot Subject Style Composition</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"SubZero enables tuning-free subject-style-action composition in diffusion models via orthogonal attention and disentangled latent optimization, eliminating content leakage for efficient edge deployment."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2023-12</span>
      <a href="/notes/multimodal_&_vision/multi-modal_latent_cot.html" class="paper-link">Multi-Modal Latent CoT</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Leverages diffusion processes to create deeply aligned text-image latent spaces, dramatically improving multi-modal chain-of-thought reasoning accuracy."</em>
    </div>
  </div>
</div>

</div>

<div class="topic-section-group" data-topic="embodied_ai_&_robotics" markdown="1">

## 🤖 Embodied AI & Robotics

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The current frontier coalesces around latent-space Vision-Language-Action architectures that integrate generative flow matching with stable, end-to-end world modeling to enable generalist physical reasoning and high-frequency dexterous control across diverse embodiments. This trajectory emphasizes mathematical tractability via minimal loss formulations and commodity-scale parameterization, revealing a critical bottleneck in scaling latent dynamics for real-time deployment while eliminating heuristic collapse mitigation in favor of intrinsic stability mechanisms.</p>
</div>

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-03</span>
      <a href="/notes/embodied_ai_&_robotics/stable_end-to-end_world_models.html" class="paper-link">Stable End-to-End World Models</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"LeWorldModel enables stable, end-to-end latent world modeling from raw pixels using only two loss terms, eliminating collapse heuristics while enabling fast planning and physical reasoning."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-10</span>
      <a href="/notes/embodied_ai_&_robotics/π0_general_dexterous_robot.html" class="paper-link">π0 General Dexterous Robot</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Integrates pre-trained vision-language models with flow matching to enable generalist, high-frequency dexterous robot control across diverse embodiments."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2024-06</span>
      <a href="/notes/embodied_ai_&_robotics/openvla_generalist_robot_policy.html" class="paper-link">OpenVLA Generalist Robot Policy</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"OpenVLA establishes a new SOTA for generalist robot control via an open-source 7B VLA optimized for efficient fine-tuning and commodity-GPU deployment."</em>
    </div>
  </div>
</div>

</div>

<div class="topic-section-group" data-topic="theory_&_optimization" markdown="1">

## 📐 Theory & Optimization

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The collective trajectory indicates a fundamental departure from unstable, gradient-compressed autoregressive training toward stable, time-parallel optimization frameworks that substitute external supervision with intrinsic latent dynamics and self-calibrated confidence signals to eliminate representation collapse and resolve the severe gradient degradation inherent in standard linear projections. This mathematical unification via optimal transport and reservoir theory redefines the frontier as the direct evolution of generative distributions and rapid adaptation through world models, enabling exact population-risk minimization and one-step inference by reformulating learning as a continuous dynamical process rather than discrete token prediction.</p>
</div>

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-06</span>
      <a href="/notes/theory_&_optimization/temporal_derivative_learning.html" class="paper-link">Temporal Derivative Learning</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Temporal derivative learning bridges biologically plausible neural circuits with the computational power of error-driven gradient approximation."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-06</span>
      <a href="/notes/theory_&_optimization/pretraining_rnns_without_recurrence.html" class="paper-link">Pretraining RNNs Without Recurrence</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"SMT replaces unstable BPTT with time-parallel supervised learning on Transformer-generated memory states, enabling stable O(1) gradient paths for RNN pretraining."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/theory_&_optimization/next_implicit_token_prediction.html" class="paper-link">Next Implicit Token Prediction</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Augments discrete next-token prediction with continuous latent-space supervision to prevent representation collapse and boost downstream performance."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-05</span>
      <a href="/notes/theory_&_optimization/deep_learning_generalization_theory.html" class="paper-link">Deep Learning Generalization Theory</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Unifies generalization phenomena through signal-reservoir output dynamics and enables exact population-risk training via a lightweight SNR preconditioner."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-03</span>
      <a href="/notes/theory_&_optimization/lm_head_gradient_bottleneck.html" class="paper-link">LM Head Gradient Bottleneck</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"The standard linear LM head compresses 95–99% of backpropagated gradients, fundamentally degrading training efficiency and convergence speed."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-03</span>
      <a href="/notes/theory_&_optimization/hyperparameter_trajectory_inference.html" class="paper-link">Hyperparameter Trajectory Inference</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Leverages conditional Lagrangian optimal transport to mathematically model and interpolate neural network outputs across arbitrary hyperparameter settings, eliminating costly retraining."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/theory_&_optimization/superhuman_adaptable_intelligence_framework.html" class="paper-link">Superhuman Adaptable Intelligence Framework</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Proposes replacing the flawed AGI paradigm with Superhuman Adaptable Intelligence (SAI), emphasizing rapid task adaptation, self-supervised learning, and world models over autoregressive architectures."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2026-02</span>
      <a href="/notes/theory_&_optimization/one-step_drifting_generation.html" class="paper-link">One-Step Drifting Generation</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"Reformulates generative modeling as a training-time distribution evolution problem, enabling state-of-the-art one-step inference via a novel drift-based optimization objective."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-05</span>
      <a href="/notes/theory_&_optimization/intrinsic_rl_for_llms.html" class="paper-link">Intrinsic RL for LLMs</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"INTUITOR enables fully unsupervised LLM reasoning by replacing external rewards with self-generated confidence scores during policy optimization."</em>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-node"></div>
    <div style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap;">
      <span class="timeline-date">2025-03</span>
      <a href="/notes/theory_&_optimization/latent_thought_bootstrapping.html" class="paper-link">Latent Thought Bootstrapping</a>
    </div>
    <div class="takeaway-text">
      <span style="color: #4a5568; font-family: monospace;">└─</span> <em>"An EM-driven bootstrapping loop infers latent reasoning traces from raw text to drastically improve data efficiency during language model pretraining."</em>
    </div>
  </div>
</div>

</div>

