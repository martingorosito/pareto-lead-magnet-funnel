Build a one-page landing page for Pareto Talent's free lead magnet, "The Founder's Bottleneck Audit". Dark, premium, minimal, one goal: get the visitor to fill in the form at the bottom.

Layout: every section spans the FULL WIDTH of the browser (edge-to-edge background colour, no boxed container, no white margins on the sides). Inside each section, keep the text readable with an inner content width of about 1200px, centred, with 16px side padding on phones.

Design: page background #070C10, alternate sections slightly lighter #0E171C, cards #122027 with 1px borders #1E2E36, text #F3F6F5, muted text #9AA8B0, accent #10B981. Buttons: #10B981 background, #070C10 text, pill-shaped, bold. Headings in Plus Jakarta Sans (800 weight), body in DM Sans. No navigation menu and no links out of the page except the footer. Every "Get my free audit" button scrolls smoothly to the form section (#get-audit).

Sections, in this order, with this exact copy:

1. HERO (two columns, image on the right; stacks on mobile with headline first)
- Eyebrow: For founders who've become the bottleneck
- Headline: Find the 10 Hours a Week You Should Never Touch Again
- Sub-headline: The Founder's Bottleneck Audit scores the 8 systems where founders lose the most hours, shows you which ones still depend on you, and tells you exactly what to hand off first. Free, interactive, and it takes under 10 minutes.
- Button: Get my free audit
- Under the button, small: Free. Your link arrives in your inbox in under a minute. No call required.
- Proof strip, small, above the fold: ★★★★★ 4.9/5 on Google · 100+ founders served · 93% of placements still together at 12 months
- Right column: an image placeholder <img id="hero-shot" src="" alt="The Founder's Bottleneck Audit results screen"> in a rounded card with a soft emerald glow (I will paste the image URL).

2. WHAT'S INSIDE
- Heading: 10 minutes. Three steps. One number that changes your week.
- Three numbered step cards:
  1. Warm up (1 minute). Tick the six signals founders mention most. You'll know straight away if you're a bottleneck.
  2. Score 8 systems (6 minutes). From inbox to invoicing, two numbers each: who runs it, and how many hours it takes you.
  3. Get your plan (3 minutes). Your results and a 30-day plan to hand off the top three.
- Sub-heading: What you'll walk away with. A checklist with emerald ticks:
  - Your Bottleneck Score (0 to 24). Are you the Delegator, Stretched, the Bottleneck, or the Business Is You?
  - Your Hand-off Hours. The hours a week you spend on work someone else should own. Most founders find 10 or more.
  - The real cost. A simple formula that turns those hours into dollars a year. (A $1M founder with 12 Hand-off Hours spends about $300,000 a year of their own time on it.)
  - Your hand-off-first list. The three systems to delegate first, ranked by hours.
  - A 30-day handoff plan. Week by week, from giving access to measuring the hours you got back.
  - Interactive, in your browser. One question at a time, with your score, hours, cost and plan revealed at the end.
- Button: Get my free audit

3. WHO IT'S FOR
- Heading: Built for founders who've become the bottleneck in their own company
- "This is for you if:" list:
  - You run a growing founder-led business, and you still make most of the calls yourself.
  - You built a company and now you're working in it as a job: 10 to 12 hour days, every day.
  - Your inbox, calendar and Slack all route through you. You're the message router.
  - You've tried a VA before and it didn't stick, so you went back to doing it yourself.
  - Most of the business runs from your memory, and things fall through the cracks every week.
- Muted line: It's not for you if you've already handed off your inbox, calendar and follow-ups to someone you trust, and your week is mostly strategy. (Send it to a founder friend who needs it.)
- Large pull quote: "I'm the bottleneck in my own company." With the line: That's the sentence we hear most from founders. This audit shows you exactly why, in hours.
- Button: Get my free audit

4. PROOF
- Heading: Built from 1,500+ conversations with founders like you
- Body: Pareto Talent places AI-trained Right Hands with US founders. The 8 systems in this audit are the ones those founders hand off first.
- Four big stats in a row: 100+ founders served · 93% of placements still together at 12 months · 1 in 1,000 applicants accepted · 4.9/5 across 84 Google reviews
- Small line: From Pareto's analysis of 1,500+ founder calls: 80% are drowning in admin · 60% have been burned by a VA before · the average founder runs 14 systems from memory
- Three testimonial cards:
  - "I've had three different executive assistants before, and I thought it was me... burning through them." · Eric Ritter
  - "It's only day 2 and I'm already feeling such a relief." · Daneen Goncalves
  - "I can't imagine going back to like pre-Paula, or pre-an EA." · Bo Royal
- Text row: Trusted by founders like Justin Donald, Joe Polish and Jon Vroman
- Button: Get my free audit

5. CTA WITH THE FORM (section id="get-audit")
- Heading: Get your free Bottleneck Audit
- Sub-heading: Tell us where to send it. The last few questions help us tailor what we send you next.
- A centred card about 720px wide containing an empty <div id="audit-form"></div> with min-height 620px, where I will paste my survey embed code.
- Under the card: Free. We never share your details. Your audit arrives in under a minute, and you can unsubscribe in one click.
- Risk reversal line: If you ever want a Right Hand, Pareto backs it with three guarantees: Freedom 40 (40+ hours back in 30 days or next month free), Matching (no payment until you're excited about your match) and Lifetime Replacement.

6. FOOTER (thin): © Pareto Talent · paretotalent.com · Privacy policy

Technical: output one self-contained HTML block (inline <style>, no external scripts, Google Fonts link allowed) that I can paste into a GoHighLevel Custom HTML element. Make it full width and responsive: columns stack under 900px, buttons are full width on phones, no horizontal scroll at 375px. Use smooth scrolling for the #get-audit links.

---
(Not part of the prompt.) After AI Studio generates the code, paste this line at the very top of it before putting it in GoHighLevel. It forces the dark background edge to edge, the same fix used on the audit page:

<style>html,body{background:#070C10!important;overflow-x:hidden}</style>
