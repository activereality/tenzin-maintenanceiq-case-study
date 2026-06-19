# ADR 0005 — Separate Answer Feedback from Citation Feedback

## Status

Accepted

## Context

Users can have different opinions about an answer and its supporting references. An answer may be useful while one citation is weak, or a citation may be relevant while the generated summary is not helpful.

## Decision

Model answer feedback and citation feedback as separate concepts with separate allowed feedback types.

## Consequences

Benefits:

- Cleaner analytics
- Better validation
- More precise product improvement signals
- Reduced ambiguity in feedback storage

Tradeoffs:

- Slightly more frontend and backend complexity
- Requires clear UI labels so users understand what they are rating
