# Gameday: North Andover booking (Lobbie) URL — 2026-05-14

**Microsite:** https://gamedaymenshealth.com/north-andover-ma

**Target Lobbie self-scheduling URL (apply this):**  
https://my.lobbie.com/patient/scheduling?accountPublicUuid=f7af85e8-5012-47f7-9346-0b2cd10e929a&selfSchedulingSettingPublicUuid=10e80074-e0cb-4abe-9064-b9a4b5a612fb

## Where to change it (from internal notes)

Per Ignite handover (`meetings/notes/2026-05-06-gameday-web-architecture-diagram.md`, `meetings/notes/2026-05-05-ignite-gameday-website-handover.md`, `context/gameday-architecture-attention.md`):

1. **Live locations:** **Yext** is described as the **source of truth** for live clinic entities. Updates flow **Yext → webhook → field mapper → Webflow CMS item → publish → D1** (Cloudflare Worker reads D1 for routing and dynamic behavior).
2. **Practical order:** Find the **North Andover** record in **Webflow CMS** (location or clinic collection) and see which field drives the primary **Book** / **Schedule** CTA. If that field is **synced from Yext**, change the value in **Yext** on the location entity (matching field in the Yext-to-Webflow mapper) so the next sync does not overwrite a Webflow-only edit.
3. **“Coming soon” only in Webflow:** Notes call out clinics that exist **only in Webflow** until promoted; North Andover is live in Yext-style terms, so assume **Yext + Webflow** alignment unless Ignite’s mapper says otherwise.

**Owner to execute:** Web delivery (**Anthony** with Webflow access); confirm with Ignite or Gameday if the booking URL field is **Yext-owned** vs **Webflow-only** for this brand.

## Status

- [ ] URL updated in the correct system (Yext and/or Webflow) and site published so production shows the new Lobbie link.
