> **Source:** `gameday/meeting-notes/2026-05-12-ab-test-handover-infrastructure.md` (synced 2026-06-02)

# Florencia Martinez Carranza and Matthew New — AB test handover, infra, final transition

**Date:** 2026-05-12  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)

## Participants

**Core:** Florencia Martinez Carranza (Ignite), Matthew New (Game Day / Uptech)

**Invited / discussed:** Sara Esquivel (Ignite — AB test handover), William Morales, Jefferson Soares (Ignite), Anthony Castelli

**Referenced:** Blaine, Nicole (PostHog access; GitHub migration discussion), **Timothy (Teemo)** (GitHub migration—**verify** if one person or two), QA team, Lobby team (shared API / secrets rationale)

## Summary

Sara walked through the **PostHog** A/B test on clinic homepages: **Option A (control)** keeps current behavior (CTAs → **Lobby**, with a **safety-net banner** toward the contact form if Lobby fails). **Option B (variant)** inserts a **decision page** so users can go straight to **Lobby** in a new tab **or** use a **short Webflow form**. Only **12 clinics** are in the experiment (**6 control / 6 variant**) due to constraints; **statistical significance** estimated at **~4 weeks**, possibly **5–6** if traffic is lower.

**Implementation:** Global **Webflow** custom code (footer): JS reads PostHog **feature flag** and adjusts the **DOM**. Metrics called out: **Webflow lead submit** and **lobby link click** (click only, not downstream booking).

**Telehealth gating (worker):** Jefferson described **two checks** before showing telehealth UI: (1) **user IP** via a **worker API** plus Webflow script, and (2) **location state** from **D1**; content stripped if user or clinic is **outside Florida**.

**Forms → GHL:** Submissions hit Ignite’s **API**; worker informs correct **Go High Level** sub-account; secrets (**location IDs**, **GHL private integration token / PIT**, etc.) live in **AWS Secrets Manager** (shared across Lobby and other consumers like Snowflake per Lobby team request).

**Handover:** Full control still **pending QA final approval**; Florencia expected notice **EOD or next morning**, with a **few days overlap**. GitHub org migration still sticky (**Actions**, cost); Matthew floated **light ongoing support** until resolved—Florencia to discuss with Nicole and Blaine same day.

**Yext:** Multiple name fields explained (principal, location finder display name, custom location name). Florencia **reset/sent verification** for Matthew’s Yext access; plan to **remove legacy Yext users** toward **end of week**.

## Architecture and product notes

| Topic | Detail |
|--------|--------|
| PostHog | Experiment + **feature flag**; platform handles bucketing / distribution. |
| Metrics | **Webflow lead submit**; **Lobby link click** (pre-Lobby navigation only). |
| Telehealth | Florida-only via **IP + D1 state** validation in worker/script path. |
| Secrets | **AWS Secrets Manager** for GHL tokens/IDs—**not** DB—by design for **shared API** across Lobby, Snowflake, etc. |
| Yext names | Principal vs **location finder** display name vs **custom** name fields for edge cases. |

## Action items

| Owner | Action |
|--------|--------|
| Matthew New | **PostHog:** Contact **Blaine** and **Nicole**; confirm whether broader team needs **PostHog** access. |
| William Morales | **Share repo details** so Uptech can review **AB test code** implementation. |
| Florencia Martinez Carranza | With **Nicole** and **Blaine**: **GitHub** repo + **Actions** migration, **ongoing support contract** needs. |
| Florencia Martinez Carranza | **Reset Yext** access for **Matthew New** (verification flow). |
| Florencia Martinez Carranza | **Remove** existing **Yext** users toward **end of week** (per transition plan). |
| William Morales | **Schedule** time with **Timothy (Teemo)** to clarify **GitHub migration** status. |
| Matthew New, Blaine | **Define prioritization / urgency criteria** for incoming work together. |

## Detailed themes (from notes)

1. Sara: purpose of call — AB test handover materials and status update.  
2. Matthew: origin, goals, stakeholders for the test.  
3. Variant rationale: customer feedback on contact form; decision page emphasizes form path.  
4. Control vs variant; 12-clinic split; timeline to significance.  
5. PostHog mechanics: experiment, flag, metrics.  
6. Webflow footer script: flag-driven DOM changes; PostHog owns sampling.  
7. GitHub: Actions + cost; support contract idea; Florencia ↔ Nicole/Blaine.  
8. Yext naming fields; access reset for Matthew; end-of-week user cleanup.  
9. Worker: telehealth Florida gating (IP API + D1).  
10. Forms API, GHL routing, Secrets Manager rationale (Lobby shared API).  
11. QA gate and overlap before full control.

## Review checklist

- [ ] Confirm whether **Timothy (Teemo)** is one contact or two.  
- [ ] Confirm **12 clinic** list and **6/6** split in PostHog matches production.  
- [ ] Align event names (`web flow lead submit` vs actual PostHog event naming).  
- [ ] Document **Yext** user removal list and comms before cutover.  
- [ ] Capture **prioritization rubric** from Matthew + Blaine once agreed.
