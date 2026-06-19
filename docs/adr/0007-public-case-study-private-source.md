# ADR 0007 — Public Case Study, Private Source Code

## Status

Accepted

## Context

The Tenzin production codebase is an active commercial product build. Publishing source code could expose intellectual property, implementation details, and security-sensitive patterns.

At the same time, a public artifact is useful for portfolio conversations, recruiter outreach, and technical interviews.

## Decision

Publish a public technical case-study repository while keeping production source code private.

## Consequences

Benefits:

- Demonstrates engineering ownership and architectural depth
- Protects active product IP
- Avoids publishing secrets, private implementation details, or security-sensitive code
- Provides a professional artifact for employers

Tradeoffs:

- Reviewers cannot inspect exact implementation code
- The repo must be maintained so it does not become stale marketing material
