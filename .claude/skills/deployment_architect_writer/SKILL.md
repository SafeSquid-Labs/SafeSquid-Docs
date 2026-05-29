---
name: deployment_architect_writer
description: Use when SafeSquid SWG documentation must explain enterprise deployment design, topology assumptions, proxy modes, client onboarding, rollout sequencing, clustering, high availability, disaster recovery, or other architecture-sensitive implementation choices.
---

# Deployment Architect Writer

Use this skill when a documentation task depends on topology, rollout design, or deployment variation.

## Goal

Write deployment guidance that is safe, explicit, and useful in large enterprises and mission-critical environments.

## Read first

1. `/home/administrator/Mintlify-Docs/.claude/skills/doc_program_standards/references/world_class_quality_rubric.md`
2. `/home/administrator/Mintlify-Docs/.claude/skills/doc_program_standards/references/source_of_truth_policy.md`
3. `/home/administrator/safesquid-labs/knowledge/product/technical_architecture.md`
4. `/home/administrator/safesquid-labs/knowledge/architecture/solution_topology.md`
5. `/home/administrator/safesquid-labs/knowledge/architecture/complex_topology_solution_pattern.md`

## What to cover

- Deployment objective
- Topology assumptions and trust boundaries
- Client-side preparation
- SafeSquid-side setup
- Upstream and downstream dependencies
- Variations by environment
- Pilot and rollout sequencing
- Rollback considerations
- Monitoring and steady-state operations

## Required output behaviors

- Distinguish lab guidance from production guidance.
- Explain why a topology choice is appropriate.
- Call out when guidance changes for branch, cloud, hybrid, clustered, or high-availability deployments.
- Highlight failure domains and blast radius.
- Prefer diagrams or tables when they reduce ambiguity.

## Do not do

- Do not assume a single deployment pattern fits all enterprises.
- Do not hide architecture dependencies inside a step list.
- Do not describe high availability or disaster recovery vaguely.
