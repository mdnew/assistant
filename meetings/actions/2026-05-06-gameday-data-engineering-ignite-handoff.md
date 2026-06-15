# Gameday data engineering (Ignite walkthrough): follow-ups, 2026-05-06

From `meetings/notes/2026-05-07-gameday-ignite-data-engineering.md` (meeting **2026-05-07**).

## Ignite and Gameday commitments from the session

- [ ] **Jake (Ignite):** Send **data join diagram** mapping **GHL contact IDs** to **Lobby patient IDs**; ensure **Russell** receives the **handoff document**
- [ ] **Russ:** Contact **Allan** re **Lobby** gaps (including missing attribution tracking); confirm whether Lobby plans a fix and on what timeline
- [ ] **Jake (Ignite):** Transfer **Looker Studio** dashboard **ownership and access** to **Blaine**

## Matt (Uptech)

- [ ] **Slack:** Create **Uptech ↔ Ignite** coordination channel (notes said “Optek”; use **Uptech** naming unless Gameday requests a literal channel name)
- [ ] **Slack:** Invite **Jake Daniels** to that channel
- [ ] **Slack:** Add required people to existing **Embeddables and Lobby** channel (coordinate list with Florence / Jake / Russell)

## Track as open technical / product items (no single owner on this list)

- [ ] **BigQuery → Snowflake** path for GA4, GBP, GSC: **unpause or rebuild** for franchise dashboard
- [ ] **MX Merchant:** pursue **user ID** or join strategy so payments reconcile to patients in warehouse and reporting
- [ ] **Lobby UTM preservation:** escalate with Allan / Christian roadmap; unblock **campaign-level** truth in GHL and downstream tools
- [ ] **Braze attributes:** reconcile **Graphid vs Grafted** naming; align Ignite join doc with Russell’s Snowflake → Braze stream testing
