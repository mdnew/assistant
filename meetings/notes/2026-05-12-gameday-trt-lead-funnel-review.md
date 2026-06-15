> **Source:** `gameday/meeting-notes/2026-05-12-trt-lead-funnel-review.md` (synced 2026-06-02)

# Review TRT lead funnel

**Date:** 2026-05-12  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)

## Participants

**Game Day / Uptech:** Matthew New, Russell Cloak, Anthony Castelli

**Referenced:** Blaine (sponsor / scope decisions), **Grafted** (partner named in notes for Braze triggers—**verify**; may be **Gravy** or another vendor spelling), compliance team, media buying agency, Ignite/AWS contacts (secrets / GHL IDs)

## Summary

The group reviewed a **multi-step TRT lead funnel** (wizard-style flow, optional **virtual care** via query params like `virtual_care=true`, **edge score quiz**, zip-based clinic matching, Lobby handoff for booking). Major themes: **funnel tracking** vs **nav leakage**, **when to capture email** if early steps are skipped, **attribution / match source** propagation to **Braze** and **Go High Level (GHL)**, and **heavy operational complexity** from **non-standard GHL** pipelines and **location → sub-account → token** mappings (often tied to **AWS Secrets Manager** per prior architecture).

**Strategic tension:** The build may be **re-implementing GHL-native** (or LP-tool) capabilities mostly for **UX/branding**, with **multi-month / budget-risk** scope. The team aligned on **challenging viability**, preparing **questions and a boxes-and-arrows plan** for **Blaine**, and a **scheduled discussion** (notes: **tomorrow 2:00 PM**—**confirm date** against calendar).

**Technical conclusions:** **GHL remains SoT** for franchise lead ops; a **backend API** is likely required for **routing**, secrets-backed **GHL location tokens**, zip/geo matching (possibly sourcing **lat/lon, Yext ID, GHL ID** from **Cloudflare D1**), and **server-side** conversion/analytics hooks. **Terraform / AWS (EC2/K8s)** raised as realistic complexity if hosting a new service. **Open compliance** items: pre-checked consent language (**“ECPA” in notes—likely TCPA-related; verify**), and whether “no PHI” claims hold given names/appointments.

## Product / UX (funnel design)

| Topic | Notes |
|--------|--------|
| Entry / gating | Virtual care path only when routing logic sends users there (not organic discovery). |
| Steps | “Step zero” hero + testimonials → quiz / data capture → clinic pairing (**edge score quiz**); quiz skippable if **zip** in URL or **multiple clinic IDs** for disambiguation. |
| Matching | Zip → nearest clinic (centroid + distance; zip-to-lat/lon lookup historically); unique IDs (e.g. `Plano` vs `Plano-0123`) vs messy cross-system naming. |
| Virtual care fallback | Zip outside coverage → virtual care path; FE must record **match source** (URL param, zip, manual, virtual fallback) for Braze + GHL. |
| Nav | Option to **hide nav** after step one to reduce **paid-traffic leakage**. |
| Forms | Confirm required fields per step; if step 1 skipped via zip, still need **email** capture timing (debate: capture email earlier on abandon risk). |
| UX patterns | Single-select **auto-advance** vs forced timed submit—tradeoffs called out. |
| Booking | CTA → **Lobby** page for scheduling; booking confirmation via **Lobby appointment-created webhook** feeding Braze + GHL (phase 2 wiring). |
| Lobby | Open question: **query param prefill** on Lobby scheduling page. |
| Duplicates | Business rule TBD: update vs new contact on repeat email within **24h**. |

## Integrations and data

| System | Role |
|--------|------|
| **Braze** | Create/update contact with attributes + quiz payload; fire **`lead submitted`** (exact event TBD); workflows—**split ownership with “Grafted”** per notes (**verify**). |
| **GHL** | SoT for local sales/SMS; lead into **correct sub-account**; place in **`new lead`** stage—**pipeline IDs vary by location** → needs mapping table. |
| **D1** | Candidate SoT for **location records** (lat/lon, Yext id, GHL id, booking links) vs Webflow-only assumptions. |
| **Secrets** | GHL **location ID / PIT or access token** patterns—Anthony to confirm storage/contact (**ping** owner). |
| **Ads / CAPI** | Russell: **media agency** should own **GA4, Meta CAPI, Google enhanced conversions** config unless dev only supplies per-clinic URLs. |

