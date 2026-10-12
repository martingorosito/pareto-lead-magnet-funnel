# Qualifying Form

The opt-in and qualifying form: every question, its answer options, which answers qualify, and how the form sends qualified founders to the booking page and everyone else to the thank-you page.

- **Built as:** a GoHighLevel **Survey** (Sites → Surveys), not a plain Form. A survey shows one short step at a time, which feels lighter than a 9-field form, and it has a built-in **Disqualify** setting that sends a lead to a different URL based on their answers. That's exactly the two-way redirect the brief asks for.
- **Name in GHL:** `Qualifying Form`
- **Field keys:** every custom field key starts with `fp_mg_` (for example `fp_mg_role`). The GoHighLevel account is shared with other people, so the prefix keeps these fields from clashing with anyone else's. The field label is the question the founder sees.
- **Where it lives:** embedded in section 5 of the landing page (CTA with the form), and also reachable on its own share link.

---

## The rule

A lead is **qualified only if all five qualifying answers pass**: founder or decision maker, $500K+ a year, based in the US, OK with $3,600 a month, and wants help within 3 months. One failing answer makes them not qualified. Everyone gets the audit by email either way: qualified founders through the delivery email, everyone else through Nurture Email 1.

**Pipeline stages**: Opted In, Qualified, Call Booked, Client, Unqualified.

---

## The questions, slide by slide

### Slide 1 · Where should we send your audit?

| Field | Type | Required | Maps to |
|---|---|---|---|
| First name | Short text | Yes | `first_name` |
| Work email | Email | Yes | `email` |

Button: **Next**

Name and email come first on purpose: even if someone drops off later, the contact exists and the opt-in workflow can still send the audit.

### Slide 2 · Tailor your follow-up (segmenting, never disqualifies)

| # | Question | Options | Custom field |
|---|---|---|---|
| S1 | Where does most of your week go? | Inbox and calendar · Clients and delivery · Admin and finance · Sales and follow-ups | `fp_mg_week_goes_to` |
| S2 | Have you worked with a VA or assistant before? | Yes, it went well · Yes, it didn't work out · No | `fp_mg_va_history` |

These two never qualify or disqualify. They become tags and personalise the nurture emails (for example, "Yes, it didn't work out" gets the burned-by-a-VA story in nurture email 2).

### Slide 3 · About your business (qualifying)

| # | Criterion | Question | Options (✅ qualifies · ❌ disqualifies) | Custom field |
|---|---|---|---|---|
| Q1 | Founder or decision maker | What's your role? | ✅ Founder or Co-Founder · ✅ CEO or owner · ❌ Executive or manager · ❌ Other | `fp_mg_role` |
| Q2 | $500K+ a year | What's your business's annual revenue? | ❌ Under $250K · ❌ $250K to $500K · ✅ $500K to $1M · ✅ $1M to $5M · ✅ More than $5M | `fp_mg_annual_revenue` |
| Q3 | Based in the US | Where is your business based? | ✅ United States · ❌ Canada · ❌ Europe · ❌ Latin-America · ❌ Asia · ❌ Somewhere else | `fp_mg_business_location` |

### Slide 4 · About the help you want (qualifying)

| # | Criterion | Question | Options (✅ qualifies · ❌ disqualifies) | Custom field |
|---|---|---|---|---|
| Q4 | Ready to invest | A full-time Right Hand starts at $3,600 a month. Is that within your budget? | ✅ Yes · ✅ Yes, if the fit is right · ❌ Not right now | `fp_mg_budget_fit` |
| Q5 | Within 3 months | When do you want help in place? | ✅ Now · ✅ Within 30 days · ✅ In 1 to 3 months · ❌ Later than 3 months, just exploring | `fp_mg_timeline` |

Button: **Get my audit**

Small print under the button: *By submitting, you agree to receive your audit and a few short emails from Pareto Talent. Unsubscribe any time.*

---

## Redirect logic

