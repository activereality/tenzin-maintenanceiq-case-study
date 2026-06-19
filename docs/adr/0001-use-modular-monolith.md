# ADR 0001 — Use a Modular Monolith

## Status

Accepted

## Context

Tenzin is an early-stage SaaS product with multiple related domains: assets, documents, issues, chat, feedback, tenancy, and storage. The product needs clear boundaries but does not yet need the operational complexity of distributed microservices.

## Decision

Use a modular monolith with domain-oriented application slices.

## Consequences

Benefits:

- Simpler local development
- Simpler deployment
- Easier transaction boundaries
- Faster product iteration
- Clear path to split modules later if needed

Tradeoffs:

- Requires discipline to preserve module boundaries
- Shared database access must be carefully controlled
- Teams must avoid turning the application into an unstructured monolith
