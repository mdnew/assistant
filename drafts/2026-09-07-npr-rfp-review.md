# NPR RFP Response: Review and Gap Analysis

**Prepared:** September 7, 2026
**Bid:** Option 3, Track B Only (Native Mobile Architecture & Production Engineering)
**Submission window closes:** September 8, 2026

Reviewed against the NPR App RFP, the NPR FAQ / Tech Research document, and the current Uptech Studio proposal.

---

## Round 1 Scoring Weights (for prioritization)

| Criterion | Weight |
|---|---|
| Design, UI/UX Craft & Multimodal Experience | 25% |
| Product Strategy Understanding & Audience Discovery | 20% |
| Content Architecture & Network Curation | 15% |
| Technical Architecture & Native Mobile Build | 15% |
| Commercial Terms, Financials & Stability | 15% |
| Multi-Agency Governance & Work Plan | 10% |

**Qualification threshold:** 4.00 out of 5.00 weighted consensus score to reach the Round 2 shortlist.

Note the structural challenge: 45% of the Round 1 score sits in design and product strategy criteria. As a Track B bidder we still have to score on those, "as they pertain to your selected Track." They should be answered through the implementation lens: design integrity through the build, technical feasibility input during discovery, design system fidelity.

---

## Fix Before Sending

### 1. The pricing model is the one NPR explicitly discourages

The RFP states twice that milestone-based payments tied to tangible deliverables are strongly preferred, and that "proposals relying purely on Time-and-Materials (T&M) or flat monthly retainers for the core build are highly discouraged."

Our pricing slide is hourly T&M at $50,000 per month. Commercial Terms is 15% of the Round 1 score. This is the highest-value edit available before submission.

**Our constraint:** Uptech bills every two weeks and cannot carry months of unpaid work. NPR also operates on Net 30.

**These are compatible.** The RFP's objection is not to frequent invoicing. It is to paying for time with no tangible output, and to open-ended retainers. Nothing prevents defining a large number of small milestones.

#### The core move

Define a milestone per sprint, each with a named tangible deliverable, and invoice on acceptance of that deliverable. The proposal already promises monthly internal builds, so the artifact exists. A sprint milestone reads like:

> **Sprint 7 (bi-weekly):** On demand audio player with livestream handoff, CarPlay Now Playing integration, delivered as an internal TestFlight and Play Internal Testing build with release notes.

That satisfies both "tied to tangible deliverables" and their requirement that invoices be "heavily itemized by track, phase, and specific deliverable," while preserving a two week payment cadence. NPR gets accountability, we get cash flow.

#### Three provisions that protect cash flow

**A mobilization milestone at contract execution.** This is the largest exposure. With Net 30 and a first delivery 30 days out, we would be 60 or more days unpaid at the start. Front-load a kickoff milestone paid on signature, tied to a real deliverable so it does not read as a naked deposit: technical architecture document, repository and CI setup, integration plan against CDS and their existing API layer, and environment provisioning. Roughly 8% of the total. Standard and easy to justify.

**Deemed acceptance language.** Milestone billing fails on slow acceptance, and the risk is real here because NPR's engineering governance mandates internal review of all vendor-authored code before merge, and their review capacity is not under our control. Proposed terms language:

> Each milestone deliverable is deemed accepted if NPR does not provide written objection identifying specific acceptance criteria failures within five business days of delivery.

Without this, a busy reviewer can hold an invoice indefinitely without intending to.

**Retention instead of back-loading.** NPR will want value withheld until launch. Offer that as a small retention across every milestone (5 to 10%) released at Code Handoff, rather than allowing whole milestones to be pushed to the end. Same accountability for them, materially better cash profile for us.

#### Proposed structure against the $600,000 cap

