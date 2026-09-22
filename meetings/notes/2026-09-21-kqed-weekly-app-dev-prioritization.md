# KQED - Weekly App Dev Prioritization

**Date:** Sep 21, 2026, 11:30 AM PDT
**Participants:** Matt New (Uptech), Mark (Uptech), Jon Holtan (Uptech), J. Hughes (KQED), M. Wu (KQED)
**Source:** Granola (`3d5d557f-01a4-4461-aad0-3bdf158aee8b`)

## Election alerts: notification toggle decision

**Decided: the election alerts toggle lives only in the Elections Hub, not in the full Notification Center.**

- Tapping an election alert will not expose the broader notification settings page. The change stays isolated to the new elections notification channel
- The Notification Center overhaul is **deferred until email notifications are ready**. Airship kickoff for email work is later today. Email will complement in-app push (news, product announcements)
- When the Elections Hub is removed post-election, alerts stop automatically. Users cannot opt out mid-cycle, and the list carries forward to the next cycle, so future elections and runoffs do not start from scratch
- Team aligned this is an app-side call. Mwu to give Kim and Brian a heads-up, no approval needed

## Election build status

- Development builds are in review but testable now
- **Real election data flowing by Mon Sep 28**, the in-person week
- Matt's work this week: election analytics (2-3 parts), notification toggle changes plus an analytics event for the toggle, and a design feedback pass

## Upcoming feature prioritization (decided next week, in person)

Topics on the table: automated QA, livestream improvements, playback improvements, widgets.

- **Livestream improvements flagged high priority.** Recurring user complaints building in support. Complex because foreground, background and lock screen behaviors all interact, and Flutter adds overhead versus native
- **Live Activities floated for election night** and it is a natural fit: clear start and end, polls open through results called. Jon found a Flutter package that may handle Live Activities on both iOS and Android. Decision deferred to the in-person session
- Matt did the initial widgets exploration

## Google Cast and Watch tab

- **Google Cast ticket deprioritized.** Mark reviewed it and it is not viable at this stage. May resurface when the Watch tab gets a broader rethink
- **Watch tab usage is higher than expected, roughly 10% of users select it.** Slide-in traffic correlates with Watch tab taps. Current assumptions about Watch demand may be wrong, worth a conversation before any dev work

## In-person visit planning (week of Sep 28)

- **Monday:** app-focused. Most KQED staff do not come in Mondays
- **Tuesday:** broader KQED product team (Teresa, Caroline, Suching, Kevin). Jon meets the TV team about Watch tab performance, others welcome. Email team meeting to be scheduled this day
- **Wednesday:** Jason on-site, mostly web and Cody focused
