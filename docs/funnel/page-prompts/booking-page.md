Build a one-page booking page for Pareto Talent. Dark, premium, minimal, one goal: book a call.

Design: page background #070C10, cards #122027, borders #1E2E36, text #F3F6F5, muted text #9AA8B0, accent and buttons #10B981 with #070C10 button text, pill-shaped buttons. Headings in Plus Jakarta Sans (bold), body in DM Sans. No navigation menu, no footer links except "© Pareto Talent · paretotalent.com". Generous spacing, max content width about 1100px.

Sections, in this order, with this exact copy:

1. Thin emerald bar at the very top: "✓ Your audit is on its way to your inbox. Before you open it, one more step."

2. Hero, two columns. Left: eyebrow "You qualify for a free Right Hand Fit Call", headline "You're a fit. Let's find your 10 hours together.", sub-headline "Based on your answers, you're exactly the kind of founder Pareto's Right Hands work with. Pick a time for a free 30-minute call. Do the audit first if you like, or we'll go through it with you on the call. Either way, you leave with your first 30 days of delegation mapped, whether or not you hire.", then a secondary outline button (transparent background, 1px #10B981 border, #10B981 text, pill-shaped) "Get my free audit now →" linking to AUDIT_URL in a new tab. It must look clearly less prominent than the calendar. Right: a card titled "Pick a time that works for you" with the line "30 minutes · Video call · Times shown in your time zone" and an empty space for a calendar (leave room for a booking calendar about 500px tall).

3. "What we'll cover in 30 minutes", three numbered cards:
- Your audit, together. Done it already? We start from your Bottleneck Score and top three Hand-off Hours. Not yet? We run through it with you in the first 10 minutes.
- Your first 30 days. We map which system to hand off first, what access it needs, and what "done" looks like.
- Whether a Right Hand fits. If it does, we explain how matching works. If it doesn't, you still leave with the plan.
Small line under: "No pressure, no hard sell. You keep the plan either way."

4. "Not a VA. A Right Hand." Paragraph: "A full-time, AI-trained operator from Latin America, fluent in English, who works your hours and takes broad goals, not just tasks. They own your inbox and calendar, follow-ups, projects, systems and client communication, and they notice what's missing before you do." Four short points: Matched in 24 hours (three vetted profiles after your matching call) · Only 1 in 1,000 applicants accepted · 30-day integration with a dedicated Success Manager · Weekly Delegation Mastermind with 100+ founders.

5. "Three guarantees, so the risk is ours", three cards:
- Freedom 40 Guarantee: reclaim 40+ hours in your first 30 days, or your next month is free.
- Matching Guarantee: you don't pay until you're excited about your match.
- Lifetime Replacement: if the fit is ever wrong, we replace them, any time.

6. Proof. Two quotes: "I've had three different executive assistants before, and I thought it was me... burning through them." (Eric Ritter) and "I can't imagine going back to like pre-Paula, or pre-an EA." (Bo Royal). Stats row: 100+ founders served · 93% together at 12 months · 4.9/5 on Google.

7. FAQ (accordion):
- What does a Right Hand cost? $3,600 a month on the monthly plan (quarterly and annual plans are lower per month), plus a one-time $3,000 placement fee. Full time only. You don't pay anything until you're excited about your match.
- I've been burned by a VA before. Why is this different? Right Hands are full time, vetted (1 in 1,000), trained 40+ hours on the AI stack, matched to your personality with the PI Behavioral Assessment, and supported by a Success Manager. And if it's not right, we replace them.
- Do I have to decide on the call? No. The call is for mapping your first 30 days. You decide later, if at all.
- Do I need to finish the audit first? No. It helps if you have, but we can do it together on the call.

8. Final section: one centred button "Pick my time →" that scrolls back to the hero.

Technical: output one self-contained HTML block (inline <style>, no external scripts, Google Fonts link allowed) that I can paste into a GoHighLevel Custom HTML element. Make it full width and responsive (stacks to one column under 900px, no horizontal scroll on phones). In the hero's right card, put an empty <div id="fit-call-calendar"></div> where I will paste my booking calendar's embed code. The final "Pick my time" button links to #fit-call-calendar.


---
(Not part of the prompt.) After generating, find AUDIT_URL in the code and replace it with your full /audit preview link.
