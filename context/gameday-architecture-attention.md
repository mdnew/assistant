# Gameday architecture: items to track

Distilled from **`gameday-architecture`** (local clone: `~/code/gameday/gameday-architecture`). Update the source repo when facts change; this file is the quick surface for the assistant workspace.

## Stakeholder request you should not lose (Apr 2026)

- **Zendesk** is the target home for **dynamic franchise support ticketing** (ticket logic described as already designed; **implementation** of the dynamic form in Zendesk is in scope).
- **Monday.com** is used for **PM and communication** next to support work.
- **Zendesk and Monday.com are not connected today.** Desired outcome: implement the dynamic Zendesk form **and** build a **supported link between Zendesk and Monday.com** so support and PM stay aligned.
- **Still TBD:** sync direction, objects, automations, and field or brand mapping (boards, groups, item types vs ticket fields).

## Takeover scope (from `architecture/ownership.md`)

- **Taking over:** work tied to **Kippi** (Snowflake, Knowi) and **Outliant** (Webflow, Looker), with exact cutover to align with stakeholders.
- **Not taking over:** **SEO** and **ad spend** (stay with Outliant or agreed partner scope).

## Website handover (Ignite context, May 2026)

**Ignite** has deep continuity on Gameday web (PM eng and tech leads on account since 2023). They are briefing Uptech for **web takeover**; full notes and actions: `meetings/notes/2026-05-05-ignite-gameday-website-handover.md`, `meetings/actions/2026-05-05-gameday-ignite-web-handover.md`.

**Production shape:**

- Sites: national corporate, regionals, microsites; **Yext** is the dynamic content layer (reviews show 4+ only; clinic availability hides treatments on microsites).
- **Two components must run:** an **AWS-hosted** integration layer (**Yext**, **Snowflake**, **GoHighLevel**) and a **Cloudflare Worker** serving HTML transformations. Both stay in scope for ops and deployment understanding.

**Gaps:**

- **AWS** ownership split (Gameday account, Ignite delegation, maybe prior agency): align with **Timon** before assuming access paths.
- **Monday.com** is the live mirror for PM tickets but **migration from ClickUp** means partial history (Q2 fresher than Q1). **Zendesk vs Monday integration** remains a separate open item above.

## Snowflake to Braze and identity (May 2026 sync)

- **Russ** built **user attribute sync Snowflake → Braze**: stream/connector **ready for testing**, demo in Snowflake, **obfuscated schema sample** for PHI-safe sharing.
- **Commercial:** Braze can use **cloud data ingestion** or **direct connector**; direct connector discussed as roughly **$10k upcharge** (confirm with Braze or procurement).
- **Hard problems still open:**
  - **No single user ID** wired across **Lobby**, **GoHighLevel**, **MX Payments** (formats and naming differ).
  - **Locations:** on the order of **four** tables or sources with **conflicting location IDs** (mapping blocker).
  - **Kippy** did not resolve ID conflicts during their engagement.
- **Next:** Session with **Ignite** and **Outliant** on **warehouse work to date** and **source of truth** for attributes and IDs; strategy is **start confident, enrich later**. Notes: `meetings/notes/2026-05-06-grafted-gameday-lifecycle-sync.md`.

## Ignite data warehouse walkthrough (May 2026)

Full notes: **`meetings/notes/2026-05-07-gameday-ignite-data-engineering.md`** (meeting **2026-05-07**). Actions: **`meetings/actions/2026-05-06-gameday-data-engineering-ignite-handoff.md`**.

**What Ignite described in Snowflake (high level):**

