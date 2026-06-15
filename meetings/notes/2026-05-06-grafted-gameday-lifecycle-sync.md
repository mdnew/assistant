# Grafted + Gameday sync — 2026-05-06

Cross-functional sync on data pipeline, Braze, creative/strategy progress, and coordination.

**Granola transcript:** https://notes.granola.ai/t/f0de0db2-ae2d-4a55-a278-5b3add8c1d92

## Data pipeline and Snowflake integration

- **Russ:** Built **user attribute syncing from Snowflake to Braze**
  - Stream and connector **ready for testing**
  - Demo version running in **Snowflake**
  - **Obfuscated schema sample** ready to share (PHI-safe)
  - Braze path options: **cloud data ingestion** vs **direct connector** (direct connector described as **~$10k upcharge**)

- **Architecture challenges (called out in meeting):**
  - **No unified user ID** across **Lobby**, **GoHighLevel**, **MX Payments**
  - Each platform uses **different ID formats and naming**
  - **Location mapping:** ~**four** location-related tables with **conflicting IDs**
  - **Kippy** team did not resolve ID conflicts during their tenure

- **Follow-up session:** Meeting scheduled with **Ignite / Outliant** (warehouse vendors; notes sometimes say “Outlier”) **the day after this sync** to review **data warehouse work from the past year**
  - **Goal:** Identify **source of truth** for user attributes and **ID mapping**
  - **Approach:** Start from **high-confidence** data points; **enrich** as understanding improves

## Project updates and coordination

- **Blaine:** Presented to **FAC** leaders; **strong reception**, **Gameday** segment stood out vs other presentations; support for direction and **transition from Outliant**

- **SSL:** Still **pending**; **Timothy** tied up with **security software rollout** (delays). Plan to add **Timothy** to **future calls** and **Slack** for visibility

- **Creative:** Image selection and **Figma** mockups in progress (**Barry** driving strategy implementation). Cropping and template overlays for visual review

- **Strategy feedback deadline:** **May 8, 2026** for overall strategy review
  - **Blaine** to review **that evening** after Outliant transition work
  - Focus: **structural fit** vs nit-level copy edits

## Next steps (see actions file)

| Owner | Item |
|-------|------|
| Russ | Send **obfuscated schema sample** to **Barry** |
| Matthew + Russ | **Ignite / Outliant** meeting on **data warehouse architecture** (scheduled day after this sync) |
| Barry | Follow **Timothy** on **SSL** (email + Slack) |
| Blaine | Complete **strategy review** by **May 8** |
| Blaine | Send **quiz flow** details to **Matthew** for development sizing |
| Nicole | Finish **Slack workspace** setup with correct **billing** |

## Related context

- `context/gameday-architecture-attention.md`
- `meetings/notes/2026-05-05-ignite-gameday-website-handover.md`
