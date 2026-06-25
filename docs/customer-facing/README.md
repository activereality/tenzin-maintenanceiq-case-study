# Customer-Facing Collateral

This folder contains public-facing collateral drafts for Tenzin MaintenanceIQ. Keep claims practical, source-traceable, and aligned with the public technical case study.

- [Tenzin MaintenanceIQ One-Page Overview](tenzin-one-page-overview.md) - customer-facing overview for plant, maintenance, reliability, operations, and technical decision makers.
- [Pilot Discovery Questions](pilot-discovery-questions.md) - discovery guide for shaping facility scope, documents, pain points, security concerns, and success metrics.
- [Demo Script](demo-script.md) - lightweight customer walkthrough for showing documentation upload, plain-language questions, cited answers, source opening, feedback, and data boundaries.
- [Pilot Success Criteria](pilot-success-criteria.md) - validation goals for deciding whether to expand, revise, pause, or stop a pilot.

## Sendable PDFs

The Markdown files above remain the source of truth. The PDFs are generated artifacts for sending as customer or pilot attachments.

- [Tenzin MaintenanceIQ One-Page Overview PDF](pdf/tenzin-maintenanceiq-one-page-overview.pdf)
- [Tenzin MaintenanceIQ Pilot Collateral Packet PDF](pdf/tenzin-maintenanceiq-pilot-collateral-packet.pdf)

Regenerate the PDFs from the repository root with Python and ReportLab available:

```powershell
python scripts/export-customer-collateral-pdfs.py
```
