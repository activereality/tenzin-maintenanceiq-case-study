# ADR 0004 — Citation-First AI Responses

## Status

Accepted

## Context

Industrial troubleshooting requires trust. Generic AI answers without references can be misleading or unsafe. Users need to see which manual, document, or reference supported an answer.

## Decision

Treat citations as a first-class part of AI-assisted answers.

## Consequences

Benefits:

- Improves user trust
- Makes answers auditable
- Encourages document-grounded workflows
- Supports future feedback and quality analytics

Tradeoffs:

- Retrieval and answer-generation logic is more complex
- UI must make citations easy to inspect
- Poor document quality can still produce weak answers, so feedback loops are important
