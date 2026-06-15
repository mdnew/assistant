# Gameday franchisee portal — user stories (high level)

**Source:** `meetings/notes/2026-04-16-gameday-franchisee-portal-sow-context.md` (Allen/Blaine direction and Northpoint prototype)

**Format:** Short capability statements for SOW and backlog shaping. Not full INVEST stories.

**Phasing:** **v1** = read-only portal aligned to prototype; **v2** = workflows and nav areas not proven in screenshots; **platform** = cross-cutting engineering requirements.

---

## Access and context

- **v1** A franchisee owner can log in with their own account (not shared clinic credentials).
- **v1** A franchisee owner can see only the locations assigned to them.
- **v1** A franchisee owner can switch between their clinics from the nav.
- **v1** A regional or corporate user can see a broader set of locations than a single owner (role-based scope).
- **v1** A user can see who they are logged in as and their role in the header.

---

## Dashboard (home)

- **v1** A franchisee owner can pick a time period (e.g. this month) that applies across the dashboard.
- **v1** A franchisee owner can see headline KPIs: revenue, active members, new members, MRR-style metric, and average revenue per transaction.
- **v1** A franchisee owner can see how each KPI changed vs the prior period.
- **v1** A franchisee owner can see revenue verification status (e.g. QC check, not verified) on revenue KPIs.
- **v1** A franchisee owner can see total active members as a top-level number.
- **v1** A franchisee owner can see member counts by category (TRT, peptides, weight loss, ED, lab work, supplements, canceled).
- **v1** A franchisee owner can refresh or sync data when metrics feel stale (exact behavior TBD).

---

## Revenue analytics

- **v1** A franchisee owner can explore revenue by day, week, month, or quarter.
- **v1** A franchisee owner can split revenue into recurring vs one-time.
- **v1** A franchisee owner can view revenue as bars or as a trend line with actuals vs trend.
- **v1** A franchisee owner can drill into revenue for the selected clinic and period.

---

## Member census

- **v1** A franchisee owner can open a member census view for the selected clinic.
- **v1** A franchisee owner can see category stat cards as unique members per category (same member can count in multiple categories).
- **v1** A franchisee owner can browse a detail table of member-product rows (one row per member per product).
- **v1** A franchisee owner can filter the census by category tab.
- **v1** A franchisee owner can search members in the census list.
- **v1** A franchisee owner can see how many rows they are viewing out of the total (e.g. showing 50 of N).
- **v1** A franchisee owner can switch between a detailed list view and a by-member view.
- **v1** A franchisee owner can sort the census table on key columns (member, product, category, status, amounts, dates, referral source, etc.).
- **v1** A franchisee owner can open transaction detail for a member-product row.
- **v1** A franchisee owner can mark or track Google review status from a row (write behavior TBD).

---

## Trust, performance, and definitions

- **platform** A franchisee owner can trust that numbers match agreed definitions (active member, revenue, category rules).
- **platform** A franchisee owner can load dashboard and census views in seconds, not minutes.
- **platform** A franchisee owner cannot see another franchisee’s clinic data (row-level security).

---

## Later phase (separate scope from read-only dashboards)

- **v2** A franchisee owner can get suggestions or prompts on the dashboard (rules TBD).
- **v2** A franchisee owner can receive reminders to follow up with customers (in-app, email, or SMS TBD).
- **v2** A franchisee owner can complete or track follow-up tasks tied to census or revenue events.
- **v2** A franchisee owner can use additional nav areas when scoped (revenue deep-dive, medication orders, bonus tracker, close rate, inventory, contracts).

---

## Out of scope for v1 (named for estimate boundaries)

- CMS-style content, approvals, ticketing, and heavy workflow builders (ReplyWise-style): priced separately from charts and census.
- Corporate-only analytics views: same portal shell, different role (confirm auth model in discovery).
