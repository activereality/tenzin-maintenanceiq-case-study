# ADR 0006 — Keep MaintenanceIQ Asset-Scoped

## Status

Accepted

## Context

It would be easy for MaintenanceIQ to become a generic ticketing or CMMS feature. That would dilute the MVP and distract from Tenzin's core value: machine-specific knowledge and troubleshooting.

## Decision

Keep issues and issue workflows scoped to assets/machines for the MVP.

## Consequences

Benefits:

- Preserves machine context
- Reduces scope creep
- Keeps troubleshooting history connected to the asset
- Differentiates Tenzin from generic issue trackers

Tradeoffs:

- Users may eventually want global issue views
- Reporting workflows may need additional design later
