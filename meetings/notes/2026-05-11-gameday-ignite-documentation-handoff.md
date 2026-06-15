> **Source:** `gameday/meeting-notes/2026-05-11-documentation-handoff-ignite-uptech.md` (synced 2026-06-02)

# Ignite <> Uptech: Documentation handoff

**Date:** 2026-05-11  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)

## Participants

**Discussed / invited:** Florencia Martinez Carranza (Ignite), Matthew New (Uptech), Anthony Castelli

**Referenced:** Jefferson Soares, William Morales, Jake Daniels (data handoff), Teemo (AWS admin), Nicole, Blaine, Allan, Russ (fractional CTO suggestion), Sarah (CRO / PostHog A/B), Dina (Canadian market), design team, QA

## Summary

Ignite is **finishing exports** and **ticket documentation** for engineering/QA handoff, with a target of **wrap by tomorrow ~noon Eastern** (per notes) and **full Cloudflare + Webflow access** after **QA sign-off** (called out as **tomorrow afternoon** in one detail—**reconcile times** on calendar).

Topics covered: **blog workflow** (corporate vs franchise, duplicate content), **steady-state maintenance** expectations and request hygiene, **telehealth** UX/initiative status and **where display logic lives** (follow-up with Jeff/William), **Canadian treatment pages** (staging, SEO copy), **“coming soon”** location cleanup (~750 → ~200, legal/territory sensitivity), **corporate blogs on microsites** (new tab, local over national), **national US hero** slider/accessibility, **landing page template** strategy vs one-off WordPress pages, **deprioritized designs** still to hand off, **data messiness** and CTO/fractional oversight, **PostHog** intermediary booking A/B test (Sarah), and **scheduling** follow-ups via Matthew’s Calendly.

## Decisions and direction

| Topic | Direction / status |
|--------|---------------------|
| Blogs (national) | Process in **Webflow** today; SEO team could be **Webflow collaborators** for write/publish (outside Uptech core scope per Matthew). |
| Corporate blogs on microsites | Add **dedicated section** on microsites; **open in new tab**; **prioritize local blogs** over national when both exist—mitigates **duplicate content** vs old agency approach. |
| Canadian treatments | Two new treatment pages (**GHKCU** and **HCG** per notes—**verify abbreviations**) on national, regional, and microsites; **staging only** first for Nicole’s **content review**; US vs CA copy variants to reduce **canonicalization** issues. |
| Coming soon | Short list **~200** (vs ~750); **in-house** redirect confirmation (Blaine/Nicole) due to **legal / territory** concerns; UX: **wait list** CTA, **estimated opening** season/date, **static Mapbox** image (non-interactive map), Webflow form → **GHL**. |
| Game Day Difference (homepage) | Design/animation ready; **blocked on client images** aligned to current branding. |
| Franchise landing pages | **1–3 reusable Webflow templates** vs many bespoke legacy WordPress pages; Matthew floated **third-party SaaS** for LP hosting—designs available either way. |
| A/B test (booking friction) | **PostHog**; intermediary page (non-dynamic calendar visual, two paths: **Lobby** self-schedule vs **Webflow** short form); subset of clinics; possibly **up to ~4 weeks**. |
| Architecture oversight | Messy dual paths (**Snowflake**, **BigQuery** context per notes); Matthew may suggest **Russ as fractional CTO** to Allan. |

## Risks and coordination notes

- **Request pattern:** Past **Slack** requests outside hours with unrealistic turnaround (“death by a thousand paper cuts”). Uptech SOW through **July** per Matthew; align on **steady-state** hours/cadence.
- **Telehealth:** Trial paused; franchise participation **drifted** without notice; new chip/dual CTAs in plan—**confirm worker-side data source** with Jeff/William.
- **Access sequencing:** **AWS** via **Teemo** (admin); **GitHub** transfer in flight; **Cloudflare + Webflow** full control **after QA** (notes: “tomorrow noon” vs “tomorrow afternoon”—confirm).

## Action items

| Owner | Action |
|--------|--------|
| Group | **Finalize blogs:** tickets + publish **3 approved** blogs this week. |
| Jefferson Soares, William Morales | **Confirm telehealth display logic** location in **worker / data** (double-check). |
| Florencia Martinez Carranza | **Schedule ~30m calls:** Jeff/William (telehealth + GHL form), **Jake** (data transfer), **Sarah** (PostHog A/B)—use **Matthew’s Calendly**. |
| Group / design | **Deliver Figma** for **US and Canadian** sites. |
| Teemo | Provide **AWS administrator** access to instances (per Florencia). |
| Group | After **QA review**, grant **full control** to **Cloudflare** and **Webflow** (notes: likely **tomorrow noon Eastern** for access—**vs** “tomorrow afternoon” elsewhere—**align**). |
| Florencia Martinez Carranza | **Update delivery tickets** with notes, requirements, and **acceptance criteria** for client requests. |
| Florencia Martinez Carranza | Share **paid ads** and **LCM** documentation and related materials. |

## Detailed themes (from notes)

1. Handoff/export timing and remaining tasks before final turnover.  
2. Blog publishing workflow and SEO team role in Webflow.  
3. Maintenance scope / “steady state” expectations and ticket completeness.  
4. Telehealth initiative history (Florida trial, two treatments), pause reasons, planned UX (chip, dual CTAs).  
5. Telehealth data logic—defer to Jeff/William.  
6. Access: AWS (Teemo), GitHub, post-QA Cloudflare/Webflow.  
7. Canada: GHKCU + HCG pages, staging, SEO-supplied copy, privacy practices page, Dina/WhatsApp request pattern.  
8. Coming soon: legal-driven redirect ownership; list reduction; UX changes.  
9. Game Day Difference: UAT feedback, animation, missing brand images.  
10. Microsite blogs: new section, tab behavior, local-first ordering.  
11. US hero: video → slider, a11y (no hardcoded text on images), left-aligned hero.  
12. Landing pages: template strategy vs legacy WordPress one-offs.  
13. Deprioritized: Franchise Opportunities, Influencer pages—designs still handed off.  
14. Data: Jake follow-up on Snowflake/BigQuery connect; CTO gap discussion.  
15. PostHog A/B: intermediary page design; clinic subset; duration.  
16. Scheduling: Calendly for Jeff/William, Jake, Sarah.

## Review checklist

- [ ] Reconcile **noon vs afternoon** Eastern for access cutover.  
- [ ] Verify treatment codes **GHKCU** / **HCG** spelling and clinical meaning.  
- [ ] Confirm **Teemo** spelling (notes also said “Teimo” in summary line).  
- [ ] Confirm **LCM** expansion (likely lifecycle marketing—verify).  
- [ ] Match ticket IDs/links in Monday/Jira when Florencia updates AC.
