# NPR Round 1 pitch deck

Nine slides, 15 minutes, three presenters. Open `index.html` in any browser.

## Keyboard

| Key | Does |
|---|---|
| `→` `space` `PageDown` | Next slide (or click the right half of the screen) |
| `←` `PageUp` | Previous slide (or click the left half) |
| `S` | Speaker notes panel. The slide shrinks so the panel never covers it |
| `T` | Start / pause the 15:00 countdown. Amber at 3:00, red at 1:00, counts up past zero |
| `R` | Reset the timer |
| `G` | Grid overview, jump to any slide |
| `F` | Fullscreen |
| `Home` `End` | First / last slide |

Clicking works with a presentation remote, since most clickers send arrow keys or a click.

`Cmd-P` prints one slide per page if you need a PDF.

## Run of show

| # | Speaker | Section | Target | Running |
|---|---|---|---|---|
| 1 | Adam | Cover and introductions | 0:20 | 0:20 |
| 2 | Adam | Executive Summary | 1:30 | 1:50 |
| 3 | Adam | Company Overview | 1:40 | 3:30 |
| 4 | Claude | Technical Requirements | 2:10 | 5:40 |
| 5 | Claude | How We Work | 1:40 | 7:20 |
| 6 | Matt | Feature Requirements | 2:10 | 9:30 |
| 7 | Matt | Local and National | 1:20 | 10:50 |
| 8 | Adam | Timeline & Pricing | 1:40 | 12:30 |
| 9 | Adam | Close and questions | 0:30 | 13:00 |

Two minutes of buffer against the 15. If Q&A is inside the 15, you need to land at 11:00.

## Slide 7 was changed

The original slide 7 was **Non-functional Requirements**: WCAG 2.1 AA, app store account
ownership, no access to PII. All true, all necessary in the written response, and worth
nothing in a pitch. It was 80 seconds spent on hygiene.

It is now **Local and National**, which answers the hardest problem in NPR's brief and the
thinnest part of the written response: a local-national distribution model across 240+ Member
stations. Content Architecture and Network Curation is 15% of the Round 1 scoring, and the
geolocated PBS broadcast work at KQED is a shipped, verifiable answer that most bidders will
not have.

The non-functional items are still covered, as a single grey line at the bottom of the slide.
Read it fast and flat. It is there so nothing is missing, not to be discussed.

### To put the original back

Replace the slide 7 `<section>` in `index.html` with this:

```html
<section class="slide" data-who="Matt" data-sec="Non-functional Requirements" data-time="1:20">
  <div class="frame">
    <p class="eyebrow">Non-functional Requirements</p>
    <h2 class="t">Your accounts. Your data. Your repositories.</h2>
    <ul class="pts">
      <li><b>We build to WCAG 2.1 Level AA.</b> Contrast defined once in tokens per mode, so it is verified at the system level rather than screen by screen.</li>
      <li><b>App store accounts stay yours,</b> with our team added as users to submit and manage builds.</li>
      <li><b>We do not need access to user PII,</b> and we do not ask for it.</li>
    </ul>
    <p class="foot">Uptech Studio</p>
  </div>
  <div class="slide-notes">
    <p>The fastest slide in the deck. None of this wins the work, but any of it can lose it, so state it and move.</p>
  </div>
</section>
```

## Editing

Slides are plain `<section class="slide">` blocks with three data attributes that drive the
HUD: `data-who`, `data-sec`, `data-time`. Add or remove slides freely, the counter and grid
rebuild themselves.

Frame variants: default is white, `frame--brand` is the purple full-bleed, `frame--dark` is
the navy panel used for Feature Requirements.

Everything is sized in `cqw`, so type scales with the slide rather than the window. If you add
copy and it overflows, shrink the font size rather than the padding.

## Open questions before rehearsal

1. **Is Q&A inside the 15 minutes?** Worth asking Kahlia. If yes, cut to 11:00: trim slides 3
   and 6 by 30 seconds each and take slide 7 down to a single sentence.
2. **Adam presents twice,** which is four speaker transitions. At 15 to 20 seconds each that is
   over a minute of the budget. Having Claude or Matt close on Timeline and Pricing halves it.
3. **Slide 4 is the most technical.** If the NPR room is mostly product and design, move 30
   seconds from it into slide 6.

## Slide 2 headline

Currently: **"At Uptech Studio, we're all about execution."**

Says what the firm is for, then lets the three bullets turn it into the bid and prove it. Bullet 1
was resequenced so it no longer repeats the word "execution" straight after the headline.

Earlier attempts and why they were dropped:

| Headline | Why not |
|---|---|
| You have already seen this engagement work. | "Engagement work" parses two ways, and it assumes NPR knows the KQED story before you tell it |
| Another agency did discovery. We shipped the app. | Accurate and punchy, but it leads with someone else's role rather than yours |

Sharper variants of the current line, if "all about" feels soft for the room:

| Headline | Register |
|---|---|
| At Uptech Studio, execution is the whole point. | Same shape, firmer landing |
| We are built for execution. | Shortest. Very confident, slightly blunt |
| At Uptech Studio, we are an execution and iteration shop. | Matches the proposal's own p.4 wording exactly |
