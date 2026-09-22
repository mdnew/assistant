# KQED: Bi-Weekly Metrics Review

**Date:** September 16, 2026
**Participants:** Matt New, Mark, Jon Holtan, Cody Swartz (Uptech); Julia Hughes, Michelle Wu, Bryan Bindloss, K Low, Jasmine Garnett, Ki Sung (KQED)
**Source:** Granola (96d54508-0452-4e00-b3db-b872bbf7cc82)

## Acquisition and ratings

- **Best install week in 12 weeks.** Store visitors back over 1,000, total installs at 700
- Organic bump likely driven by pre-pledge messaging (continuous listening stream push) and site slide-ins
  - Radio V4 and TV slide-ins both spiked, but pledge activity may be masking the true source
  - Pre-pledge emails shifted messaging to "log in to get pledge-free stream," pushing login over direct link
- **Android rating slipping: now 4.71**, combined iOS/Android around 4.8
  - New Android ratings campaign floated but **deprioritized given current workload**

## Activation funnel issues

- **Activation rate went down despite the new onboarding flow**
- Big drop between first open and onboarding screen: **only 77% of users even see the onboarding screen**
  - Suspected cause: Strapi data not loading, or a GrowthBook toggle causing a failed network call
  - Jon noted **no Sentry alerts on the API side**, so no confirmed failures
- **ATT prompt flagged as a likely drop-off trigger**
  - KQED users skew less app-savvy and react to tracking prompts with high paranoia
  - Bryan's Experiences Hub test showed a similar reaction to social/surveillance features
  - Idea: a **pre-ATT screen** explaining what tracking is and why it is benign ("to serve you better content"), similar to Apple TV app patterns
  - **Jon and Mark pushed back on delaying ATT:** attribution breaks if the prompt is deferred
- **Push notification pre-prompt is working:** measurable lift in opt-ins since adding it
- **10% of onboarding users tapping "Watch TV"**, higher than expected
  - Julia has a meeting end of September with a new TV director about improving the watch tab
  - Risk flagged: auto-setting the homepage to Watch after a casual tap would be a bad experience

## Conversion, engagement, retention

- **Pledge driving strong conversion: $15K raised last week, average donation $98.** Donation trend line now flat instead of declining
- Active members up the week of the 6th, tied to pre-pledge membership emails
- Push engagement low on some messages. **Top stories vs. breaking news distinction needs sharper editorial thinking, especially ahead of election coverage**
  - Top 2 carousel stories consistently get the most clicks (prime home feed real estate)
- Week 1 retention holding **above the 30% target**
- Uninstalls trending down
- 4-screen reactivation sequence has only hit screen 1 so far, needs more time to evaluate
- Email flagged as a high-leverage retention channel for KQED's audience
  - Idea: run the same reactivation sequence via email with richer content (programming, news context)

## On-site visit

Julia asked each person to send what they want to accomplish during the in-person visit (work goals, plus food preferences).
