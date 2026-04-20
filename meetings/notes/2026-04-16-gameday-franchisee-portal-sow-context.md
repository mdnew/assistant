# Gameday — Franchisee portal (Allen and Blaine) and internal SOW prep

**Date**: 2026-04-16 (conversation with Allen Brooke and Blaine; internal Slack same day)

**Purpose**: Capture product direction, risks, and technical options so we can scope and estimate when the SOW conversation lands.

## What Gameday wants

- A **franchisee portal** where **owners can see metrics for their locations** (not only corporate views).
- Strong interest in a **modern, polished UI** (they referenced how the prototype looks multiple times).
- Beyond charts, there may be **operational or workflow features** (internal read: “CMS-like” capabilities, possible future tools such as franchisee-facing workflows; Matt raised **ReplyWise** as an analogy for “custom workflows on top of data”).
- **Follow-up and engagement workflows (verbal, not in screenshots)**: They may want **reminders or lightweight workflows for franchisee owners** to **follow up with customers** (version unclear: in-app tasks, email or SMS nudges, playbooks tied to census or revenue events, etc.). This is **operational software**, not a chart, and should be **scoped and priced separately** from read-only dashboards.

## Reference prototype (franchisee “vibe coded”)

Screenshots came from a Meet where **Allen Brooke** walked through a franchisee-built prototype for **Gameday Men’s Health**, example clinic **Northpoint**. Treat this as **directional UX**, not as engineering or security baseline.

**Dashboard (conceptual scope)**

- Clinic selector in nav; role hint in header (example: provider id).
- KPI cards: revenue, active members, new members, MRR-style figure, average revenue per transaction, period comparisons, links such as “QC Check” and states like “Not verified” on revenue.
- Revenue area: granularity (daily, weekly, monthly, quarterly), recurring vs one-time, bar vs trend, line chart with actuals vs trend.
- Patient or membership analytics: counts by category (TRT, peptides, weight loss, ED, lab work, supplements, canceled), with **total active members** as a headline number.

**Member census (conceptual scope)**

- Same category stat cards with explicit copy: **unique members per category**; members on multiple products appear once per category; **detail table is member-product rows**.
- Filters: category tabs, search, counts (“showing X of Y”), view modes (detailed vs by member).
- Table columns along the lines of: first sale, member, product, category, status, amount, transaction count, referral source, Google review toggle, drill-in for transactions.

**Implication for SOW**: each surface implies **definitions** (what is “active,” how revenue is verified, how categories are derived), **data freshness** (example “Sync Data” control), and **permissions** (who sees which clinic and which rows).

### Functionality inferred from the two screenshots

**What we can say with high confidence (visible in UI)**

- **Multi-clinic context**: Clinic picker in the sidebar (address shown), implying **one user, one or more assigned locations** (exact assignment rules not shown).
- **Global date context**: Dashboard uses a period control (example **“This Month”**); revenue chart shows a **daily series** for part of a month.
- **KPI summary layer**: Cards with **current value**, **delta vs prior period** (up or down percents), and at least one **sub-status or action** on revenue (“QC Check,” “Not verified”).
- **Revenue exploration**: Toggles for **time grain** (daily, weekly, monthly, quarterly), **recurring vs one-time**, and **bar vs trend** view; chart shows **actuals vs a trend line**.
- **Category analytics**: **Eight buckets** (TRT, peptides, weight loss, ED, lab work, supplements, canceled, plus total active) with **color coding** consistent across dashboard and census.
- **Census list experience**: **Category tabs** with counts, **search**, **pagination or windowing** (“showing 50 of …”), **two view modes** (detailed vs by member), **sortable columns** on key fields, **row-level actions** (example **Google Review** as a toggle, **transaction detail** via an icon).
- **Explicit census semantics** (from on-screen copy): stat cards are **unique members per category**; table is **member-product rows** (so one member can appear multiple times).

**What is implied but not proven by static screenshots**

- Whether **“Sync Data”** triggers ETL, a warehouse refresh, or is placeholder; who can run it; latency and cost.
- Whether **QC / verified** states are **manual workflow**, **rule-based**, or **integration** from another system.
- Whether **Google Review** toggle **writes** somewhere or is UI-only.
- Whether **“Suggestions”** (dashboard header) is populated, rules-driven, or empty in v0.

**What the screenshots do not show**

- Behavior of other nav items (**Revenue**, **Medication Orders** and children, **Bonus Tracker**, **Close Rate**, **Inventory**, **Contracts**): no detail in these two images.
- **Auth**: real **login, SSO, session, audit** (header shows a user label and role text only).
- **Corporate vs franchisee** views: not distinguishable from these frames alone.

## Risks and non-negotiables (engineering)

1. **Data correctness**: If Snowflake (or upstream) is wrong, **a new UI does not fix trust**. Plan for **validation work** per metric or report before we promise franchisee-facing numbers.
2. **Performance**: Existing **Knowi**-style experiences were described as **very slow** (order of **minutes** to load). Avoid “another skin on a massive, unoptimized query.” Likely needs **pre-aggregation, caching, or a semantic layer** with sensible rollups, not only raw warehouse queries on every page load.
3. **Security and tenancy**: **Hundreds of locations** (~**400** in Russell’s note). Need **row-level security** and **role-based views**: franchisees see **their clinics**; **corporate** can see broader scope. **Per-user logins** (not shared “Z” credentials) should be assumed in architecture from day one.
4. **Compliance**: If clinical or PHI-adjacent data appears, **HIPAA posture** matters for vendor choices and hosting (Cube was mentioned as **HIPAA-capable** in Slack; still needs Gameday legal and BAA path confirmation, not assumed).

