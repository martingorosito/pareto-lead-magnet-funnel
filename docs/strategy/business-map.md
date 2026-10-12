# Business Map

The full journey of a founder from the first ad to the Right Hand Fit Call, as it is actually built and tested, with every step linked to the real asset behind it and the gaps marked honestly. Updated October 6, 2026.

**Where the map lives:** the diagram is `assets/business-map.drawio` (opens free in diagrams.net, no account needed). This document carries the same journey as tables, with the links.

**Live site:** every page of the funnel runs on one site, https://fp-martin-gorosito.vibepreview.app. The CRM behind it (form, calendar, pipeline, workflows, emails) is GoHighLevel.

---

## The journey at a glance

```
[1 Five Facebook ads]
      │ Learn More
[2 Landing page /  ·  qualifying form embedded]
      │ submits the form
[3 Opt-in workflow: tag, opportunity in Opted In, notify Martin, check the 5 answers]
      │
      ├── QUALIFIED (all 5 answers pass) ─────────────────────┐
      │                                                       │
[4b /thanks: confirms, sends to /audit-results]        [4a /book: Right Hand Fit Call calendar]
      │                                                       │  + Lead Magnet Delivery Email → /audit
[5b Unqualified Nurture: 3 emails,                            ├─ doesn't book ─→ [5a Qualified Follow-up: 3 emails, then Martin is told]
     email 1 delivers /audit-results]                         │                        │ nudges back to /book
      │                                                       └─ books ─→ [/booked] + [6 Booking Workflow: confirmation, 24 h + 1 h reminders]
      └─ re-invite to book when ready ──→ /book                                        │
                                                                              [7 Right Hand Fit Call]
                                                                                       │
                                     ┌────────────────────┬─────────────────────┬──────┴──────────────┐
                               no-show                 signs                 doesn't sign           comes back
                    [8a No-show Follow-up:      [8b Client Tagging:     [8c Not Signed Tagging:   [8d Reopened Tagging:
                     back to Qualified,          stage Client, Won]      status Lost/Abandoned]    status Open again]
                     email to rebook]
```

The lead magnet itself, **The Founder's Bottleneck Audit**, is an interactive page in two versions: `/audit` (for qualified founders, with a button to book the call) and `/audit-results` (for everyone else, with no booking button, so nobody is told they don't qualify). A printable PDF is the extra for anyone who prefers paper.

---

## Every step, linked to its asset

| # | Step | Asset (name inside the tool) | Link | Pipeline | What can break |
|---|---|---|---|---|---|
| 1 | Facebook ads (5) | `ads/final/ad1.png` to `ad5.png`, one per persona; copy and hooks in `docs/ads/ads.md` | https://drive.google.com/drive/folders/1TwOJYmAgbu3bTNMb824TEi7BDuS4ytqy · imagery and prompts, https://drive.google.com/drive/folders/1a9cQSnhcbSW3VFrYIDAsoh5Hx76Ysg4q | (none) | Wrong audience, weak creative |
| 2 | Landing page | Hero, what's inside, who it's for, proof, CTA with the form | https://fp-martin-gorosito.vibepreview.app/ | (none) | Slow load, hero doesn't say what it is |
| 2a | Qualifying form | GHL survey `Qualifying Form`, embedded on the landing page: contact details + 5 qualifying questions | on the landing page above | Opted In | Doesn't fire, wrong redirect |
| 3 | Opt-in workflow | ① `Opt-in Workflow`: tag `fp-mg-lead-magnet-audit`, opportunity in Opted In ($3,600), internal email `New Lead Notification` to Martin, If/Else on the 5 answers | L12 (workflow screenshots) | Opted In → Qualified or Unqualified | Tag or field misspelled, If/Else misses a case |
| 4a | Booking page | `/book` with the calendar `Right Hand Fit Call` embedded; the qualified branch also sends `Lead Magnet Delivery Email` (link to /audit) | https://fp-martin-gorosito.vibepreview.app/book | Qualified | No open slots, wrong time zone |
| 4a+ | Call booked page | `/booked`: the calendar redirects here after booking; confirms the call, links to the audit | https://fp-martin-gorosito.vibepreview.app/booked | Call Booked | Calendar redirect not set |
| 4b | Thank-you page | `/thanks`: confirms, delivers the audit (button to /audit-results), next steps, support. Never says "you don't qualify" | https://fp-martin-gorosito.vibepreview.app/thanks | Unqualified | Dead end with no next step |
| 4c | Lead magnet | Interactive audit, qualified version with booking button | https://fp-martin-gorosito.vibepreview.app/audit | (none) | Script doesn't load, page needs a login |
| 4c | Lead magnet | Interactive audit, nurture version without booking button | https://fp-martin-gorosito.vibepreview.app/audit-results | (none) | Wrong version linked in an email |
| 5a | Qualified follow-up | ② `Qualified Follow-up`: Follow-up Emails 1, 2, 3 on days 1, 3 and 6, a "Booked yet?" check before each, then an internal email to Martin | [screenshots](../../assets/screenshots) | Qualified | Keeps sending after they book |
| 5b | Unqualified nurture | ③ `Unqualified Nurture`: Nurture Email 1 at once (delivers /audit-results), day 2 split on past VA experience (2A burned before, 2B everyone else), Nurture Email 3 on day 5 re-invites to book, tag `fp-mg-nurture-complete` | [screenshots](../../assets/screenshots) | Unqualified | Wrong branch, sends after they book |
| 6 | Booking workflow | ④ `Booking Workflow`: removes from ② and ③, tag `fp-mg-call-booked`, stage Call Booked, Booking Confirmation Email, Call Reminder Email 24 h before, short reminder 1 h before | [screenshots](../../assets/screenshots) | Call Booked | Reminder never fires |
| 7 | Right Hand Fit Call | 30 minutes with Pareto: reviews the audit, maps the first 30 days | Gap (see below) | Call Booked | No-show |
| 8a | No-show | ⑤ `No-show Follow-up`: when the appointment is marked No show, tag `fp-mg-call-no-show`, back to Qualified, No-show Follow-up Email to rebook | [screenshots](../../assets/screenshots) | Call Booked → Qualified | Nobody marks the no-show |
| 8b | Signed | ⑥ `Client Tagging`: card moved to Client or marked Won, tag `fp-mg-client` | [screenshots](../../assets/screenshots) | Client (Won) | Card left in Call Booked |
| 8c | Didn't sign | ⑦ `Not Signed Tagging`: status Lost or Abandoned, tag `fp-mg-call-not-signed` | [screenshots](../../assets/screenshots) | Status Lost / Abandoned | Status never set |
| 8d | Came back | ⑧ `Reopened Tagging`: status back to Open removes `fp-mg-call-not-signed` | [screenshots](../../assets/screenshots) | Status Open | (none found in testing) |
| 9 | Client | Right Hand Program: PI assessment, 3 matches in 24 hours, 30-day integration | Gap (see below) | Client | (outside this funnel) |

