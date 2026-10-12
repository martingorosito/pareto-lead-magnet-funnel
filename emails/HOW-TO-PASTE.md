# Email HTML: how to paste them into GHL

Twelve branded, ready-to-paste emails (the New Lead Notification is typed straight into the workflow, so it has no file). Same look in every email: near-black header with the Pareto Talent wordmark, emerald stripe and button, DM Sans body.

## 1 · Create the 3 Custom Values first (2 minutes)

**Settings** → **Custom Values** → **+ Add Custom Value**. Create these three, then check that the key GHL shows next to each one matches exactly (that key is what the emails use):

| Name | Key the emails use | Value |
|---|---|---|
| fp_mg_audit_url | `{{custom_values.fp_mg_audit_url}}` | `https://fp-martin-gorosito.vibepreview.app/audit` |
| fp_mg_audit_url_fit_no | `{{custom_values.fp_mg_audit_url_fit_no}}` | `https://fp-martin-gorosito.vibepreview.app/audit-results` (the audit copy without the booking button) |
| fp_mg_booking_url | `{{custom_values.fp_mg_booking_url}}` | `https://fp-martin-gorosito.vibepreview.app/book` |

If GHL gives a slightly different key, update `LINKS` in `generate_emails.py` and re-run it, or use find-and-replace in the code editor.

## 2 · Paste each email (about 2 minutes each)

1. **Marketing** → **Emails** → **Templates** → **+ New** → choose the **Code editor / HTML** option (not the drag-and-drop builder). If you already made a design template with this name, delete it or rename it first.
2. Name the template exactly as in the table below.
3. Open the HTML file in a text editor (Notepad or TextEdit), select all, copy, paste into the code editor, **Save**.
4. Set the **subject** and **preview text** from the table (in the template settings, or in the workflow's Send Email step).
5. **Send a test** to yourself. Merge fields like `{{contact.first_name}}` and the appointment times only fill in when a real contact goes through the workflow; in a test they may show blank.
6. Check GHL adds an **unsubscribe** link at the bottom when sent from a workflow (it normally does for marketing emails).

## 3 · Files, names, subjects

| File | Template name in GHL | Subject | Preview text |
|---|---|---|---|
| `01-lead-magnet-delivery-email.html` | `Lead Magnet Delivery Email` | Your Bottleneck Audit is here | Find the 10 hours a week you should never touch again. |
| `02-qualified-follow-up-email-1.html` | `Qualified Follow-up Email 1` | What your score is telling you | One of four answers. Here's what to do with yours. |
| `03-qualified-follow-up-email-2.html` | `Qualified Follow-up Email 2` | "I thought it was me" | Why delegation fails, and why it isn't you. |
| `04-qualified-follow-up-email-3.html` | `Qualified Follow-up Email 3` | Should I close your spot? | Quick question, one-word answer is fine. |
| `05-nurture-email-1.html` | `Nurture Email 1` | Your Bottleneck Audit is here | Find the 10 hours a week you should never touch again. |
| `06-nurture-email-2a.html` | `Nurture Email 2A` | Why your last assistant didn't stick | It probably wasn't them, and it definitely wasn't you. |
| `07-nurture-email-2b.html` | `Nurture Email 2B` | Hand off one system this week | Start with the one that frees the most hours. |
| `08-nurture-email-3.html` | `Nurture Email 3` | When the 10 hours come back | A simple test for when it's time for full-time help. |
| `09-booking-confirmation-email.html` | `Booking Confirmation Email` | You're booked: Right Hand Fit Call, {{appointment.start_time}} | Here's what to bring (it takes 10 minutes). |
| `10-call-reminder-email.html` | `Call Reminder Email` | Tomorrow: your Right Hand Fit Call | 10 minutes of prep makes it twice as useful. |
| `11-call-reminder-1-hour-email.html` | `Call Reminder 1 Hour Email` | In 1 hour: your Fit Call | Here's your link. |
| `13-no-show-follow-up-email.html` | `No-show Follow-up Email` | We missed you today | No problem. Here's a new time, if you still want it. |
