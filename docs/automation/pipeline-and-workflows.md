# Pipeline and Workflows

The CRM side of the funnel: one pipeline, four workflows, the timing of every email, and the test that proves the chain works. The copy of every email lives in the companion file **docs/automation/emails.md**.

Everything below reuses the names from the funnel docs: the survey `Qualifying Form`, the pages `/`, `/book` and `/thanks`, the calendar `Right Hand Fit Call`, the tags `fp-mg-lead-magnet-audit`, `fp-mg-qualified`, `fp-mg-not-qualified`, and the seven custom fields from the qualifying form.

---

## How the two versions of the spec fit together

The written spec and the summary slide asked for slightly different email counts. This build satisfies both:

| Requirement | Written spec | Summary slide | This build |
|---|---|---|---|
| Pipeline | Stages incl. where unqualified go | Opted In, Qualified, Call Booked, Client + an unqualified stage | Those five; founders who called but didn't sign up are marked with GHL's built-in **Lost** status (the shared account doesn't allow editing the pipeline after creation) |
| Opt-in workflow | Deliver, tag, opportunity, notify yourself | Same | Same, triggered by the survey |
| Qualified follow-up | 2 emails | 3 emails, value plus a nudge to book | **3 emails**, stop the moment they book |
| Unqualified nurture | 3 emails | 1 email that delivers the lead magnet | **3 emails, the first one delivers the audit** |
| Booking workflow | Confirmation and reminder | Same | Confirmation, 24-hour reminder, optional 1-hour reminder |

---

## 1 · The pipeline

**Pipeline name in GHL:** `Right Hand Pipeline`

| # | Stage | Who is here | How they get here |
|---|---|---|---|
| 1 | **Opted In** | Everyone who submitted the survey, for a split second | Opt-in workflow creates the opportunity here |
| 2 | **Qualified** | Passed all five qualifying answers but hasn't booked yet | Opt-in workflow, qualified branch |
| 3 | **Call Booked** | Booked a Right Hand Fit Call | Booking workflow (from either branch) |
| 4 | **Client** | Signed up for the Right Hand Program | Moved by hand after the call (Pareto's sales team owns this step); workflow ⑥ adds `fp-mg-client` |
| 5 | **Unqualified** | Failed one or more qualifying answers. They're in nurture, not deleted | Opt-in workflow, unqualified branch |

**Opportunity value:** $3,600 (one month of the Right Hand Program), so the pipeline total reads as monthly revenue in play.
**Opportunity name:** `{{contact.first_name}} {{contact.last_name}} · Bottleneck Audit`
**Opportunity source:** `Bottleneck Audit Funnel`

**Why the unqualified stage stays in the pipeline:** an unqualified founder today is often a qualified one in six months (revenue grows, budget frees up). Keeping them visible as a stage, not just a tag, means the sales team can see the size of the future pool and move a contact to Call Booked if they come back through the soft door on the thank-you page.

> Note: the qualifying form doc used working names for the stages (New Lead, Qualified (Not Booked), Not Qualified (Nurture)). Use the five names above everywhere, so the Business Map, the SOP, the project plan and the screenshots all match.

---

## 2 · The four workflows

The workflows are split by job, so each screenshot shows one clean idea. They hand off to each other with tags.

```
Survey submitted
   │
   ▼
① Opt-in Workflow ── tag fp-mg-lead-magnet-audit · opportunity in Opted In · notify Martin
   │
   ├── all five answers pass ──► tag fp-mg-qualified ──► stage Qualified
   │                              send audit (qualified version)
   │                              └──► ② Qualified Follow-up (3 emails, stops on booking)
   │
   └── any answer fails ───────► tag fp-mg-not-qualified ──► stage Unqualified
                                  └──► ③ Unqualified Nurture (email 1 delivers the audit, then 2 more)

Fit Call booked (from either path)
   └──► ④ Booking Workflow ── leave ② and ③ · stage Call Booked · confirmation · reminder(s)
```

**Every founder gets the audit exactly once, within a minute:** qualified founders from the opt-in workflow, unqualified founders from nurture email 1 (which has no delay). Nobody gets it twice.

### Email timing at a glance

| Day | Qualified (didn't book) | Unqualified | Booked a call |
|---|---|---|---|
| 0, instantly | Audit delivery (qualified version) | Nurture 1: your audit | Booking confirmation |
| 1 | Follow-up 1: what your score means | | |
| 2 | | Nurture 2: hand off your first system (2A or 2B) | |
| 3 | Follow-up 2: "I've been burned before" | | |
| 5 | | Nurture 3: when you're ready | |
| 6 | Follow-up 3: last nudge | | |
| 24 h before call | | | Reminder |
| 1 h before call | | | Short reminder (optional) |

All waits after day 0 send between **9 am and 5 pm, Monday to Friday, in the contact's time zone** (use the wait step's "advanced window"). Founders read email at their desk, and nothing lands at 3 am.

---

### ① `Opt-in Workflow`

**Trigger:** Survey Submitted → filter: Survey is `Qualifying Form`

| # | Action | Settings |
|---|---|---|
| 1 | **Add Contact Tag** | `fp-mg-lead-magnet-audit` |
| 2 | **Create / Update Opportunity** | Pipeline `Right Hand Pipeline`, stage **Opted In**, name `{{contact.first_name}} {{contact.last_name}} · Bottleneck Audit`, value 3600, source `Bottleneck Audit Funnel`, status Open |
| 3 | **Internal Notification** → Email | To: **Specific user → Martin** (not "All users"). Template: `New Lead Notification` |
| 4 | **If / Else** · "Qualified?" | Branch **Qualified** when ALL of these are true (AND): `fp_mg_role` is not *Executive or manager* · `fp_mg_role` is not *Other* · `fp_mg_annual_revenue` is not *Under $250K* · `fp_mg_annual_revenue` is not *$250K to $500K* · `fp_mg_business_location` is *United States* · `fp_mg_budget_fit` is not *Not right now* · `fp_mg_timeline` is not *Later than 3 months, just exploring*. Everything else goes to **None** (the unqualified branch). |

**Qualified branch**

| # | Action | Settings |
|---|---|---|
| 5a | Add Contact Tag | `fp-mg-qualified` |
| 6a | Create / Update Opportunity | Same pipeline, stage **Qualified** |
| 7a | Send Email | `Lead Magnet Delivery Email` (qualified version, with the Fit Call P.S.) |

**Unqualified branch**

| # | Action | Settings |
|---|---|---|
| 5b | Add Contact Tag | `fp-mg-not-qualified` |
| 6b | Create / Update Opportunity | Same pipeline, stage **Unqualified** |

The unqualified branch sends no email itself: the tag starts workflow ③, whose first email delivers the audit with no delay.

**Why the If/Else reads custom fields instead of the survey's Disqualify flag:** the survey's Disqualify setting moves the founder's browser, but GHL doesn't expose it as a clean workflow condition. Reading the same five answers keeps the tag and the redirect in agreement (see L8).

---

### ② `Qualified Follow-up`

**Trigger:** Contact Tag Added → `fp-mg-qualified`
**Goal:** they book a call. The booking workflow removes them from this one the moment they do.

| # | Action | Settings |
|---|---|---|
| 1 | Wait | 1 day, advanced window Mon to Fri 9 am to 5 pm |
| 2 | If / Else · "Booked yet?" | Branch **Booked** when Contact Tags *includes* `fp-mg-call-booked` → nothing under it (ends there). The **None** branch carries on to the email. |
| 3 | Send Email | `Qualified Follow-up Email 1` |
| 4 | Wait | 2 days, same window |
| 5 | If / Else · "Booked yet?" | Branch **Booked** when Contact Tags *includes* `fp-mg-call-booked` → nothing under it (ends there). The **None** branch carries on to the email. |
| 6 | Send Email | `Qualified Follow-up Email 2` |
| 7 | Wait | 3 days, same window |
| 8 | If / Else · "Booked yet?" | Branch **Booked** when Contact Tags *includes* `fp-mg-call-booked` → nothing under it (ends there). The **None** branch carries on to the email. |
| 9 | Send Email | `Qualified Follow-up Email 3` |
| 10 | Internal Notification → Email to Martin | "{{contact.first_name}} qualified 6 days ago and hasn't booked. Worth a personal email?" (the human checkpoint from Day 4) |

**Why the "Booked yet?" checks:** the Booking Workflow already removes founders from this workflow when they book. The checks are a safety net, so nobody who booked ever gets "Should I close your spot?", even if a booking reaches GHL another way. Checking `fp-mg-qualified` would not work, because booking never removes that tag.

**Settings:** Allow re-entry **off**. Stop on response **on** (if a founder replies, a person should answer, not the next automated email).

---

### ③ `Unqualified Nurture`

**Trigger:** Contact Tag Added → `fp-mg-not-qualified`

| # | Action | Settings |
|---|---|---|
| 1 | Send Email (no wait) | `Nurture Email 1` (delivers the audit) |
| 2 | Wait | 2 days, advanced window Mon to Fri 9 am to 5 pm |
| 3 | If / Else · "Burned by a VA?" | Branch **Burned** when `fp_mg_va_history` is *Yes, it didn't work out* |
| 4a | Send Email (Burned branch) | `Nurture Email 2A` |
| 4b | Send Email (None branch) | `Nurture Email 2B` |
| 5 | Wait | 3 days, same window (both branches join here) |
| 6 | Send Email | `Nurture Email 3` |
| 7 | Add Contact Tag | `fp-mg-nurture-complete` (so a future newsletter or re-qualification campaign can find them) |

**Settings:** Allow re-entry **off**. Stop on response **on**.

**Why email 2 splits:** 60% of founders on Pareto's calls were burned by a VA before (Day 1). The qualifying form already asks about it, so those founders get the email that answers their real objection, and everyone else gets a practical hand-off guide. This is the persona personalisation promised on the thank-you page notes.

---

### ④ `Booking Workflow`

**Trigger:** Customer Booked Appointment → filter: Calendar is `Right Hand Fit Call`
(Optional second trigger: Appointment Status → *Rescheduled*, same calendar, so reminders follow the new time.)

| # | Action | Settings |
|---|---|---|
| 1 | Remove from Workflow | `Qualified Follow-up` **and** `Unqualified Nurture` |
| 2 | Add Contact Tag | `fp-mg-call-booked` |
| 3 | Create / Update Opportunity | Same pipeline, stage **Call Booked** (turn on "Allow opportunity to move to any previous stage in pipeline", because Unqualified sits after Call Booked; leave "Allow duplicate opportunities" off) |
| 4 | Send Email | `Booking Confirmation Email` |
| 5 | Internal Notification → Email to Martin | "Fit Call booked: {{contact.first_name}}, {{contact.fp_mg_annual_revenue}}, {{appointment.start_time}}" |
| 6 | Wait | **Event / Appointment time → 24 hours before** the appointment start |
| 7 | Send Email | `Call Reminder Email` |
| 8 | Wait (optional) | Event / Appointment time → 1 hour before |
| 9 | Send Email (optional) | `Call Reminder 1 Hour Email` |

**Settings:** Allow re-entry **on**, so a founder who no-shows and rebooks gets a fresh confirmation and reminder.

**Important:** turn off the calendar's own default confirmation and reminder emails (Calendar settings → Notifications), otherwise the founder gets two confirmations. One source of truth: this workflow.

**If the call is booked less than 24 hours out,** the 24-hour wait is already in the past and GHL skips straight on. That's fine: the confirmation email already carries the time and the link.

---

### Extra ⑤ · `No-show Follow-up`

Not part of the original spec. Built after the four required workflows work.

**Trigger:** Appointment Status → status is **No show**, filter: Calendar is `Right Hand Fit Call`. (GHL doesn't detect no-shows by itself: after a missed call, open the appointment in Calendars and set its status to **No show**. That one click starts this workflow.)

| # | Action | Settings |
|---|---|---|
| 1 | Add Contact Tag | `fp-mg-call-no-show` |
| 2 | Remove Contact Tag | `fp-mg-call-booked` |
| 3 | Create / Update Opportunity | Same pipeline, stage **Qualified** (they're still a qualified lead; rebooking moves them back to Call Booked) · turn on "Allow opportunity to move to any previous stage in pipeline" |
| 4 | Wait | 30 minutes (so the email doesn't arrive the second you click No show) |
| 5 | Send Email | `No-show Follow-up Email` |

**Settings:** Allow re-entry **on**. Stop on response **on**.

If they rebook, the Booking Workflow (re-entry on) sends a new confirmation and reminder and moves them back to Call Booked.

### Extra ⑥ · Outcome tagging (two small workflows)

Tags the outcome automatically after the call, so you never tag by hand. Split into two workflows (one event each) so the result never depends on the order you click in, and each removes the other outcome tag so a contact only ever carries one.

**`Client Tagging`** (two triggers, same actions)
Trigger 1: Pipeline Stage Changed → In pipeline `Right Hand Pipeline`, stage *Client*.
Trigger 2: Opportunity Status Changed → same pipeline, moved to status *Won*.
1. Add Contact Tag `fp-mg-client`
2. Remove Contact Tag `fp-mg-call-not-signed`

**`Not Signed Tagging`** (two triggers, same actions)
Trigger 1: Opportunity Status Changed → same pipeline, moved to status *Lost*.
Trigger 2: Opportunity Status Changed → same pipeline, moved to status *Abandoned* (the founder went quiet; for follow-up purposes they didn't sign).
1. Add Contact Tag `fp-mg-call-not-signed`
2. Remove Contact Tag `fp-mg-client`

**`Reopened Tagging`**
Trigger 1: Opportunity Status Changed → same pipeline, moved from *Lost* to *Open*.
Trigger 2: Opportunity Status Changed → same pipeline, moved from *Abandoned* to *Open*.
1. Remove Contact Tag `fp-mg-call-not-signed`
(No client tag here: reopening means "back in play", not "signed".)

**Settings (all):** Allow re-entry **on**. Every trigger in a workflow runs the same actions, which is why "reopened" is its own workflow.

After a call: signed → drag the card to **Client** and mark it **Won**; didn't sign → set its status to **Lost**; went quiet → **Abandoned** (works from any stage). A Lost or Abandoned founder who signs later: mark **Won** (or drag to Client) and the tags swap on their own, in any order.

### Optional extra · `Engaged Lead Tagging`

The Day 6 stretch goal. **Trigger:** Email Events → Opened or Clicked, filtered to any of the follow-up or nurture emails. **Action:** Add Contact Tag `fp-mg-engaged-lead`. Clicks on nurture email 3 are the best signal that an unqualified founder is warming up; Martin gets a weekly list of them for a personal check-in.

---

## 3 · Build it in GoHighLevel, step by step

Allow about 90 minutes. Build in this order, because each step needs the one before it.

### A · Pipeline (10 minutes)
1. Left menu → **Opportunities** → **Pipelines** tab → **+ Create new pipeline**.
2. Name: `Right Hand Pipeline`.
3. Add the stages in order: Opted In, Qualified, Call Booked, Client, Unqualified. Delete any default stages GHL adds.
4. Save.

### B · Tags (2 minutes)
1. **Settings → Tags → + New tag**. Create these 9, and paste the description into each one:

| Tag | Description |
|---|---|
| `fp-mg-lead-magnet-audit` | Opted in to the Founder's Bottleneck Audit through the qualifying form. Every lead gets it. |
| `fp-mg-qualified` | Passed all 5 criteria (founder, $500K+, US, budget OK, help within 3 months). Starts the Qualified Follow-up. |
| `fp-mg-not-qualified` | Failed at least one criterion. Starts the Unqualified Nurture, which delivers the audit. |
| `fp-mg-call-booked` | Booked a Right Hand Fit Call. Stops the follow-up and nurture emails and starts the Booking Workflow. |
| `fp-mg-nurture-complete` | Received all 3 nurture emails. Use it for future newsletters or a re-qualification campaign. |
| `fp-mg-engaged-lead` | Opened or clicked a follow-up or nurture email. A warm lead worth a personal check-in. |
| `fp-mg-client` | Signed up for the Right Hand Program after the Fit Call. Leave them out of all marketing and nurture emails. |
| `fp-mg-call-not-signed` | Qualified and showed up to the Fit Call, but didn't sign up yet. Check in again in about 3 months. |
| `fp-mg-call-no-show` | Booked a Fit Call but didn't attend. Gets one follow-up email inviting them to rebook. |
2. Spell them exactly like this. Workflow triggers match the text exactly.
3. **Why the `fp-mg-` prefix:** the GHL account is shared. If another team also uses a tag called `fp-qualified`, their "tag added" workflows would fire on your contacts (and yours on theirs). The prefix keeps your tags yours, the same reason the custom fields start with `fp_mg_`.

### C · Email templates (30 minutes)
1. **Marketing → Emails → Templates → + New → Blank template** (or duplicate the delivery email you already built, which keeps the branding).
2. Create one template per email in the Emails file and name each one exactly as written there.
3. Brand every template the same way: near-black `#070C10` header bar with the Pareto Talent wordmark, white body, emerald `#10B981` buttons with white text, headings in Plus Jakarta Sans (Arial if the editor doesn't offer it), body in DM Sans or Arial, 600 px wide.
4. In each, set the first-name fallback to "there" (merge field `{{contact.first_name}}`).
5. Send a test of each one to yourself and check it on your phone.

### D · Workflow ① Opt-in (15 minutes)
1. **Automation → Workflows → + Create Workflow → Start from scratch**.
2. Click the name at the top and rename it `Opt-in Workflow`.
3. **Add New Trigger → Survey Submitted → Add filter → Survey is → Qualifying Form**. Save trigger.
4. Click **+** under the trigger and add the actions in the table above, in order. For **Internal Notification**, choose Email, then under recipients pick **Specific user** and select yourself.
5. For the **If / Else**, name the branch "Qualified", choose **Contact details → Custom fields** for each condition, and set the joiner between conditions to **AND**.
6. Build the two branches. Click **Save**, then switch the toggle from Draft to **Publish**.

### E · Workflows ② and ③ (15 minutes)
1. Create each workflow from scratch with the name, trigger and actions above.
2. For every **Wait** after day 0: choose **Time delay**, enter the days, then open **Advanced window** and tick Mon to Fri, 9:00 am to 5:00 pm, contact's time zone.
3. Open the workflow **Settings** tab (top of the builder): Allow re-entry off, Stop on response on.
4. Save and **Publish**.

### F · Workflow ④ Booking (10 minutes)
1. First, in **Calendars → Calendar settings → Right Hand Fit Call → Notifications**, turn off the default confirmation and reminder emails.
2. Create the workflow with trigger **Customer Booked Appointment**, filter Calendar is the Fit Call calendar.
3. For the reminder wait, choose **Wait → Event/Appointment time → Before → 24 hours**.
4. In the workflow **Settings** tab, turn **Allow re-entry on**.
5. Save and **Publish**.

### F2 · Extras ⑤ and ⑥ (10 minutes, after the test of ①–④ passes)
1. Build them from the tables above, the same way as the others.
2. Test the no-show: book a slot as your qualified test contact, open it in **Calendars**, set the status to **No show**, and check that the tag, the stage (back to Qualified) and the email all arrive.
3. Test the outcome tags: drag a test card to **Client**, check the contact gets `fp-mg-client`; set another card's status to **Lost**, check `fp-mg-call-not-signed`.

### G · Screenshots
The screenshots of the finished pipeline and workflows are in [`assets/screenshots`](../../assets/screenshots). Zoom the workflow canvas out until the whole flow fits on screen before each screenshot, and make sure the workflow name at the top is readable.

---

## 4 · Test the full chain

Use two addresses that land in your own inbox: `yourname+q@gmail.com` and `yourname+nq@gmail.com`. Run the test from a private browser window, starting at the landing page.

### Test 1 · Qualified founder who books
Answers: Founder or co-founder · $1M to $5M · United States · Yes · Within 30 days · VA history: Yes, it didn't work out.

| Check | Expected | ✓ |
|---|---|---|
| Redirect | Lands on `/book` | |
| Delivery | "Your Bottleneck Audit is here" (qualified version) arrives within a minute; the PDF opens without a login | |
| Tags | `fp-mg-lead-magnet-audit` + `fp-mg-qualified` | |
| Pipeline | Opportunity in **Qualified** | |
| Notification | You get the New Lead Notification | |
| Follow-up | Contact is waiting on step 1 of workflow ② (Execution Logs) | |
| Booking | Book a slot on `/book` | |
| After booking | Confirmation email arrives; stage moves to **Call Booked**; tag `fp-mg-call-booked`; contact removed from workflow ② | |
| Reminder | Contact is waiting on the 24-hour step of workflow ④ | |

### Test 2 · Unqualified founder
Answers: CEO or owner · $250K to $500K · United States · Yes · Now · VA history: No.

| Check | Expected | ✓ |
|---|---|---|
| Redirect | Lands on `/thanks` | |
| Delivery | Nurture Email 1 arrives within a minute with the audit link | |
| Tags | `fp-mg-lead-magnet-audit` + `fp-mg-not-qualified` | |
| Pipeline | Opportunity in **Unqualified** | |
| Nurture | Contact is waiting on the 2-day step of workflow ③, and will take the 2B branch | |

### Speed up the waits (so you can see emails 2 and 3 today)
Duplicate workflows ② and ③, rename the copies with `· TEST` at the end, change every wait to 2 minutes and remove the advanced window. Run a third test contact through them, screenshot the inbox with all emails, then **delete the TEST copies** so only the real workflows remain.

### Test result
 "Tested on October 5 with two contacts. The qualified contact landed on /book, got the audit in 40 seconds, booked, moved to Call Booked and left the follow-up. The unqualified contact landed on /thanks, got the audit through nurture email 1 and is in the Unqualified stage."

---

## 5 · Common beginner mistakes (check before going live)

- **Workflow left in Draft.** Every workflow must show **Published**. Draft workflows don't run.
- **Notification to "All users".** Notify yourself only.
- **Calendar sends its own emails too.** Turn its notifications off, or founders get double confirmations.
- **Tag spelled differently** in the trigger and the action (`fp-mg-qualifed`). Copy and paste the tag names.
- **Custom field values don't match.** The If/Else compares text exactly. Use the dropdown values, don't type them.
- **Generic names.** Every workflow, email and the pipeline starts with `FP | Martin Gorosito |`. Nothing called "New Workflow" or "Copy of".
