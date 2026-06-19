# 09 — Verification

## Verification gates

The private implementation uses the following verification gates after meaningful slices:

```bash
dotnet build
dotnet test
npm run build
git diff --check
```

## Current test discipline

The backend has an active automated test suite. Recent private checkpoints have passed hundreds of tests along with backend and frontend builds.

## What the gates cover

| Gate | Purpose |
| --- | --- |
| `dotnet build` | Confirms backend compilation and project references |
| `dotnet test` | Confirms application/domain behavior and regression coverage |
| `npm run build` | Confirms Angular compilation, templates, types, and production build safety |
| `git diff --check` | Catches whitespace and patch hygiene issues before commit |

## Manual smoke areas

Manual checks are used when UI behavior or workflow state is difficult to validate fully through automated tests.

Examples:

- Issue detail view loads correctly
- Attachment expand/collapse behaves correctly
- Read-only controls are hidden/disabled appropriately
- Timeline refreshes after archive behavior
- Chat answer citations render clearly

## Release mindset

The product is still pre-release, so verification currently emphasizes build correctness, regression tests, API/DTO safety, and workflow integrity before broader deployment automation.
