---
layout: post
title: "Parameter Space vs. Observation Space: TTA on the Edge"
date: 2026-05-30
categories: research
---

The pivot from building a startup back to focusing entirely on core research brings a certain clarity. When you step away from the commercial infrastructure of deployment, you stop asking *"how do we wrap this into a product?"* and start asking the harder question: *"why are these models fundamentally failing to become personal?"*

The current paradigm of AI relies on monolithic, centrally hosted snapshots. They are frozen in time, serving a statistical average of humanity from a cloud server. Even the shift toward "AI Agents" hasn't solved this. Current agent frameworks operate almost entirely within what can be called the **observation space**. They store memory as text files, interact via Markdown logs, and perform vector lookups (RAG) to patch over the fact that the underlying model hasn't learned a single thing about the user since it left the cluster.

That is not how human intelligence works, and it is not how we achieve true personalization. 

## The Abstract Mind: Parameter Space is for Thinking

Human cognition maintains a strict boundary between internal abstraction and external expression. We do not store our core habits, intuitions, and daily adaptations as a collection of text files that we reread every morning. Instead, our experiences directly reshape our neural pathways. Knowledge lives in the **latent or parameter space**. 

We only relegate information to the observation space when the cognitive load demands an external framework. 

> **The Math Derivation Analogy:** Think about deriving a complex mathematical formula. You do not store every single intermediate algebraic step in your working memory simultaneously; your brain would run out of context window instantly. Instead, you keep the abstract logic internal (parameter space) and use a piece of paper (observation space) to write down the intermediate steps, reasoning through them sequentially. The paper acts as an external scaffolding, not the intelligence itself.

Current AI agents treat the text file as the intelligence. By jamming raw logs and endless context histories into the observation window, we are cluttering the working memory of the system rather than building a deeper, continuous internal abstraction.

## Moving Personalization to the Edge via Test-Time Adaptation

If an AI is going to adapt to the idiosyncratic behavior, preferences, and mental models of a specific individual over months and years, it cannot live in a centralized cloud serving millions of people simultaneously. It has to live on the edge. 

Localized deployment on edge devices provides the perfect environment for a different kind of architecture: **Continuous Test-Time Adaptation (TTA)**. 


