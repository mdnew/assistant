> **Source:** `gameday/meeting-notes/2026-05-28-gameday-uptech-lobbie-sync.md` (synced 2026-06-02)

# Gameday × Uptech × Lobbie sync

**Date:** 2026-05-28  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)  
**Transcript:** [Granola notes](https://notes.granola.ai/t/8179ab04-c275-4c21-a5aa-f367b39b03f3)

## Participants

**Referenced:** Russell Cloak (Gameday Central / canonical identities), Cristian (individual BAAs with clinics), franchisees (MX vs Lobbie payment adoption), Uptech (BAA / AWS compliance), Lobbie (payment matching, SMS proxy, Partner API)

## Summary

The sync focused on **payment and identity fragmentation** between **MX Merchant** and **Lobbie**: MX lacks reliable **unique customer identifiers**, causing duplicate records and weak soft-matching—only **~30%** of payments flow through Lobbie today, with franchisee **change-management** resistance for the rest. That blocks **loyalty**, **customer history**, and **mobile app** payment plans unless reconciliation improves.

**Lobbie** mitigates via **MX Merchant ID ↔ Lobbie ID** association, confidence scoring, and **manual franchisee review**; the **Lobbie Partner API** path (framable payment forms, in-app) creates **unified records** for new transactions. **Gameday Central** strategy: Russ builds **canonical user/location identities**; enrichment pipeline **Lobbie → Gameday Central → LCM/Braze**, phased from **appointment webhooks** (imminent) before fuller **payment** integration as Lobbie adoption grows—possibly driven by **franchisee portal** / **loyalty** requirements.

**Comms consolidation:** notifications today span **GHL**, **Lobbie**, **MX**, and planned **Braze**; Lobbie is adding **SMS proxy via GHL** for consistent numbers and per-location appointment settings. **Braze** targets **corporate/transactional** with local clinic contact info; **GHL** stays for **direct clinic–patient** conversation.

**Implementation:** API access to **3 corporate CA clinics + 3 Florida** locations; **production-only** (no sandbox); **appointment webhooks** starting immediately; **LCM** can proceed without payment data. **Compliance:** franchise-level **BAA** complexity for Uptech vs **Cristian’s** existing clinic BAAs; **AWS RDS Postgres** HIPAA posture and possible additional **BAA** needs.

## Payment system integration challenges

| Topic | Notes |
|--------|--------|
| **MX Merchant IDs** | No required **unique ID** (email, phone, etc.) → **duplicate customers** per location; **soft matching only**, not 100% reliable. |
| **Volume split** | **~30%** of payments via **Lobbie**; remainder **MX direct**—legacy process + franchisee resistance to switching. |
| **Downstream impact** | Fragmented **transaction history**; hard to tie payments to customers → blocks **loyalty** and complicates **mobile app** payments. |

## Data reconciliation solutions

| Approach | Notes |
|----------|--------|
| **Lobbie (current)** | Force association of **MX Merchant ID** to **Lobbie ID**; surface **potential matches** to franchisees for **manual review**; confidence-based matching + manual cleanup for ambiguous cases. |
| **Lobbie Partner API** | Route payments through Lobbie → **unified records**; **framable payment forms** for in-app; avoids matching problems for **new** transactions. |

## Gameday Central development strategy

| Topic | Notes |
|--------|--------|
| **Canonical identities** | Russ building canonical **users** and **locations**. |
| **Enrichment pipeline** | **Lobbie → Gameday Central → LCM/Braze**. |
| **Phasing** | Prioritize available sources: **appointment webhooks** first (**releasing tonight / next week** per notes); **payment data** as Lobbie adoption increases. |
| **Adoption lever** | **Franchisee portal** requirements; **loyalty program** may require new payment flow through Lobbie. |

## Communication system consolidation

| Source | Role today / planned |
|--------|----------------------|
| **Go High Level** | Appointment reminders, lead nurture; remains **direct clinic–patient** channel. |
| **Lobbie** | Appointment notifications, form reminders; **SMS proxy through GHL** for consistent patient-facing numbers; per-location notification config. |
| **MX Merchant** | Payment receipts. |
| **Braze** | Planned **corporate** communications—**transactional** with **local clinic contact** info. |

## Technical implementation plan

| Item | Notes |
|------|--------|
| **Clinic API access** | **3 corporate (CA)** + **3 Florida** locations for development. |
| **Environments** | **Production only**—no sandbox currently. |
| **Webhooks** | **Appointment events**—start **immediately**. |
| **LCM** | Automation development can proceed **without** waiting on payment data fixes. |

## Compliance & legal requirements

| Topic | Notes |
|--------|--------|
| **Franchise BAAs** | Uptech may need **BAAs with each clinic** for patient data access. |
| **Alternative model** | **Corporate visibility limits** + **row-level security** instead of broad franchise data access. |
| **Current state** | **Cristian** has **individual BAAs** with all clinics. |
| **AWS / HIPAA** | **RDS Postgres** HIPAA-eligible by default; may still need **additional BAA execution**—review required. |

## Action items

| Owner | Action |
|--------|--------|
| Lobbie / Gameday | Enable **appointment webhooks** (tonight / next week per notes). |
| Russ / platform | Continue **canonical identity** and **Lobbie → Central → LCM/Braze** pipeline. |
| Product / ops | Define **loyalty / franchisee portal** requirements that may mandate Lobbie payment flow. |
| Uptech / legal | Resolve **BAA** model (per-clinic vs RLS-limited corporate access vs Cristian’s existing BAAs). |
| Uptech / infra | **HIPAA compliance review** for AWS database setup; execute BAAs if gaps found. |
| Dev | Use **6-clinic** API access (3 CA corporate + 3 FL) in **production**; plan around **no sandbox**. |
| Comms owners | Align **Braze corporate transactional** vs **GHL direct** vs **Lobbie/GHL SMS proxy** boundaries. |

## Review checklist

- [ ] Confirm **appointment webhook** release date (tonight vs next week).  
- [ ] Verify **6 clinic** list names and API credentials process.  
- [ ] Document **~30% Lobbie payment** baseline and adoption target.  
- [ ] Legal sign-off on **BAA** strategy (Uptech per-clinic vs RLS vs Cristian coverage).  
- [ ] Map **LCM** automations that can ship before payment reconciliation.  
- [ ] Confirm **Lobbie Partner API** timeline for in-app / framable payments.