Pipeline and workflow screenshots: [`assets/screenshots`](../../assets/screenshots). Every email in the workflows is named `...`, so each one can be found from its workflow.

### The pipeline

`Right Hand Pipeline`, opportunity value $3,600 (one month of the Right Hand Program).

1. **Opted In:** submitted the form
2. **Qualified:** passed all 5 answers, hasn't booked yet (no-shows come back here)
3. **Call Booked:** booked the Right Hand Fit Call
4. **Client:** signed up for the Right Hand Program (also marked Won)
5. **Unqualified:** didn't pass, in nurture, kept rather than deleted

A founder who took the call and didn't sign is marked with GoHighLevel's built-in **Lost** status (or **Abandoned** if they went quiet) instead of a sixth stage. The GoHighLevel account is shared, and it doesn't allow editing a pipeline after it's created, so the status does the job a Lost stage would have done, and the outcome workflows tag it.

### Qualified means all five
Founder or decision maker · $500K+ a year in revenue · based in the US · OK with $3,600 a month · wants help within 3 months.

### The emails, by route

| Route | Emails |
|---|---|
| Qualified, didn't book | Lead Magnet Delivery Email (instantly), Qualified Follow-up Emails 1, 2, 3 (days 1, 3, 6) |
| Unqualified | Nurture Email 1 (instantly, delivers the audit), Nurture Email 2A or 2B (day 2), Nurture Email 3 (day 5) |
| Booked | Booking Confirmation Email, Call Reminder Email (24 h), Call Reminder 1 Hour Email |
| No-show | No-show Follow-up Email |
| Internal | New Lead Notification to Martin, plus a nudge to Martin when a qualified founder hasn't booked after 6 days |

Waits send between 9 am and 5 pm, Monday to Friday, in the founder's time zone.

### Tested end to end
Tested on October 5 and 6 with test contacts: every page opened logged out; a qualified founder landed on /book, booked, reached /booked, moved to Call Booked and left the follow-up; two unqualified founders landed on /thanks and each got the right nurture branch (2A or 2B) through to `fp-mg-nurture-complete`; no-show, signed, not signed and reopened were each triggered once and tagged correctly.

---

## Gaps, marked honestly

1. **The ads aren't running.** The 5 ads are finished creatives and copy, not live campaigns, so there's no CTR, CPC or conversion data yet.
2. **No tracking installed.** No Meta Pixel, Conversions API or GA4 on the site. In a real launch this goes in first, with the form submit as the conversion.
3. **The call and the client stages aren't built here.** They're Pareto's sales and matching process, mapped from paretotalent.com. The booking page uses my own Right Hand Fit Call calendar; in production it would route to Pareto's sales team.
4. **The site runs on a preview domain.** fp-martin-gorosito.vibepreview.app, not a paretotalent.com subdomain.
5. **Shared GoHighLevel account.** The pipeline can't be edited after creation (hence the Lost status instead of a stage), the account hit its email sending limit on October 6 so emails pause until it resets, and other users' workflows can touch the same contacts. All my tags and fields carry the `fp-mg-` / `fp_mg_` prefix to keep them separate.
6. **No-shows are marked by hand.** GoHighLevel doesn't detect a missed call; someone sets the appointment to No show, and that one click starts the follow-up.
7. **No SMS.** Email only, because SMS needs a verified number and A2P registration.
8. **No re-engagement after nurture.** After Nurture Email 3 an unqualified founder gets no further touch. The `fp-mg-nurture-complete` tag is there so a later newsletter or re-qualification campaign can find them; an "Engaged Lead" tagging workflow is designed but not built.
9. **Tested with test contacts only,** not real founders.

---

## What else I'd bring
- **Pareto's org map** from the intake call: Client Success (Bri), Sales (Christian), Marketing (Ivan), Ops (Virginia), Finance (Juan Cruz), showing who would own each step of this funnel.
- **Post-call map:** PI assessment, 3 matches in 24 hours, compatibility interview, 30-day integration with a Success Manager.
