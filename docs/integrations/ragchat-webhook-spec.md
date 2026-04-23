# RagChat / Humatic AI — Webhook Lead Integration Spec

## What RagChat sends

`POST {webhook_url}` with `Content-Type: application/json`

### Headers

- `Authorization: Bearer {secret}` (if configured, otherwise omitted)

### Body

```json
{
  "event": "lead_created",
  "lead": {
    "id":               "uuid-string",
    "name":             "John Smith",
    "email":            "john@example.com",
    "phone":            "+357 99 123456",
    "notes":            "Looking for 2-bed apartment in Limassol, budget €200k",
    "source":           "chat",
    "thread_id":        "thread-uuid",
    "user_id":          "visitor-uuid",
    "api_key_id":       "apikey-uuid",
    "visitor_ip":       "203.0.113.42",
    "visitor_country":  "CY",
    "visitor_city":     "Limassol",
    "transcript":       "Visitor: Hi, I'm looking for...\nAssistant: ...",
    "language":         "en",
    "created_at":       "2026-03-19T12:00:00+00:00"
  }
}
```

### Field availability

| Field | Always present | Can be null/empty |
|---|---|---|
| `id` | Yes | No — internal UUID |
| `name` | Yes | No — always collected |
| `email` | Yes | **Yes** — null if only phone collected |
| `phone` | Yes | **Yes** — null if only email collected |
| `notes` | Yes | **Yes** — conversation summary, may be empty |
| `source` | Yes | No — always `"chat"` |
| `thread_id` | Yes | **Yes** |
| `user_id` | Yes | **Yes** |
| `api_key_id` | Yes | **Yes** |
| `visitor_ip` | Yes | **Yes** |
| `visitor_country` | Yes | **Yes** — ISO 2-letter code |
| `visitor_city` | Yes | **Yes** |
| `transcript` | Yes | **Yes** — full chat log, may be absent |
| `language` | Yes | **Yes** — detected from transcript |
| `created_at` | Yes | No — ISO 8601 UTC |

**Not sent** (receiver must handle internally):
- `assigned_to` / owner
- Deal stage, pipeline, priority
- Any CRM-specific fields

## What RagChat expects back

### Success (HTTP 2xx)

Return JSON with the created record's ID in any of these fields:

```json
{ "id": "123" }
```
or
```json
{ "deal_id": "123" }
```
or
```json
{ "lead_id": "123" }
```

RagChat stores this as `crm_remote_id`, shown in the Leads table as "Sent #123".
If no ID is returned, the lead is still marked as "Sent" but without a reference number.

### Failure (HTTP 4xx/5xx)

Return optional JSON error:

```json
{ "error": "Description of what went wrong" }
```

RagChat marks the lead as "Failed" and stores the error message for display and retry.

## Matrix Pipeline implementation

- **Edge Function:** `lead-webhook` on `tiuansahlsgautkjsajk` (Sharp Matrix Sandbox — hosts this ad-hoc integration; the Matrix Pipeline production DB is `mydojctcewxrbwjckuyz`)
- **Auth:** Bearer token matched against `app_settings.leads_integration.webhook_secret`
- **Settings UI:** Matrix Pipeline → Settings → Leads Integration tab
- **Creates:** Contact (crm_contacts) + Lead (leads) + Deal (deals) + deal_contacts link
- **Response:** `{ "success": true, "id": "deal-uuid", "deal_id": "deal-uuid", ... }`