| Milestone | Trigger | Amount |
|---|---|---|
| Mobilization | Contract execution. Architecture doc, repo and CI setup, integration plan | $50,000 |
| Sprints 1 to 24 | Bi-weekly, each on accepted sprint deliverable and build | ~$21,700 each |
| Phase gate: Private Beta | January 2027, beta accepted | Gate only, no payment |
| Phase gate: V1 Launch | September 2027, App Store and Play live | Gate only, no payment |
| Retention release | Code handoff and documentation accepted | $30,000 |

The two phase gates carry no payment of their own. They are checkpoints where NPR can stop or renegotiate, which is the real purpose of their milestone preference, and they cost us nothing in cash timing.

#### Replacement copy for the pricing slide

Replace the "Hourly (time & materials) billing for actual work performed" bullet with:

> **Milestone-based billing.** Work is organized into two week increments, each with a defined deliverable and acceptance criteria agreed in advance. We invoice on acceptance of each increment, Net 30, itemized by phase and deliverable. A mobilization milestone at contract execution covers architecture definition and environment setup, and 5% of each milestone is retained and released at final code handoff.
>
> Phase gates at Private Beta and V1 Launch give NPR formal checkpoints to confirm scope and direction before the next phase proceeds.

This answers the milestone preference, the itemized invoicing requirement, and Net 30 in a single block. It also reads as more disciplined than the current T&M framing, not less.

#### Residual risk

Net 30 is stated as NPR's standard and is unlikely to move, so we carry roughly 30 days regardless of structure. The mobilization payment is what prevents that from becoming 60 or 90 days at project start.

### 2. No rate card by role

RFP Financials: "Please indicate the charges associated with roles in U.S. dollars, including the key driver of staff by role and experience." We never give a rate by role.

They also ask whether we offer service bundles and what effect bundling has on pricing. Also unanswered.

The RFP states that blank responses, or responses of "to be determined," are not acceptable.

### 3. The budget math will get scrutinized

$50,000 per month across 3 developers, plus a Product Designer, PM, and Partner, works out to roughly $100 per hour for the developers alone with the other three roles unfunded.

NPR states explicitly that they are not selecting the lowest bid, and encourages respondents to be "as aggressive and creative as possible." A number this low against a ground-up platform targeting 5x WAU growth risks reading as under-scoped rather than as value.

**Recommendation:** Either raise the number, or add a paragraph that honestly explains team allocation. As written, the team slide (3 dedicated developers) and the budget do not reconcile.

### 4. Say "Swift" and "Kotlin" in writing

The architecture slide says "native iOS and Android applications" but never names the languages.

Given that Uptech is publicly associated with Flutter, and KQED appears in Flutter's own showcase, an evaluator could reasonably assume a cross-platform approach. Cross-platform frameworks and web wrappers are excluded for core experiences.

**Recommendation:** Name Swift and Kotlin explicitly. Mention MVVM to align with their existing app architecture.

### 5. We hedge on a stated non-negotiable

Accessibility slide currently reads: "we will need to discuss and agree to what level we are comfortable satisfying the range of WCAG 2.1 Level AA standards."

WCAG 2.1 and ADA compliance is listed as a non-negotiable. That sentence is also close to the prohibited "to be determined."

**Recommendation:** Commit to WCAG 2.1 AA and describe the mechanics: contrast tokens, Dynamic Type support, VoiceOver and TalkBack passes, automated checks in CI. Note that design-dependent items depend on Track A output.

### 6. Our backend proposal may conflict with what NPR owns

We propose a single TypeScript API that consumes "the CMS." Per their documentation:

- CDS is the central API hub and single source of truth for all client applications
- They already run an API layer positioned between the client apps and CDS
- They own encoding, storage, CDN strategy, DRM, and core streaming architecture
- Grove CMS itself is out of scope for the RFP

As written, this reads as if we are proposing to rebuild something they already have. Their FAQ does permit "new client-facing microservice development... if required by the proposed UX and feature set."

**Recommendation:** Reframe as integrating with CDS and their existing API layer, with a thin client-facing layer proposed as an option, deployed to NPR's cloud infrastructure and handed over at completion.

