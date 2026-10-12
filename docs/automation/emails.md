# Workflow Emails

Every email the four workflows send, in the order a founder receives them. Names match the GHL template names exactly. Workflow logic, timing and build steps are in **docs/automation/pipeline-and-workflows.md**.

**Brand (same as the pages and the audit):** near-black `#070C10` header bar with the Pareto Talent wordmark, white body, emerald `#10B981` button with white text, Plus Jakarta Sans headings (Arial fallback), DM Sans or Arial body, 600 px wide, one button per email. From name **Pareto Talent**, reply-to your own inbox.

**Links (in the HTML versions these are GHL Custom Values, see the HTML folder):** `{{AUDIT_URL}}` = full `/audit` URL (qualified emails) · `{{AUDIT_URL_NO_BOOKING}}` = the full `/audit-results` URL (the copy of the audit without the booking button; nurture emails only) · `{{BOOKING_URL}}` = full `/book` URL · `{{GUIDES}}` = https://paretotalent.com/guides
**Merge fields:** `{{contact.first_name}}` (fallback "there"). Appointment fields come from the merge-field picker under **Appointment**.

**Voice rules for every email:** short paragraphs, one idea, one button, the founder's own words, no hype. Each email gives something useful even if they never book.

| # | Template name | Workflow | When |
|---|---|---|---|
| 1 | Lead Magnet Delivery Email | ① Opt-in (qualified branch) | Instantly |
| 2 | Qualified Follow-up Email 1 | ② Qualified Follow-up | Day 1 |
| 3 | Qualified Follow-up Email 2 | ② | Day 3 |
| 4 | Qualified Follow-up Email 3 | ② | Day 6 |
| 5 | Nurture Email 1 | ③ Unqualified Nurture | Instantly |
| 6 | Nurture Email 2A (burned by a VA) | ③ | Day 2 |
| 7 | Nurture Email 2B (everyone else) | ③ | Day 2 |
| 8 | Nurture Email 3 | ③ | Day 5 |
| 9 | Booking Confirmation Email | ④ Booking | Instantly |
| 10 | Call Reminder Email | ④ | 24 h before |
| 11 | Call Reminder 1 Hour Email (optional) | ④ | 1 h before |
| 12 | New Lead Notification (internal) | ① | Instantly, to Martin only |
| 13 | No-show Follow-up Email (extra) | ⑤ No-show Follow-up | 30 min after the call is marked No show |

---

## 1 · `Lead Magnet Delivery Email` (qualified)

This is the lead magnet delivery email, with the qualified P.S. Only qualified founders get it now; unqualified founders get the same audit through Nurture Email 1.

**Subject:** Your Bottleneck Audit is here
**Preview text:** Find the 10 hours a week you should never touch again.

Hi {{contact.first_name}},

Here's your copy of **The Founder's Bottleneck Audit: Find the 10 Hours a Week You Should Never Touch Again.**

**[ Open my audit ]** → {{AUDIT_URL}}

Three tips to get the most out of it:

1. **Block 10 minutes today**, not "this week". It works best while the week is fresh in your head.
2. **Be honest about who runs each system.** If you're torn between two answers, pick the one closer to "Only me". Founders almost always underestimate it.
3. **Keep your Hand-off Hours number.** It's the one that matters: most founders find 10 or more.

When you're done, hit reply and tell me your Bottleneck Score. I read every reply.

Talk soon,
The Pareto Talent team

P.S. Based on what you shared, you're a fit for a free **Right Hand Fit Call**. If you didn't grab a time on the last page, you can [pick one here]({{BOOKING_URL}}). Bring your audit and we'll map your first 30 days of delegation together.

---

## 2 · `Qualified Follow-up Email 1` · Day 1

**Job:** deliver value (help them read their result) and make the call feel like the obvious next step.

**Subject:** What your score is telling you
**Preview text:** One of four answers. Here's what to do with yours.

Hi {{contact.first_name}},

If you filled in the audit yesterday, you now have two numbers. Here's how to read them.