<div class="architecture-comparison-container" style="width: 100%; overflow: hidden; background: #131415; border-radius: 12px; padding: 2rem 0; margin: 2.5rem 0; border: 1px solid #2d3748;">
  <svg viewBox="0 0 800 380" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
    
    <line x1="400" y1="20" x2="400" y2="360" stroke="#2d3748" stroke-width="2" stroke-dasharray="8,4" />

    <text x="200" y="35" fill="#f7fafc" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">Observation Space (Agent)</text>
    <text x="600" y="35" fill="#f7fafc" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">Parameter Space (Continuous TTA)</text>

    <circle cx="55" cy="210" r="18" fill="#2b6cb0" />
    <text x="55" y="214" fill="#fff" font-size="11" text-anchor="middle" font-weight="600">User</text>
    <line x1="73" y1="210" x2="145" y2="210" stroke="#4a5568" stroke-width="1.5" stroke-dasharray="4,2" />

    <rect x="145" y="110" width="90" height="180" fill="#1a202c" stroke="#4a5568" stroke-width="2" rx="6" />
    <text x="190" y="95" fill="#a0aec0" font-size="12" font-weight="600" text-anchor="middle">KV Cache</text>

    <rect class="sheet-obs so1" x="152" y="270" width="76" height="12" rx="2" />
    <rect class="sheet-obs so2" x="152" y="250" width="76" height="12" rx="2" />
    <rect class="sheet-obs so3" x="152" y="230" width="76" height="12" rx="2" />
    <rect class="sheet-obs so4" x="152" y="210" width="76" height="12" rx="2" />
    <rect class="sheet-obs so5" x="152" y="190" width="76" height="12" rx="2" />
    <rect class="sheet-obs so6" x="152" y="170" width="76" height="12" rx="2" />
    
    <g class="danger-alert">
      <rect x="152" y="120" width="76" height="24" fill="#742a2a" rx="4" opacity="0.9"/>
      <text x="190" y="136" fill="#fff" font-size="10" font-weight="700" text-anchor="middle" letter-spacing="0.5">OUT OF MEM</text>
    </g>

    <line x1="235" y1="210" x2="310" y2="210" stroke="#2d3748" stroke-width="2" />
    
    <circle cx="340" cy="210" r="26" fill="#4a5568" stroke="#2d3748" stroke-width="2" />
    <text x="340" y="214" fill="#a0aec0" font-size="13" text-anchor="middle" font-weight="700">θ</text>
    <text x="340" y="260" fill="#718096" font-size="11" text-anchor="middle" font-weight="500">Frozen Weights</text>

    <circle class="pkt-obs po1" cx="55" cy="210" r="5" fill="#63b3ed" />
    <circle class="pkt-obs po2" cx="55" cy="210" r="5" fill="#63b3ed" />
    <circle class="pkt-obs po3" cx="55" cy="210" r="5" fill="#63b3ed" />
    <circle class="pkt-obs po4" cx="55" cy="210" r="5" fill="#63b3ed" />
    <circle class="pkt-obs po5" cx="55" cy="210" r="5" fill="#63b3ed" />
    <circle class="pkt-obs po6" cx="55" cy="210" r="5" fill="#63b3ed" />


    <circle cx="455" cy="210" r="18" fill="#2b6cb0" />
    <text x="455" y="214" fill="#fff" font-size="11" text-anchor="middle" font-weight="600">User</text>
    <line x1="473" y1="210" x2="545" y2="210" stroke="#4a5568" stroke-width="1.5" stroke-dasharray="4,2" />

    <rect x="545" y="140" width="80" height="120" fill="#1a202c" stroke="#4a5568" stroke-width="1.5" stroke-dasharray="4,4" rx="6" />
    <text x="585" y="125" fill="#a0aec0" font-size="12" font-weight="600" text-anchor="middle">KV Cache</text>

    <rect class="sheet-param sp1" x="552" y="240" width="66" height="12" rx="2" />
    <rect class="sheet-param sp2" x="552" y="220" width="66" height="12" rx="2" />
    <rect class="sheet-param sp3" x="552" y="200" width="66" height="12" rx="2" />

    <path class="discharge-pipe" d="M 625 210 L 705 210" stroke="#4a5568" stroke-width="2" stroke-dasharray="5,5" />

    <circle class="tta-manifold" cx="735" cy="210" r="32" fill="none" stroke="#48bb78" stroke-width="2" />
    <circle class="tta-core" cx="735" cy="210" r="24" fill="#22543d" stroke="#38a169" stroke-width="2" />
    <text x="735" y="215" fill="#fff" font-size="15" text-anchor="middle" font-style="italic" font-family="serif" font-weight="600">θ<tspan dy="3" font-size="9" font-style="normal">TTA</tspan></text>
    <text x="735" y="260" fill="#48bb78" font-size="11" text-anchor="middle" font-weight="600">Adaptive Weights</text>

    <circle class="pkt-param pp1" cx="455" cy="210" r="5" fill="#68d391" />
    <circle class="pkt-param pp2" cx="455" cy="210" r="5" fill="#68d391" />
    <circle class="pkt-param pp3" cx="455" cy="210" r="5" fill="#68d391" />
    
    <circle class="gradient-pulse gp1" cx="625" cy="210" r="4" fill="#f6ad55" />
    <circle class="gradient-pulse gp2" cx="625" cy="210" r="4" fill="#fc8181" />
  </svg>
</div>