## Options discussed (BI vs custom portal)

| Direction | Pros | Cons / open questions |
| --- | --- | --- |
| **Tableau / Looker (paid, serious BI)** | Faster for v1 if specs are standard metrics; less custom UI work | **Looker**: concern about **maintaining hundreds of near-duplicate reports** for per-location filtering; **UI polish** and “sex appeal” vs a custom React dashboard; may not cover **CMS-style** or deep custom workflows |
| **Custom React portal** | Full control of UX (dark mode, layout, workflows), can grow past charts | More build and ongoing ownership; must still solve **data modeling, caching, and auth** well |
| **Hybrid mental model** | Use a semantic or metrics layer for speed and consistency; custom app for presentation and workflows | Two systems to integrate and operate |

**Internal sentiment**: Pretty **vibe-coded demos** set visual expectations but are often **not scalable or secure**; commercial work needs explicit scope, tenancy, and data contracts so we do not “rebuild the demo for peanuts.”

## Russell’s proposed direction (Cube.dev)

High-level (from Slack, not validated in production by us yet):

- **Cube.dev** between **Snowflake** and the app for **modeling, caching, and API-style access**, including patterns that support **RLS** across many locations.
- **Front end**: **React** plus a modern component kit (example: **Tremor** blocks at `https://blocks.tremor.so/`) for dashboard density and polish.
- Goals called out: **snappy loading** (cache and middle tier), **RBAC and clinic scoping**, **modern UI**, forward **SaaS cost** to Gameday where applicable.

**Open technical question (Claude)**: For **non-Cube** behavior (profile images, arbitrary business logic, orchestration), we still need a **normal application API** (BFF or services). Cube addresses **analytics-shaped** read paths; **custom workflows** live in the app and supporting services, not inside the BI cube alone unless we deliberately extend there.

## Build vs buy (Cube and “more features later”)

**How to split the problem**

- **“Buy” (or rent) what is commoditized and painful to get right**: a **metrics layer** on Snowflake with **caching**, **consistent definitions**, and **tenant-aware queries** (Cube is one option; alternatives exist). That is **not** the same as buying a full franchisee portal.
- **Build what is differentiating and open-ended**: the **web app** (navigation, branding, clinic switching, role UX), **auth and session** integration with their identity story, **workflows** (follow-up reminders, tasks, approvals), **write paths**, **notifications**, **audit**, and any **CMS-like** content. Those features **want a normal application backend**, not a BI tool.

**Recommendation for Gameday-shaped scope**

- Default to a **hybrid**: **custom portal** plus a **semantic or headless analytics tier** for dashboard and census style reads. Cube fits the **second** bucket if evaluation checks out (performance, RLS story, HIPAA and contract path, cost).
- Draw a **hard boundary** in architecture: the portal calls **Cube (or successor)** only for **aggregates and drill queries**; the portal’s own API owns **users, orgs, clinics, tasks, schedules, outbound messaging metadata**, and anything that **mutates state**.
- If they later need **more portal features**, you are **not** trapped as long as you did not embed business logic inside the BI layer. You add tables and services in the **app**, and keep Cube focused on **numbers**.

**When “buy more” (classic BI) could win**

- If v1 were **read-only executive reporting**, they accepted **standard BI chrome**, and workflows were off the table, **Looker or Tableau** could reduce custom front-end cost. Their stated desires (look and feel, franchisee logins, future workflows) push **away** from pure BI as the whole answer.

**When “build more” would be the mistake**

- Building **only** a pretty React app that hits Snowflake **directly** for every chart across **~400** clinics without a modeling and caching strategy. That repeats the **Knowi** failure mode (slow, fragile definitions).

**Matt’s concern (other features down the line)**

- Treat **Cube as an implementation detail of the analytics module**, not as “the platform.” Plan the product as **one portal** with **pluggable subsystems** (analytics today, workflows tomorrow). If Cube ever needed replacing, the **portal shell and workflow services stay**; you swap the metrics provider behind the same internal contract.

## What we need before a credible estimate

1. **Inventory of reports and screens** (v1 vs later): exact metrics, filters, drill paths, exports, alerts.
2. **Metric definitions and source of truth** per number (which Snowflake tables or marts, grain, refresh cadence, reconciliation to finance or EMR if applicable).
3. **Auth model**: roles (franchisee owner, regional, corporate, read-only vendor), **SSO or not**, audit expectations.
4. **Non-dashboard scope**: workflows, write-backs, approvals, content management, integrations (email, ticketing, etc.). Include **customer follow-up reminders** for owners: triggers (time-based, segment-based, manual), channels (in-app, email, SMS), ownership and completion tracking, and any **PHI or marketing consent** constraints.
5. **Budget envelope** from Gameday (Matt was pushing for this so we can propose a phased path that fits).

## Suggested phasing language (for SOW drafts)

- **Phase A — Discovery and data validation**: lock definitions, prototype queries, performance benchmarks on representative clinics, RLS design.
- **Phase B — Analytics read path**: semantic layer or aggregation jobs, core dashboards matching approved definitions.
- **Phase C — Portal shell and auth**: login, clinic picker, corporate vs franchisee experience.
- **Phase D — Extended workflows**: only after A through C are stable; priced separately. **Customer follow-up reminders** for franchisee owners fit here unless they are a thin MVP (then define “thin” explicitly).

## Follow-ups

- Watch for **Gameday follow-up email** after the meeting (Russell).
- When estimating, assume **separate line items** for **data correctness**, **performance and caching**, **auth and RLS**, **UI build**, and **workflow features** so scope creep stays visible.
