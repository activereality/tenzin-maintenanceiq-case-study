# 04 — Example API Surface

This is a sanitized view of the product's API areas. It is intended to show backend design and product boundaries without exposing implementation source code.

## Health

```http
GET /api/v1/health
```

Used for basic deployment and runtime verification.

## Auth / account context

```http
POST /api/v1/auth/login
GET  /api/v1/auth/session
```

Public responses use account-facing terminology where possible. Internal tenant resolution remains server-side.

## Assets / machines

```http
GET    /api/v1/assets
POST   /api/v1/assets
GET    /api/v1/assets/{assetId}
PATCH  /api/v1/assets/{assetId}
```

Assets are the central context for maintenance knowledge.

## Documents

```http
GET    /api/v1/assets/{assetId}/documents
POST   /api/v1/assets/{assetId}/documents
GET    /api/v1/documents/{documentId}
GET    /api/v1/documents/{documentId}/download
```

Document access is mediated through API endpoints. Public responses should not expose internal storage paths.

## Chat / AI assistance

```http
POST   /api/v1/chat/sessions
GET    /api/v1/chat/sessions/{sessionId}
POST   /api/v1/chat/sessions/{sessionId}/messages
```

Chat workflows are designed to support cited answers grounded in retrieved machine documentation.

## Feedback

```http
POST   /api/v1/feedback/answers
POST   /api/v1/feedback/citations
```

Answer feedback and citation feedback are handled separately so validation and analytics remain clean.

## MaintenanceIQ issues

```http
GET    /api/v1/assets/{assetId}/issues
POST   /api/v1/assets/{assetId}/issues
GET    /api/v1/issues/{issueId}
PATCH  /api/v1/issues/{issueId}
GET    /api/v1/issues/{issueId}/timeline
```

Issues are asset-scoped. The product deliberately avoids a global issues page in the MVP so machine context remains central.

## Issue attachments

```http
GET    /api/v1/issues/{issueId}/attachments
POST   /api/v1/issues/{issueId}/attachments
GET    /api/v1/issues/{issueId}/attachments/{attachmentId}/view
GET    /api/v1/issues/{issueId}/attachments/{attachmentId}/download
POST   /api/v1/issues/{issueId}/attachments/{attachmentId}/archive
```

Read-only users may view/download when allowed, while edit/archive actions remain guarded.
