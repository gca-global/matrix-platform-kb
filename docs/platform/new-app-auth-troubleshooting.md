# New App Auth Troubleshooting Guide

> When a newly registered Matrix app cannot authenticate users via SSO,
> work through the checklist below in order. Each section covers one
> failure mode with its symptoms, root cause, and fix.

## Prerequisites

- App registered in SSO Console (`https://intranet.sharpsir.group/console/iam/apps`)
- `CLIENT_ID` set in the app's `src/lib/matrix-sso.ts`
- Redirect URIs configured (Lovable custom name + project UUID)

---

## 1. `401 invalid_client` — Client ID Mismatch

### Symptoms

- Browser console: `oauth-authorize?client_id=... 401 (Unauthorized)`
- Response body: `{"error":"invalid_client","error_description":"Invalid client_id"}`
- Happens immediately on app load (before login form appears)

### Root Cause

The `CLIENT_ID` in the app's `matrix-sso.ts` does not exactly match the
`client_id` column in the `sso_applications` table. Common causes:

- **Special characters dropped or altered** — client IDs are auto-generated
  and may contain dots (`.`), underscores (`_`), tildes (`~`), or hyphens (`-`).
  Copy-paste from the SSO Console's "full data view" mode, not the friendly view.
- **Whitespace or invisible characters** — trailing space or newline after paste.
- **App not yet saved** — the SSO Console "Edit Application" dialog was open but
  "Save Changes" was never clicked.
- **`is_active` is false** — the query filters on `is_active = true`.

### How to Verify

Query the database directly:

```bash
curl -s "https://xgubaguglsnokjyudgvc.supabase.co/rest/v1/sso_applications?client_id=eq.<YOUR_CLIENT_ID>&select=client_id,is_active,app_title" \
  -H "apikey: <SERVICE_ROLE_KEY>" \
  -H "Authorization: Bearer <SERVICE_ROLE_KEY>"
```

- Empty array `[]` → client_id not found or `is_active` is false.
- Non-empty → client_id is registered; problem is elsewhere (skip to section 2).

### Fix

1. Open SSO Console → Applications → your app → toggle to **Full** data view.
2. Copy the exact `client_id` value.
3. Paste into `src/lib/matrix-sso.ts` as the `CLIENT_ID` constant.
4. Ensure the Lovable preview rebuilds (watch for the green ready indicator).
5. **Hard-reload** the preview (Ctrl+Shift+R) to pick up the new bundle.

---

## 2. `401 invalid_token` — Stale Supabase Session

### Symptoms

- Browser console: `oauth-authorize?client_id=... 401 (Unauthorized)`
- Response body: `{"error":"invalid_token","error_description":"invalid JWT: ..."}`
- SSO login page shows **"Signing in..."** spinner but never completes.
- Network tab shows **pairs of requests** to `oauth-authorize` (OPTIONS preflight +
  GET), confirming an `Authorization` header is being sent.

### Root Cause

The SSO login page (`intranet.sharpsir.group/sso-login/`) shares the Supabase
SSO instance with all Matrix apps. It stores the Supabase session in
`localStorage` under the key `sb-xgubaguglsnokjyudgvc-auth-token`.

If the user previously logged in to any Matrix app from the same browser, the
SSO login page finds this session and tries to auto-complete the OAuth flow
without prompting for credentials. If the session token has expired, the call to
`oauth-authorize` with the stale `Authorization: Bearer <expired_token>` returns
`401 invalid_token`.

The `oauth-authorize` function validates tokens at line 328-335:

```
Authorization header present → extract Bearer token → getUserFromToken()
  → token valid: proceed to generate auth code
  → token invalid/expired: return 401 invalid_token
```

### How to Verify

Test the same URL with and without an Authorization header:

```bash
# Without auth header → should return 302 (redirect to login)
curl -s -o /dev/null -w "%{http_code}" \
  "https://xgubaguglsnokjyudgvc.supabase.co/functions/v1/oauth-authorize?client_id=<ID>&redirect_uri=<URI>&response_type=code&scope=openid+profile+email&state=test&code_challenge=abc&code_challenge_method=S256"

# With invalid auth header → returns 401
curl -s \
  "https://xgubaguglsnokjyudgvc.supabase.co/functions/v1/oauth-authorize?client_id=<ID>&redirect_uri=<URI>&response_type=code&scope=openid+profile+email&state=test&code_challenge=abc&code_challenge_method=S256" \
  -H "Authorization: Bearer some_expired_token"
```

