# AI / RAG Citation Flow

This diagram shows the simplified flow for machine-specific AI answers with citations.

```mermaid
sequenceDiagram
    participant User as Maintenance User
    participant Web as Angular Web App
    participant API as ASP.NET Core API
    participant Search as Document Search
    participant DB as PostgreSQL
    participant AI as AI Provider

    User->>Web: Ask machine-specific question
    Web->>API: Submit chat message
    API->>Search: Search tenant/asset-scoped document chunks
    Search->>DB: Retrieve relevant chunks and metadata
    DB-->>Search: Matching document context
    Search-->>API: Ranked context with source metadata
    API->>AI: Generate answer using retrieved context
    AI-->>API: Return answer draft
    API->>DB: Save chat message and citations
    API-->>Web: Return answer with citations
    Web-->>User: Display answer and cited references
```

## Notes

The design goal is not just to generate an answer. The goal is to return an answer that can be traced back to source documentation.

This supports maintenance teams that need practical troubleshooting help while still being able to verify the source material behind the response.