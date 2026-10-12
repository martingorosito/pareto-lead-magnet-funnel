# Five Facebook Ads

Five Facebook ads and the AI image prompts behind them. Each ad speaks to a different founder persona from the Research Doc, for a different reason they need a Right Hand. Five different messages, not five hooks on one idea.

Every ad has the six parts from Day 8: **Hook, Offer, Qualifier, Proof, Mechanism, Call to action (one only).** Every ad sends traffic to the same place: the landing page `https://fp-martin-gorosito.vibepreview.app`, offering the free audit.

---

## The five ads at a glance

| Ad | Persona (by cause) | Angle | Funnel stage | Hook |
|---|---|---|---|---|
| 1 | The Founder With No Life | Freedom: you built a job, not a business | Top (broad) | You built a company for freedom. It gave you a job. |
| 2 | The Bottleneck Agency Owner | You've become the message router | Middle (named persona) | Agency owners: you didn't start an agency to forward emails. |
| 3 | The Burned-Before Coach, Speaker or Consultant | It wasn't you, it was the setup | Middle | After the third assistant, you start to think the problem is you. |
| 4 | The Dropped-Ball Founder | Your memory is the only system | Middle | You're not disorganized. You're the only system your business has. |
| 5 | The Established Firm That Wants Zero HR Risk | Risk reversal: someone else carries the hiring risk | Bottom (qualifier and guarantees up front) | Offshore hiring is a gamble. Unless someone else carries the risk. |

**Why these five are genuinely different:** each one names a different cause (no time, too many messages, bad past hire, no systems, hiring risk), so each needs a different proof point and a different reason to take the audit. They also cover all three funnel stages (Day 8: one broad top-of-funnel hook, named personas in the middle, qualifier and offer at the bottom).

**How the ads qualify:** the US filter sits in the ad set's targeting, not the copy. Every qualifier names a situation that signals a real business: a team, paying clients, a full calendar, things slipping. No ad states a revenue figure. Ad 5, the bottom-of-funnel ad, filters harder with the value of the founder's hour ($150+, roughly what $500K a year works out to per working hour), so the ads don't scare off founders who'd still be a fit; the survey's revenue question does the real filtering.

**Hook rules used (Day 8 scripting findings):** no numbers in the hooks (they underperform), negation pointed at the reader, not at a trend, and the founder's own words wherever possible.

---

## Every ad's image layout (final, built in Claude Design)

From top to bottom:
- **Label:** "The Founder's Bottleneck Audit".
- **Hook:** two lines, the second in emerald.
- **Action line:** "Take the free audit and find your bottleneck in under 10 minutes."
- **What Pareto does:** "Pareto Talent places a full-time executive assistant who takes this off your plate. Top 1%, fluent in English, trained on AI."
- **Footer:** the Pareto Talent wordmark, and a "Take the free audit →" button.

## One visual identity

The ads use the same look as the landing page, the emails and the audit PDF, so a founder who clicks recognises the page instantly.

| Element | Value |
|---|---|
| Background | Near-black `#070C10` |
| Accent | Emerald `#10B981` (one accent per image: a light, an object, or the headline highlight) |
| Text | White `#FFFFFF`, secondary grey `#9CA3AF` |
| Headline font | Plus Jakarta Sans, Bold |
| Body font | DM Sans |
| Photo style | Editorial, cinematic, low-key lighting, real-looking founders aged 35 to 55, no stock-photo smiles |
| Layout | Photo fills the frame; headline in the top or left third; small Pareto Talent wordmark bottom left; small "Free audit" emerald pill bottom right |
| Sizes | 1080 × 1350 (4:5, feed) as the master; 1080 × 1080 (1:1) and 1080 × 1920 (9:16, Stories) as crops |

