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
  .topic-pill { padding: 6px 14px; background: #1a202c; border: 1px solid #4a5568; color: #a0aec0; border-radius: 20px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.2s; }
  .topic-pill.active { background: #3253DC; color: white; border-color: #6382f2; box-shadow: 0 0 8px rgba(50, 83, 220, 0.4); }
  .topic-pill:hover:not(.active) { background: #2d3748; color: white; }
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
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The field is converging on a paradigm shift from static parameter optimization to dynamic inference-time computation, where capability acquisition is decoupled from model weights and formalized as the continuous optimization of auxiliary state spaces and iterative numerical processes during the forward pass. This trajectory establishes runtime computational allocation—spanning external memory dynamics, text-space gradient optimization, and meta-control orchestration—as the primary bottleneck and frontier for scaling frozen architectures without parametric or architectural modification.</p>
</div>

| Date | Paper | Core Takeaway |
| :---: | :--- | :--- |
| `2026-05` | [SkillOpt Text Space Agent Optimization](/notes/test-time_adaptation/skillopt_text_space_agent_optimization.html) | Treats agent skills as trainable external state optimized via text-space gradients, enabling weight-free procedural adaptation across models and harnesses. |
| `2026-05` | [Compact Test-Time Memory](/notes/test-time_adaptation/compact_test-time_memory.html) | An 8×8 online memory matrix dynamically updates during inference, enabling frozen LLMs to efficiently retain long-term context without fine-tuning or context expansion. |
| `2026-05` | [Training-Free Looped Transformers](/notes/test-time_adaptation/training-free_looped_transformers.html) | Retrofitting frozen LLMs with inference-time layer looping and numerical integration yields significant accuracy gains without any training or architectural changes. |
| `2025-12` | [RL Conductor Agent Orchestration](/notes/test-time_adaptation/rl_conductor_agent_orchestration.html) | A 7B RL-trained model dynamically orchestrates and recursively scales worker LLMs at inference time to achieve state-of-the-art reasoning performance. |

</div>

<div class="topic-section-group" data-topic="in-context_learning" markdown="1">

## 🧠 In-Context Learning

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The current frontier converges on dynamic prompt optimization paradigms that fuse reinforcement learning with language-native iterative feedback, fundamentally addressing the dual bottlenecks of sample inefficiency and catastrophic forgetting inherent in static or gradient-sparse adaptation methods. This trajectory establishes a collective shift toward hybrid evolutionary-reflection mechanisms that navigate the prompt landscape via semantic self-correction rather than raw gradients, thereby decoupling rapid task-specific plasticity from the degradation of foundational model generalization.</p>
</div>

| Date | Paper | Core Takeaway |
| :---: | :--- | :--- |
| `2026-05` | [Fast-Slow LLM Adaptation](/notes/in-context_learning/fast-slow_llm_adaptation.html) | Interleaving prompt optimization with reinforcement learning enables rapid task adaptation while preserving model plasticity and preventing catastrophic forgetting. |
| `2025-07` | [Reflective Prompt Evolution](/notes/in-context_learning/reflective_prompt_evolution.html) | GEPA replaces sparse RL gradients with iterative natural language reflection and evolutionary search to optimize LLM prompts with drastically higher sample efficiency. |

</div>

<div class="topic-section-group" data-topic="efficient_architectures" markdown="1">

## ⚡ Efficient Architectures

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The frontier is defined by a fundamental shift from discrete token attention to continuous functional representations governed by structured linear operators and recursive latent condensation, which reframe context processing as an optimization over compressed signal manifolds rather than fixed sequence lengths. This mathematical trajectory unifies algorithmic sparsity, modular memory integration, and dynamic system routing to resolve KV cache I/O bottlenecks, enabling order-of-magnitude efficiency gains through hardware-aware co-design and parameter-efficient workflows that preserve frontier performance without architectural overhaul.</p>
</div>

| Date | Paper | Core Takeaway |
| :---: | :--- | :--- |
| `2026-05` | [Functional Attention Architecture](/notes/efficient_architectures/functional_attention_architecture.html) | Lifts attention from discrete tokens to functional spaces via structured linear operators for efficient, resolution-invariant operator learning. |
| `2026-05` | [Global Regression KV Cache](/notes/efficient_architectures/global_regression_kv_cache.html) | Training-free global ridge regression aligns compressed KV caches with full-cache attention, eliminating over-merging while preserving long-context performance. |
| `2026-05` | [Self-Regulated Simulative Planning](/notes/efficient_architectures/self-regulated_simulative_planning.html) | Decomposing agentic reasoning into a self-regulated configurator and simulative planner slashes token consumption by up to 95% while matching trillion-parameter model performance. |
| `2026-05` | [Modular Memory Architecture](/notes/efficient_architectures/modular_memory_architecture.html) | Plug-and-play modular memory enables efficient, noise-robust knowledge integration in frozen LLMs without retraining or context expansion. |
| `2026-05` | [Agentic Workflow Compilation](/notes/efficient_architectures/agentic_workflow_compilation.html) | Fine-tuning small LLMs to internalize agentic workflows cuts inference costs by two orders of magnitude while maintaining near-frontier quality. |
| `2026-04` | [Latent Condensed Attention](/notes/efficient_architectures/latent_condensed_attention.html) | LCA natively condenses context within MLA’s latent space, slashing KV cache by 90% and accelerating prefilling by 2.5× without extra parameters. |
| `2026-03` | [Efficient Sparse LLM Kernels](/notes/efficient_architectures/efficient_sparse_llm_kernels.html) | Custom CUDA kernels and sparse packing formats unlock >99% unstructured sparsity in LLMs for major throughput and memory gains with negligible accuracy loss. |
| `2026-02` | [DualPath KV Cache Optimization](/notes/efficient_architectures/dualpath_kv_cache_optimization.html) | DualPath eliminates KV-cache I/O bottlenecks in agentic LLM inference by dynamically routing cache loads across prefill and decode engines to double system throughput. |
| `2026-02` | [Progressive Thought Encoding](/notes/efficient_architectures/progressive_thought_encoding.html) | Encodes evicted KV cache tokens into LoRA adapters, enabling large reasoning models to train and infer under strict memory constraints without sacrificing accuracy. |
| `2025-10` | [Tandem S2S-LLM Architecture](/notes/efficient_architectures/tandem_s2s-llm_architecture.html) | A tandem architecture injects real-time LLM knowledge into a speech-to-speech model via oracle tokens, achieving cascaded-system quality without latency penalties. |
| `2025-06` | [DiffusionBlocks Block-Wise Training](/notes/efficient_architectures/diffusionblocks_block-wise_training.html) | Recasting residual networks as diffusion processes enables memory-efficient, independent block training that matches end-to-end performance. |
| `2023-05` | [Efficient Long Context Compression](/notes/efficient_architectures/efficient_long_context_compression.html) | Teaching LMs to recursively compress long contexts into accumulated soft prompts enables efficient window extension and faster inference without architectural overhaul. |
| `2023-04` | [Gist Token Prompt Compression](/notes/efficient_architectures/gist_token_prompt_compression.html) | Compresses arbitrary LLM prompts into cached gist tokens via modified attention masks, slashing inference compute by up to 40% with minimal quality loss. |

</div>

<div class="topic-section-group" data-topic="multimodal_&_vision" markdown="1">

## 👁️ Multimodal & Vision

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The field is converging on temporally decoupled multimodal architectures that disentangle knowledge acquisition from real-time inference via asynchronous retrieval pipelines, fundamentally shifting away from monolithic synchronous generation. This trajectory demands rigorous optimization of cross-temporal information flow under strict causal latency bounds, with the collective bottleneck residing in aligning heterogeneous processing rates without inducing phase lag or degrading streaming coherence.</p>
</div>

| Date | Paper | Core Takeaway |
| :---: | :--- | :--- |
| `2026-04` | [Asynchronous RAG for Speech](/notes/multimodal_&_vision/asynchronous_rag_for_speech.html) | Integrates asynchronous retrieval into full-duplex speech models to boost factuality without sacrificing real-time conversational latency. |

</div>

<div class="topic-section-group" data-topic="embodied_ai_&_robotics" markdown="1">

## 🤖 Embodied AI & Robotics

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The frontier is characterized by a convergence toward minimal, stable objective functions for end-to-end latent world modeling that eliminate collapse heuristics via intrinsic mathematical constraints, enabling direct mapping from raw pixels to predictive representations capable of supporting rapid planning and physical reasoning. This trajectory indicates a fundamental shift toward unifying representation learning and control within a single optimization landscape, where robust causal inference is achieved by reducing the loss topology to its essential components rather than relying on auxiliary regularization or modular decomposition.</p>
</div>

| Date | Paper | Core Takeaway |
| :---: | :--- | :--- |
| `2026-03` | [Stable End-to-End World Models](/notes/embodied_ai_&_robotics/stable_end-to-end_world_models.html) | LeWorldModel enables stable, end-to-end latent world modeling from raw pixels using only two loss terms, eliminating collapse heuristics while enabling fast planning and physical reasoning. |

</div>

<div class="topic-section-group" data-topic="theory_&_optimization" markdown="1">

## 📐 Theory & Optimization

<div style="background: #16181d; border: 1px solid #2d3748; border-left: 4px solid #3253DC; padding: 1.25rem; border-radius: 4px 8px 8px 4px; margin: 1.25rem 0 2rem 0;">
  <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
    <span style="font-size: 1.1rem;">🧭</span>
    <strong style="color: #6382f2; font-size: 0.85rem; font-family: monospace; text-transform: uppercase; letter-spacing: 1px;">Research Trend</strong>
  </div>
  <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.6; margin: 0;">The research frontier converges on a paradigm of stable, time-parallel optimization for recurrent systems that supplants unstable gradient propagation with continuous latent-space supervision and temporal derivative learning, effectively bridging biological plausibility with scalable error-driven approximation. This trajectory unifies generalization and representation fidelity by exploiting signal-reservoir output dynamics and signal-to-noise preconditioning to augment discrete prediction objectives, thereby enabling exact population-risk minimization while mitigating collapse through precise control of internal signal statistics.</p>
</div>

| Date | Paper | Core Takeaway |
| :---: | :--- | :--- |
| `2026-06` | [Temporal Derivative Learning](/notes/theory_&_optimization/temporal_derivative_learning.html) | Temporal derivative learning bridges biologically plausible neural circuits with the computational power of error-driven gradient approximation. |
| `2026-06` | [Pretraining RNNs Without Recurrence](/notes/theory_&_optimization/pretraining_rnns_without_recurrence.html) | SMT replaces unstable BPTT with time-parallel supervised learning on Transformer-generated memory states, enabling stable O(1) gradient paths for RNN pretraining. |
| `2026-05` | [Next Implicit Token Prediction](/notes/theory_&_optimization/next_implicit_token_prediction.html) | Augments discrete next-token prediction with continuous latent-space supervision to prevent representation collapse and boost downstream performance. |
| `2026-05` | [Deep Learning Generalization Theory](/notes/theory_&_optimization/deep_learning_generalization_theory.html) | Unifies generalization phenomena through signal-reservoir output dynamics and enables exact population-risk training via a lightweight SNR preconditioner. |

</div>