```
Founder submits the survey
        │
        ├── any ❌ answer on Q1 to Q5 ──→  Disqualified  ──→  /thanks  
        │
        └── all ✅ on Q1 to Q5 ─────────→  Qualified     ──→  /book   

Either way: Survey Submitted trigger → opt-in workflow → tag + opportunity (Opted In) + notify Martin
   qualified branch → delivery email, stage Qualified · unqualified branch → Nurture Email 1 (delivers the audit), stage Unqualified
```

| Lead | Redirect | Tag | Pipeline stage | Workflow that picks them up |
|---|---|---|---|---|
| Qualified | Booking page `/book` | `fp-mg-qualified` | Qualified (Call Booked once they book) | Delivery email, then qualified follow-up emails, stop on booking |
| Not qualified | Thank-you page `/thanks` | `fp-mg-not-qualified` | Unqualified | Unqualified nurture; Nurture Email 1 delivers the audit |
| Everyone | (n/a) | `fp-mg-lead-magnet-audit` | starts at Opted In | Opt-in workflow (tag, opportunity, notify Martin) |

**Why the redirect happens in the survey, not the workflow:** a workflow can tag and email, but it can't move the founder's browser. The survey decides the page; the workflow decides the emails. Both read the same answers, so they always agree.

**The two test cases (run both before submitting):**
- **Qualified test:** Founder or co-founder, $1M to $5M, United States, Yes, Within 30 days → lands on `/book`, gets the delivery email, tagged `fp-mg-qualified`, opportunity in Qualified.
- **Not-qualified test:** CEO or owner, $250K to $500K, United States, Yes, Now → lands on `/thanks`, gets Nurture Email 1 with the audit, tagged `fp-mg-not-qualified`, opportunity in Unqualified.

---

## Build it in GoHighLevel (about 30 minutes)

1. **Create the custom fields first.** Settings → Custom Fields → add `fp_mg_week_goes_to`, `fp_mg_va_history`, `fp_mg_role`, `fp_mg_annual_revenue`, `fp_mg_business_location`, `fp_mg_budget_fit`, `fp_mg_timeline`, each as a single-option dropdown or radio with the options above, spelled exactly the same.
2. **Create the survey.** Sites → Surveys → Add Survey → blank. Name it `Qualifying Form`.
3. **Build the 4 slides** with the fields above. Mark name, email and Q1 to Q5 as required.
4. **Mark the disqualifying answers.** On each of Q1 to Q5, open the field's options and tick **Disqualify** next to every ❌ answer.
5. **Set the disqualify behaviour.** Survey Settings → Disqualify: choose **disqualify after submit** (not "immediately"), so the founder finishes every slide and all answers are saved. Set the action to **Redirect to URL** → your full `/thanks` URL.
6. **Set the success behaviour.** Survey Settings → On Submit → **Redirect to URL** → your full `/book` URL. Only founders with no disqualifying answer reach this.
7. **Style it** to match the page: emerald `#10B981` buttons, white card, DM Sans. Turn on the progress bar.
8. **Embed it** in section 5 of the landing page (CTA with the form) (Survey element), then copy the survey's share link from Sites → Surveys → Integrate.
9. **Test both paths** with two different email addresses (use `yourname+q@gmail.com` and `yourname+nq@gmail.com`). Check the redirect, the contact's custom fields, and that both contacts got the audit by email (the delivery email for the qualified one, Nurture Email 1 for the other).

**If your GHL account doesn't show "Disqualify after submit":** keep "Disqualify immediately" but move Slide 2 (the segmenting questions) before the qualifying slides, as above, so name, email and segment answers are always saved before any disqualification. Then confirm in your test that a disqualified contact still triggers the opt-in workflow.

**Workflow tip:** in the opt-in workflow, use the **Survey Submitted** trigger filtered to this survey, then an **If/Else** on the five custom fields (all passing → add `fp-mg-qualified`, otherwise → add `fp-mg-not-qualified`). That keeps the tag correct even if the survey's disqualify flag isn't available as a trigger filter.
