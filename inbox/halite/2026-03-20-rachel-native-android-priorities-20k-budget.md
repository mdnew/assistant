---
Forwarded: Hi! 

Thanks for meeting again.  I really appreciate the conversation so we can figure out what we need to do. 

I spoke with Harsha and we agree that we need to move forward with Native on Android.  

Here's the priority list at a high level:

1. Moving everything Harsha's created using React Native to Native and output a TCCC.
2. Multi-user
3. Multi-patient
4. Off-line first

Budget to start: $20k

I'd like to see where this gets us, with the option to increase the budget as we move forward.  

Let me know if that sounds good.  I recognize that the quoted features exceed $20k, but I'd like to see how far we can get with the current budget.

Have a good weekend. 

Warm regards,
Rachel


On Tue, Mar 17, 2026 at 4:53 PM Matthew New <matt@uptechstudio.com> wrote:
Hey Rachel - here’s a link to Claude and my shared calendar if you want to grab a time. It looks like we are both available at 11:30


30 Minute - Claude/Matt
calendly.com


On Mar 17, 2026, at 4:08 PM, Rachel Wong <rachel.wong@halitemedical.com> wrote:

﻿
Hey Matt - Do you have time for a chat tomorrow morning? 

I have some questions and then I can walk you through our thinking.

Thanks,
Rachel

On Tue, Mar 17, 2026 at 2:54 PM Matthew New <matt@uptechstudio.com> wrote:
Hi Rachel,

Thanks for the context. It’s really helpful to understand how you and Harsha are working together right now. Happy to walk you through the costs. Our rate is $150/hr for a US-based, senior full-stack developer. We work in 8-hour days, so that comes out to $1,200/day. The estimates below are based on those numbers.

---

C-STAR — Air Force 711th Performance Wing

Phase 1 (P0)
• Multi-User: 5–8 days | $6,000–$9,600

Phase 2 (P1)
• Central Command View: 4–6 days | $4,800–$7,200

C-STAR Subtotal: 9–14 days | $10,800–$16,800

---

LASD — LA Sheriff's Department

Phase 2 (P0)
• Multi-Patient — min 2 per medic: 4–6 days | $4,800–$7,200

Phase 2 (P1)
• ePCR Output (LASD format): 6–10 days | $7,200–$12,000
• Non-Trauma Workflows: 4–6 days | $4,800–$7,200

LASD Subtotal: 14–22 days | $16,800–$26,400

---

ANTX-CT26 — Navy / Austere Field Deployment

Required (P0)
• Austere / Offline-First Architecture: 9–15 days | $10,800–$18,000
• On-Device AI Integration: 6–10 days | $7,200–$12,000
• HIPAA Compliance: 6–10 days | $7,200–$12,000
• Audit Trail: 6–10 days | $7,200–$12,000
• ePCR (JTTR / JoMoS — military format): 5–10 days | $6,000–$12,000
  (Incremental on LASD ePCR)

Required (P1)
• Role-Based Access Control: 6–10 days | $7,200–$12,000

ANTX-CT26 Subtotal (P0+P1): 38–65 days | $45,600–$78,000

---

Future Items — ANTX-CT26 (P2/P3)

• HRI Algorithmic Alerts: 4–6 days | $4,800–$7,200
• Sensor Integration: 4–6 days | $4,800–$7,200
• ATAK / BatDoc Architecture: 2–4 days | $2,400–$4,800

Future Items Subtotal: 10–16 days | $12,000–$19,200

---

A few things worth keeping in mind as you look at these:

The shared capabilities (multi-user, multi-patient, ePCR) are counted once across all deployments, so there’s no double-billing as Halite expands from LASD to the Navy.
The ANTX-CT26 range is wide because the exercise details were still TBD when we spoke. Once you have more from the Navy side, we can tighten those up.
These estimates already factor in AI-assisted development, which meaningfully reduces the time compared to traditional development approaches.

Happy to set up a call to walk through any of this with you and Harsha. We really want to figure out a way to work with you that makes sense for where you are right now.

Thanks!
- Matt



On Mar 17, 2026 at 9:03:53 AM, Rachel Wong <rachel.wong@halitemedical.com> wrote:
Thanks Matt. 

Let me talk to Harsha and get back to you. 

Right now, Harsha pretty much owns the product. I have input when it comes to features and capabilities, and did some initial work on the UI design.  We also have other mockups in Figma from when we worked with a UI/UX designer, but those were more focused on the waiting room for emergency medicine.  

Harsha now owns all updates. I'd love to be more involved but don't have the time.  Right now, I use the tech whenever he releases updates.  It sounds funny, but I watch The Pitt (on HBO) and let the tech run to see if it's picking up people, medical terms, etc. 

Do you have cost estimates for each of these? Or is there an hourly rate? Can you help me understand the cost?  

Thanks,

Rachel

On Mon, Mar 16, 2026 at 11:31 AM Matthew New <matt@uptechstudio.com> wrote:
Hi Rachel and Harsha,

Claude and I really enjoyed our conversation last week with you guys and we're super excited about what you're building at Halite. We spent some time going through the stories on Friday and came up with the following high level estimates covering both frontend and backend work across the different deployments.

A couple things:

The reason we estimated both the frontend and backend work for all three deployments is because we’ve had some bad experiences on projects where split up the work strictly along frontend/backend lines. Unfortunately, we’ve found that it can create friction, especially when the teams aren't working the same hours. If Harsha isn't always available when our team is working, that can introduce delays and overhead with handing off code. 

One model that could work better in practice is dividing ownership by feature rather than by layer. That way each team owns a full slice of functionality end-to-end. If that makes sense, we could set up a planning session to talk through that before we get started.

