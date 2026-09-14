# KQED: Election 2026 Ideas

**Date:** August 26, 2026
**Participants:** Matt New, Jon Holtan, Mark (Uptech); Julia Hughes, Michelle Wu (KQED)
**Source:** Granola (cfaa21b3-eb48-41c2-b93c-26204f7733b1)

## Voter guide in app

- Biggest feature, most pieces to figure out
- Currently a WordPress/Gutenberg site, excluded from the mobile app
- Mobile API assumes everything is a post; needs changes to handle pages
- Feed currently filters out election articles, leaving almost no content during election season
- Voter guide content publishes in bulk, needs special feed handling
- Goal: keep users in app when tapping voter guide promos (currently exits to browser)
- Approach: match mobile web styling, keep it simple, no custom extras

## Election alerts and notifications

- Expose the existing notification settings page (built by Mark, not yet surfaced)
- Add "Elections 2026" as a notification category; use Airship to drive opt-ins
- Likely one toggle, not multiple (not enough content to justify granular options)
- Two alert types:
  - Scheduled pushes for key dates (voter registration deadline, ballot return), coordinated with the news team
  - Automated pushes when election-tagged content publishes, via WordPress webhooks
- Julia to ask Noah about setting up WordPress webhooks so the system listens for publishes rather than polling
- Podcast/radio alerts also noted: easier since Uptech controls that data; recurring alerts for favorite shows floated
- Caroline built a live election results feed (official AP-style source); could push real-time race updates election night
  - Unclear whether to plug into her pipeline or the spreadsheet; need a demo

## Sequencing and stretch goals

- Two workstreams start now, without news team input:
  - Voter guide rendering in app (Julia driving)
  - Election notification opt-in and alert setup (Matt driving)
- News team input needed later for message copy and send timing
- Bonus: radio/podcast election playlist using the new segment-sharing feature

## Election week success metrics

- 500+ new installs
- Notification opt-in rate toward 25% target
- 8,000+ article views
- 30,000+ active users (never hit before during election week)
- 130-150 Foggy Find completes