- **GHL:** Pulled via **AWS**, UTM cleanup, lands as **GHL proxy S3** in Snowflake. Two emphasis tables: **`contacts created`** (first-touch) vs **`contacts updated`** (current). Core CRM for in-person; **PII** (phones) may be **masked** until unmask permission.
- **Lobby:** **`lobby raw appointments`** and **`lobby raw payments`**; separate **`lobby`** path for **telehealth**. Join: GHL **`contact ID`** → Lobby **`go high level contact ID`** → **patient UUID** for appointments and payments (Ignite to send **diagram** to Russell).
- **Latency:** Non-telehealth Lobby via **FTP**, about **1–2 day lag**; **telehealth** uses **webhooks** (lower volume, more real time).
- **Attribution:** Lobby redirects **strip UTMs**; GHL often has **no campaign** for those bookings; **Lobby fix** status **unknown** (ping **Allan** re roadmap). Form paths that post **Webflow → GHL** preserve UTMs better; **~60% coverage** style estimate mentioned (confirm definition with Ignite).
- **MX Merchant:** Many locations; **no clean join** to patient today; partial revenue in dashboards; effort to get **MX user IDs** for history.
- **Reverse ETL:** **dbt** + **Segment** from Snowflake to ads (**Meta**, **Google**, offline conversions, ~**400 locations**).
- **BigQuery bridge:** GA4, GBP, GSC into Snowflake for franchise reporting; **paused in Kippy era**, needs **recovery or rebuild**.
- **Looker Studio:** Fed by **`dev consumption`** tables; **ownership** moving from Ignite (**Jake**) to **Blaine**.

**Coordination:** **Matt** creates **Uptech ↔ Ignite** Slack, adds **Jake**; broaden **Embeddables / Lobby** Slack membership as Florence and Jake suggested.

## Uptech delivery (May 2026)

- **Russ** is **primary** on Gameday **data engineering** (Snowflake, Segment, warehouse and pipeline work, Jira rhythm and technical syncs with vendors and Gameday on the data layer).
- **Anthony** works with **Matt** on the **website** track (Webflow takeover, Ignite handover, AWS and Cloudflare Worker access and releases as that work lands).
- **Matt** steps in for **partner-level** topics (architecture reviews with Allen/Blaine, Grafted alignment, SOW or scope edges) when useful, and pairs with **Anthony** on web delivery.

## Ownership snapshot (who owns what today)

| Owner | Systems |
|--------|---------|
| Kippi | Snowflake, Knowi |
| Outliant | Webflow, Looker, SEO, ad spend |
| Nicole’s team | Monday.com, Zendesk |
| Lobbie team | Lobbie |

Other systems in the diagrams without a single named owner here: **GoHighLevel**, **MX Payments**, paid media platforms.

## Open questions (validate when you can)

From `notes/project-notes.md` and architecture notes:

- **Unified identity (blocking lifecycle):** Can we define **one durable user key** and **one location key** across Lobby, GoHighLevel, MX Payments, and warehouse tables? Conflicting location tables called out May 2026; see **Snowflake to Braze and identity** above.
- Does **MX Payments** data land in **Snowflake** today, or is reporting Lobbie-centric only?
- Are **ad platform metrics** (Facebook, Google, Instagram, TikTok) centralized in Snowflake?
- What **patient/appointment identifiers** are used across **GoHighLevel** and **Lobbie** for dedupe and matching? **(Ignite May 2026:** GHL **contact ID** ↔ Lobby **`go high level contact ID`** ↔ **patient UUID**; validate in their handoff diagram.)
- Is **GoHighLevel to Lobbie** integration real-time, near-real-time, or batched? **(Ignite:** non-telehealth **FTP**, ~**1–2 day** lag; **telehealth webhooks**, more immediate.)
- Are there **reverse sync** flows (Lobbie back into GoHighLevel) for lifecycle stage updates?
- **Zendesk to Monday:** Should tickets create or update Monday items, the reverse, or both? Which objects map to which ticket fields or brands?
- Should **franchise support** data ever flow into **Snowflake** or other reporting next to clinical and marketing metrics?

## Diagram and doc hygiene

- `architecture/ownership.md` references **`architecture/gameday-systems-and-ownership.png`** for a combined connections plus ownership visual. Regenerate or replace when ownership or scope changes (file may not exist in every clone until someone adds it).
- Canonical living docs in the architecture repo: `notes/project-notes.md`, `notes/decisions.md` (decision log is mostly empty; use it when you lock answers), `architecture/system-overview.md`, `architecture/current-state-architecture.md`.

## Franchisee portal and BI (Allen direction, May 2026)

