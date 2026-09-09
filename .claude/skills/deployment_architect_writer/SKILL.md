---
name: deployment_architect_writer
description: Use when SafeSquid SWG documentation must explain enterprise deployment design, topology assumptions, proxy modes, or HA/DR.
---

# Deployment Architect Writer

Use this skill when a documentation task depends on topology, rollout design, or deployment variation.

## Goal
Write deployment guidance that is safe, explicit, and useful in mission-critical environments.

## Information Gathering
- **MANDATORY:** Use `graphify query` and `graphify path` to locate architecture dependencies (e.g., `graphify explain "solution_topology"` or `graphify query "high_availability"`) before writing.

## What to Cover
- Deployment objective and trust boundaries.
- SafeSquid-side setup vs. Client-side preparation.
- Upstream and downstream dependencies.
- Variations by environment (branch, cloud, hybrid, clustered).
- Failure domains and blast radius.

## Constraints
- Distinguish lab guidance from production guidance.
- Prefer Mermaid diagrams (`flowchart TB`) or markdown tables over dense text.
- Do not assume a single deployment pattern fits all enterprises.