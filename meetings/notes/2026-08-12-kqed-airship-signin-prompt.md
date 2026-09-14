# KQED: Airship prompt for Sign In / Sign Up

**Date:** August 12, 2026
**Participants:** Matt New, Mark (Uptech); Julia Hughes, Michelle Wu (KQED)
**Source:** Granola (b0a08743-51cf-40b9-8c3e-06f281a335df)

## OKR context and Airship data

- **OKR: grow weekly signed-in users 20%, from ~7K to 8.5K, within ~6 weeks**
- Current baseline just under 8K, target feels within reach
- Airship now receiving logged-in/member user attributes (recently rolled out)
  - iOS data available; **Android blocked by Play Store**
  - ~12-16K iOS users identified as logged-out, enough to start targeting
- Logged-in users already ~8K despite no forced login, driven largely by live streamers avoiding pledge breaks

## Prompt design and targeting logic

- Delivery via Airship custom HTML, shown only to users with the logged-out attribute set (not unknowns)
- CTA: "Not Now" dismisses; signing in sets campaign goal and stops future prompts
- Initial CTA links to My KQED tab; may later deep-link straight into login flow if friction observed
  - Julia flagged a known issue: personalization sends users to My KQED tab rather than the login screen
- Trigger thresholds:
  - Breaking news prompt currently uses 10 article views; slow to reach, may drop to 6
  - Login prompt should use a lower threshold
  - Home feed scrolling floated as an alternative trigger (~20% of users scroll at all)
  - Specific in-app events (saving, game play) also viable
- Frequency: 30 days between prompts proposed. Combined logic possible (10 article views + 30-day cooldown)

## Benefit messaging

Current mockup benefits are placeholder; need refinement per segment:
- **Live radio listeners:** pledge-free streaming (frame as "eligible for pledge-free" to avoid overpromising)
- **Article readers:** save articles, personalized feed, Foggy Find score history
- **Game players:** save Foggy Find streak (avoid "streaks" for crossword until built)

Julia suggested reordering: pledge-free streaming at top, saving at bottom; replace "follow topics" with "personalize". A Google News Initiative coach independently suggested "just ask people to log in", validating the effort.
