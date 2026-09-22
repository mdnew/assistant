# Pipeline — Notes and Context

**HubSpot is the source of truth** for stages, amounts, close dates, and CRM activity. This file carries the story: risks, next steps, and the context that does not fit in a CRM field. If this file and HubSpot disagree on a fact, HubSpot wins and this file gets corrected.

**Synced from HubSpot:** September 18, 2026
**Scope:** active pipeline only (open deals, excluding the Cold stage). 11 deals. See the "active pipeline" rule in `CLAUDE.md` for the canonical query.

Owners: **MN** Matthew New · **AK** Adam Korman · **CC** Claude Ciocan

---

## Snapshot

| Deal | Stage | Amount | Weighted | Close | Owner |
|---|---|---|---|---|---|
| KQED - 2026/2027 Web Development | Contract sent (SOW) 90% | $700,000 | $630,000 | 10/01/26 | MN |
| KQED - 2026/2027 Mobile Development | Contract sent (SOW) 90% | $600,000 | $540,000 | 10/01/26 | MN |
| Phillips - Rate Increase | Contract sent (SOW) 90% | — | — | 07/31/26 ⚠️ | CC |
| Schedulefly - Billing Migration | Proposal sent 50% | — | — | 12/31/25 ⚠️ | AK |
| Victory Live - Will Clark | Estimates (In Progress) 30% | — | — | 08/15/26 ⚠️ | CC |
| Jasper - web portal | Estimates (In Progress) 30% | — | — | 07/31/26 ⚠️ | CC |
| Mogul - New Deal | Exploration (NDA) 20% | — | — | 09/30/25 ⚠️ | AK |
| Golf Agronomics - New Deal | Exploration (NDA) 20% | — | — | 08/31/26 ⚠️ | CC |
| LAist - Internal Programming Tool (Merlin) | Exploration (NDA) 20% | — | — | 09/30/26 | MN |
| Gameday - Team Expansion | Possibility (Email) 10% | — | — | 09/30/26 | AK |
| LAist - New Mobile App | Possibility (Email) 10% | — | — | 12/01/26 | MN |

⚠️ = close date in the past

**Quantified pipeline: $1.3M gross, $1.17M weighted, all resolving by Oct 1, 2026.** Only two of eleven deals carry a current amount, so weighted totals understate reality rather than forecasting it.

**Sep 18: NPR closed lost**, taking $600K gross and $300K weighted out. What remains is **almost entirely the two KQED SOWs**, which are one document. The quantified pipeline is now a single point of failure.

---

> **Note on KQED (Sep 11, 2026):** Uptech is **running hot on the current KQED budget**, so Matt is **intentionally throttling his billable KQED work until the new SOW starts in October**. Low utilization on KQED through September is deliberate. See `decisions/2026-09-11-throttle-kqed-billable-work-until-october-sow.md`. **Matt's read: these SOWs will happen, it is a question of papering them up.** The Oct 1 date is a contracting milestone, not a competitive risk. **Update Sep 16: both deals moved to Contract sent (SOW) 90%**, which now matches Matt's read.

## Matt's deals

### NPR - New Deal — $600K, **CLOSED LOST 09/18/26**
The big one, and the nearest deadline. Bid is **Option 3, Track B only** (Native Mobile Architecture & Production Engineering). RFP submitted Sep 8 against a submission window that closed that day.

> **Outcome: lost at the Round 1 shortlist cut, Sep 18.** Joel Sucherman emailed that NPR narrowed to "a small group of finalists" and Uptech is not among them. No reason given beyond a competitive field. Door left open: "hope to stay connected", "keep your agency in mind for future opportunities." Email archived at `inbox/npr/2026-09-18-joel-sucherman-rfp-declined.md`. **HubSpot set to Closed Lost, close date 09/18/26.**
>
> **Worth doing:** ask Joel for debrief feedback while the evaluation is fresh. We bid Track B only against criteria that were **45% design and product strategy**, and we still do not know whether that framing, the price, or the national-vs-local answer is what sank it. That answer is reusable for LAist and the next public radio RFP.

**History below is kept for the next public radio pursuit.**

