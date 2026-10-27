# Northside Local: Facebook growth and conversion plan

Page: **Northside Local** (Facebook page ID `1401246633065923`, reachable through the Porter Metrics `facebook-insights` connector).

## 0. Read this first: what's wrong with the original idea

1. **"Large following" is not a business goal.** A local page with 20k followers and no booked calls is worth $0 to you. Track the chain *views → follows → DMs → booked calls → clients*, and judge every post by what it does further down that chain.
2. **Decide who the "client" is.** You sell appointment setting. Your buyers are **local business owners** (contractors, med spas, dentists, gyms, real estate), not the general public. The page's job is to build a local audience, which you then use as proof and leverage with those owners: *"I reach 8,000 Northside locals a month, and here's how I fill calendars."* Every T2 and T3 post speaks to owners. T1 speaks to everyone local, because owners are locals too, and the follower count becomes social proof.
3. **100% AI motion graphics is the weakest format for the conversion tier.** Faceless motion graphics work well for T1 and T2: stats, local lists, "did you know", before/after numbers. They do badly at building trust for a service sale. Meta also labels AI-generated media, and in Meta's own guidance on original content, plain recycled or templated content gets less distribution. **Recommendation:** keep the motion-graphics pipeline for 100% of T1 and T2, and make T3 a hybrid: a 10 to 20 second selfie clip of you, wrapped in a motion-graphic intro, outro and captions. If you refuse to show your face, expect T3 to convert noticeably worse, and fill the gap with screenshots of real booked appointments and client results.
4. **Full autopilot posting is a mistake.** One badly generated post (a wrong local fact, a broken render) on a local page costs more trust than it earns. The system includes a mandatory approval step, and approving a week of posts takes about 15 minutes.
5. **Organic reach on Facebook is low for anything but video.** Industry benchmarks put organic page post reach at roughly 1–5% of followers for link and image posts. Reels get recommended to non-followers, which is the only realistic way to grow from zero. So: **Reels only** for T1 and T2, with no link posts. Links get deprioritized, so put any link in the first comment.

## 1. The three tiers

| Tier | Job | Who it's for | Success metric | Share of posts |
|---|---|---|---|---|
| **T1 Reach** | Stop the scroll, earn a follow | Anyone in Northside | 3-sec hold rate, shares, new follows | 60% → 50% |
| **T2 Interest** | Make owners feel the cost of missed leads | Local business owners | Saves, comments from business accounts, profile visits | 30% |
| **T3 Convert** | Get a DM or booked call | Warm owners | DMs with your keyword, calls booked | 10% → 20% |

### T1: Reach formats (motion graphics, 7–20 s)
- **Local lists:** "5 Northside spots locals won't shut up about", "New businesses that opened this month"
- **Local data hooks:** "Northside home prices vs. 2020", "The busiest road in Northside, ranked"
- **This-or-that polls** as video, with the comment prompt "Which one? 👇" (comments push distribution)
- **Shout-outs to local businesses** (tag them). This is your secret weapon: every tagged owner is a future T3 prospect, and they share the post.
- **Event roundups:** "What's on in Northside this weekend" (post Thursday)

### T2: Interest formats (motion graphics, 20–45 s)
- **Cost-of-a-missed-call math:** "A Northside roofer misses 3 calls a week. At a $9k average job and a 20% close rate, that's about $280k a year walking to a competitor." Animated counters work well here.
- **Speed-to-lead stat:** the commonly cited Harvard Business Review / InsideSales research found that contacting a lead within 5 minutes makes qualifying them many times more likely than waiting 30+ minutes. Animate it.
- **Myth vs. reality:** "More ads won't fix an empty calendar"
- **Local owner spotlight** focused on how they get customers. This doubles as relationship-building for outreach.
- **"Owner checklist" carousels-as-video:** "3 signs you're losing leads after the click"

### T3: Convert formats (hybrid, 20–40 s)
- **Result breakdown:** "Booked 14 appointments for a Northside HVAC company in 30 days. Here's the exact follow-up sequence." Use real numbers only. If you don't have a client yet, run a free or low-cost pilot first and post that.
- **Offer post:** "I'm taking 3 Northside businesses this month. DM 'CALENDAR' and I'll audit your lead follow-up for free."
- **Objection killers:** "Why not just hire a receptionist?"
- **Every T3 post** ends with a single CTA: comment or DM a keyword. Don't use a link-only CTA.

## 2. Weekly calendar

Cadence: **2 Reels per week.** At this volume, each post has to do more work, and you need a way to spread posts beyond your own page (below).