**Your Bottleneck Score (0 to 24):**
- **0 to 6, the Delegator.** Most of your systems already run without you.
- **7 to 12, Stretched.** The obvious work is gone, but you're still the glue.
- **13 to 18, the Bottleneck.** Work waits for you every day.
- **19 to 24, the Business Is You.** Take two weeks off and most of the company stops.

**Your Hand-off Hours** are the hours you spend on systems you scored 2 or 3. If that number is 10 or more, you're spending over 40 hours a month on work a trained person could own.

Now multiply. A founder doing $1M a year is worth about $500 an hour. Twelve Hand-off Hours is roughly **$300,000 a year** of founder time going to inboxes, invoices and follow-ups.

The last page of the audit gives you a 30-day plan to hand off your top three systems. You can run it alone. Or you can run it with us on a free 30-minute call, where we map exactly who takes what in week one.

**[ Map my first 30 days ]** → {{BOOKING_URL}}

The Pareto Talent team

P.S. Haven't opened it yet? [Here it is again]({{AUDIT_URL}}). It takes under 10 minutes.

---

## 3 · `Qualified Follow-up Email 2` · Day 3

**Job:** handle the biggest objection (60% of founders were burned by a VA before) with proof and the guarantees.

**Subject:** "I thought it was me"
**Preview text:** Why delegation fails, and why it isn't you.

Hi {{contact.first_name}},

One of our founders, Eric Ritter, told us this before he joined:

> "I've had three different executive assistants before, and I thought it was me... burning through them."

It wasn't him. It almost never is. Delegation usually fails for three boring reasons:

1. **Part-time help.** Someone juggling five clients can't own your inbox.
2. **Tasks, not systems.** You hand off a to-do, so you're still the one who remembers the next one.
3. **No match.** The person was capable, but didn't work the way you do or sound like you.

A Pareto Right Hand fixes all three. They're **full time**, they're trained 40+ hours on the AI stack before they meet you, and they're matched to your personality with the PI Behavioral Assessment. Only **1 in 1,000** applicants is accepted, and **93%** of placements are still together at 12 months.

And the risk is ours, not yours:
- **Matching Guarantee:** you don't pay until you're excited about your match.
- **Freedom 40 Guarantee:** 40+ hours back in your first 30 days, or your next month is free.
- **Lifetime Replacement:** if the fit is ever wrong, we replace them.

If you've been burned before, the Fit Call is the right place to say so. We'll show you what's different, using your own audit.

**[ Book my Fit Call ]** → {{BOOKING_URL}}

The Pareto Talent team

---

## 4 · `Qualified Follow-up Email 3` · Day 6

**Job:** a short, honest last nudge with an easy out. Plain text style (button still emerald), feels like a person.

**Subject:** Should I close your spot?
**Preview text:** Quick question, one-word answer is fine.

Hi {{contact.first_name}},

Quick one. You qualified for a free Right Hand Fit Call this week, and I don't want to keep nudging you if the timing is wrong.

So, which is it?

- **"Yes, let's talk."** [Pick a time here]({{BOOKING_URL}}) and bring your audit.
- **"Not now."** Reply with "later" and I'll stop these emails. Your audit is yours to keep.
- **"I have a question first."** Hit reply. A real person reads it.

Here's what founders usually say after their first two weeks with a Right Hand:

> "It's only day 2 and I'm already feeling such a relief." · Daneen Goncalves

**[ Pick my time ]** → {{BOOKING_URL}}

The Pareto Talent team

---

## 5 · `Nurture Email 1` · Instantly (delivers the audit)

**Job:** deliver the lead magnet and set up the next two emails. No call to action beyond the audit.

**Subject:** Your Bottleneck Audit is here
**Preview text:** Find the 10 hours a week you should never touch again.

Hi {{contact.first_name}},

Here's your copy of **The Founder's Bottleneck Audit: Find the 10 Hours a Week You Should Never Touch Again.**

**[ Open my audit ]** → {{AUDIT_URL_NO_BOOKING}}

Three tips to get the most out of it:

1. **Block 10 minutes today**, not "this week". It works best while the week is fresh in your head.
2. **Be honest about who runs each system.** If you're torn between two answers, pick the one closer to "Only me". Founders almost always underestimate it.
3. **Keep your Hand-off Hours number.** It's the one that matters, and it's what my next email is about.

When you're done, hit reply and tell me your Bottleneck Score. I read every reply.

Talk soon,
The Pareto Talent team

P.S. Most founders say the same thing when they finish: "I knew I was the bottleneck, I just didn't know it was *that* many hours." That's normal. The last page shows you what to hand off first.

---

## 6 · `Nurture Email 2A` · Day 2 · for `fp_mg_va_history` = "Yes, it didn't work out"

**Job:** value for the founder who was burned before. Teach them why it failed and how to hand off a system so it sticks, even without Pareto.

**Subject:** Why your last assistant didn't stick
**Preview text:** It probably wasn't them, and it definitely wasn't you.

Hi {{contact.first_name}},

You told us you've worked with a VA or assistant before and it didn't work out. You're in good company: 6 in 10 founders on our calls say the same.

Here's the pattern we see most. The founder hands off **tasks** ("book this flight", "answer that email"). The assistant does them. But the founder still has to remember the next task, explain it, and check it. After a month, it feels faster to do it yourself. So you do.

The fix is to hand off a **system**, not a task. Try it this week with the #1 system on your audit:

1. **Record it once.** Five minutes of video, doing the job yourself and talking out loud. That's your first SOP.
2. **Define "done" in one sentence.** For example: "Every email gets answered, filed or flagged for me within 24 hours."
3. **Ask for an end-of-day report.** Three lines: Done, In progress, Blockers. You read it, correct once, then let go.

That works with a freelancer, a team member or a future hire. It's the same method our Right Hands use in their first 30 days.

**[ Read: How to Delegate as a Founder ]** → {{GUIDES}}

The Pareto Talent team

---

## 7 · `Nurture Email 2B` · Day 2 · everyone else

**Job:** a practical quick win with the audit result. Builds trust before any offer.

**Subject:** Hand off one system this week
**Preview text:** Start with the one that frees the most hours.

Hi {{contact.first_name}},

Got your Hand-off Hours? Good. Don't try to hand everything off at once. Pick **one** system, the one with the most hours, and do this:

1. **Record it once.** Five minutes of video, doing the job yourself and talking out loud. That's your first SOP.
2. **Define "done" in one sentence.** For example: "Every invoice goes out on the 1st and late payments get a reminder on day 7."
3. **Ask for an end-of-day report.** Three lines: Done, In progress, Blockers. Correct once, then let go.

**Not sure where to start?** For most founders it's the inbox and calendar. Create one rule today that moves every newsletter and notification out of your main inbox, and share your calendar with one person on your team so they can book meetings for you. Small, but you'll feel it tomorrow.

Then re-score that system on your audit in two weeks. The drop in hours is time you got back.

**[ Read: The Bottleneck ]** → {{GUIDES}}

The Pareto Talent team

---

## 8 · `Nurture Email 3` · Day 5

**Job:** stay useful, then leave a clear door back to a call for when their situation changes (revenue, budget or timing).

**Subject:** When the 10 hours come back
**Preview text:** A simple test for when it's time for full-time help.

Hi {{contact.first_name}},

Last email from me for now. I want to leave you with one test.

**Re-take your audit once a quarter.** The day your Hand-off Hours pass 10 a week is usually the day full-time help starts paying for itself. At that point you're spending 40+ hours a month on work someone else should own.

Some founders hit that number at $500K a year, some at $2M. Either way, you'll know, because you'll have the number.

In the meantime, here's our free library on delegation, written for founders who want to do it themselves first:

- **The Bottleneck:** why the business slows down at you
- **How to Delegate as a Founder:** systems, not tasks
- **The Second Brain for Founders:** get the business out of your head

**[ Read the free guides ]** → {{GUIDES}}

And when your number says it's time, reply to this email. We'll set up a call and bring your audit.

The Pareto Talent team

P.S. Lost the audit? [Here it is]({{AUDIT_URL_NO_BOOKING}}).

