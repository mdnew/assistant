# NPR Mobile App Redesign & Build Presentation — Uptech (Round 1)

**Date:** September 15, 2026
**Participants:** Matt New, Adam Korman, Claude Ciocan (Uptech); Michael Seifollahi, Laura Galbraith, Erica Osher, Vincent Farquharson, Kahlia Ali, Monica Ostolaza, Emily Barocas, Bryan Moffett, Malik Abdullah, Joel Sucherman (NPR)
**Source:** Granola (8d4b77f0-76bd-4e2b-9a5c-b2356391fda3)
**Deal:** `NPR - New Deal`

## What we presented

Focused pitch on **Track B (build/execution) only**, not Track A. Three partners presented: Adam on design, Claude on dev, Matt on product.

Proof points used:
- **KQED**: app rating went from 2 stars to 4.8
- **Radio Paradise**: Android Automotive, Android Auto, CarPlay, Apple TV, analytics overhaul

## Proposed tech stack

- Native mobile: Swift/SwiftUI (iOS), Kotlin/Jetpack Compose (Android), MVVM architecture
- **Single TypeScript API layer** in front of all internal services (CDS, entitlements, etc.)
  - Reduces attack surface, enables fixes without a full app store release cycle
  - Third-party SDKs (Algolia, analytics, crash reporting) connect directly from the client
- Design-to-code sync via Figma tokens or Token Studio, collaborative feedback during the design phase
- All code and infrastructure in **NPR's own accounts and GitHub from day one**

## Q&A

**National vs local (NPR's stated biggest challenge).** Building a national app that still feels local to each market. KQED is Bay Area specific; NPR must serve ~240 stations with varying resources. NPR framed it as a **"co-design" platform**, citing an MLB co-branding model as a loose analogy.

**Innovation.** Uptech acknowledged this is hard to answer without knowing NPR's strategy. Two paths discussed: go deep into local communities (KCRW events model) or leverage national content assets (Wait Wait, Tiny Desk). Recommended starting Track A with personas, segmentation, and customer journey mapping.

**Multi-platform (Malik).** Confirmed experience with TV, CarPlay, Android Auto, Android Automotive. GraphQL API layer proposed as a way to serve different payload sizes across clients.

**Biggest concern (Bryan).** Fixed target dates (beta January, V1 September) with scope still undefined. Matt flagged a potential conflict of interest between NPR and member stations; NPR clarified the co-design intent.

## Pricing and process presented

- Estimate: **~$600,000 total**
- Timeline: beta by January 2027, V1 by September 2027
- **Monthly milestone billing** tied to discovery outputs, then monthly dev builds
- Cadence: daily standups, weekly priority check-ins, biweekly dev demos, monthly roadmap/retros
- Handoff philosophy: NPR team participates throughout, so no documentation-heavy transition needed

## Next step

**Await NPR's shortlist decision.** Michael indicated finalists will be communicated **by end of week (Fri Sep 19)**.
