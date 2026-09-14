# LAist: App Redesign and Merlin Newsroom Tool

**Date:** September 8, 2026
**Participants:** Matt New (Uptech), Andy Cheatwood (LAist)
**Source:** Granola (7ce67d64-16da-4e63-86c1-8c5c2218e54f)
**Deals:** `LAist - New Mobile App`, `LAist - Internal Programming Tool (Merlin)`

## App Redesign: status and approach

- Andy's team spent the summer in research mode, resisting a one-to-one migration
  - Current product not working; need breathing room to rethink the experience
  - Plan: sketch broad strokes over the next month or two, then bring back to Uptech for collaborative scoping
- Andy sees Uptech as a thought partner, not just an executor
  - Bottleneck is now on his side: too many workstreams, not enough bandwidth to generate options
  - Wants the team to bring suggestions proactively, similar to how Matt works with Julia at KQED
- Web is being downsized in the migration; focus is the app
  - Web will pivot toward a personalized newsfeed experience
  - App-only features are the priority: Andy wants things that require coming into the app

## Newsroom tool: "Merlin" RFP

- Web-based internal newsroom assignment desk to replace a 7-year-old Airtable build
  - ~50 people in the newsroom; multiple newscasts and broadcast shows to coordinate
  - Airtable is expensive, unwieldy, does not integrate with CMS or broadcast scripting platforms
  - Story status updates rely on manual input from editors and reporters, making the data unreliable
- Core concept: a web-based story database
  - Each story is a slug with multiple deliverables (radio, web, social video)
  - Needs a queue for unvetted story ideas, status tracking, long-term project visibility
  - Hosting on AWS (or Supabase); low cost given it is text-heavy, not media
- Andy drafted an 18-page RFP with functional requirements from newsroom working sessions
  - Sending functional requirements doc Sep 8; full RFP once dates and rules are finalized
  - VP of Finance pushing it forward: wants cost and timeline before next budget season (no hard deadline)
  - Andy open to a follow-up call and can bring in the editor-in-chief to speak to pain points
- Matt flagged Jon as the right fit: built KQED's backend, internal tools, lightweight scheduling apps; on KQED web security and systems this fall

> **Correction (Matt, Sep 11):** Granola's summary overstates this. **Jon built the Mobile API for the KQED app, not the entire KQED backend.** Use the narrower claim in anything client-facing.
