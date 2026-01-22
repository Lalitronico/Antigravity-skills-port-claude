# Antigravity-skills-port-claude
This repository is a compatibility port of Anthropic’s official Claude Code Skills collection (anthropics/skills) adapted to run smoothly in Antigravity.

**What’s included**

A curated set of Skills originally published by Anthropic, refactored so they can be used in Antigravity without friction.

The same skill organization and intent as the upstream project (folders + SKILL.md), preserved for familiarity and easy updates.

**What was adapted for Antigravity**

Depending on the skill, the port focuses on practical compatibility changes such as:

Normalizing skill metadata / discovery so Antigravity can reliably load and route skills.

Adjusting paths, tool calls, and environment assumptions that are Claude Code–specific.

Making scripts and resources portable across common runtimes and repo layouts.

**Why this exists**

If you like the breadth and quality of the official Anthropic Skills library but you build and run agents in Antigravity, this repo gives you a drop-in, Antigravity-friendly version—without having to manually translate each skill.

**Upstream reference & credit**

Original Skills collection: Anthropic – anthropics/skills.
Skills concept and structure are described in Claude Code documentation.
