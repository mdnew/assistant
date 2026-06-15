# Gameday / Lobbie webhook — follow-ups (2026-05-21)

**Context:** `meetings/notes/2026-05-21-gameday-lobbie-webhook-etl-sync.md`

## Uptech (Russ / data engineering)

- [ ] Confirm receipt of **webhook event list** from Lobbie; document payload types and enrichment needs.
- [ ] Design **webhook consumer** flow: register webhooks via API, handle **appointment created** first, enrich via **REST API** where needed.
- [ ] Plan **native ID** usage once Lobbie adds IDs to ETL dumps (backfill and join strategy).
- [ ] Define **ETL reconciliation** jobs for missed webhooks, location onboarding, and **MX-to-Lobbie** payment migration.

## Uptech (Matt / coordination)

- [ ] Track Lobbie **API credentials** for **3 corporate clinics** (client ID, tokens).
- [ ] Confirm Lobbie release timing (**tonight or Monday**) for appointment webhooks; note when **payment endpoints** ship.

## External (Lobbie)

- API credentials for 3 corporate clinics.
- Release with appointment webhooks (target tonight or Monday).
- Payment endpoints in subsequent release.
- Native IDs in ETL dumps (code release TBD).
