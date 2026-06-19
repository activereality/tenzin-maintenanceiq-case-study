# Interview Walkthrough

This document provides a short guided explanation of the Tenzin MaintenanceIQ public case-study repository. It is intended for interviews, recruiter conversations, and technical discussions where the production source code is private but the architecture and engineering decisions are public.

## 30-Second Summary

Tenzin MaintenanceIQ is an AI-assisted SaaS platform for industrial maintenance teams. It helps technicians search machine documentation, ask asset-specific troubleshooting questions, receive AI-assisted answers with citations, and capture issue history for future maintenance work.

The production source code is private because the product is actively being built, but this public repository documents the architecture, domain model, API boundaries, AI/RAG citation flow, security and tenancy approach, implementation history, verification process, and sanitized product screenshots.

## 2-Minute Walkthrough

Tenzin MaintenanceIQ is built around a common industrial maintenance problem: machine knowledge is often scattered across manuals, PDFs, technician notes, tribal knowledge, and issue history. When a machine goes down, technicians need fast answers, but they also need to know where those answers came from.

The application is designed as a tenant-aware SaaS platform. The core model centers on industrial assets and machine components. Assets can have documents, document pages, chunks, embeddings, chat sessions, answer citations, maintenance issues, issue events, and attachments.

The backend is designed around ASP.NET Core, EF Core, PostgreSQL, and Azure-oriented storage. The frontend is Angular. The architecture is intentionally modular so product areas such as assets, documents, chat, citations, feedback, and MaintenanceIQ issue workflows can evolve without becoming tightly coupled.

The AI workflow is citation-first. A user asks a machine-specific question, the system searches tenant- and asset-scoped document chunks, sends relevant context through an AI provider abstraction, and returns an answer with citations back to source material. The goal is not just to generate an answer, but to give technicians a response they can verify.

The product also separates answer-level feedback from citation-level feedback. An answer can be marked helpful or not helpful, while individual citations can be marked helpful, wrong source, or outdated. That distinction creates better quality signals than treating all feedback as one generic rating.

A major design concern is tenant safety and public DTO safety. The application avoids exposing internal tenant identifiers, storage paths, internal user IDs, and implementation details through public responses. Tenant context is resolved server-side, and the application is designed to fail closed rather than accidentally crossing tenant boundaries.

The public repository is structured as a technical case study instead of a source-code mirror. It includes architecture notes, domain diagrams, sanitized API examples, implementation logs, verification notes, ADRs, and screenshots. This allows the system design and engineering reasoning to be reviewed without exposing proprietary source code.

## Suggested Repo Tour

When walking someone through the repository, use this order:

1. Start with the `README.md` to explain what the project is and why the source code is private.
2. Open the screenshots to show the product exists beyond documentation.
3. Open the system context diagram to show the high-level architecture.
4. Open the domain model diagram to explain the core entities and relationships.
5. Open the AI/RAG citation flow to show how answers are generated and cited.
6. Open the security and tenancy document to highlight senior-level SaaS concerns.
7. Open the implementation log to show completed engineering slices and verification discipline.
8. Open the ADRs to show architectural decision-making.

## What I Personally Built

The private implementation includes work across the product stack:

- ASP.NET Core API design
- Angular frontend workflows
- PostgreSQL and EF Core domain modeling
- Tenant-aware application boundaries
- Asset, document, chat, citation, feedback, and issue workflow foundations
- MaintenanceIQ issue timeline and attachment workflows
- AI provider abstraction for answer generation and future provider flexibility
- Citation-first answer design
- Feedback boundaries for answer-level and citation-level quality signals
- DTO safety hardening to avoid exposing internal identifiers and storage details
- Build, test, frontend, and quality-gate verification

## Key Technical Decisions

### Private Source, Public Case Study

The production source code is private because Tenzin MaintenanceIQ is an active product. The public repository is meant to demonstrate system design, architectural reasoning, product thinking, and engineering discipline without exposing proprietary implementation details.

### Modular Monolith First

The application is designed as a modular monolith rather than starting with microservices. This keeps local development and deployment simpler while still allowing clear boundaries between product areas such as assets, documents, chat, feedback, and issues.

### Citation-First AI

The system is designed so AI responses are connected back to source material. In maintenance workflows, a plausible answer is not enough. Technicians need the ability to verify where the answer came from.

### Tenant Safety

Tenant context is treated as a backend concern. Public request and response models avoid exposing unnecessary tenant internals, and tenant boundaries are designed to fail closed.

### Separate Answer and Citation Feedback

Answer feedback and citation feedback are intentionally separated because they measure different things. A response can be useful while one citation is weak, or a citation can be correct while the generated answer needs improvement.

## Strong Interview Talking Points

### On SaaS Architecture

Tenzin MaintenanceIQ is designed as a tenant-aware SaaS product from the start. Even though the MVP is focused on machine knowledge and troubleshooting, the underlying architecture considers account boundaries, DTO safety, storage abstraction, and future product expansion.

### On AI Integration

The AI feature is not just a chatbot. It is tied to industrial assets, document retrieval, source citations, feedback loops, and maintenance workflows. The emphasis is on practical decision support with traceability.

### On Product Judgment

The MVP intentionally avoids becoming a full CMMS. The focus is machine knowledge, troubleshooting, cited answers, and maintenance issue history. That keeps the product focused while still leaving room for integrations later.

### On Engineering Discipline

Completed slices are verified through backend builds, automated tests, frontend builds, and diff checks. The implementation log captures what changed, what was preserved, and how the work was verified.

## Questions I Can Answer in an Interview

- How is tenant context resolved and protected?
- Why did I choose a modular monolith instead of microservices?
- How are assets, documents, chunks, citations, chat messages, and issues related?
- How does the AI/RAG flow work?
- How does the system prevent source citations from becoming generic or untraceable?
- Why separate answer feedback from citation feedback?
- How would this evolve into a production SaaS deployment on Azure?
- How would document ingestion and embeddings scale over time?
- What parts would need more hardening before onboarding real customers?
- What would I build next?

## Areas Still In Progress

Tenzin MaintenanceIQ is actively being built. Current and future areas include:

- Document ingestion hardening
- Embedding/search quality improvements
- More complete machine component modeling
- Program-load and disaster-recovery repository support
- Azure release process
- Production observability
- Billing and subscription management
- Admin and account-management workflows
- More polished UI/UX
- Expanded screenshot and demo data coverage

## How to Explain the Private Source Code

Use this phrasing:

> The source code is private because this is an active product, not a throwaway portfolio app. I created the public repository as a technical case study so reviewers can still see the architecture, domain model, API boundaries, AI/RAG flow, security decisions, implementation history, verification approach, and screenshots without exposing proprietary implementation details.

## Short Closing Pitch

Tenzin MaintenanceIQ demonstrates my ability to design and build a real SaaS-style application across backend, frontend, data modeling, AI integration, security boundaries, and product workflows. The public repo is intentionally documentation-first because the source is private, but it reflects the actual system architecture and implementation decisions behind the product.