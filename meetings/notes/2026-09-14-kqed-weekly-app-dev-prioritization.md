# KQED: Weekly App Dev Prioritization

**Date:** September 14, 2026, 11:30 AM
**Participants:** Matt New, Mark, Jon Holtan (Uptech); Julia Hughes, Michelle Wu (KQED)
**Source:** Granola (45ab7f53-8aff-4643-8db8-4e8642b269bf)

## Election Hub feed: current state

- **Feed card is live:** voter guide link, election notifications toggle, curated content (articles, videos)
  - Card height is a UX tradeoff on smaller screens; acceptable for the ~1 month run
  - All content types (articles, JW player videos) confirmed working
  - Entire card is tappable, not just the search icon
- **Content is 100% curated via Strapi**, no auto-pull of all election news. **Julia will manage curation herself** (Jasmine may help but is not counted on)
- Election articles in the feed are standard news articles, no special handling needed
- Voter guide deep links (results, props) route correctly. **Links inside the voter guide still need work from Mark**

## Election night build and cache

- **No new build expected between now and election night.** The app should handle the results page switch automatically
  - Shorebird patcher available as a safety net
  - Most fixes can be patched at the API level anyway
- **Results page cache: reduce from 10 minutes to 2 minutes** ahead of election night. Single configurable value. **Decision: change it now so it does not get forgotten**

## Bespoke and LiveSegment

- **Bespoke share links will be used instead of the bespoke card** (card dropped). Links render a preview in the Strapi card; if the preview breaks, that is a Bespoke API issue
- LiveSegment transcript error in the demo was likely Mark using **dev segments instead of production**. LiveSegment does work in-app when Bespoke does not break it

## Jira and current workstreams

- Ticket 26:35 marked dev complete, move out of In Development
- **Mark:** wrapping up election work, PRs for Jon, Airship subscription list. **Analytics ticket assigned to Julia**; she can assess needs once a build is available (**target: later today or tomorrow**). Anticipating design feedback from Molly on election tickets
- **Jon:** security work, finishing Bitrise/Shorebird automation step, patching RadioShare share tags for Julia
- **Julia:** Event Guide content editing in Strapi (content team behind on delivery), board presentation, Experiences Hub workshop, planning for the Uptech visit

## Upcoming priorities and trip planning

- **Livestream improvements and auto QA automation:** target for the next 2 weeks before the trip. Start researching next week, not going hard yet
- **Election alerts: Matt and Julia to align this week** to get that piece running
- Longer term: Matt looking into **live activities and widgets**, reviewing what other apps do
- **Uptech team visiting in ~2 weeks.** Julia asked for input on desired activities and outcomes
- KCRW mobile feature and local events email shared as inspiration for KQED's community and events direction
