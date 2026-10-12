Build a one-page "call booked" page for Pareto Talent, as a new step in this funnel. It is the sister page of the existing thank-you page: same layout, same style, same section rhythm. Dark, premium, calm. Main goal: the visitor knows their call is booked, knows how to prepare, and opens their free audit.

Layout: every section spans the FULL WIDTH of the browser (edge-to-edge background, no boxed container, no white margins). Inner content width about 900px, centred, 16px side padding on phones.

Design: page background #070C10, alternate sections #0E171C, cards #122027 with 1px borders #1E2E36, text #F3F6F5, muted text #9AA8B0, accent #10B981. Primary button: #10B981 background, #070C10 text, pill-shaped, bold, large. Headings in Plus Jakarta Sans (800), body in DM Sans. No navigation menu.

Sections, in this order, with this exact copy:

1. CONFIRMATION (centred, generous space, a small emerald check icon above the headline)
- Headline: You're booked. Your call is on its way to your calendar.
- Sub-headline: Your confirmation and calendar invite are in your inbox now. While you wait, take The Founder's Bottleneck Audit so we can spend the call on your numbers.
- Big button: Start my audit now → (link: AUDIT_URL, opens in a new tab)

2. BEFORE THE CALL
- Heading: Three things to do before we talk
- Three numbered cards:
  1. Accept the calendar invite so the call is on your calendar. Can't find it? Check Promotions or Spam.
  2. Take the audit if you have 10 minutes. Bring your Bottleneck Score and Hand-off Hours. No time? We'll go through it together on the call.
  3. Write down the three tasks you'd hand off tomorrow if you could. We'll start there.

3. WHAT HAPPENS ON THE CALL
- Heading: 30 minutes, no pressure
- Body: We look at where your week goes, pick the first systems to hand off, and map your first 30 days. You leave with that plan whether or not you hire.
- Three small cards, one per guarantee:
  - Freedom 40: 40+ hours back in your first 30 days, or next month is free.
  - Matching: you don't pay until you're excited about your match.
  - Lifetime Replacement: if your Right Hand ever isn't the right fit, we find you a new one.
- Quote: "It's only day 2 and I'm already feeling such a relief." · Daneen Goncalves

4. SUPPORT
- Heading: Need to change the time?
- Body: Use the reschedule link in your confirmation email, or reply to it and a real person will help within one business day.

5. FOOTER (thin): © Pareto Talent · paretotalent.com

Responsive: cards stack under 900px, the main button is full width on phones, no horizontal scroll at 375px. Use the literal placeholder AUDIT_URL for the button link so I can replace it.

---
(Not part of the prompt.) Setup:
1. Funnel step name `Call Booked`, path `/booked`.
2. Replace AUDIT_URL with your full plain /audit link (not /audit-results: these founders qualified).
3. Calendar form `Calendar Form` → submit button → redirect to the full /booked URL.
4. Test: book a slot from /book in a private window and land on /booked.
5. No AI Studio credits? Paste audit-app/booked-page-embed.html into a Custom HTML element instead (same purpose and design).
