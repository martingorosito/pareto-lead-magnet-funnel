# SOP: Launching a Lead Magnet Funnel

The exact process I followed for this project, written so the next lead magnet launch at Pareto follows it step by step. Fill in exact button names and add screenshots as you run it.

---

## Why I chose this process
This whole project *is* a lead magnet launch, and Pareto will run more of them. Every launch repeats the same chain (research, offer, asset, funnel, automation, ads, test), and most failures happen at the hand-offs: a link left private, a redirect pointing the wrong way, an email that never fires (Day 4: "no test run" and "no error handling" are the top automation pitfalls). Writing it once means the next Right Hand can run a launch without rebuilding the process from memory (Day 9).

---

## 1. Purpose
Take a new lead magnet from idea to a live, tested funnel that sends qualified founders to a call and everyone else into nurture.

## 2. Scope
Covers: research, offer, the lead magnet, landing page, qualifying form, booking and thank-you pages, CRM pipeline, the four workflows, ads and the final test.
Doesn't cover: running paid ad campaigns or Pareto's sales call.

## 3. Owner, timing and access
- **Owner:** the Right Hand running the launch. **Approver:** the founder signs off the offer (step 5.2) and the go-live (step 5.8).
- **Time:** about four working days for a first launch (this project ran Oct 3 to Oct 7).
- **Access needed:** Claude (Project), Google Drive, GoHighLevel sub-account (Funnels, Forms, Calendars, Workflows, Opportunities), ClickUp, Canva or an image tool, Loom.

## 4. Naming rules (use everywhere)
- Files and folders: `Prefix_Name_L##_ItemName`, e.g. bottleneck-audit-printable.pdf
- Inside tools: `Prefix | Name | Item Name`, e.g. "Qualifying Form"
- Nothing called "Copy", "Untitled" or "Workflow 3".

## 5. Procedure

### 5.1 Plan it in ClickUp
1. Create a Space for the launch, one List per milestone, and tasks with owner, deadline, status and priority.
2. Work backwards from the launch date; put the full-chain test the day before launch.

### 5.2 Research and lock the offer
1. Load the business's context into a Second Brain (Claude Project): website, testimonials, founder story, call transcripts, frameworks.
2. Study 3 competitor lead magnets: format, promise, audience, how they capture and qualify, what happens after opt-in.
3. Write the ICP in one paragraph and 3+ personas by cause, in client words.
4. Decide the format and a promise that solves one problem in under 10 minutes; name it with MAGIC; check it against the Value Equation.
5. Write the exact qualification criteria the form will use, and the next-step offer.
6. **Founder sign-off** before building anything.

### 5.3 Build the lead magnet
1. Draft the content with the Second Brain; it must be useful even if the reader never talks to the business.
2. Design it on-brand (same palette, fonts and tone as the funnel).
3. Upload to Drive, set sharing to "Anyone with the link can view", and open it in incognito to confirm.

### 5.4 Build the funnel
1. Landing page sections: hero, what's inside, who it's for, proof with real numbers, CTA with the form.
2. Qualifying form: contact details plus the qualification questions; set conditional redirects (qualified to booking page, everyone else to thank-you page).
3. Booking page with the appointment calendar embedded (US time zones, buffers). Give the calendar its own form (named with the launch prefix) using the standard contact fields: first name, last name and email required, phone optional so no one drops off over it. Email must stay required, because it is what links the booking to the contact who filled in the qualifying form.
4. A call-booked confirmation page: next steps before the call and a link to the lead magnet. Set the calendar form's submit action to redirect to it (the calendar's own redirect setting alone may not fire); test it in incognito.
5. Thank-you page that confirms, delivers the resource, gives next steps and a support contact.