If the first returns 302 and the second returns 401, the issue is the stale token.

### Fix

1. Open DevTools → **Application** tab → **Local Storage**.
2. Select the `https://intranet.sharpsir.group` origin.
3. Delete the `sb-xgubaguglsnokjyudgvc-auth-token` entry (or clear all).
4. If testing in Lovable preview, also check the app's preview origin
   (`id-preview--<uuid>.lovable.app`) and clear any `sb-` entries there.
5. Hard-reload (Ctrl+Shift+R).

The SSO login page will now do a fresh Azure AD login instead of reusing the
expired session.

---

## 3. `400 invalid_request` — Redirect URI Mismatch

### Symptoms

- Response body: `{"error":"invalid_request","error_description":"Invalid redirect_uri"}`
- Status code: 400 (not 401)

### Root Cause

The `redirect_uri` sent by the app does not match any entry in the
`redirect_uris` array stored in `sso_applications`.

Lovable apps have four standard redirect URIs that should be registered:

| Pattern | Example |
|---------|---------|
| `https://<custom-name>.lovable.app/auth/callback` | `https://matrix-people-access.lovable.app/auth/callback` |
| `https://preview--<custom-name>.lovable.app/auth/callback` | `https://preview--matrix-people-access.lovable.app/auth/callback` |
| `https://<uuid>.lovableproject.com/auth/callback` | `https://210fc609-...lovableproject.com/auth/callback` |
| `https://id-preview--<uuid>.lovable.app/auth/callback` | `https://id-preview--210fc609-...lovable.app/auth/callback` |

### How to Verify

Check the Network tab → Payload → `redirect_uri` value, then compare against
the registered URIs in the SSO Console.

### Fix

Add the missing redirect URI in SSO Console → Edit Application → redirect URIs,
then save.

---

## 4. `403 access_denied` — No User Permissions

### Symptoms

- Login completes, Azure AD auth succeeds, but final redirect fails.
- Response body: `{"error":"access_denied","error_description":"User does not have access to this application"}`
- Status code: 403

### Root Cause

The `oauth-authorize` function checks user permissions after token validation.
Access is granted if the user has `rw_global`, `rw_org`, or `rw_own` permissions,
OR if default permission settings are configured in `admin_settings`.

New users with no explicit permissions AND no default settings configured
will be denied.

### Fix

Either:
- Assign the user a role/permission in SSO Console → Users → Edit User.
- Or configure default user assignment in SSO Console → Settings →
  Default User Assignment (sets `default_permission_type` so new users
  get baseline access).

---

## 5. Lovable Preview-Specific Issues

### Preview not picking up code changes

- **Symptom**: Fixed `CLIENT_ID` in code but 401 persists.
- **Cause**: Old JS bundle cached, or Lovable hasn't rebuilt yet.
- **Fix**: Wait for Lovable rebuild indicator, then Ctrl+Shift+R.
- **Verify**: Check deployed bundle — the published app at
  `https://<custom-name>.lovable.app/` may already have the fix while
  the preview lags behind.

### SSO login page in iframe loses context

- **Symptom**: SSO login shows but Azure AD redirect fails or loops.
- **Cause**: Third-party cookie restrictions block the Supabase session
  in the SSO login iframe.
- **Fix**: Test on the published URL (`*.lovable.app`) in a new tab
  instead of the Lovable editor preview.

---

## Quick Diagnostic Flowchart

```
App calls oauth-authorize → what HTTP status?
│
├─ 401 → Check response body:
│  ├─ "invalid_client" → Section 1 (client_id mismatch)
│  └─ "invalid_token"  → Section 2 (stale session)
│
├─ 400 → "invalid_request" → Section 3 (redirect_uri mismatch)
│
├─ 403 → "access_denied" → Section 4 (no permissions)
│
├─ 302 → Working correctly (redirects to SSO login)
│
└─ 500 → Server error; check Supabase Edge Function logs
```

---

## Relevant Source Files

| File | Purpose |
|------|---------|
| `supabase/functions/oauth-authorize/index.ts` | Authorization endpoint (client lookup, token validation, permission check) |
| `supabase/functions/oauth-token/index.ts` | Token exchange endpoint |
| `supabase/migrations/001_sso_schema.sql` | `sso_applications` table definition |
| `src/lib/matrix-sso.ts` (in each app) | Client-side OAuth configuration (`CLIENT_ID`, `BASE_PATH`) |

> **Source repo**: `/home/bitnami/matrix-platform-foundation`