We put these estimates together assuming that we will be leveraging AI-assisted development. As Harsha already knows based on his own experience, what that really means is that we’re trying to estimate how long it will take for us to dial in each story based on the feedback we get from you. Not just a checkbox that the feature is done. So if any estimates look high, that’s because we’ve tried to anticipate a feedback loop between our two teams.

These estimates do not include any design or product work. One thing that we’re noticing now that development moves a lot faster is that someone needs to really own how the product needs to work. That can either be done upfront by working with you or through iterations of development. Curious how you and Harsha handle this now. 

On to the estimates...

---

C-STAR — Air Force 711th Performance Wing

Phase 1 (P0)
• Multi-User: 5-8 days
  (Shared capability - also satisfies LASD Phase 1 and ANTX-CT26 P1)

Phase 2 (P1)
• Central Command View: 4-6 days

C-STAR Subtotal: 9-14 days

---

LASD — LA Sheriff's Department

Phase 2 (P0)
• Multi-Patient — min 2 per medic: 4-6 days
  (Shared capability - also satisfies ANTX-CT26 P1)

Phase 2 (P1)
• ePCR Output (LASD format): 6-10 days
  (Shared capability - also satisfies ANTX-CT26 P0 civilian handoff)
• Non-Trauma Workflows: 4-6 days

LASD Subtotal: 14-22 days

---

ANTX-CT26 — Navy / Austere Field Deployment

Required (P0)
• Austere / Offline-First Architecture: 9-15 days
• On-Device AI Integration: 6-10 days
• HIPAA Compliance: 6-10 days
• Audit Trail: 6-10 days
• ePCR (JTTR / JoMoS — military format): 5-10 days
  (Incremental on LASD ePCR)

Required (P1)
• Role-Based Access Control: 6-10 days

ANTX-CT26 Subtotal (P0+P1): 38-55 days

---

Total (P0 + P1): 61-91 days

A few other things worth flagging:
April 16 is close. The LASD Phase 1 multi-user work needs to kick off essentially now to give us any buffer before the drill. Happy to prioritize this as soon as we're aligned.
The ANTX-CT26 ePCR range is wide. If we can build the LASD ePCR first, we save 5-8 days on the military version. Sequencing these deployments will have a real impact on the total.
 ANTX-CT26 scope is still provisional. Since the exercise details were TBD when we spoke, we may need to revisit those estimates once you have the full brief from the Navy.
 ePCR timelines depend on specs. Both the LASD and ANTX-CT26 ePCR items are contingent on receiving the relevant field specs - the sooner we can get those, the better.

Happy to jump on a call to walk through any of this. Let us know how you'd like to move forward!
- Matt


On Mar 12, 2026 at 5:41:15 PM, Matthew New <matt@uptechstudio.com> wrote:
I’m in, too. Claude and I are going to take a look tomorrow afternoon. We will let you know early next week what we think!

On Mar 12, 2026 at 3:41:19 PM, Claude Ciocan <claude@uptechstudio.com> wrote:
I've got access, thanks. 

On Thu, Mar 12, 2026 at 3:24 PM Sriharsha Pothapragada <harsha@halitemedical.com> wrote:
I've given y'all pull access until everything is kicked off. Please confirm. 

On Wed, Mar 11, 2026 at 6:23 PM Matthew New <matt@uptechstudio.com> wrote:
And my handle is mdnew

On Mar 11, 2026 at 6:14:03 PM, Claude Ciocan <claude@uptechstudio.com> wrote:
Hey Harsha,

My github handle is cciocan. I'll take a look when you've added me. 

Thanks,
Claude

On Wed, Mar 11, 2026 at 5:43 PM Sriharsha Pothapragada <harsha@halitemedical.com> wrote:
Hi Matt,

Please send me your GitHub handles and ill add to the Org / Repo. 

Thanks,
Harsha

On Wed, Mar 11, 2026 at 3:27 PM Matthew New <matt@uptechstudio.com> wrote:
Hey Rachel - Thank you for sending this over, it’s helpful. I think what we would like to do now is to get access to your repo, so we can figure out the estimates for the chunks of work that you listed here for us to do. That way we can recommend a budget for this chunk of work.

Sound good?
- Matt

On Mar 11, 2026 at 1:44:10 PM, Rachel Wong <rachel.wong@halitemedical.com> wrote:
Hi All -

Please see the attachment. I've compiled notes from the meeting, recapped our current status, and separated the events into CSTARs (Phase 1/2), LASD MCI (Phase 1/2), and LASD ANTX-CT26. 

I spoke with Harsha and the best break down would be Harsha handling the front end and UpTech handling the back end. 

I think we should start with Phase 1 for both CSTARs and LASD MCI because their requirements overlap significantly (and soonest).  The biggest jump will be for the LASD ANTX-CT26.

Let me know if we need a follow up to go over everything. Near term - Harsha can handle the 30 minutes increase in the ambient listening but requires backend support for multi-user functionality (more than one medic).  We then build into Phase 2 for CSTARs and LASD MCI with multi-patient management, then ANTX-CT26 (a larger project with offline first capabilities). 

Let me know if there are questions or @Sriharsha Pothapragada you have anything to add. 

Warm regards,

--
Rachel Wong
CEO & Co-founder

Phone: 714-914-3680
Email: rachel.wong@halitemedical.com


--
Rachel Wong
CEO & Co-founder

Phone: 714-914-3680
Email: rachel.wong@halitemedical.com


--
Rachel Wong
CEO & Co-founder

Phone: 714-914-3680
Email: rachel.wong@halitemedical.com


--
Rachel Wong
CEO & Co-founder

Phone: 714-914-3680
Email: rachel.wong@halitemedical.com