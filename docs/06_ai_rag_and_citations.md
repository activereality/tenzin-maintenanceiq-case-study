# 06 — AI, RAG, and Citations

## AI product principle

The AI assistant should not behave like a generic chatbot. It should answer within the context of the selected machine, cite the documentation it used, and make it easy for technicians to identify whether the response was useful.

## Retrieval flow

```text
User question
   |
   v
Asset / machine context
   |
   v
Relevant document chunks
   |
   v
AI provider abstraction
   |
   v
Answer + citations
   |
   v
Feedback capture
```

## Document processing model

Uploaded documents are modeled as source documents with pages and chunks. Chunks are retrieval units used to locate relevant information for an answer. Embeddings support semantic matching against the user's question and machine context.

## Citation-first answers

Citations are a first-class product requirement. A useful answer should show where it came from, especially in industrial troubleshooting contexts where incorrect or uncited advice can waste time or create risk.

## Feedback boundaries

Answer-level feedback and citation-level feedback are intentionally separate.

Answer feedback is about the overall usefulness of the answer:

- Helpful
- Unhelpful

Citation feedback is about the quality of a specific reference:

- Selected helpful reference
- Wrong source
- Outdated document

This separation keeps analytics cleaner and prevents unrelated feedback types from being stored in the wrong context.

## Provider abstraction

The AI provider integration is kept behind an application-facing abstraction so the product workflow does not become tightly coupled to one model or vendor. The application should own the concepts of asset context, retrieved evidence, answer construction, citations, and feedback. The model provider should remain replaceable infrastructure.
