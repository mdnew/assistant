---
posted:
quality (1-5):
engagement (1-5):
impressions:
reactions:
comments:
topics: product-management, analytics, onboarding, activation, funnels
notes: Draft for Wed Sep 23. Source: KQED bi-weekly metrics review Sep 16 (activation down after new onboarding flow; only 77% of users reach the onboarding screen; no Sentry alerts on the API side). Client unnamed. Natural sequel to the Sep 10 success-metrics post: that one was about setting the number, this one is about what to do when the number goes the wrong way.
---

We shipped a new onboarding flow and activation went down.

Cleaner screens, fewer steps, the thing everyone agreed was better. Then the number moved the wrong way, and the room did what rooms do. Maybe the copy. Maybe the order of the screens. Maybe we should test a variant.

Then someone pulled the step before the step we changed. Only 77% of users were reaching the onboarding screen at all. Almost a quarter of the drop had nothing to do with the flow we spent weeks on. They never saw it.

The likely culprits are boring. Content not loading in time, or a feature flag firing a network call that quietly fails. Nothing showed up in error monitoring, because nothing was broken in the way monitoring understands broken. People just were not getting there.

Two things I am taking from it.

First, when a metric moves against you, check the denominator before you debate the design. It is very easy to spend a sprint optimizing step two while step one leaks.

Second, silence from your alerting is not evidence. A drop-off that produces no errors is the most expensive kind, because it looks like a product problem and gets treated like one.

The redesign might still be great. We genuinely do not know yet, and I would rather say that out loud than pick the story that flatters the work.

What is the step before the step you are optimizing?