### 7. Compliance gaps in Company Background

Enumerated asks in RFP Section I that are currently unanswered:

- How many employees are dedicated to account management and/or technical support
- How many employees are full-time, part-time, or independent contractors
- Whether we will subcontract any components (needs an explicit "no," or details)

Blank responses are stated as unacceptable.

### 8. No metrics anywhere

Round 1 is explicitly a "Qualifications & Portfolio Review." Every rubric asks for KPIs, organizational impact, and engagement metrics before and after.

We have two short case study paragraphs and zero numbers. Even two or three real KQED figures would move this.

---

## Substantive Gaps Worth Adding

The proposal is at 39 of a 40 page limit, and the limit includes supporting documentation. Four of the six full-bleed section title slides are pure page spend, so cutting them frees room.

### Figma-to-production is the named Track B qualifier and we do not answer it directly

The RFP: Track B vendors "must demonstrate experience translating external Figma design systems into production code." Section E adds: "Proposals should outline a clear strategy for integrating a Figma library into the project lifecycle which keeps branding consistent and ensures accessibility."

We have the ideal story (Metalab led discovery and directional design at KQED, we took it to production and carried the design work forward) but it appears only as two bullets in the executive summary.

**Recommendation:** Give it a dedicated slide with the actual workflow: token pipeline, component parity, design QA loop, and how we handle gaps in the spec.

### Station co-branding and multi-tenancy

240+ Member stations, the Organization Service for branding metadata, localized curation, local sponsorship management, and the explicit goal of stations adopting this as their primary mobile presence.

This is arguably the hardest engineering problem in the brief and the proposal does not mention it. Content Architecture and Network Curation is 15% of the score.

### The integration matrix

We cover CMS, analytics, and push notifications. Unaddressed must-integrate systems:

- Algolia search
- Single Sign-On infrastructure
- NPR API entitlement services (NPR+ benefits, member station donations)
- Organization Service (branding and station metadata)
- Feature toggles and in-app messaging
- Consent management (GDPR / CCPA)
- Dynamic ad serving and ad quality monitoring
- Crash reporting

**Recommendation:** A single table naming each system and our integration approach closes this cheaply.

### NPR's mandated code review

Their engineering governance requires internal review of all vendor-authored code and technical design prior to merge and production deployment. They state that our staffing profile is used to size their internal review capacity.

We mention peer review and private GitHub repositories but never address theirs.

**Recommendation:** State where repos live (their organization), and our PR cadence and batch sizing so their reviewers are not swamped.

### Handoff without retainers

Their Track B deliverable list includes complete technical architecture documentation, and the requirement is that deliverables be "fully maintainable by NPR's internal Product Design and Technology Teams upon completion without ongoing retainers."

Our Support Options slide leans the other direction, and there is no knowledge transfer plan.

**Recommendation:** Name documentation as a deliverable, and add an engineer onboarding and pairing plan.

### Sub-second start performance

Called out as an explicit technical evaluation criterion: "Technical evaluations explicitly require architectures supporting sub-second start performance." Not mentioned in our proposal.

**Recommendation:** Address audio start latency, prewarming, cold start budgets, and how we would measure it.

### Video

The platform is explicitly text, audio, and video, with fluid format switching as a core capability. We cover audio and articles only.

### Cross-device continuity

Our Saved Favorites slide says local storage only, and defers accounts until "user accounts become a higher priority."

That reflects KQED's situation, not NPR's. They have SSO infrastructure and cite Netflix-grade cross-device resume as a benchmark. As written, this slide argues against a requirement.

### UGC, community, and live events

Moderated discussions, user-submitted audio and video commentary to newsrooms, and virtual or local live events are explicitly in scope. Unaddressed.

### Multi-agency governance (10% of score)

They ask for the mechanism for settling conflicting viewpoints, communications cadence, governance model, and decision-making approach, plus examples of workshops and co-design sessions.