| Day | Slot (local time) | Tier | Format |
|---|---|---|---|
| Tue | 12:00 PM | T1 (every week) | Local business shout-out (tag them), local list or local data hook |
| Thu | 7:30 AM | Rotates T2 → T2 → T3 | Cost-of-missed-leads / owner checklist, then a result or offer every 3rd week (owners plan their week Mon–Thu) |

Over a 3-week cycle that's 3×T1, 2×T2 and 1×T3, about 50/33/17. After 1,000 followers, change the rotation to T2 → T3.

**Spreading each post (do this every time; it's what makes 2 posts a week workable):**
- Share every T1 Reel into 2–3 local Northside Facebook groups (community, buy/sell, "what's happening" groups) right after it posts. For a local page, group shares are the biggest reach lever you control. Follow each group's self-promo rules or you'll get removed.
- Tag every business you feature and message them: "Featured you on Northside Local". A good share of them reshare it to their own followers.
- Pin your best T3 post to the top of the page so new followers see the offer first.

These slots are starting guesses based on common commute, lunch and evening scroll patterns. After 6 weeks, move them based on your page's real views by hour from Page Insights.

## 3. Your schedule (fill in, then I'll re-fit the calendar)

You didn't give me your schedule, so this assumes you're setting full-time and protecting your prime calling hours:

| Block | When | Time | What |
|---|---|---|---|
| Ideas + approval | Sunday | 15 min | Send 2 one-line ideas (or say "pick for me"), watch the 2 renders and approve. The pipeline schedules both. |
| Post-day engagement | Tue + Thu, right after the post goes up | 15 min | Share to local groups, message tagged businesses, reply to every comment in the first hour |
| DM follow-up | Daily, end of setting shift | 5 min | Move DMs to a booked call. This is the money step. |
| Monthly review | Last Sunday | 10 min | Read the auto-report and kill or double down on formats |

**Total: about 1–1.5 hours a week.** The two post-day blocks matter more than the videos do. Skip them and 2 posts a week won't grow the page.

**Tell me:** your setting hours, your days off, and your time zone. I'll move the slots so none of them land when you can't reply in the first hour.

## 4. The production system (idea → video → scheduled post)

Built as a Claude skill: `.claude/skills/northside-post/SKILL.md`. Run it with: *"northside-post: <your idea>"* or *"northside-post: plan next week"*.

```
idea ─▶ classify tier ─▶ hook + script + caption ─▶ HyperFrames motion comp (1080×1920)
     ─▶ render MP4 ─▶ YOU APPROVE ─▶ Porter prepare_upload ─▶ facebook_insights.video_upload
        (published=false + scheduled_publish_time = next open slot) ─▶ log to northside/post-log.csv
weekly: facebook_insights.postinsights_get per post ─▶ tier report
```

Porter capabilities verified on 2026-10-27:
- `facebook_insights.video_upload`: uploads a video to a Page, supports `scheduled_publish_time`, and needs no access token (Porter resolves it).
- `facebook_insights.post_create`: text and link posts (scheduled).
- `facebook_insights.postinsights_get` and `insights_get`: per-post and per-page metrics for the weekly report.
- Northside Local shows as **available, not yet materialized** in Porter. The first query or upload takes a licence slot in your Porter workspace. That's expected, but know it before it happens.

## 5. Scorecard: review weekly, decide monthly

Targets are set for 2 posts a week (about 24 posts in 90 days). These are my estimates, not benchmarks; adjust them after the first month of real data.

| Metric | Source | Week 4 target | Week 12 target |
|---|---|---|---|
| Followers | `page_daily_follows_unique` | 200 | 1,000–1,500 |
| Avg Reel views (T1) | `post_total_media_view_unique` | 500 | 2,000 |
| Owner DMs/month | Manual tag in post-log | 1 | 4 |
| Booked calls/month from page | Your CRM | 0–1 | 2 |

**Kill rules (judged monthly, since 2 posts a week means less data):**
- Any format under 50% of your median views after 3 attempts gets dropped.
- If 2 T3 posts in a row get 0 DMs, the offer is wrong, not the content. Rework the offer before you make more videos.

## 6. The honest bottom line

The page alone won't make you wealthy. It's a **lead source and proof asset** for your setting business. Compare its cost to cold outreach: if 2.5 hours a week here produces 4 calls a month, while 2.5 hours of cold DMs or calls produces 10, the page is the worse use of your time until it compounds. Track both for 90 days and let the numbers decide.
