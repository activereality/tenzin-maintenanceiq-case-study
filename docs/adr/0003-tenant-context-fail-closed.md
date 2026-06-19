# ADR 0003 — Tenant Context Must Fail Closed

## Status

Accepted

## Context

Tenzin is a multi-tenant SaaS product. Tenant/account isolation is a foundational security requirement.

## Decision

Resolve tenant/account context server-side and fail closed when context is missing, invalid, or ambiguous.

## Consequences

Benefits:

- Reduces risk of cross-tenant data exposure
- Keeps client-side code from owning isolation decisions
- Makes authorization rules easier to reason about

Tradeoffs:

- Requires strong testing around tenant-scoped queries
- Requires discipline when adding new endpoints and background workflows