### The shared style sentence (paste at the end of every prompt)
> Editorial cinematic photograph, premium dark aesthetic, deep near-black background (#070C10), a single emerald green (#10B981) accent light, soft directional side lighting, shallow depth of field, natural skin texture, realistic, shot on a 50mm lens, generous negative space in the upper third for a headline, no text, no logos, no watermarks, 4:5 vertical.

**How the imagery was made (Day 7 method):** each prompt = the scene description + the shared style sentence + a screenshot of the palette as a reference image. Iterate on the best result (edit, don't regenerate from scratch), then upscale. Images were generated in ChatGPT. Headline text is added afterwards in Claude Design with the brand fonts, because AI text in images is unreliable.

---

## Ad 1 · The Founder With No Life

- **Persona and cause:** owner-operator at $500K to $5M who built the company for freedom and got a 12-hour, 7-day job.
- **Angle:** the cost of the freedom they gave up. Top of funnel, broad.
- **Client words used:** "I built a company, and now I'm working in it as a job." "I wanted a business that would give me freedom, but instead I work 12 hours a day, every day." (Day 8, verbatim)

**Primary text**

> **[Hook]** You built a company for freedom. It gave you a job.
>
> The inbox, the calendar, the invoices, the follow-ups. Somehow they all still need you.
>
> **[Offer]** The Founder's Bottleneck Audit is a free interactive audit that finds the hours you should never touch again. It takes under 10 minutes.
>
> **[Mechanism]** You score 8 systems on two numbers: who runs it and how many hours it takes you. Out come your Bottleneck Score, your Hand-off Hours, what those hours cost you a year, and a 30-day plan to hand off the top three.
>
> **[Proof]** Built from Pareto Talent's analysis of 1,500+ founder calls. 70% said the same thing: no time, no life.
>
> **[Qualifier]** Made for founders who already have a team and paying clients, but still run every system themselves.
>
> **[CTA]** Get your free audit below.

- **Headline:** Find the 10 hours you should never touch
- **Description:** Free founder audit · under 10 minutes
- **Button:** Learn More
- **On-image text:** "You built a company chasing freedom. **It hired you as its only employee.**" (second line in emerald)

**Image prompt**
> A founder in his mid-40s sitting on metal bleachers at a youth soccer game at dusk, next to his wife. She is smiling and watching their son play on the floodlit field. He is hunched over a laptop on his knees, face lit by the screen with a subtle emerald glow, not watching the game. Shot from slightly in front and to the side, the couple in the lower half of the frame, the field and stadium lights softly blurred behind them, dark evening sky filling the upper third. The tension between work and family is the point. *+ shared style sentence*

**File:** `ad1.png`

---

## Ad 2 · The Bottleneck Agency Owner

- **Persona and cause:** agency or service-firm owner, $500K to $3M; the business outgrew their capacity and every message routes through them.
- **Angle:** they've turned into a message router instead of running the agency. Middle of funnel, named persona.
- **Client words used:** "I'm the bottleneck in my own company." (verbatim) "I've become the full-time manager of communications, a message router." (adapted, Day 8)

**Primary text**

> **[Hook]** Agency owners: you didn't start an agency to forward emails.
>
> Clients message you. Your team messages you about the clients. You answer, forward, remind, and chase. By 6 pm you've done a full day of work and none of it was yours.
>
> **[Offer]** Take the free Founder's Bottleneck Audit and see exactly which messages, follow-ups and approvals still route through you.
>
> **[Mechanism]** Each of the 8 systems comes with a "still yours if" test. Score them in under 10 minutes and you'll get a ranked list of what to hand off first, starting with the inbox.
>
> **[Proof]** From Pareto Talent, who've placed full-time Right Hands with 100+ founders, rated 4.9/5 across 84 Google reviews.
>
> **[Qualifier]** For agency and service-firm owners whose team has grown, but whose inbox never let go.
>
> **[CTA]** Get the free audit below.

- **Headline:** Stop being the message router
- **Description:** Free audit for agency owners
- **Button:** Learn More
- **On-image text:** "Every invoice. Every follow-up. **All of it lives in your head.**"

**Image prompt**
> An agency owner in their late 30s standing in a dark open-plan studio at night, holding a phone, surrounded by dozens of softly glowing floating message bubbles converging toward them from every direction like light trails, all lines of light routing through the person, one bright emerald line among grey ones, team desks empty in the background. *+ shared style sentence*

**File:** `ad2.png`

---

## Ad 3 · The Burned-Before Coach, Speaker or Consultant

- **Persona and cause:** personal-brand founder (coach, speaker, consultant, author) whose past assistants didn't sound like them.
- **Angle:** "it wasn't you, it was the setup", answering the 60% who were burned by a VA. Middle of funnel.
- **Client words used:** "I've had three different executive assistants before, and I thought it was me... burning through them." (Eric Ritter, verbatim, Wall of Love) "My last VA sent AI fluff. It didn't sound like me." (adapted, Day 8)

**Primary text**

> **[Hook]** After the third assistant, you start to think the problem is you.
>
> "I've had three different executive assistants before, and I thought it was me... burning through them." That's Eric Ritter, before Pareto.
>
> It usually isn't you. Delegation fails when you hand off tasks instead of systems, to someone part time who doesn't work the way you do.
>
> **[Offer]** The free Founder's Bottleneck Audit shows which parts of your week truly need your voice, and which only feel like they do.
>
> **[Mechanism]** Score 8 systems in under 10 minutes. You'll get your Hand-off Hours and a 30-day plan that starts with recording yourself once, so the next person learns how you sound.
>
> **[Proof]** 6 in 10 founders on Pareto's calls were burned by a VA before. 93% of Pareto placements are still together at 12 months.
>
> **[Qualifier]** For coaches, speakers and consultants whose name is the brand and whose calendar is already full.
>
> **[CTA]** Get your free audit below.

- **Headline:** It wasn't you. It was the setup.
- **Description:** Free audit · under 10 minutes
- **Button:** Learn More
- **On-image text:** "After the third assistant, **you stopped handing anything off.**"

**Image prompt**
> A confident coach in their early 50s in a warm home podcast studio, sitting in front of a microphone with headphones around their neck, looking thoughtfully at three printed email drafts on the desk, two crossed out in grey marker and one marked with a small emerald check, acoustic panels and bookshelves softly blurred behind. *+ shared style sentence*

**File:** `ad3.png`

---

## Ad 4 · The Dropped-Ball Founder

- **Persona and cause:** fast-growing founder with no systems; everything runs from memory, so invoices, referrals and follow-ups slip.
- **Angle:** they're not disorganized, they're the only system the business has. Middle of funnel.
- **Client words used:** "I'm chasing invoices, opportunities, referral emails, and I start missing things." (adapted, Day 1) "My executive assistant runs point on critical projects and keeps track of endless opportunities." (Joe Polish, verbatim, Wall of Love)

**Primary text**

> **[Hook]** You're not disorganized. You're the only system your business has.
>
> The unpaid invoice, the referral you meant to answer, the proposal that went quiet. Nothing is lost, it's all in your head. Which is exactly the problem.
>
> **[Offer]** The free Founder's Bottleneck Audit gets the open loops out of your head and onto one page.
>
> **[Mechanism]** In under 10 minutes you score 8 systems, from sales follow-ups to invoicing, and see which ones only run because you remember them. Then you get a 30-day plan to hand off the top three, with a daily end-of-day report so nothing slips again.
>
> **[Proof]** "My executive assistant runs point on critical projects and keeps track of endless opportunities." · Joe Polish, Genius Network, a Pareto client.
>
> **[Qualifier]** For founders growing fast enough that things have started to slip.
>
> **[CTA]** Get your free audit below.

- **Headline:** Get the business out of your head
- **Description:** Free audit · 8 systems · 10 minutes
- **Button:** Learn More
- **On-image text:** "You're not disorganized. **You're the only system.**"

**Image prompt**
> Overhead flat-lay of a dark walnut desk at night covered with dozens of scattered grey sticky notes, a phone with notifications, an open notebook and a cold coffee, one single emerald sticky note in the center sharply in focus, a founder's hands at the edge of the frame reaching for it, moody top-down light. *+ shared style sentence (use "top-down composition" instead of "upper third")*

**File:** `ad4.png`

---

## Ad 5 · The Established Firm That Wants Zero HR Risk

- **Persona and cause:** owner or CEO of an established firm (around 50 people) who needs a seat filled reliably and won't gamble on an unvetted offshore hire.
- **Angle:** risk reversal. Someone else vets, manages and replaces. Bottom of funnel: qualifier and guarantees up front.
- **Client words used:** "We want somebody who's vetted, who's proven, who's managed." "If this person is not doing a good job, we want a guarantee." (adapted, Day 8)

**Primary text**

> **[Hook]** Offshore hiring is a gamble. Unless someone else carries the risk.
>
> **[Qualifier]** For founders whose hour is worth more than $150, vetting, training and replacing an assistant yourself is the most expensive way to hire.
>
> **[Proof]** Pareto Talent accepts 1 in 1,000 applicants, trains every Right Hand 40+ hours before they meet you, and 93% of placements are still together at 12 months. Pareto is the employer of record, and every placement comes with a Lifetime Replacement Guarantee.
>
> **[Offer]** Before you hire anyone, find out what the role should own. The free Founder's Bottleneck Audit shows the hours you and your leaders should hand off, and what they cost you a year.
>
> **[Mechanism]** 8 systems, two numbers each, under 10 minutes. You leave with a hand-off-first list that doubles as the job scorecard for your Right Hand.
>
> **[CTA]** Get your free audit below.

- **Headline:** Hire without the hiring risk
- **Description:** Free audit for established firms
- **Button:** Learn More
- **On-image text:** "Offshore hiring is a gamble. **Unless someone else carries the risk.**"

**Image prompt**
> A composed CEO in their early 50s in a dark glass-walled corner office at dusk, standing with arms folded, looking out over a calm, busy open-plan office floor of around fifty people, a single emerald desk lamp lit on the CEO's desk, city lights blurred through the windows, a sense of order and control. *+ shared style sentence*

**File:** `ad5.png`

---

## Pareto Score check (Day 8, 0 to 3 per factor, 16+ ships)

| Factor | Ad 1 | Ad 2 | Ad 3 | Ad 4 | Ad 5 |
|---|---|---|---|---|---|
| View potential | 3 | 2 | 2 | 2 | 2 |
| Proven concept | 3 | 3 | 3 | 2 | 2 |
| Intrigue | 2 | 2 | 3 | 3 | 2 |
| ICP resonance | 2 | 3 | 3 | 3 | 3 |
| Payoff | 2 | 3 | 2 | 3 | 3 |
| Pre-selling power | 2 | 2 | 3 | 2 | 3 |
| Brand alignment (veto) | 3 | 3 | 3 | 3 | 3 |
| **Total / 21** | **17** | **18** | **19** | **18** | **18** |

All five clear the 16-point bar. If one has to be cut for budget, test Ads 3 and 2 first: they name the persona and the objection directly.

---

## Meta ad policy notes (so the ads would actually be approved)

- **No personal attributes asserted about the reader.** Meta rejects copy like "Are you broke?" or "You make $500K". Every qualifier is written about the audience ("For founders growing fast enough that..."), never "You make...".
- **No before-and-after promises of income.** The ads promise hours and a plan, not money.
- **Quotes are real.** Eric Ritter and Joe Polish quotes are verbatim from paretotalent.com's Wall of Love; adapted client words are never presented as testimonials.
- **One CTA, one destination:** every ad points to the landing page `https://fp-martin-gorosito.vibepreview.app` with the Learn More button.

---

## Build the images (about 60 minutes)

1. **Make a palette reference.** In Canva, create a 1080 × 1080 square with three blocks: `#070C10`, `#10B981`, `#FFFFFF`. Download it as `palette.png`.
2. **Generate each image.** In ChatGPT (image generation) or OpenArt, paste the ad's prompt plus the shared style sentence, and attach the palette image. Ask for a 4:5 vertical image.
3. **Iterate, don't restart.** If the first result is close, ask for one change at a time ("make the emerald light smaller", "make the founder look less posed"). Keep the best version.
4. **Upscale** to at least 1080 × 1350 (OpenArt upscale, or Canva's Magic Upscale).
5. **Add the text in Canva.** New design 1080 × 1350. Drop in the image, add a soft dark gradient on the top third, the on-image text in Plus Jakarta Sans Bold (white, with the second line in `#10B981`), the Pareto Talent wordmark bottom left and an emerald "Free audit" pill bottom right. Keep text under about a fifth of the image.
6. **Save the brand kit** (colours and fonts) in Canva once, and reuse it for all five, so they look like one campaign.
7. **Export** each as PNG with the exact file name above.

---

## Where the files are

- Finished ads with text: [`ads/final`](../../ads/final) (`ad1.png` to `ad5.png`)
- Raw AI images without text: [`ads/raw`](../../ads/raw)
- The script that overlays the text on the raw images: [`ads/render_ads.py`](../../ads/render_ads.py)

**Optional, if you want the ads live in Meta:** in Ads Manager, create a campaign named `Bottleneck Audit Ads` (objective: Leads, conversion location: Website), one ad set (United States, broad interests in entrepreneurship and small business owners), and five ads named `Ad 1 · No Life` through `Ad 5 · Zero HR Risk`. Leave it as a draft until there is a budget.