### 5.5 Set up the CRM and workflows
1. Pipeline stages: Opted In, Qualified, Call Booked, Client, Unqualified (didn't-sign founders use the built-in Lost status).
2. Tags, all with the launch prefix so they never clash with anyone else's in a shared account: lead magnet, qualified, not qualified, call booked, nurture complete, engaged lead, client, call not signed, call no-show. Write a one-line description on each.
3. Opt-in workflow (trigger: form submitted): tag, create the opportunity, notify yourself only, then branch. Qualified: tag, stage Qualified, send the resource. Not qualified: tag, stage Unqualified (the nurture delivers the resource).
4. Qualified follow-up: 3 emails that deliver value and nudge anyone who qualified but didn't book. Exit when they book or reply.
5. Unqualified nurture: first email delivers the lead magnet with no delay, then 2 value emails (split by persona where the form allows) that leave a door back to a call.
6. Booking workflow: remove from both email workflows, stage Call Booked, confirmation immediately, reminder 24 hours before. Allow re-entry, so rebookings get a new confirmation. Turn off the calendar's own emails.
7. Extras: no-show follow-up (one rebook email), outcome tagging when a card moves to Client or is marked Won, Lost or Abandoned, engaged-lead tagging on opens and clicks.
8. Build email templates first, then workflows, and publish every workflow (Draft workflows don't run).

### 5.5b After every call (manual, the founder or sales owner)
1. **Didn't show:** open the appointment in Calendars and set its status to **No show**. The no-show follow-up runs from that click.
2. **Signed up:** drag the card to **Client** and set its status to **Won**. The client tag is added automatically and keeps them out of marketing emails.
3. **Didn't sign:** open the card, set its status to **Lost** (or **Abandoned** if they went quiet) and add a note on why. The "call not signed" tag is added automatically; set a reminder to check in after 3 months.
4. **Lost founder signs later:** set the card's status to **Won** (or drag it to **Client**). The outcome workflows swap the tags automatically, whatever order you click in. Reopening a card (status **Open**) only removes the "not signed" tag.

### 5.6 Make the launch materials
1. Build 5 ads from the persona and angle work, each a different message: hook, offer, qualifier, proof, mechanism, CTA.
2. Generate imagery from a section description, a style-guide sentence and a palette screenshot; save the prompts.
3. Keep one visual identity across ads, pages, emails and the lead magnet.

### 5.7 Test the full chain (incognito)
1. Open every public link in an incognito window, on desktop and phone. Nothing may ask for a login.
2. **Qualified route:** submit with a qualified test email (e.g. you+qualified@gmail.com). Expect: redirect to the booking page, qualified tag, opportunity in Qualified, notification to you, resource email in the test inbox.
3. **Booking:** book a slot. Expect: redirect to the call-booked page, confirmation email, stage moves to Call Booked, follow-up emails stop, reminder scheduled.
4. **Qualified but not booked:** submit again and don't book. Shorten the waits temporarily and confirm the follow-up emails arrive in order.
5. **Unqualified route:** submit with failing answers. Expect: thank-you page, unqualified tag, Unqualified stage, nurture emails in order.
6. **No-show and outcomes:** mark the test booking No show (expect: no-show tag, back to Qualified, rebook email); drag a test card to Client and mark another Lost (expect: the matching tags).
7. **Clean up:** restore the real wait times, tag test contacts "test", cancel the test booking.
- [ ] Screenshot each expected result

### 5.8 Go live and hand over
1. **Founder sign-off** on the tested funnel.
2. Record a 2-minute Loom walking through the lead magnet, funnel, workflows and ads.
3. Update the Business Map with every live link; mark anything not built as a gap.
4. Run the reflection: what went well, what didn't, what we learned. Add the lessons to this SOP.

## 6. Pass or fail
A launch is live only when every expected result in 5.7 happened. If anything fails, note the step, check the workflow's execution log for that contact, fix it, and rerun 5.7 from the start. Never go live on a partial pass.

## 7. Common problems
| Symptom | Likely cause | Fix |
|---|---|---|
| Resource asks for access | Drive sharing still "Restricted" | Share → "Anyone with the link can view" |
| Everyone goes to the thank-you page | Redirect checks the wrong field or answer text | Re-check the form's conditional redirect |
| Emails land in spam | Default sending domain | Set up a dedicated sending domain |
| Lead gets follow-ups after booking | Booking doesn't end the workflow | Add "Remove from workflow" for both email workflows at the top of the booking workflow |
| A workflow never fires | Left in Draft, or the tag in the trigger is spelled differently | Publish it; copy and paste tag names |
| Someone else's automation fires on your contacts | Shared account, generic tag names | Prefix every tag with the launch prefix |
| Notification goes to everyone | Recipient set to all users | Set it to a specific user (you) |

## 8. Record of launches
| Date | Lead magnet | Run by | Test passed? | Lessons added |
|---|---|---|---|---|
| Oct 2026 | The Founder's Bottleneck Audit | Martin Gorosito | | |

## 9. Video walkthrough
Link a 2 to 3 minute screen recording of yourself running step 5.7, so the next person can watch the process as well as read it.
