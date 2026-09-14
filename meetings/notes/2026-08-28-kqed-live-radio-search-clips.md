# KQED: Live Radio Search Clips

**Date:** August 28, 2026
**Participants:** Matt New, Mark, Jon Holtan (Uptech); Julia Hughes (KQED)
**Source:** Granola (5ff4d750-7963-4ded-9349-4334d1a80067)

## Election feature scope

- Four election initiatives split across the team:
  - **Julia owns** voter guide, results, and live radio search clips
  - **Matt owns** alerts
- Timeline: September start; results only needed for a day or two around November 3
- Priority order: voter guide in-app first, then clips/hub, results last

## Live radio search clips

- Election-focused page in the app showing a list of clip cards (audio) and optionally articles
  - Users tap to play; no stitched/blended audio needed right now
  - Tab structure (All / Read / Listen) seen as valid and good
- Three-tier fallback for sourcing clips:
  1. Best: clipping tool Duke and bespoke are building for newscast (Julia investigating timeline)
  2. OK: query bespoke search API, display results as clip list
  3. Fallback: deep link to existing live radio search page with a pre-filled election query
- Bespoke search is fuzzy, not precise: clips often include buffer content and duplicates, so human curation preferred over full automation
  - Julia can talk to Keto about an editor manually picking clips and articles
  - Users do not need to know if curation is human or AI
- Suggestion prompts in live radio search are hardcoded; should change to election-focused queries now
  - Longer term: make them dynamic as news cycles change (Jon waiting on bespoke)
- Real-time streaming for bespoke search response is on Jon's list; could be a good moment to ship

## App architecture for the hub

- Need a list-of-clips view; currently only single-clip deep links exist
- Feed card (home screen entry point) managed via Strapi
- Hub content managed via a lightweight admin tool (Foggy Find pattern): separate admin tool on Deno Deploy, with override/takedown
- Voter guide: open in web view first, then iterate; follow mobile web design conventions and voter guide branding, not app branding
- Election alerts toggle: tap hub card to join/leave the Airship list directly, no need to visit preferences; module disappears after election season