**Sep 8:** Matt sent the response to Joel Sucherman, cc Monica Ostolaza and Kahlia Ali. Single consolidated PDF, **Track B only**. Flagged in the cover note: native Swift and Kotlin throughout on MVVM, no cross-platform frameworks in the core experience (per NPR's request); the KQED engagement as the closest comparable, where Metalab led discovery and directional design and Uptech carried the design work forward, which is why the Track A/B split fits; and **milestone-based billing tied to named deliverables with a budget cap**, not an open-ended engagement. Offered availability for the Round 1 presentation **any day Sep 14-16**.

**Sep 8, 2:30 PM — Kahlia Ali replied:** "We look forward to reviewing the proposal for Track B. I will be in touch shortly with timing options for the upcoming presentations."

**Sep 10 — presentation options sent to NPR.** **Sep 14 — NPR picked: Round 1 presentation is Tue Sep 15, 10:00-10:30 AM PT.** Kahlia's agenda: **15 minutes presentation, 15 minutes Q&A**, open to more Q&A if preferred. Zoom.

**11 NPR attendees**, including four who were not on the Aug 25 intro call: **Vincent Farquharson, Emily Barocas, Bryan Moffett, Malik Abdullah**. Returning: Michael Seifollahi, Laura Galbraith, Erica Osher, Kahlia Ali, Monica Ostolaza, Joel Sucherman.

**Resolved:** the milestone pricing restructure did go out, not the original T&M slide.

Their schedule, per `drafts/2026-09-07-npr-rfp-review.md`:
- NPR internal review: Sep 9–11
- **Vendor intro + 30 minute presentation: Sep 14–16**
- Finalists notified: Sep 17
- Finalist presentations: Sep 21–25
- Contract award: Sep 29
- Private beta Jan 2027, App 1.0 live Sep 2027

**Risks carried into the submission.** Round 1 needs a 4.00/5.00 weighted consensus to reach the shortlist, and **45% of that score sits in design and product strategy** criteria that a Track B bidder has to answer through an implementation lens. The review flagged that our pricing slide was hourly T&M at $50K/month, which the RFP explicitly discourages in favor of milestone payments tied to tangible deliverables (Commercial Terms is 15% of the score). Recommended fix was a milestone-per-sprint structure against the $600K cap, plus a mobilization milestone at contract execution, deemed-acceptance language at five business days, and 5–10% retention across milestones instead of back-loading.

**Sep 15 — Round 1 presentation delivered**, 10:00 AM PT, 11 NPR attendees. Three partners presented: Adam on design, Claude on dev, Matt on product. Track B only. KQED carried the proof (2 stars to 4.8), with Radio Paradise for multi-platform breadth (Android Automotive, CarPlay, Apple TV). Stack pitched: native Swift/Kotlin on MVVM, a **single TypeScript API layer** in front of CDS and entitlements, everything in **NPR's own accounts and GitHub from day one**. Pricing presented as **~$600K on monthly milestone billing**, beta Jan 2027, V1 Sep 2027.

**What the room actually pushed on.** Two things, and both should shape Round 2:
- **National vs local.** NPR's own stated hardest problem: a national app that still feels local across ~240 stations of wildly different size. They framed it as a **co-design platform** and reached for an MLB co-branding analogy. KQED cuts both ways as a reference here, it is a single Bay Area station.
- **Fixed dates, undefined scope** (Bryan Moffett). Beta January and V1 September are hard targets with scope not yet settled. Matt named the NPR-vs-member-station conflict of interest out loud; NPR answered with the co-design framing.

On innovation we deferred to their strategy, offering two paths (deep local community on a KCRW events model, or leaning on national content assets like Wait Wait and Tiny Desk) and recommending Track A start with personas, segmentation, and journey mapping. **Worth having a point of view here before Round 2 rather than deferring again.**

**Schedule slipped two days:** Michael Seifollahi said finalists will be told **by end of week, Fri Sep 19**. The published schedule said Sep 17. Finalist presentations Sep 21–25 and award Sep 29 are unchanged, which compresses finalist prep to a weekend if we make the cut.

**Next:** nothing to drive on the deal. **Debrief ask sent to Joel on Sep 18**; if he comes back with anything substantive, capture it here for the next public radio RFP.

### KQED - 2026/2027 Mobile Development — $600K, Contract sent (SOW), closes 10/01
Renamed from "KQED - 2026/2027 SOW" on Sep 9. Paired with the Web Development deal below; together they are the 2027 KQED relationship.

> **One document, two deals.** Mobile and Web are **combined into a single SOW**. Matt deliberately keeps them as **separate deals in HubSpot** for tracking, but there is only one contract, so they **close together or not at all**. Do not treat them as independent bets, and do not report one advancing without the other.

**Sep 15: SOW sent. Sep 16: it is with Julia, who takes it to legal.** Both deals moved to **Contract sent (SOW) 90%** in HubSpot on Sep 16.

**Next:** legal review is the gate. Nothing to drive until Julia's legal comes back.

### KQED - 2026/2027 Web Development — $700K, Contract sent (SOW), closes 10/01
Renamed from "KQED - 2026 Extra Devs" on Sep 9. Web budget conversation with Jason goes back to the Aug 31 standup.

**Staffing is contingent on this SOW, not underway.** There is no web team until this closes. **Jason Cater** would be the Technical Architect running it; **Julia Hughes** is PM. Matt introduced **Neil Matatall** (ex-Twitter, GitHub, ActBlue; worked with Uptech on RealPractice) to both on Sep 2 as a candidate, keeping him warm ahead of the deal. **Update Sep 9 (BD check-in): Neil was well received at KQED and it is now pending his decision to join.** Separately, **Harris is replacing Cody** at KQED with **Frankie Lee bridging** to make a full-time equivalent.

The dependency runs SOW first, then staffing. Do not treat the Neil thread as onboarding.

**Next:** same single SOW as Mobile above, now with Julia for legal review. Keep Neil warm in the meantime — legal is the last gate before staffing can actually start.

**Sep 9 (BD check-in):** the KQED SOW goes first of everything in the pipeline. **Six bullet points sent and Julia approved the structure**; only the number was outstanding. **Resolved: the combined SOW went out Sep 15.** Run a billing report Oct 1 2025 to now, partner clients, to confirm total billed before setting it (time tracking moved to Keito on Sep 21; pull from Harvest if the Keito import is not reconciled yet). Prior billing was ~$375 mobile-only plus separate security and website budgets.

### LAist - Internal Programming Tool (Merlin) — Exploration (NDA), closes 09/30
Created Sep 9 off the **call with Andy Cheatwood (LAist)** on Sep 8. Internally LAist calls this **"Merlin."**

**Scope, from the Sep 8 call:** a web-based internal newsroom assignment desk replacing a 7-year-old Airtable build. ~50 people in the newsroom, multiple newscasts and broadcast shows to coordinate. Airtable is expensive, unwieldy, does not integrate with the CMS or broadcast scripting platforms, and story status depends on manual editor/reporter input so the data is unreliable.

Core concept is a story database: each story is a slug with multiple deliverables (radio, web, social video), a queue for unvetted ideas, status tracking, and long-term project visibility. Text-heavy rather than media, so hosting on AWS or Supabase is cheap.

**Andy drafted an 18-page RFP.** Functional requirements doc was going out **Sep 8**; full RFP follows once dates and rules are set. **Their VP of Finance is driving it** and wants cost and timeline before next budget season. No hard deadline yet.

Matt positioned **Jon** as the fit here. **Jon built the Mobile API for the KQED app, not the entire KQED backend** (corrected by Matt, Sep 11). He has also built internal tools and lightweight scheduling apps, and is on KQED web security and systems this fall.

Andy's Sep 4 email confirms **the RFP, functional requirements, and early wireframes are all already written.** He described it there as the newsroom **budgeting** platform and "the central hub of our newsroom's story tracking", connected to key content distribution services. He was unsure whether Uptech does this kind of work; Matt confirmed they do, citing the editorial infrastructure tools built for KQED.

**This is the further-along of the two LAist deals.** The app work is a Nov/Dec RFP; Merlin has documents ready now.

**Sep 11:** the doc had not arrived, so Matt sent a low-pressure nudge naming Jon as the fit. **Now waiting on Andy.**

**Next:** when the doc lands, share with Jon and come back with a ballpark on scope and cost.

### LAist - New Mobile App — Possibility (Email), closes 12/01
**Revived Sep 9** from "LAist - Flutter App," which had been parked in *No Fit Currently* since May. Carries **14 notes** of history from that earlier run, the richest record of any Matt-owned deal. Reframed from a Flutter-specific build to a general new mobile app.

**No amount.** The old Flutter scope carried $15,000; that was cleared on revival because we have not seen the new app yet. Price it once scope is visible.

Second LAist pursuit alongside Merlin, both off the Andy relationship.

**Scope, from the Sep 8 call:** Andy's team spent the summer in research mode and is deliberately resisting a one-to-one migration of the current product, which is not working. They will sketch broad strokes over **the next month or two**, then bring it back to Uptech for collaborative scoping. That timing is why this closes 12/01.

**Web is being downsized** in the migration; the app is the focus, pivoting web toward a personalized newsfeed. Andy wants app-only features, things that require coming into the app.

**Andy wants a thought partner, not an executor.** He said the bottleneck is on his side, too many workstreams and not enough bandwidth to generate options, and he explicitly wants Uptech bringing proactive suggestions, the way Matt works with Julia at KQED. That is the relationship to play for here.

**This is a competitive RFP, not a direct award.** Per Andy's Sep 4 email: designs and specs by **November**, **RFP process restarts Nov/Dec**, **build starts January**. The 12/01 close date is the RFP restart window, not a signature.

**The opening:** Andy's **CEO is "very anxious to level up our app game."** She has been patient with a roadmap Andy cannot adjust because of his team's commitments. **Andy is already talking to a strategic consultant about doing something sooner** and explicitly wants to discuss options. That is both the competitive risk and the way in: whoever helps him give his CEO something before January is positioned for the January build.

History: the original May 8 proposal was a **Flutter rebuild**. Andy said it "looks great" and "checks most of the boxes," but timing killed it (stream upgrade plus major CMS migration starting July, CMS work running through the fall). He has since moved off a 1:1 migration entirely. The Flutter framing is dead.

**Next:** wait for their v1 framework, then identify gaps and additions. Introduce Andy to **Sarah Marks** (designed for KQED, now embedded with their team) when the app project moves forward. Separately, come back to Andy on the "something sooner" question before the strategic consultant fills that space.

---

## Other owners

### Phillips - Rate Increase (CC) — Contract sent (SOW) 90%, close 07/31 ⚠️
**Highest-probability deal on the board and the most stalled.** At 90% since Jul 31 and not modified since. No amount, no notes. A rate increase at contract-sent that goes quiet for six weeks usually means it needs a nudge, not more time.

### Mogul - New Deal (AK) — Exploration 20%, close 09/30/25 ⚠️
Reassigned from Matt to Adam on Sep 9. **Adam has taken it over and is running with it**, including the Jeff-to-Sarah design intro that had been sitting on Matt since mid-August.

Close date is a **full year past** and there is no amount on the record, so the CRM understates it. Worth Adam re-dating and pricing rather than leaving it looking dormant. The live path is a design engagement: Jeff has no appetite for outsourced engineering and was lukewarm on the $165/hr senior design rate.

### Schedulefly - Billing Migration (AK) — Proposal sent 50%, close 12/31/25 ⚠️
Proposal sent, close date **eight months past**. Created Dec 2025. No notes.

### Victory Live - Will Clark (CC) — Estimates 30%, close 08/15 ⚠️
**Sep 9 (BD check-in): emerging as Claude's potential anchor project.** Started as a couple of devs but could expand if the first engagement goes well. **Will requested a rate card and team bios**, and they had a **security incident over the weekend**, which makes the timing good. Rate card should be framed as **budget-based, not 40hrs x rate**.

Two notes, last contact Aug 4, record touched Sep 7.

### Jasper - web portal (CC) — Estimates 30%, close 07/31 ⚠️
**Sep 9 (BD check-in): low budget, low priority, not being pushed.** Untouched since Jul 15.

### Golf Agronomics - New Deal (CC) — Exploration 20%, close 08/31 ⚠️
**Sep 9 (BD check-in): not pursuing.** Uptech advised them to find an ERP consultant; not much opportunity here. **Should move to Closed Lost or No Fit Currently in HubSpot** — flagged, not changed, since it is Claude's deal.

Created Aug 26, untouched since Sep 2, close date already past. No amount, no notes. Reassigned from Matt to Claude on Sep 9.

### Gameday - Team Expansion (AK) — Possibility 10%, close 09/30
**Sep 9 (BD check-in): the Gameday SOW is open-ended and likely was not intended to be.** Claude to nail down status with Blaine ASAP. Gameday also needs to expand for the anchor-client model to balance.

**21 notes, last contact Sep 8** — the most actively worked record in the CRM despite the lowest stage. Adam owns it; Russ runs Gameday data engineering. Does not appear in Matt's standups, which is correct given that split.

---

## Hygiene

Carrying over from the Sep 9 sync:

1. **Most deals have no amount.** Any forecast is currently three deals wide.
2. **Six have close dates in the past**, one by a year. Overdue dates make stage probability meaningless in aggregate.
3. **Most records have zero notes.** Gameday (21), LAist New Mobile App (14), and Victory Live (2) are the only ones with CRM history.
4. **~90 deals sit in the Cold stage** going back to 2018 and are excluded from this file by design.