---

## 9 · `Booking Confirmation Email` · Instantly after booking

**Subject:** You're booked: Right Hand Fit Call, {{appointment.start_time}}
**Preview text:** Here's what to bring (it takes 10 minutes).

Hi {{contact.first_name}},

You're booked for your free **Right Hand Fit Call**.

**When:** {{appointment.start_time}} ({{appointment.timezone}})
**Where:** {{appointment.meeting_location}}
**How long:** 30 minutes

**[ Join the call ]** → {{appointment.meeting_location}}

**One thing to do before the call:** fill in your audit, if you haven't yet ([open it here]({{AUDIT_URL}})). Bring two numbers, your Bottleneck Score and your Hand-off Hours, and your top three systems to hand off.

**What we'll cover:**
1. Your audit, together.
2. Your first 30 days: which system goes first, what access it needs, what "done" looks like.
3. Whether a Right Hand fits. If not, you still leave with the plan.

Need a different time? [Reschedule here]({{appointment.reschedule_link}}).

See you soon,
The Pareto Talent team

---

## 10 · `Call Reminder Email` · 24 hours before

**Subject:** Tomorrow: your Right Hand Fit Call
**Preview text:** 10 minutes of prep makes it twice as useful.

Hi {{contact.first_name}},

Quick reminder: your Fit Call is **tomorrow, {{appointment.start_time}}**.

**Join here:** {{appointment.meeting_location}}

To get the most out of 30 minutes, have these ready:
- ☐ Your Bottleneck Score
- ☐ Your Hand-off Hours
- ☐ Your top three systems to hand off ([open the audit]({{AUDIT_URL}}) if you need it again)

**[ Join the call ]** → {{appointment.meeting_location}}

Can't make it? [Pick a new time]({{appointment.reschedule_link}}).

The Pareto Talent team

---

## 11 · `Call Reminder 1 Hour Email` (optional) · 1 hour before

**Subject:** In 1 hour: your Fit Call
**Preview text:** Here's your link.

Hi {{contact.first_name}}, we start in an hour. Bring your audit results if you've done it; if not, we'll go through it together.

**[ Join the call ]** → {{appointment.meeting_location}}

The Pareto Talent team

---

## 12 · `New Lead Notification` (internal, to Martin only)

**Subject:** New audit opt-in: {{contact.first_name}} {{contact.last_name}}

New lead from the Bottleneck Audit Funnel.

- **Name:** {{contact.first_name}} {{contact.last_name}}
- **Email:** {{contact.email}}
- **Role:** {{contact.fp_mg_role}}
- **Revenue:** {{contact.fp_mg_annual_revenue}}
- **Location:** {{contact.fp_mg_business_location}}
- **Budget:** {{contact.fp_mg_budget_fit}}
- **Timeline:** {{contact.fp_mg_timeline}}
- **Week goes to:** {{contact.fp_mg_week_goes_to}}
- **VA history:** {{contact.fp_mg_va_history}}

Open the contact in GHL to see their stage (Qualified or Unqualified).

*(Custom field merge keys: pick them from the merge-field picker under Custom Fields, so the key matches exactly.)*

---

## 13 · `No-show Follow-up Email` (extra) · 30 minutes after the call is marked No show

**Job:** make rebooking easy with no guilt. Founders miss calls because they're busy, which is the exact problem a Right Hand solves.

**Subject:** We missed you today
**Preview text:** No problem. Here's a new time, if you still want it.

Hi {{contact.first_name}},

We had your Right Hand Fit Call in the calendar today, but it looks like the day got away from you.

No problem. Honestly, that's the most common reason founders talk to us in the first place: too much on the calendar and nobody guarding it.

If you still want to map your first 30 days of delegation, pick a new time here. It takes 30 minutes, and you keep the plan whether or not you hire.

**[ Pick a new time ]** → {{BOOKING_URL}}

If now isn't the right moment, just reply "later" and we'll leave it there. Your audit is yours to keep: [open it here]({{AUDIT_URL}}).

The Pareto Talent team

