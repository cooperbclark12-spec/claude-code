---
name: northside-post
description: Turn a one-line idea into a motion-graphics Reel for the Northside Local Facebook page, get the owner's approval, and schedule it through the Porter Metrics MCP. Also plans the week's 2 posts and reports monthly performance by funnel tier. Use when the user says "northside-post", "make a Northside video", "plan next week's Northside posts", or "Northside report".
---

# northside-post

Strategy and calendar live in `northside/STRATEGY.md`. Read it before the first run in a session, starting with its Correction section.

Business facts come from the Master Brief (`MASTER-BRIEF.md` in Cooper's Drive, or uploaded in chat). Live data in Drive or Airtable beats the brief. The business sells Google Business Profile setup and Profile Care to owner-run trades and personal-care businesses in North Brisbane. Every post must follow the brief's hard rules (section 8): no promised rankings, calls or results, and no naming clients without written OK. Use Australian spelling and no jargon. The T3 CTA is always "Comment CHECK" for the free Listing Check. Times are Australia/Brisbane. Never commit the brief to this repo, because it holds lead phone numbers.

Template: `northside/renders/2026-10-28-reviews-lose-the-job/` is the reference composition. Copy it for new posts, and use its `--variables` (trade, suburb, review counts) for niche variants.

Constants:
- Page: Northside Local, Facebook page ID `1401246633065923`
- Porter connector: `facebook-insights`. Get the `account_id` with `list_accounts(connector="facebook-insights", query="Northside Local")`.
- Log file: `northside/post-log.csv` (columns: `date,slot,tier,idea,hook,cta_keyword,post_id,status`)
- Video spec: 1080×1920 MP4, 7–45 s, burned-in captions (most viewers watch muted), hook on screen within the first 1 s

## Mode A: one idea → scheduled post

1. **Classify the tier.** T1 Reach (local, no selling), T2 Interest (cost of missed leads for owners), T3 Convert (proof + one DM keyword CTA). If the idea doesn't fit any tier, say so and suggest a reframe.
2. **Write the script.** Hook (max 8 words on screen), 3–6 beats, closing line. T1 ends with a comment prompt, T2 with "follow for more", T3 with "DM '<KEYWORD>'". Write the caption (max 2 lines plus 3 local hashtags). Never invent local facts, prices or client results. Ask for the real numbers, or mark them `[VERIFY]`.
3. **Build the video.** Load `anthropic-skills:hyperframes-animation` first, then build a 9:16 HyperFrames composition in `northside/renders/<date>-<slug>/` and render it to MP4. T3 is a hybrid: if the user supplies a selfie clip, use it as the middle segment.
4. **Get approval. Never skip this step.** Send the MP4, script and caption with SendUserFile, along with the proposed slot. Do nothing more until the user says approve. Apply any edits, then re-render.
5. **Pick the slot.** Use the next open slot for that tier from the calendar in STRATEGY.md §2, skipping slots already in `post-log.csv`. Convert it to a Unix timestamp in the user's time zone. Facebook requires 10 min to 30 days ahead.
6. **Upload and schedule.**
   `prepare_upload(purpose="action", action="facebook_insights.video_upload", account_id=<id>)`, then POST the MP4 bytes from Bash per the returned `how_to_post`, with params `page_id=1401246633065923`, `title`, `description=<caption>`, `published=false`, `scheduled_publish_time=<ts>`. Never paste the base64 into chat.
7. **Log it.** Append a row to `post-log.csv` with the returned id and `status=scheduled`.
8. **For T1 posts,** remind the user to share the Reel into 2–3 local groups and message the tagged business once it goes live.

## Mode B: plan next week
Take 2 ideas (Tue T1, Thu per the T2 → T2 → T3 rotation), or generate them from the format lists in STRATEGY.md §1. Map them to the week's calendar slots and run Mode A steps 1–3 for each. Present both for **one** batch approval, then run steps 5–8 for the approved ones.

## Mode C: monthly report
Run monthly. For each post in the log from the last 28 days, call `facebook_insights.postinsights_get` (`post_total_media_view_unique,post_clicks,post_reactions_by_type_total`). For the page, call `facebook_insights.insights_get` (`page_daily_follows_unique,page_post_engagements`, `date_preset=last_28d`). Report by tier: views, follows, DMs (ask the user), and calls booked. Apply the kill rules in STRATEGY.md §5 and recommend next month's mix.

## Rules
- Nothing publishes without explicit approval in this session.
- Only one CTA per post. Don't put links in captions; put them in the first comment.
- The first Porter call against the page materializes it and uses a licence slot. Tell the user before the first call.