- **Allen** intends to drive a **Q3 franchisee portal** built in **AWS** with **Supabase** for **identity and user management**, not only Power BI alone.
- **Near term:** **Power BI** evaluated for franchisee dashboards; **auth** is hard if reports must be **fully public**; **Premium capacity** vs **per-user** pricing under review; **Entra B2B guests** as likely pattern for external users.
- **Interim:** **scheduled email reports** possible while portal and embedding mature.
- **Later:** **Embed Power BI** inside the **custom portal** once it exists.
- **Sushma** trialing **Power BI Premium** for **guest access** behavior (short spike).
- Notes: `meetings/notes/2026-05-07-gameday-lobbie-webhooks-infrastructure.md` (meeting **2026-05-07**), actions `meetings/actions/2026-05-06-gameday-lobbie-webhook-powerbi.md`.

## Gameday data hub (internal direction, May 2026)

- **Gameday as integration hub:** Lobbie **webhooks → Gameday enriches →** Braze, warehouse, Facebook ads; stop ad-hoc messages **bypassing** Gameday. **Canonical Gameday user** + **centralized locations** (corporate vs franchise, each with **merchant ID**) called out as fixing attribution and MX/Lobbie matching pain.
- **API endpoints** expected **next day** after 2026-05-21; **webhooks ~1–2 weeks** on Gameday timeline; webhooks **required for Braze** and **Jackson**. **Gameday-owned metrics/counters**, not Lobbie-only.
- **Telehealth:** same appointment webhook + **type** param (no separate Segment integration).
- **Landing pages:** Claude-assisted builds; **gift card** page on GHL needs **UTM** before live (**Nicole**); **Clay** owns pages forward; template + tracking rules in prompts TBD.
- **Web:** Webflow **unmaintainable** post-Ignite (custom code blocks); **quiz funnel** needs **custom app** (location-scoped clinics, dynamic Q&A). Vision: agency landers → **standard booking** with attribution preserved.
- Full notes: `meetings/notes/2026-05-21-gameday-internal-data-architecture-landing-pages.md` (internal); Lobbie vendor: `meetings/notes/2026-05-21-gameday-lobbie-webhook-etl-sync.md`.

## Lobbie webhooks and AWS (May 2026)

- **2026-05-21 Lobbie call:** Registration **via API** in place; **appointment created** in test; **event list** to Russ. Lobbie target release **tonight or Monday** for appointment webhooks; **payment endpoints** in the **next** release after that. **API credentials** (client ID, tokens) promised for **3 corporate clinics**. Full notes: `meetings/notes/2026-05-21-gameday-lobbie-webhook-etl-sync.md`.
- **Integration pattern:** Webhook payloads are **discrete** vs legacy **S3 nightly ETL** shapes; plan **REST enrichment** on each event. **ETL** shifts to **reconciliation** (missed webhooks, location onboarding, **MX-to-Lobbie** payments). Lobbie can add **native IDs** to ETL dumps (their **code release**) for backfill and API joins.
- **Payments:** Goal is **Lobbie as single source of truth**; retire **MX Merchant** UI dependency while **Priority Gateway** stays the processor.
- **Telehealth:** Moving from **segment-only** to **webhooks**; appointment types flag telehealth vs in-clinic; **UTM endpoints** planned.
- **Earlier (2026-05-07):** Two developers on webhooks; **payload spec** and **broader partner API package**; **LCM / Braze** priority. Notes: `meetings/notes/2026-05-07-gameday-lobbie-webhooks-infrastructure.md`.
- **Lobby → Snowflake:** **nightly ETL**; still need explicit **dashboard gaps** vs dump where not covered by webhooks.
- **AWS:** Webhook **consumption** services planned **in Gameday’s existing AWS account** (confirm whether **Alliant** vs another vendor name for deploys).
- **GitHub Enterprise** access **blocked**; **Timothy** on support case; urgent before **Ignite** ends.

## Operational flags called out in notes

- **TikTok** campaign operations recently started (called out as newer channel).
- Franchise support runs in **Zendesk**; internal projects and comms use **Monday.com**.
- **SSL** configuration **still pending** (May 2026): **Timothy** on security software rollout; pull **Timothy** into **calls and Slack** until resolved.
- **Lifecycle/strategy feedback:** target **May 8, 2026** for overall strategy review (**Blaine**); quiz flow details expected from Blaine to Matt for dev sizing.
