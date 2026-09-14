# KQED: Voter Guide

**Date:** August 25, 2026
**Participants:** Matt New (Uptech); Julia Hughes, Michelle Wu (KQED)
**Source:** Granola (a87b763c-9ef9-459a-9a59-37a6b8823f4c)

## App feature priorities for election coverage

- Core parity work: voter guide pages open in-app (web feature baseline)
- App-specific features to drive installs and differentiation:
  - Automated "latest election news" playlist (radio content collections)
  - Election-night live results hub (Caroline building an AI/API tool for faster results pulling)
  - **Ballot scratch pad:** personal, private space to track how users are leaning on races
- Word searches can be scheduled against known upcoming articles (no extra content work)
- Target segments: **Evidence Builders** (breaking news, politics, government, daily updates) and **Inquisitive Explorers** (social issues, equity, local races). Not Boundary Keepers
- Coverage depth: heavy focus on school board races across all nine counties; props covered but not deeply updated; city-level measures only if newsworthy

## Election push notifications strategy

- Proposed three-tier notification structure:
  1. **Breaking news** (wildfires, major events; rare, always-on)
  2. **Top stories** (editorial / Jasmine-scheduled; most regular sends)
  3. **Elections** (new, opt-in segment; targeted to politics-interested users)
- Elections segment keeps election content from flooding non-interested users for two months
- Segmentation options:
  - "Local politics" interest category already stored in Personalize; users already opted in
  - Can push that data into Airship to build a matching segment
  - Or create a dedicated Airship segment for election opt-ins via in-app prompt
- Opt-in campaign idea: prompt users who have politics selected but push disabled
- Swap the current push notification promo for an elections-specific campaign starting October
- Automation possible via content tags (posts tagged for the elections landing page); could auto-trigger without Jasmine's involvement
- Notification settings screen (built by Mark, not yet live) should surface elections as an explicit category
- Geographic segmentation (East Bay vs Marin vs South Bay) tabled until after the election

## Slide-ins

- Update kqed.org slide-ins in October to promote app downloads with election-specific value props: breaking news on local races, sound bites from radio coverage, real-time results on election night
- Key open question: will editorial (Jasmine) commit to scheduling election-specific alerts
