> **Source:** `gameday/meeting-notes/2026-05-06-technical-architecture-knowledge-transfer.md` (synced 2026-06-02)

# Technical architecture and knowledge transfer

**Date:** 2026-05-06  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)

## Participants

**Present / core discussion:** Florencia Martinez Carranza (Ignite), Matthew New (Game Day)

**Invited:** Anthony Castelli, Jefferson Soares, William Morales, Lucas Lima (Ignite); Timothy Rempher (Game Day)

**Also referenced:** Russ (data engineering), Nicole (process/tooling), Blaine (Yext / product stance), Allan (AI / ops exploration), Pam (Yext access verification)

## Summary

The group walked through how clinic and location content flows through **Yext → Webflow → Cloudflare (D1 + Workers)** and aligned on **maintenance-first** work under the current SOW. **Yext is the source of truth** for live location data that syncs to Webflow and D1; **D1** exists largely to work around Webflow URL/routing limits for clinic, service, and treatment pages, with Workers injecting D1 content into templates.

**Access and handoff** (GitHub Enterprise under Game Day, AWS, Cloudflare) were called out as immediate priorities, along with cleanup (legacy Webflow templates/pages, D1 legacy/closed locations), **redirect documentation** (large legacy URL surface from the former WordPress setup), and a **follow-on session** on data engineering / Snowflake.

## Architecture and operations (agreed / stated)

| Topic | Notes |
|--------|--------|
| Source of truth | **Yext** drives updates to **Webflow** and **D1** for the automated path. |
| Manual exceptions | **“Coming soon”** locations can be managed in **Webflow CMS** without Yext; open clinics are populated from Yext. |
| D1 | Replicated location data for routing/pages Webflow cannot represent cleanly. **Avoid manual DB edits**—changes flow from Yext/Webflow. |
| Webflow role | Described as **templating**: Workers inject content from D1 into templates shared across clinics. |
| Cloudflare | **D1** for location data; **separate DB for redirects** (redirect limits in Cloudflare were a constraint). Workers include sitemap, `robots.txt`, a **third-party telehealth** integration (vendor name unclear in notes—was transcribed as “Inventables”; verify), lobby link (WIP), Instagram/iframe behavior, etc. |
| Environments | Webflow has UAT/production domains; **one D1** reflects the unified Webflow CMS; Workers can branch behavior by URL with dev/prod behavior. |
| CI/CD | Workers tied to **GitHub** (e.g. Actions, **Wrangler**); transfer to Game Day org should preserve pipeline behavior once verified. |
| Franchises | Use **Yext** for listings/GBP with **permissioned** access; scalable customization (e.g. FAQs, meet the team, about) possible if scoped. |
| Risk | Replacing **Yext** would break the current micro-site architecture unless connections are redesigned. |

## Process and policy

- **Deletion:** Manual, with approval—typically unpublish/delete in Webflow, clear D1, mark **closed** in Yext.
- **Game Day vs Ignite:** Game Day does not edit Webflow directly today; avoid **one-off franchise content** outside templates to preserve scale.
- **Priorities:** Emphasis on **support/maintenance** and walking Anthony through operational flows (new locations, products) vs net-new build.
- **SEO / agency backlog:** Critical items addressed; lower/medium items to backlog for the incoming team; Friday session may include **Director of SEO** and co-working on feasibility.

## Action items

| Owner | Action |
|--------|--------|
| Timothy Rempher | Set up **Game Day GitHub Enterprise**; add **Matthew New** for login; add **Anthony Castelli** and **Russ** as users. |
| Timothy Rempher | Provide **Matthew New** existing **AWS** credentials (billing-only view called out as current limitation). |
| Timothy Rempher | Add **Anthony** to **AWS** using his email (from chat). |
| Timothy Rempher, William Morales, Lucas Lima | **Test GitHub repo transfer** and **Cloudflare pipeline** integrity (target: before Monday). |
| Jefferson Soares | Review **Yext location creation** video, add **voiceover**, send **by end of week**. |
| Pam | **Verify Yext access** / account manager access for the team. |
| Jefferson Soares | **Webflow cleanup**: delete legacy CMS pages/templates with the team this week. |
| William Morales | **Clean D1**: remove closing/legacy location data. |
| William Morales | **Document redirects**: each redirect with description and reason (large legacy URL set from WordPress era). |
| William Morales | **Cloudflare**: add **Anthony**; **remove Claude** access. |
| Matthew New | **Schedule data engineering / Snowflake** meeting (include Russ; Florencia suggested including their **data analyst**). |
| Florencia Martinez Carranza | **Confirm availability** for the data discussion (referenced as “tomorrow” in notes). |
| Florencia Martinez Carranza | **Ticket export**: define process to export/share **Monday** tickets (images, videos, URLs); align with Nicole on **Monday vs Jira**. |
| Florencia Martinez Carranza | **Friday call**: invite **Director of SEO**. |
| Florencia Martinez Carranza | Share **developer/support doc** on frequent **franchise support** requests. |

## Detailed discussion (chronological themes from notes)

1. **GitHub:** Enterprise org under Game Day; transfer blocked pending GitHub support linking enterprise to account—plan to complete transfer and integration tests the following Monday.
2. **AWS:** Important for understanding services feeding the warehouse and site; not “Webflow only.”
3. **SOW / focus:** Maintenance and operational understanding before new features; Q3 enhancements possible after integration.
4. **Why Webflow:** Historical decision predating current Ignite team; Webflow + separate backend complicates dev and AI leverage vs a single repo on AWS/GitHub.
5. **AI:** Interest from Allan in AI for ops/product; Webflow connector tested for **content** updates; **design** still weak—AI in estimates with caveats.
6. **Live demo:** Jefferson shared screen—locations/regions in Webflow; manual creation vs **Yext → webhook → Webflow API** as primary automated path.
7. **Replication:** After Yext/Webflow, data flows to **D1** for URL/page structure needs.
8. **Access model:** Game Day relies on web team for Webflow; franchises use constrained Yext; account manager access provided to Matthew and Anthony.
9. **Cleanup:** Remove legacy WordPress-era Webflow pages/templates; keep latest working templates.
10. **Cloudflare overview:** D1 + workers; redirect DB; worker inventory (sitemap layers—Webflow sitemap enriched with legacy URLs, robots, telehealth worker, lobby WIP, Instagram iframe injection, etc.).
11. **GitHub ↔ Cloudflare:** Actions + Wrangler; post-transfer verification.
12. **Data / Snowflake:** Separate meeting; Russ on data engineering; Anthony focused on web.
13. **Cadence:** Possible daily rhythm—data session next, **Friday** status/SEO-oriented sync.
14. **Tooling:** Monday vs Jira; need sustainable request tracking.
15. **Long-term:** Question whether Webflow must remain vs templates in repo—open strategic topic; William noted AI limits on design in Webflow today.

## Review checklist

These bullets are **summarized from meeting notes**, not a verbatim transcript. Before treating any item as binding:

- [ ] Confirm names, owners, and deadlines against calendar and tickets.
- [ ] Confirm **Pam** identity and Yext verification scope.
- [ ] Spot-check technical claims (single D1 vs environments, worker list) against production/docs.
- [ ] Align product names: **Webflow**, **Yext**, **Cloudflare D1**, **Snowflake**.
