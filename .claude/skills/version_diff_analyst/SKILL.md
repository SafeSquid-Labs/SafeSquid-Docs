---
name: version_diff_analyst
description: Use when SafeSquid SWG documentation may vary by release, UI revision, platform baseline, or behavior change and you need to identify what changed, what remains true, and how the docs should represent version-sensitive guidance.
---

# Version Diff Analyst

Use this skill when product behavior or documentation may differ by version.

## Goal

Keep docs accurate across releases and prevent silent drift.

## Workflow

1. Identify the versions in scope.
2. Compare release notes, docs, UI behavior, and knowledge files.
3. Separate stable behavior from version-specific behavior.
4. Identify what docs must change.
5. Recommend how to label or isolate version-sensitive guidance.

## Output

Return:

- Stable statements safe for general docs
- Version-specific statements that need explicit labeling
- Removed or stale statements that should be deleted
- Open questions that still need confirmation

## Rules

- Do not collapse version differences into one generic statement.
- Do not let legacy docs masquerade as current behavior.
- If the default supported version is unclear, state that as a blocker.
