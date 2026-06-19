# 07 — MaintenanceIQ Workflows

## Workflow goal

MaintenanceIQ is the issue-capture and troubleshooting-memory layer of Tenzin. It is intended to help teams preserve what happened on a machine, what was tried, what documents were relevant, and what evidence supported the final resolution.

## Asset-scoped issues

Issues are intentionally scoped to assets/machines. This avoids turning the MVP into a generic ticketing system and keeps machine knowledge at the center of the product.

## Timeline foundation

Issue timeline events represent meaningful issue activity. The timeline is designed to show a safe, readable history to users while keeping internal identifiers and storage details out of the public API.

Example event categories:

- Issue created
- Issue updated
- Attachment added
- Attachment archived
- System activity

## Attachment workflow

Issue attachments are shown within the issue view and are collapsed by default to reduce visual noise. Users can expand or hide attachments as needed.

Read-only behavior matters:

- Read-only users can view/download allowed attachments.
- Edit/archive actions remain guarded.
- UI controls respect permission state.

## Frontend behavior polish

Recent frontend slices improved state cleanup and presentation:

- Attachments collapse by default.
- Attachment state resets on issue change.
- Archive-in-progress flags clean up correctly.
- Empty states are user-friendly.
- Read-only guards are enforced in the UI.

## Product boundary

The MVP should avoid a global issues page and should avoid adding issue timelines directly to unrelated asset detail areas until the asset-scoped workflow is ready. This preserves product clarity and reduces accidental scope creep.
