> **Source:** `gameday/meeting-notes/2026-05-07-gameday-lobbie-webhooks-infrastructure.md` (synced 2026-06-02)

# Gameday × Lobbie — webhooks, data & infrastructure

**Date:** 2026-05-07  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)  
**Transcript:** [Granola notes](https://notes.granola.ai/t/50ed1a28-eaf0-4906-850a-3cbce9f0fc5b)

## Participants

**Game Day / Uptech:** Matthew New, Russell Cloak, Timothy Rempher, Sushma Bulusu, Anthony Castelli (referenced), Allen (referenced)

**Lobbie:** Development team (webhook sprint)

**Referenced:** Blaine, Ignite (data call same day; handoff urgency), Kippy, Alliant (AWS deployments—**verify vs Outliant**), Braze (**“Brave” in notes—likely Braze**), Sushma (Power BI trial)

## Summary

**Webhooks:** Lobbie sprint ends **tomorrow**; **two developers** on webhooks **early next week**. **LCM** is priority (ongoing cost with **Braze** vendor). Webhooks are part of broader **partner API** package. Uptech needs **proposed payload spec** before pseudo-coding can start.

**Data:** Russ building **Snowflake → Braze** connector (**user attributes** first; **Lobbie** as SoT for events, blending beyond ETL). **Ignite data call** completed today—Russ building spreadsheet for **Kippy + Ignite** requirements. **Lobbie → Snowflake ETL** runs **nightly**; gap analysis needed for **dashboard** needs not in current dump.

**AWS / access:** Game Day has existing **AWS** account with **Alliant**-deployed services; plan **webhook consumers in AWS**. **GitHub Enterprise** still blocked (Timothy vs trial→enterprise bug)—urgent with **Ignite leaving next week**. **Yext → AWS → Webflow** for location creation; Webflow mostly **coming soon**. **Cloudflare** hosts WordPress migration services.

**BI:** **Power BI** for franchisee dashboards—public publish vs auth tradeoffs; **Premium** ~**$4k/mo** for 1k users vs **$25/user**; **Entra B2B** for externals. Alternatives: **scheduled email reports**, **Q3 custom portal** (AWS + **Supabase** auth), embed Power BI later. **Sushma** testing Premium trial for guest access.

## Webhook development progress

| Topic | Notes |
|--------|--------|
| **Sprint** | Wrapping up **tomorrow** (from meeting date). |
| **Staffing** | **Two developers** assigned to webhooks **early next week**. |
| **Uptech dependency** | Need **proposed payload spec** before pseudo-coding. |
| **Priority** | **LCM** urgent—ongoing costs with **Braze** (**“Brave”** in notes—verify). |
| **Scope** | Webhooks part of broader **partner API** package. |

## Data infrastructure & integrations

| Topic | Notes |
|--------|--------|
| **Snowflake → Braze** | Russ building **this week**—start with **user attributes**; **Lobbie** events as SoT; blend multiple sources beyond ETL. |
| **Ignite** | Data call **today**—walked through their pulls; Russ creating **spreadsheet** for **Kippy + Ignite** requirements. |
| **ETL** | **Lobbie → Snowflake** nightly dump. |
| **Gaps** | Identify **dashboard requirements** not covered by current dump. |

## AWS infrastructure discovery

| Topic | Notes |
|--------|--------|
| **Existing AWS** | Game Day account with services already deployed. |
| **Alliant** | Deploying into this account (**verify vendor name**). |
| **Webhooks** | Plan to build **consumption services in AWS**. |
| **GitHub Enterprise** | Still **blocked**—Timothy on **trial→enterprise bug** with GitHub support; needed for **Alliant repos**; urgent as **Ignite departs next week**. |
| **Yext workflow** | **Yext webhook → AWS → Webflow** location creation; Webflow minimal except **coming soon**. |
| **Cloudflare** | Additional **WordPress migration** services. |

## BI tool & dashboard strategy

| Topic | Notes |
|--------|--------|
| **Power BI** | Investigated for **franchisee dashboards**. |
| **Auth constraint** | Published reports may need to be **public** (no password protection on standard publish). |
| **Premium** | ~**$4,000/month** for **1,000 users** vs **$25/user** alternative. |
| **External users** | **Microsoft Entra B2B** guest access required. |
| **Interim** | **Scheduled email reports**. |
| **Q3 option** | **Custom portal** in **AWS** with **Supabase** user management. |
| **Future** | **Embed Power BI** in custom portal. |
| **Trial** | **Sushma** signing up for **Power BI Premium trial** to test guest access. |

## Action items

| Owner | Action |
|--------|--------|
| Lobbie dev | Deliver **webhook payload specification** **next week**. |
| Lobbie | Continue webhook sprint; assign **two devs** early next week. |
| Russell Cloak | **Snowflake → Braze** connector (attributes first). |
| Russell Cloak | Complete **Kippy + Ignite** requirements **spreadsheet**. |
| Team | Identify **dashboard data gaps** vs nightly Lobbie ETL dump. |
| Sushma Bulusu | Test **Power BI guest access** and report publishing (**~1 day**). |
| Timothy Rempher | Resolve **GitHub Enterprise** access (support ticket). |
| Allen | Share **sister brand proposal** for review. |
| Matthew New, Anthony Castelli | Schedule call **tomorrow** on **sister brand Webflow** project. |
| Uptech | **Await payload spec** before webhook pseudo-coding. |

## Review checklist

- [ ] Confirm **payload spec** received from Lobbie (week of 2026-05-12).  
- [ ] Verify **Alliant** vs **Outliant** spelling and AWS ownership.  
- [ ] Confirm **Braze** vs **Brave** (LCM cost context).  
- [ ] GitHub Enterprise resolution before **Ignite** handoff.  
- [ ] Power BI trial outcome—guest access vs public publish viability.  
- [ ] Sister brand proposal link and Webflow call outcome.  
- [ ] Dashboard gap list tied to franchisee reporting requirements.
