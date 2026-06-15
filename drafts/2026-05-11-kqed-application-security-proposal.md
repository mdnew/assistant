# Proposal: KQED – Application Security Engagement

**Date:** May 11, 2026

| Prepared by | Prepared for |
|---|---|
| Matthew New | Jason Cater |
| matt@uptechstudio.com | _(email TBD)_ |
| Partner, Uptech Studio | Principal Architect, KQED |

Jason,

Thank you for the opportunity to work with KQED on hardening the security posture of kqed.org, youthmedia.kqed.org, and the KQED Mobile App. We've prepared this proposal based on the Application Security Engineer scope you shared and Uptech's May 2026 Web Security & Infrastructure Assessment. Our goal is to stand up a strong, well-documented foundation for application security across KQED's digital products while leaving your team confident operating it day-to-day.

I look forward to discussing the details once you have a chance to review.

Thank you,

Matthew New
Partner, Uptech Studio
matt@uptechstudio.com

---

## Project Overview

Uptech Studio will embed a senior Application Security engineer alongside KQED's developer operations and application architects to harden KQED's edge, fix the current logging and monitoring posture, and reduce operational risk in the web infrastructure. Our May 2026 assessment reviewed KQED's GCP infrastructure, kqed.org DNS surface, load balancers, firewall configuration, and 8 GKE clusters. The assessment found no evidence of active exploitation, exposed credentials, or directly internet-accessible databases. The gaps are primarily operational: missing edge protection, public non-production surfaces, noisy or absent monitoring, DNS cleanup, and cluster sprawl.

Our recommended implementation approach is to complete the immediate pre-migration remediation first, then deliver the remaining work in three focused workstreams so KQED sees measurable improvements early and the team can adjust scope between phases as findings emerge.

The engagement is designed so KQED owns the resulting systems, runbooks, and policies. Uptech will document everything we implement and pair with your team throughout, including hands-on training, so the practices stick.

**Lead engineer:** Jon Stanley, Senior Engineer at Uptech Studio, will lead the application security work, backed by Matt for partner oversight and architecture review.

## Project Scope

Based on Uptech's technical review, we recommend the following phased approach. The sequence prioritizes the highest-impact edge protections first (WAF, DDoS protection, bot detection, and non-production access control), followed by a holistic observability strategy, and finally infrastructure follow-on work.

| Priority | Date | Deliverable | Description | Estimate _(DRAFT)_ |
|---|---|---|---|---|
| Critical | Immediate | Pre-Migration Remediation | Resolve time-sensitive issues before the Cloudflare migration begins: confirm Elasity vendor renewal for `elasityapp.com` before the June 23, 2026 expiration date or remove affected CNAME records; investigate `proxy.kqed.org` returning HTTP 500 in production; and identify the safest path for protecting publicly accessible dev and staging environments. | 25 hours |
| High | Now-10 weeks | Cloudflare Security Edge | Implement Cloudflare as the security edge layer across KQED web surfaces. Configure WAF, DDoS protection, geoblocking policy, bot management, Cloudflare Access with Google Workspace SSO on non-production subdomains, and Google Cloud Armor origin lockdown for GCP backends. Apply for Cloudflare Project Galileo before procurement so KQED can potentially access Enterprise-level features at minimal ongoing cost. | 125 hours |
| High | Weeks 6–16 | Observability, Monitoring & Error Handling | Establish a holistic observability strategy with clear standards for log formats, message structure, actionable alerting, and ownership. Add immediate GCP Cloud Monitoring alerts for backend services, roll out **New Relic APM** on backend services, add **New Relic Browser** before the frontend refactor ships, extend **Sentry** to backend JavaScript / TypeScript services, and apply the **Mobile API Known Error Pattern** for actionable error handling. Include training for the KQED engineering team. | 125 hours |
| Mid | Post-migration | Infrastructure Follow-On Work | Reduce operational risk after the Cloudflare migration is stable. Evaluate consolidating 8 GKE clusters to 4, assess replacing Spinnaker with GitHub Actions + GCP Cloud Deploy, audit the separate AWS account, and decommission obsolete backend services after upstream dependency review. | 75 hours |

Each phase concludes with documentation, a handover walkthrough with KQED's team, and an operating runbook so KQED can own the system going forward.

## Platform & Technology

The engagement is platform-aware rather than platform-specific. We expect to work across:

- **Edge / WAF:** Cloudflare (WAF, Geoblocking, Bot Management)
- **Origin protection:** Google Cloud Armor Standard
- **Access control:** Cloudflare Access with Google Workspace SSO
- **Backend monitoring:** New Relic
- **Application error tracking:** Sentry
- **Error handling pattern:** Mobile API Known Error Pattern
- **Cloud:** GCP and AWS (and container / Kubernetes workloads where relevant)
- **CI/CD:** Google Cloud Build, GitHub Actions, GCP Cloud Deploy, and Spinnaker evaluation
- **Languages:** Python and TypeScript / JavaScript primary; additional language coverage as needed for KQED's services

KQED will cover all costs associated with hosting, tooling licenses, and third-party services (Cloudflare, New Relic, Sentry, etc.). Uptech will help size and procure these with KQED. KQED may qualify for Cloudflare's Project Galileo program, which could significantly reduce Cloudflare's ongoing cost.

## Fees and Schedule

The total budget that we estimate to complete the project as described in the Project Scope is **$70,000 _(DRAFT)_** over an estimated **~16 weeks** of delivery, launched in stages.

Work is sequenced so KQED sees value early (pre-migration remediation and Cloudflare edge protection first) and so scope can be adjusted between workstreams based on findings.

## Changes to Scope

Changes requested to Project Scope (including those due to delayed delivery, changes to underlying platforms, or newly discovered risks during assessment) may affect the overall timeline and budget. If such changes are requested, Uptech Studio will submit a new scope of work agreement.

---

_Uptech Studio • 250 El Camino Real, Suite 200, Tustin, CA 92780 • www.uptechstudio.com • (858) 987-8324 • Confidential_
