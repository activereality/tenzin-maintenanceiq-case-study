# System Context

This diagram shows the high-level system context for Tenzin MaintenanceIQ.

```mermaid
flowchart LR
    Tech[Maintenance Technician] --> Web[Angular Web App]
    Admin[Plant / Admin User] --> Web

    Web --> API[ASP.NET Core API]

    API --> DB[(PostgreSQL)]
    API --> Blob[(Azure Blob Storage)]
    API --> AI[AI Provider Abstraction]

    AI --> LLM[LLM / Embedding Provider]

    API --> Auth[Tenant / Auth Boundary]
    API --> Search[Document Search + Citation Pipeline]

    Search --> DB
    Search --> AI
```

## Notes

Tenzin MaintenanceIQ is designed as a tenant-aware SaaS application for industrial machine knowledge, troubleshooting, cited AI answers, and maintenance workflows.

The public case-study repository does not include source code. It documents the architecture, domain boundaries, implementation approach, and verification process for employer review.