> **Source:** `gameday/meeting-notes/2026-06-01-weekly-seo-website-prioritization.md` (synced 2026-06-02)

# Gameday — Weekly SEO & Website Prioritization

**Date:** 2026-06-01  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)  
**Transcript:** [Granola notes](https://notes.granola.ai/t/2a9199b7-5924-4ce3-aa54-a8297804f976)

## Participants

**Referenced:** Nate (development), Nick (duplicate-content epic), Nicole (PostHog access), Blaine (Yelp pixel deferral, Segment), Ignite (Hot Jar request)

## Summary

The group stood up a **new SEO/website-focused project board** with clearer status columns and a **weekly Ready for Dev** queue for Nate. All work from the legacy **Uptech board** was migrated; new items should land on the board **as soon as they are identified** (e.g. Father’s Day landing page).

**Critical site issues** dominated prioritization: **broken navigation** (top priority), **duplicate content cleanup** (highest-priority epic from Nick), a **hidden mobile “Book Now”** CTA, and **severe Core Web Vitals** performance (~37 on desktop and mobile). **Access and tracking** gaps were cataloged—Hot Jar, PostHog, GTM, Segment, cookie consent / GA4, and **UTM attribution** on landing pages.

**This week’s Ready for Dev queue** (in order): navigation fix → duplicate content → Father’s Day banner → mobile booking button → CWV improvements. **Yelp pixel** slips to next month; **Meta** integration escalated internally and will align with a **server-side tracking** overhaul. **Microsoft Clarity** recommended for mobile UX insights.

## Project board & workflow

| Column / practice | Notes |
|-------------------|--------|
| **To Do** | Backlog of all items. |
| **Design** | Items needing design work. |
| **Ready for Dev** | Planned weekly work for Nate—populated during this meeting. |
| **In Dev, Testing, Done, Not Doing** | Standard execution columns. |
| Intake rule | Add upcoming work **immediately** when identified (Father’s Day LP example). |
| Weekly planning | Drag items into **Ready for Dev** during these meetings. |
| Migration | All items moved from old **Uptech** board to new SEO/website board. |

## Critical website issues

| Issue | Severity / notes |
|--------|------------------|
| **Navigation** | Breaking site functionality—**top priority**. |
| **Duplicate content** | **Highest-priority epic** (Nick). |
| **Mobile “Book Now”** | Completely hidden—buried in hamburger menu **below chat widget**; all traffic is mobile → major conversion blocker; need **sticky CTA** like desktop. |
| **Core Web Vitals** | ~**37** on desktop and mobile; **lazy-loaded text** site-wide causing delays; plan to **remove unnecessary animations** to improve speed. |

## Access & tracking setup

| Platform | Status / need |
|----------|----------------|
| **Hot Jar** | Heat mapping—request via **Ignite**. |
| **PostHog** | A/B testing—Nicole has access; **add team**. |
| **Google Tag Manager** | Access needed for **cookie consent** investigation. |
| **Segment** | Blaine added team. |
| **Cookie consent / GA4** | Sharp traffic drop after consent rollout; **~15s delay** before cookies load; need **Google Consent Mode v2**. |
| **Landing page attribution** | **UTM parameters not flowing** through to booking—audit **all existing landing pages**. |

## Development priorities this week

**Ready for Dev queue (order):**

1. Navigation fix (critical)  
2. Duplicate content updates (highest priority)  
3. Father’s Day banner implementation  
4. Mobile booking button fix  
5. Core Web Vitals performance improvements  

**Deferred / parallel tracks:**

| Item | Direction |
|------|-----------|
| **Yelp pixel** | Blaine pushing to **next month**. |
| **Meta integration** | Escalated internally; coordinate with **server-side tracking** overhaul. |
| **Microsoft Clarity** | Recommended for **mobile UX** insights. |

## Action items

| Owner | Action |
|--------|--------|
| Team | Add new work to board **immediately** when concepts emerge (e.g. Father’s Day LP). |
| Team | Keep **Ready for Dev** current during weekly SEO/website meetings. |
| Nate | Execute queue: navigation → duplicate content → Father’s Day banner → mobile Book Now → CWV. |
| Nick | Drive **duplicate content** epic (highest priority). |
| Nicole | Extend **PostHog** access to team. |
| Ignite | Request **Hot Jar** access. |
| TBD | Obtain **GTM** access; implement **Consent Mode v2**; reduce cookie load delay. |
| TBD | **Audit landing pages** for UTM → booking attribution. |
| Blaine | Yelp pixel **next month**; Meta + server-side tracking coordination. |
| TBD | Evaluate **Microsoft Clarity** for mobile UX. |

## Review checklist

- [ ] Confirm project board link/name for new SEO/website board.  
- [ ] Link Nick’s **duplicate content** epic in tracker.  
- [ ] Verify Father’s Day banner **design/assets** and launch date.  
- [ ] Document mobile sticky CTA **design spec** (parity with desktop).  
- [ ] Baseline CWV before/after animation and lazy-load changes.  
- [ ] Track Consent Mode v2 + GA4 recovery after 15s delay fix.  
- [ ] Landing page UTM audit scope and owner.
