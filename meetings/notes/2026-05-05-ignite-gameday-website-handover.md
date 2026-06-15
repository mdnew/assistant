# Gameday website handover — Ignite — 2026-05-05

Context: Conversation with **Ignite** on taking over **Gameday web** delivery; technical and PM context from their team.

## Team introductions (Ignite)

- **Florencia Carranza:** Project manager, on account since March 2023
- **William Morales:** Engineering manager, on project since start
- **Jefferson Soares (Jeff):** Tech lead since March or April 2023
- **Mary Lindsay:** Account director, supporting Florencia

## Uptech scope (reminder)

- Beyond web: originally CRM and data engineering (Snowflake), inherited DE infrastructure
- Long-term: mobile app plus supporting backend services

## Website architecture and infrastructure

- **Three-site model:** national corporate, regionals, microsites
- **Content:** Dynamic pull from **Yext**; reviews filtered to **4+ stars**, latest displayed; microsite treatments hidden when unavailable at clinic
- **Two runtime pieces (both required):**
  - **AWS-hosted** interface bridging external apps (**Yext**, **Snowflake**, **GoHighLevel**)
  - **Cloudflare Worker** rewriting or manipulating HTML server-side
- **AWS ownership:** Likely **Gameday account** with **delegated access to Ignite**; prior agency may still hold pieces. **Coordinate with Timon** for access and ownership clarity
- **Recent work:** Geolocation-enabled location finder; duplicate clinic page cleanup from prior agency; nav and footer redesigns in flight for peptides and vitamins pages

## Handover process and documentation

- **Monday.com:** Shared board, treated as daily project mirror; **partial view** while migrating from legacy **ClickUp**; **Q2** tickets mostly current, **Q1** history may be missing; Florencia updates Eastern business hours (~8am–4pm)
- **Docs incoming:** Tech stack diagram and integrations map **next week**; separate **data architecture** diagram exists; legacy **Lobby** docs stale, **current-state diagram** in progress
- **Process gaps:** Deployment process and backlog review **TBD**; **follow-up call** to walk **Monday.com** tickets
- **Resourcing:** **QA reduced to one person**, possible delays; clarify by **Friday** what is **committed web dev this week** vs **handover-only** work

## Access (Uptech)

- **Webflow:** Confirmed for **Anthony**
- **AWS:** Needed for backend services (pending coordination)
- **Other systems:** To be coordinated

## Related workspace context

- `context/gameday-architecture-attention.md` (takeover scope, tooling, open questions)
