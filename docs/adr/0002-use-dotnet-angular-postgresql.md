# ADR 0002 — Use .NET, Angular, and PostgreSQL

## Status

Accepted

## Context

The product needs a reliable backend, a structured frontend, and a relational database with a path toward vector search and document retrieval workflows.

## Decision

Use:

- .NET 8 / ASP.NET Core for the backend
- Angular / TypeScript for the frontend
- PostgreSQL with EF Core for persistence

## Consequences

Benefits:

- Strong backend typing and mature web API ecosystem
- Productive full-stack development model
- Relational data model suited to SaaS tenancy and asset/document relationships
- PostgreSQL path for future vector-search capabilities

Tradeoffs:

- Requires careful EF Core modeling and migration discipline
- Angular can add frontend structure overhead, but the structure is useful as the UI grows
