# Fit3D — team intro and iOS port context — 2026-05-07

Kickoff-style discussion: introductions, iOS setup and technical direction, business rationale, avatar quality churn topic, and next steps.

**Granola transcript:** https://notes.granola.ai/t/ec5efee2-b9c7-47d6-8788-dbbf98ed8dfa

Follow-ups: `meetings/actions/2026-05-07-fit3d-ios-kickoff.md`

## Team introductions and project context

- **Mark** introduced to **Greg Moore**
  - Mark primarily works on **KQED** with most **iOS** experience alongside **Anthony**
  - Will handle **iOS port** while learning the **Android** codebase for flexibility

- **User scale comparison**
  - **Wair:** ~50 million users, ~500 million size recommendations
  - **KQED + Anthony’s SDK** numbers combined likely higher

## iOS development setup and requirements

- **GitHub access** needed for **Mark**
  - **Android** repository access for learning
  - **New iOS repository** to be created by **Tyler**

- **Device compatibility**
  - Unlike Android (locked to a specific **Samsung tablet**), **iOS** will support **all modern iPads**
  - **No camera limitations:** any modern iPad works, including base **$299** model
  - Plan to use existing **iPad Air** for development

## Technical implementation decisions

- **UI/UX on iOS**
  - Use **native iOS layouts** vs custom Android components
  - Leverage **system navigation** instead of custom back buttons
  - Use more **screen real estate** with standard **iPad** patterns

- **Dark mode**
  - Described as **simple on iOS** (hours vs days)
  - Include it to reduce support tickets from users in dark mode

- **Authentication**
  - Same **custom sign-up endpoint** as Android
  - Recent **bot protection** issues addressed with a **separate hosted sign-up page**

## Business context and growth strategy

- **Why iOS port**
  - **International:** Android tablets predominant
  - **US:** Clients often already have **iPads** for other business tools
  - **Sales:** Removes friction, no need to buy a separate device

- **Current challenges**
  - **Churn** tied to **avatar quality** vs **Pro Scanner** expectations
  - **Prism** team working on **filter** improvements for more realistic **grayscale** avatars
  - **Pablo** following up with solutions **this week**

## Next steps (summary)

| Owner | Item |
|-------|------|
| Tyler | Create **iOS repo** and add **Mark** on GitHub |
| Mark | **Android** codebase review, then **iOS** development |
| Prism | Continue **avatar quality** improvements (new filters) |
| Team | Available for Mark’s questions during learning |
