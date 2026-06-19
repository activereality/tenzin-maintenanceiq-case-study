# Domain Model

This diagram shows a simplified, sanitized version of the main domain relationships.

```mermaid
erDiagram
    TENANT ||--o{ USER : has
    TENANT ||--o{ ASSET : owns

    ASSET ||--o{ MACHINE_COMPONENT : contains
    ASSET ||--o{ DOCUMENT : has
    ASSET ||--o{ ISSUE : tracks

    DOCUMENT ||--o{ DOCUMENT_PAGE : contains
    DOCUMENT_PAGE ||--o{ DOCUMENT_CHUNK : split_into
    DOCUMENT_CHUNK ||--o{ DOCUMENT_EMBEDDING : indexed_by

    ISSUE ||--o{ ISSUE_EVENT : records
    ISSUE ||--o{ ISSUE_ATTACHMENT : includes

    CHAT_SESSION ||--o{ CHAT_MESSAGE : contains
    CHAT_MESSAGE ||--o{ ANSWER_CITATION : cites
    ANSWER_CITATION }o--|| DOCUMENT_CHUNK : references

    CHAT_MESSAGE ||--o{ ANSWER_FEEDBACK : receives
    ANSWER_CITATION ||--o{ CITATION_FEEDBACK : receives
```

## Notes

The platform centers on industrial assets and machine-specific knowledge.

Core areas include:

- Tenants and users
- Assets and machine components
- Documents, pages, chunks, and embeddings
- Chat sessions, messages, and citations
- Maintenance issues, timelines, and attachments
- Answer-level and citation-level feedback

The actual production schema and source code are private. This diagram intentionally presents a simplified public model.