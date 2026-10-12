Build a one-page thank-you page for Pareto Talent. Dark, premium, calm. Main goal: get the visitor to open their free audit right now.

Layout: every section spans the FULL WIDTH of the browser (edge-to-edge background, no boxed container, no white margins). Inner content width about 900px, centred, 16px side padding on phones.

Design: page background #070C10, alternate sections #0E171C, cards #122027 with 1px borders #1E2E36, text #F3F6F5, muted text #9AA8B0, accent #10B981. Primary button: #10B981 background, #070C10 text, pill-shaped, bold, large. Headings in Plus Jakarta Sans (800), body in DM Sans. No navigation menu.

Sections, in this order, with this exact copy:

1. CONFIRMATION (centred, generous space, a small emerald check icon above the headline)
- Headline: Your audit is on its way.
- Sub-headline: We just sent The Founder's Bottleneck Audit to your inbox. Don't want to wait? Open it right here.
- Big button: Start my audit now → (link: AUDIT_URL, opens in a new tab)

2. NEXT STEPS
- Heading: What to do in the next 10 minutes
- Three numbered cards:
  1. Open the audit (here or from your inbox). If it isn't there in two minutes, check Promotions or Spam and drag it to your inbox.
  2. Block 10 minutes today and go through it, one question at a time.
  3. Write down two numbers: your Bottleneck Score and your Hand-off Hours. We'll follow up by email with ideas on what to do with them.

3. A QUICK WIN
- Heading: Start with the system that frees the most hours
- Body: For most founders, that's the inbox and calendar. Try this today: create one rule that moves every newsletter and notification out of your main inbox, and share your calendar with one person on your team so they can book meetings for you. Small, but you'll feel it tomorrow.

4. "NOT READY YET" (objections)
- Heading: "I'm not ready for help yet." That's fine.
- Three cards:
  - "My business isn't big enough yet." The audit works at any size. Run it every quarter: the day your Hand-off Hours pass 10 is usually the day a Right Hand pays for itself.
  - "I tried delegating and it didn't stick." Most founders hand off tasks, not systems. Your audit results include a 30-day plan for handing off a whole system, with a recorded walkthrough and a daily end-of-day report.
  - "I don't have time to train someone." That's why the 30-day plan starts with recording yourself once, not training anyone. Five minutes of video is your first SOP.
- Quote: "It's only day 2 and I'm already feeling such a relief." · Daneen Goncalves

5. SUPPORT
- Heading: Questions or didn't get it?
- Body: Reply to the audit email or write to SUPPORT_EMAIL and a real person will answer within one business day.
- Small muted line: If your business grows or your timeline changes, reply to any of our emails and we'll set up a Right Hand Fit Call.

6. FOOTER (thin): © Pareto Talent · paretotalent.com

Technical: output one self-contained HTML block (inline <style>, no external scripts, Google Fonts link allowed) that I can paste into a GoHighLevel Custom HTML element. Full width and responsive: cards stack under 900px, the main button is full width on phones, no horizontal scroll at 375px. Use the literal placeholders AUDIT_URL and SUPPORT_EMAIL so I can find and replace them.

---
(Not part of the prompt.) Before pasting into GoHighLevel:
1. Find AUDIT_URL and replace it with your full /audit preview link with ?fit=no added to the end (for example https://.../audit?fit=no). Everyone on this page was screened out by the qualifying form, and that ending hides the booking button on their audit results.
2. Find SUPPORT_EMAIL and replace it with an inbox you actually read.
3. Paste this line at the very top, the same full-width fix as the audit page:
<style>html,body{background:#070C10!important;overflow-x:hidden}</style>
