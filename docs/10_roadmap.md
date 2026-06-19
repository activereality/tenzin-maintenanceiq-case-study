# 10 — Roadmap

## Near-term focus

- Strengthen machine profile as the central AI assistance context
- Continue MaintenanceIQ issue workflow development
- Improve document ingestion and citation UX
- Expand feedback analytics
- Add public identifier / QR machine lookup workflow
- Continue DTO, tenancy, and permission hardening

## Product foundation

The MVP should continue to prioritize:

- Asset/machine context
- Components
- Documents
- Search and embeddings
- Chat and citations
- Feedback
- Issues and timeline
- Attachment handling
- Program-load repository planning

## Future product areas

### Program loads and disaster recovery

Tenzin should eventually house program backups for machine components such as PLCs, HMIs, VFDs, robot controllers, and related automation devices. This can become a disaster recovery repository tied directly to each machine profile.

### Azure release process

The product will need a production-ready Azure release process. Initial deployment can remain simple, but the path should mature toward repeatable CI/CD, environment-specific configuration, secrets handling, database migration discipline, and smoke checks.

### Facility knowledge graph

Over time, the asset/component/document/issue model can support a richer machine knowledge graph that helps users move from symptom to source document to component to prior issue.
