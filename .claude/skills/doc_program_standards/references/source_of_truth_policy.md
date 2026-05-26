# SafeSquid Documentation Source-of-Truth Policy

SafeSquid documentation should become the source of truth for the product. To get there, every documentation task must resolve conflicts with a consistent evidence hierarchy.

## Source hierarchy

Use sources in this order of authority:

1. Directly observed product behavior
2. Live SafeSquid UI verification
3. Engineering-confirmed statements and release notes
4. Current documentation in this repo, after verification
5. Internal knowledge files under `/home/administrator/safesquid-labs/knowledge/`
6. Official SafeSquid product collateral and website content
7. External standards, frameworks, and authoritative threat references

## Rules

- Do not let marketing collateral override live product behavior.
- Do not let stale docs override current UI or verified behavior.
- Do not promote internal roadmap items into current product claims.
- When knowledge files contain unverified or bounded statements, preserve those bounds in docs.
- When a point cannot be verified, mark it as unknown and route it for confirmation.

## Required handling of conflicts

When sources disagree:

1. Name the conflict explicitly.
2. Prefer the highest-authority verified source.
3. Downgrade lower-authority conflicting claims.
4. Record open questions for later resolution.

## Source use by task type

- Writing: use the highest verified source available and cite the operational implications.
- Validation: reject unsupported claims and unverified UI references.
- Research: separate confirmed facts from gaps, contradictions, and roadmap items.
- Troubleshooting: prefer observed behavior, logs, and validated runbooks over general descriptions.

## Knowledge base handling

The knowledge base at `/home/administrator/safesquid-labs/knowledge/` is a strategic internal source. Use it heavily, but preserve its confidence levels and caveats.

- `confidence: confirmed` can inform docs when it does not conflict with higher-authority sources.
- `confidence: unverified` must not become a definitive product claim.
- `status: current` still requires caution if the live UI or release behavior differs.

## Documentation promise

Every final documentation page should reflect the most trustworthy product truth available at the time of writing. Where certainty is incomplete, the page should state the condition, assumption, or open question rather than hiding it.