<style>
  /* ================= LEFT SIDE ANIMATIONS (6s Cycle) ================= */
  @keyframes drop-obs-1 { 0%, 2% {cx:55; cy:210; opacity:0;} 4% {opacity:1;} 10% {cx:190; cy:210;} 12% {cx:190; cy:276; opacity:1;} 13%, 100% {opacity:0;} }
  @keyframes drop-obs-2 { 0%, 12% {cx:55; cy:210; opacity:0;} 14% {opacity:1;} 20% {cx:190; cy:210;} 22% {cx:190; cy:256; opacity:1;} 23%, 100% {opacity:0;} }
  @keyframes drop-obs-3 { 0%, 22% {cx:55; cy:210; opacity:0;} 24% {opacity:1;} 30% {cx:190; cy:210;} 32% {cx:190; cy:236; opacity:1;} 33%, 100% {opacity:0;} }
  @keyframes drop-obs-4 { 0%, 32% {cx:55; cy:210; opacity:0;} 34% {opacity:1;} 40% {cx:190; cy:210;} 42% {cx:190; cy:216; opacity:1;} 43%, 100% {opacity:0;} }
  @keyframes drop-obs-5 { 0%, 42% {cx:55; cy:210; opacity:0;} 44% {opacity:1;} 50% {cx:190; cy:210;} 52% {cx:190; cy:196; opacity:1;} 53%, 100% {opacity:0;} }
  @keyframes drop-obs-6 { 0%, 52% {cx:55; cy:210; opacity:0;} 54% {opacity:1;} 60% {cx:190; cy:210;} 62% {cx:190; cy:176; opacity:1;} 63%, 100% {opacity:0;} }

  @keyframes sheet-obs-1 { 0%, 12% {opacity:0;} 13%, 74% {opacity:1; fill:#3182ce;} 75%, 95% {opacity:1; fill:#e53e3e;} 96%, 100% {opacity:0;} }
  @keyframes sheet-obs-2 { 0%, 22% {opacity:0;} 23%, 74% {opacity:1; fill:#3182ce;} 75%, 95% {opacity:1; fill:#e53e3e;} 96%, 100% {opacity:0;} }
  @keyframes sheet-obs-3 { 0%, 32% {opacity:0;} 33%, 74% {opacity:1; fill:#3182ce;} 75%, 95% {opacity:1; fill:#e53e3e;} 96%, 100% {opacity:0;} }
  @keyframes sheet-obs-4 { 0%, 42% {opacity:0;} 43%, 74% {opacity:1; fill:#3182ce;} 75%, 95% {opacity:1; fill:#e53e3e;} 96%, 100% {opacity:0;} }
  @keyframes sheet-obs-5 { 0%, 52% {opacity:0;} 53%, 74% {opacity:1; fill:#3182ce;} 75%, 95% {opacity:1; fill:#e53e3e;} 96%, 100% {opacity:0;} }
  @keyframes sheet-obs-6 { 0%, 62% {opacity:0;} 63%, 74% {opacity:1; fill:#3182ce;} 75%, 95% {opacity:1; fill:#e53e3e;} 96%, 100% {opacity:0;} }

  @keyframes alert-flash { 0%, 74% { opacity:0; } 75%, 80%, 85%, 90%, 95% { opacity:1; } 77%, 82%, 87%, 92% { opacity:0; } 96%, 100% { opacity:0; } }

  .po1 { animation: drop-obs-1 6s infinite ease-in; }
  .po2 { animation: drop-obs-2 6s infinite ease-in; }
  .po3 { animation: drop-obs-3 6s infinite ease-in; }
  .po4 { animation: drop-obs-4 6s infinite ease-in; }
  .po5 { animation: drop-obs-5 6s infinite ease-in; }
  .po6 { animation: drop-obs-6 6s infinite ease-in; }

  .so1 { animation: sheet-obs-1 6s infinite step-start; }
  .so2 { animation: sheet-obs-2 6s infinite step-start; }
  .so3 { animation: sheet-obs-3 6s infinite step-start; }
  .so4 { animation: sheet-obs-4 6s infinite step-start; }
  .so5 { animation: sheet-obs-5 6s infinite step-start; }
  .so6 { animation: sheet-obs-6 6s infinite step-start; }
  .danger-alert { animation: alert-flash 6s infinite linear; }

  /* ================= RIGHT SIDE ANIMATIONS (5s Cycle) ================= */
  @keyframes drop-param-1 { 0%, 5% {cx:455; cy:210; opacity:0;} 10% {opacity:1;} 20% {cx:585; cy:210;} 22% {cx:585; cy:246; opacity:1;} 23%, 100% {opacity:0;} }
  @keyframes drop-param-2 { 0%, 25% {cx:455; cy:210; opacity:0;} 30% {opacity:1;} 40% {cx:585; cy:210;} 42% {cx:585; cy:226; opacity:1;} 43%, 100% {opacity:0;} }
  @keyframes drop-param-3 { 0%, 35% {cx:455; cy:210; opacity:0;} 40% {opacity:1;} 50% {cx:585; cy:210; opacity:1;} 51%, 100% {opacity:0;} }

  @keyframes sheet-param-1 { 0%, 22% {opacity:0;} 23%, 49% {opacity:1; fill:#48bb78;} 50%, 59% {opacity:1; fill:#ed8936;} 60%, 100% {opacity:0;} }
  @keyframes sheet-param-2 { 0%, 42% {opacity:0;} 43%, 49% {opacity:1; fill:#48bb78;} 50%, 59% {opacity:1; fill:#ed8936;} 60%, 100% {opacity:0;} }
  @keyframes sheet-param-3 { 0%, 49% {opacity:0;} 50%, 59% {opacity:1; fill:#ed8936;} 60%, 100% {opacity:0;} }

  @keyframes discharge-gradients { 0%, 59% { cx: 625; opacity: 0; } 60% { opacity: 1; } 75% { cx: 735; opacity: 0; } 100% { cx: 735; opacity: 0; } }

  @keyframes adapt-weights { 0%, 70% { transform: scale(1); stroke: #38a169; fill: #22543d; } 75% { transform: scale(1.15); stroke: #f6ad55; fill: #2c5282; } 85%, 100% { transform: scale(1); stroke: #38a169; fill: #22543d; } }
  @keyframes pulse-manifold-line { 0%, 70% { transform: scale(1); opacity: 0.3; stroke:#48bb78;} 75% { transform: scale(1.3); opacity: 0.9; stroke: #f6ad55; } 100% { transform: scale(1); opacity: 0.3; stroke:#48bb78;} }

  .pp1 { animation: drop-param-1 5s infinite ease-in; }
  .pp2 { animation: drop-param-2 5s infinite ease-in; }
  .pp3 { animation: drop-param-3 5s infinite ease-in; }

  .sp1 { animation: sheet-param-1 5s infinite step-start; }
  .sp2 { animation: sheet-param-2 5s infinite step-start; }
  .sp3 { animation: sheet-param-3 5s infinite step-start; }

  .gp1 { animation: discharge-gradients 5s infinite linear; animation-delay: 0s; }
  .gp2 { animation: discharge-gradients 5s infinite linear; animation-delay: 0.2s; }

  .tta-core { transform-origin: 735px 210px; animation: adapt-weights 5s infinite ease-in-out; }
  .tta-manifold { transform-origin: 735px 210px; animation: pulse-manifold-line 5s infinite ease-in-out; }
</style>
<p style="text-align: center; font-size: 0.85rem; color: #a0aec0; margin-top: -1.5rem; margin-bottom: 2rem; font-style: italic;">
  Figure 1: Observation Space processing results in an O(N) memory bottleneck (left), while Parameter Space adaptation maintains an O(1) footprint by directly updating model weights (right).
</p>


Instead of treating model weights as immutable artifacts, my research focuses on systems where the model dynamically and safely updates its own parameters based on local user interaction streams. By shifting the personalization mechanism from context-window stuffing to localized weight and parameter adaptation, several things happen at once:

1. **True Intimacy:** The model evolves a unique latent topology tailored to how its specific user structures thought, language, and tasks over time.
2. **Computational Efficiency:** We break free from the trap of ever-expanding context windows and dense KV-cache management that plagues long-term agent execution.
3. **Hardware Alignment:** The edge naturally enforces domain isolation. The model doesn't need to balance the preferences of user A with user B; it only needs to specialize in the distribution of its local environment.

## The Research Ahead

This blog serves as the active documentation of this research trajectory. The goal is to move past the engineering limitations of "agentic wrappers" and solve the deeper foundational problem: how to cleanly, securely, and continuously map human interaction directly into model parameters without catastrophic forgetting or distribution collapse. 

The startup phase laid bare what the current tools can and cannot do. Now, it's time to build the theory that makes edge intelligence genuinely adaptive.
