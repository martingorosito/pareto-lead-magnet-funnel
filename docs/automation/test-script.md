# Full Funnel Test Script

Run it top to bottom. Tick each box, and take the screenshot named in **[brackets]** when you reach it. Site: `https://fp-martin-gorosito.vibepreview.app`

**Golden rule: use a brand-new email for every run.** Workflows have re-entry off, so a contact that already went through once will not get the emails again. Use Gmail's plus trick: `yourname+q1@gmail.com`, `yourname+nq1@gmail.com`, then `+q2`, `+nq2` if you need to repeat. They all land in your normal inbox.

---

## 0 · Before you start (5 min)

- [ ] All 8 workflows show **Published** in Automation → Workflows (Opt-in, Qualified Follow-up, Unqualified Nurture, Booking, No-show Follow-up, Client Tagging, Not Signed Tagging, Reopened Tagging).
- [ ] Settings → Custom Values: the three `fp_mg_` values start with `https://`.
- [ ] Survey redirects: qualified → `https://…/book`, disqualified → `https://…/thanks`.
- [ ] Calendar form submit → `https://…/booked`.
- [ ] Calendar's own notification emails are off (Email grey on every row).

## 1 · Every page opens logged out (10 min)

Open a **private window**. Then open each page on your phone too (mobile data, not logged in).

| Page | Opens, no login | Looks right on phone | Buttons go to |
|---|---|---|---|
| Landing `/` | ☐ | ☐ | form / survey |
| Booking `/book` | ☐ | ☐ | calendar loads, shows slots |
| Booked `/booked` | ☐ | ☐ | button → `/audit` |
| Thanks `/thanks` | ☐ | ☐ | button → `/audit-results` |
| Audit `/audit` | ☐ | ☐ | results show a **booking** button |
| Audit results `/audit-results` | ☐ | ☐ | results show **no** booking button |

- [ ] Take the audit once on each version, all the way to the results screen. Score and Hand-off Hours appear.

## 2 · Qualified founder who books (15 min)

In the private window, start on the landing page and submit the form with `+q1`:
Founder or co-founder · $1M to $5M · United States · budget **Yes** · **Within 30 days** · VA history: **Yes, it didn't work out**.

- [ ] Lands on **/book**.
- [ ] Inbox: **"Your Bottleneck Audit is here"** arrives within ~1 minute (check Promotions/Spam). Your first name shows, the button opens `/audit`.
- [ ] You get the **New Lead notification** with the answers filled in.
- [ ] GHL contact: tags `fp-mg-lead-magnet-audit` + `fp-mg-qualified`.
- [ ] Opportunities: card in **Qualified**, value $3,600.
- [ ] Qualified Follow-up → Enrollment history: contact is there, waiting on "Wait 24 hours".

Now book a slot on /book with the same `+q1` email (phone empty, to test it's optional):

- [ ] Lands on **/booked**.
- [ ] Inbox: **booking confirmation** with the date and time filled in. Only one confirmation (no second one from the calendar).
- [ ] You get the **Fit Call booked** notification.
- [ ] Contact: tag `fp-mg-call-booked`. Card moved to **Call Booked**. Still only **one** card and one contact for `+q1`.
- [ ] Qualified Follow-up → contact is **no longer** active (removed).
- [ ] Booking Workflow → contact waiting on "24 hours before appointment".

**[L12_5_TestExecutionLogs]** Opt-in Workflow → Execution logs, showing the `+q1` run.

## 3 · Unqualified founder (10 min)

New private window, landing page, submit with `+nq1`:
CEO or owner · **$250K to $500K** · United States · Yes · Within 30 days · VA history: **No**.

- [ ] Lands on **/thanks**. Nothing on the page says "you don't qualify".
- [ ] Inbox: **Nurture Email 1** ("Your Bottleneck Audit is here") within ~1 minute; button opens `/audit-results`.
- [ ] No "delivery email" from the qualified branch (only one audit email in total).
- [ ] Contact: `fp-mg-lead-magnet-audit` + `fp-mg-not-qualified`. Card in **Unqualified**.
- [ ] Unqualified Nurture → contact waiting on "Wait 48 hours".

Try one more fail reason to prove each filter works (optional, `+nq2`): Founder · $1M to $5M · **outside the US** → should also land on /thanks.

## 4 · No-show and outcomes (5 min)

- [ ] Calendars → open the `+q1` appointment → set status **No show**. Within ~30 min: tag `fp-mg-call-no-show`, `fp-mg-call-booked` removed, card back in **Qualified**, "We missed you today" email arrives.
- [ ] Drag the `+q1` card to **Client** → tag `fp-mg-client` appears.
- [ ] Use a **different** card for Lost (here `+nq1`, never the one you just moved to Client): set status **Lost** → only `fp-mg-call-not-signed` appears, no `fp-mg-client`.
- [ ] Same `+nq1` card: set status **Won** → `fp-mg-client` appears and `fp-mg-call-not-signed` is gone.
- [ ] Set a Lost card back to **Open** → `fp-mg-call-not-signed` is removed, no client tag added.

## 5 · See every email today (optional, 20 min)

The real waits are 1 to 3 days. **Easiest:** open the workflow's Enrollment history and force the test contact to the next step at each wait (no copies needed). **Alternative**, to see the later emails now:

1. Duplicate **Qualified Follow-up** and **Unqualified Nurture**; add `· TEST` to the copies' names.
2. In the copies only: change every wait to **2 minutes** and remove the Mon–Fri window. Publish them.
3. Submit two fresh contacts (`+q2` qualified who **doesn't book**, `+nq2` unqualified who said a VA **didn't work out**).
4. Within ~10 minutes you should have: QF1, QF2, QF3 + the "hasn't booked" notification; Nurture 1, **2A** (the burned-by-a-VA version), 3, and tag `fp-mg-nurture-complete`.
5. **[L12_6_EmailTemplates]** screenshot of the inbox with all of them.
6. **Delete both TEST copies** when done.

**If the shared account is over its email sending limit** (Conversations shows "Email Not Sent"): prove the emails with (a) the template list in Marketing → Emails → Templates, (b) one template open in the editor, (c) Execution logs showing each email step **Executed**, and (d) one Conversations entry showing the email content and the limit error. Re-test the inbox once the limit resets.

## 6 · Email quality check (while they arrive)

For each email that arrived:
- [ ] From "Pareto Talent", subject and preview text look right.
- [ ] Name filled in (no "Hi ,").
- [ ] Every button opens the right page in a private window.
- [ ] Looks fine on your phone.
- [ ] Not in Spam. If it is, note it; it's a sending-domain issue, not your build.

## 7 · Clean up

- [ ] TEST workflows deleted.
- [ ] Test contacts tagged `test` (or deleted) so they don't sit in your pipeline as real leads.
- [ ] Cancel any test bookings left on the calendar.

## 8 · Result

"Tested on October 5 with fresh contacts. The qualified founder landed on /book, got the audit in under a minute, booked, landed on /booked, moved to Call Booked and left the follow-up. The unqualified founder landed on /thanks, got the audit through nurture email 1 and sits in Unqualified. No-show, Client and Lost each added the right tag."

**If something fails:** open that workflow's Execution logs, click the contact, and see which step stopped. Send me a screenshot of that step.
