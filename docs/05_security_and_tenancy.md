# 05 — Security and Tenancy Notes

## Tenancy principle

Tenant/account context should be resolved server-side and fail-closed. Public clients should not be trusted to choose or enforce tenant isolation.

## Public naming

The public application uses account-facing language where practical. For example, account identifiers can be exposed as `AccountId` in public responses rather than teaching users or client code to think in database-level tenant terminology.

## DTO safety rules

Public DTOs should avoid exposing:

- Internal database identifiers where not needed
- Tenant IDs where account-facing concepts are sufficient
- CreatedByUserId or other internal actor IDs
- Raw storage paths
- Blob/container implementation details
- Temporary passwords outside narrowly scoped admin-create flows
- Internal enum values that should not be part of the public contract

## Attachment access

Attachments should be viewed or downloaded through authorized endpoints. The API, not the client, decides whether the current user can access the file.

## Delete behavior

The implementation favors restricted foreign-key deletes and soft-delete filters where appropriate. This reduces accidental destructive behavior and helps preserve auditability.

## Auth response hardening

A recent implementation slice focused on reducing unnecessary identifier exposure in auth/session responses. The public auth response no longer exposes user identifiers that are not needed by the client, and account terminology is preferred for public response naming.

## Timeline actor safety

Issue timeline responses use display-safe actor names. System and unknown actors have explicit fallback labels so the UI can remain helpful without exposing internal user IDs.
