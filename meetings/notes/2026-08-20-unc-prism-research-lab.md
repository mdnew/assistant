# UNC Chapel Hill: Prism for body composition research

**Date:** August 20, 2026
**Participants:** Matt New (Uptech); Gabrielle DelBiondo, Dr. Abby Smith-Ryan (UNC Chapel Hill)
**Source:** Granola (536fae76-f470-46cd-a8c7-0f7fb4eed069)

## About the lab

- Gabrielle is a PhD student at UNC Chapel Hill; advisor is Dr. Abby Smith-Ryan
- Lab specializes in body composition validity, exercise and nutrition interventions
  - Populations: general participants, elite athletes, GLP-1 studies, resistance training trials
- Data currently in Excel, REDCap, and potentially Aletheos (a centralized research platform)
  - UNC is a Microsoft institution, likely Azure/OneDrive
  - Participants identified by ID only, no names stored

## Intended use of Prism

- In-lab scans alongside gold-standard devices (DEXA) for validity research
- Remote/decentralized scans for clinical trials and home use
- Interested in Aletheos integration (Aletheos may already have a Prism connection)
- UX requirements: simple, foolproof flow (right clothes, right position), no weight-loss framing
- Data output: raw measurements for research files, optionally returned to participants
- Also interested in feeding scan data back to Prism to improve the algorithm for elite athletes

## Technical path

- Capture flow: reference app is the recommended starting point
  - Uptech wrote the original SDKs (web, Android, iOS); can fork the reference app with minimal changes
- Backend: programmatic pull from Prism API, then push to UNC's secure servers
  - Not a folder/Dropbox export; requires a compliant, coded pipeline
  - **HIPAA compliance is the main complexity driver,** not the capture itself
- Data destination TBD: needs UNC IT input on preferred cloud storage (likely Azure)
- Rough cost signal: **tens of thousands, not hundreds of thousands**

## Caveats

- Matt flagged Prism's precision limits for elite athletes: better for tracking large changes than fine-grained body fat percentages
  - Recommendation: DEXA for high-performance precision; Prism to feed validation data back to Steve
- Abby's concern: ROI must justify build cost, especially on grant funding with multi-year budget cycles
  - Matt's framing: once built, they are a software company and must maintain it
  - Longer term it may make more sense for Prism to own and license a research-grade solution