## Build / ops concerns

- **New clinic onboarding:** Update clinic metadata, GHL creds in **one config**, refresh **service-area zip** table; table should be **geo-agnostic** (not TX-hardcoded) and **editable by non-engineers** (CMS or admin UI).
- **Backend:** API for zip/geo → location → secret → GHL submit; not “React-only SPA.”
- **IaC:** Terraform + AWS (EC2/K8s) mentioned; Russell to check existing **Terraform in GitHub**.
- **Anthony estimate:** **Phase 1 ~75%** of total scope (per notes).
- **Process:** Matthew frustrated by being asked to validate an **API spec not yet provided**; group noted **organizational disarray** slowing execution.

## Compliance / privacy (flags)

- Edge score framed as **not a medical screen** (per discussion—**legal should confirm**).
- **Pre-checked consent** needs **compliance** sign-off (**ECPA** wording in notes—**verify** statute/regime).
- Skepticism that **no PHI** in funnel/Braze/GHL is strictly true if **patient names** / **appointment counts** appear—**compliance review**.

## Action items

| Owner | Action |
|--------|--------|
| Russell Cloak, Anthony Castelli | **Plan:** questions for **Blaine**, answers before **Friday**; **high-level boxes-and-arrows** + **rough timelines**. |
| Matthew New | **Schedule** meeting with **Blaine** (**tomorrow 2:00 PM** in notes—**verify** on calendar) on **whether to rebuild** GHL-equivalent functionality vs simpler path. |
| Russell Cloak, Anthony Castelli | **Draft** full **question/comment list** on the project doc for Blaine. |
| Anthony Castelli | **Ping** contact on **where GHL IDs/secrets** live; confirm data needed to build. |
| Russell Cloak | **Comment** on doc: how to determine **sales pipeline step** for new users when pipelines differ/absent. |
| Russell Cloak | **Confirm** “API requirements” email accuracy vs current work (**by tomorrow** per notes). |

## Detailed themes (indexed outline)

1. Virtual care URL params; branching vs multiple LPs.  
2. Funnel identity gating; skip logic via zip / clinic IDs.  
3. Nav leakage and funnel analytics.  
4. Hero, testimonials, quiz, clinic matching, timeline intent, contact fields.  
5. Email capture timing across skipped steps; Lobby handoff.  
6. Auto-advance UX concerns.  
7. Clinic ID standardization gap (GHL vs Lobby vs marketing URLs).  
8. Zip centroid matching; lat/lon tables.  
9. Virtual fallback + match-source tracking.  
10. Budget/timeline risk; Blaine meeting.  
11. Braze attributes + events; partner responsibilities.  
12. GHL sub-accounts, pipelines, secrets mapping scalability.  
13. Onboarding + editable zip service areas.  
14. Rebuild vs GHL/Unbounce positioning.  
15. Token lookup security model (odd but workable per notes).  
16. API server necessity; Terraform/K8s complexity.  
17. GHL SoT vs Braze sync gap for partial funnel abandoners.  
18. Virtual care account model (tags vs sub-accounts).  
19. Lobby webhook back to Braze/GHL.  
20. API sufficiency frustration; iOS 14.5+ server-side measurement context.  
21. Compliance: quiz, consent checkbox, PHI claims.  
22. Duplicate rules; hosting domain vs persistent nav links.  
23. Phase 2: Lobby prefill + webhook wiring; agency owns ad pixels/CAPI.  
24. Meeting prep with Blaine; simplify scope.

## Review checklist

- [ ] Confirm **Blaine** meeting **date/time** (another note said “tomorrow 2pm”—ensure 2026-05-13).  
- [ ] Replace **Grafted** with correct partner name and responsibilities.  
- [ ] Replace **ECPA** with correct compliance framework if misheard.  
- [ ] Attach or link the **project document** and **API requirements** email under version control or tickets.  
- [ ] Validate **D1** field list for routing (lat/lon, Yext, GHL ids, Lobby URLs).
