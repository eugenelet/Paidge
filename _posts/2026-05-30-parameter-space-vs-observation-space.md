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

Instead of treating model weights as immutable artifacts, my research focuses on systems where the model dynamically and safely updates its own parameters based on local user interaction streams. By shifting the personalization mechanism from context-window stuffing to localized weight and parameter adaptation, several things happen at once:

1. **True Intimacy:** The model evolves a unique latent topology tailored to how its specific user structures thought, language, and tasks over time.
2. **Computational Efficiency:** We break free from the trap of ever-expanding context windows and dense KV-cache management that plagues long-term agent execution.
3. **Hardware Alignment:** The edge naturally enforces domain isolation. The model doesn't need to balance the preferences of user A with user B; it only needs to specialize in the distribution of its local environment.

## The Research Ahead

This blog serves as the active documentation of this research trajectory. The goal is to move past the engineering limitations of "agentic wrappers" and solve the deeper foundational problem: how to cleanly, securely, and continuously map human interaction directly into model parameters without catastrophic forgetting or distribution collapse. 

The startup phase laid bare what the current tools can and cannot do. Now, it's time to build the theory that makes edge intelligence genuinely adaptive.
