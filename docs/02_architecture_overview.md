# 02 — Architecture Overview

## Architecture style

Tenzin MaintenanceIQ is designed as a modular monolith. This keeps the early product simple to deploy and reason about while still enforcing clear domain boundaries inside the application.

The private implementation separates concerns by application slices such as assets, documents, issues, feedback, chat, auth/account context, and infrastructure integrations.

## Runtime shape

```text
Angular Web App
      |
      v
ASP.NET Core Web API
      |
      +--> Application / Domain modules
      |       ├── Assets
      |       ├── Documents
      |       ├── Issues / MaintenanceIQ
      |       ├── Chat
      |       ├── Feedback
      |       └── Auth / Accounts
      |
      +--> PostgreSQL / EF Core
      |
      +--> Azure Blob Storage
      |
      +--> AI Provider Abstraction
```

## Key design goals

- Keep tenant isolation server-side and fail-closed.
- Avoid leaking internal identifiers, storage paths, or implementation details through public DTOs.
- Keep AI provider integration abstracted so the application is not tightly coupled to one vendor.
- Build the product in vertical slices with tests and frontend build checks.
- Prefer simple deployability before prematurely splitting into microservices.
- Keep machine context central to the user workflow.

## Backend responsibilities

The backend owns:

- Tenant/account resolution
- Authorization boundaries
- Asset and machine data
- Document metadata and chunk lifecycle
- Issue and timeline workflows
- Attachment access policies
- AI orchestration and citation construction
- Feedback validation
- Public DTO shaping

## Frontend responsibilities

The frontend owns:

- Asset-scoped workflows
- Chat and citation presentation
- Issue and timeline presentation
- Attachment expand/collapse behavior
- Feedback UI
- Read-only versus editable state behavior
- User-friendly naming for account and machine concepts

## Infrastructure responsibilities

Infrastructure integrations are isolated behind application-facing abstractions where practical. For example, the AI integration is designed behind an `IAiProvider`-style boundary so product workflows can remain stable if model/provider choices change.
