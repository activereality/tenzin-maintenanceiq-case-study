# 03 — Sanitized Domain Model

This document shows the public, sanitized shape of the domain model. It is intentionally not a generated schema and does not expose production source code.

## Core entity map

```text
Tenant / Account
 ├── User
 ├── Asset
 │    ├── MachineComponent
 │    ├── Document
 │    │    ├── DocumentPage
 │    │    ├── DocumentChunk
 │    │    └── DocumentEmbedding
 │    ├── Issue
 │    │    ├── IssueEvent
 │    │    └── IssueAttachment
 │    └── ProgramLoadArtifact
 ├── ChatSession
 │    ├── ChatMessage
 │    └── AnswerCitation
 └── Feedback
      ├── AnswerFeedback
      └── CitationFeedback
```

## Asset / machine

The asset is the central context object. Machine documentation, machine components, chat sessions, citations, issues, and future disaster-recovery files should all relate back to the machine where possible.

Important design considerations:

- Asset numbers are unique per tenant/account.
- Public identifiers can support QR lookup without exposing internal database IDs.
- Asset detail pages should become the main operational entry point for technicians.

## Documents

Documents are uploaded references associated with an asset/machine. The private implementation models document content in pages and chunks to support search and cited AI answers.

Important design considerations:

- Public DTOs do not expose internal storage paths.
- Document chunks are internal retrieval artifacts, not normal user-facing objects.
- Citations should point users back to trusted source material.

## Issues and timeline

MaintenanceIQ issues capture troubleshooting context and preserve what happened over time. Timeline events are used to represent meaningful issue activity such as creation, updates, attachment archival, and system-generated activity.

Important design considerations:

- Timeline responses use safe actor display names.
- System and unknown actors have fallback labels.
- Internal user IDs are not exposed through public timeline DTOs.

## Feedback

Feedback is split between answer-level and citation-level concepts.

Answer feedback examples:

- Helpful
- Unhelpful

Citation feedback examples:

- Selected helpful reference
- Wrong source
- Outdated document

Missing-information feedback is treated carefully and can be deferred or rejected depending on whether the workflow has enough context to store it safely.
