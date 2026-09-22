# KQED metrics review — action items

From "Bi-Weekly Metrics Review", Sep 16, 2026.
Note: `meetings/notes/2026-09-16-kqed-biweekly-metrics.md`

**Headline: activation went down despite the new onboarding flow, and 23% of users never reach the onboarding screen at all.** That is the thing to chase.

- [ ] **Uptech (Jon / Mark):** Investigate the **onboarding drop-off between first open and onboarding screen**. Only 77% arrive. Check **Strapi data loading** and the **GrowthBook toggle** as likely culprits. No Sentry alerts on the API side, so instrument the client path rather than assuming the API is clean
- [ ] **Matt:** Dig into **when we can trigger the ATT dialog**. What does Apple actually permit on timing and placement, how late can it fire before attribution degrades, and what does the data say about firing it at a different point in onboarding? Jon and Mark pushed back on delaying it because attribution breaks, so this needs a real answer on the constraint, not an assumption
- [ ] **Matt:** Explore a **pre-ATT explanation screen**. Research patterns from other apps (Apple TV cited) to frame tracking as a user benefit. This is the design half of the ATT question; the trigger-timing item above is the constraint half, and they need to be answered together
- [ ] **Matt:** Send his **individual goal list ahead of the in-person visit** (work goals plus food preferences), per Julia's ask
- [ ] **Julia (KQED):** Book time with **Min on email reactivation strategy**, running the 4-screen sequence via email with richer content
- [ ] **KQED editorial:** Sharpen the **top stories vs. breaking news** distinction for push, ahead of election coverage

## Carried over from Sep 2

- [ ] **Matt:** Update the **Push Alert / Airship instruction doc with election guidance** — still open, and more urgent now that election coverage is near
- [~] **Matt:** New ratings campaign — **deprioritized on Sep 16 given current workload**, even though the Android rating has slipped to 4.71. Revisit after Election 2026