We have the strongest possible proof point in the KQED and Metalab precedent and are leaving it on the table.

### Legal and commercial terms

They require that material terms be disclosed in the response, and their standard provisions cover NPR ownership of deliverables, code escrow, indemnification, and insurance. Also required and currently missing or thin:

- A travel and expenses estimate (a number, not "we don't anticipate the need")
- Acknowledgment of the 5% T&E cap and prior written authorization requirement
- Itemized third-party costs (software licenses, font licenses, API usage fees)
- Net 30 payment terms, which we never state
- A commitment to invoicing itemized by track, phase, and deliverable, since generic "Professional Services" line items will not be accepted

### Track A partner option

The RFP permits naming a pre-existing partner agency for the complementary track where there is a proven track record of joint delivery. Metalab would fit. Given that 45% of the Round 1 weighting sits in design and strategy criteria, this could materially help, though it is likely too late to formalize before the deadline.

---

## Typos and Cleanup

- **Page 35:** "launching a beta version in January **2025**" should be 2027.
- **Page 35:** timeline phases sum to roughly 13 to 14 months, but pricing assumes a 12 month project at $50,000 per month. Reconcile.
- **Page 22:** the Donations slide says the same thing twice. The new "support experience" paragraph and the old "Our Approach" both land on external flows versus in-app processing. Merge them. The title still says Donations while the body argues for Support.
- **Page 24:** "we currently operate four separate buckets" reads as Uptech operating them. That is KQED context.
- **Page 13:** "the appropriate path to get their over time" should be "there." Also "what will to motivate" is missing a word.
- **Page 4 vs 6:** "10-year history" against "Founded in 2016" is fine for 2026, just keep both consistent.
- **Add a compliance line** answering RFP III.1 explicitly: "Option 3: Track B Only (Native Mobile Architecture & Production Engineering)."

---

## Submission Email

Their RFP requires Joel, Monica, and Kahlia on every message.

**Subject:** Uptech Studio RFP Response: NPR Next-Generation Mobile Platform (Track B)

Hey Joel, Monica, and Kahlia,

Attached is Uptech Studio's response to the NPR Next-Generation Mobile Platform RFP. We are bidding Option 3, Track B Only: Native Mobile Architecture and Production Engineering. It's a single consolidated PDF, within the 40 page limit.

Thanks again for the time on the 25th, and for staying on past 5 your time. That conversation and the FAQ document shaped a lot of how we approached this.

A few things worth flagging as you read:

Native Swift and Kotlin throughout, aligned to the MVVM architecture your current apps use. No cross platform frameworks in the core experience.

Our KQED engagement is the closest analog we have to what you're describing, and not just because it's public media. Metalab led discovery and directional design, and our team took that into production and carried the design work forward from there. That is the same shape as the Track A and Track B split in your governance model, with the same team that would be on this.

Pricing is structured around milestone based billing tied to the deliverables you named, with a firm budget cap rather than an open ended engagement.

Public radio matters to a lot of us here, so this is a project we would genuinely love to work on.

We're available for the Round 1 presentation any day September 14 through 16. Happy to answer questions before then, and I'll make sure all three of you are on anything we send.

Thanks!
- Matt

**Notes on the email:**

- The milestone billing line assumes we make that change. Pull it if we keep hourly T&M.
- No question about cross-platform. Their FAQ answers it in writing, so raising it now would suggest we did not read the document.
- File naming: `Uptech-Studio-NPR-Mobile-Platform-Track-B-Proposal.pdf`

---

## Key Dates

| Milestone | Date |
|---|---|
| RFP responses due | August 31 to September 8, 2026 |
| NPR internal review | September 9 to 11, 2026 |
| Vendor intro and 30 minute presentation | September 14 to 16, 2026 |
| Finalists notified | September 17, 2026 |
| Finalist presentations | September 21 to 25, 2026 |
| Contract award | September 29, 2026 |
| Private Beta | January 2027 |
| App 1.0 live | September 2027 |
