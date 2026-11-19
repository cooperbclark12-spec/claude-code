# Every-2-days Northside Local post: runbook

Runs every second morning (Australia/Brisbane) as a scheduled task. The result is one useful, honest, scheduled post on the Northside Local Facebook page, aimed at owner-run tradies and personal-care businesses in North Brisbane. The page sells Google Business Profile setup ($250/$350) and Profile Care ($100/month); the lead magnet is the free Google Listing Check.

## Rules
- Every post must teach an owner something they can act on today, or start a real conversation. If you can't make one that clears that bar, skip the day and say why. Silence beats filler.
- Facts only. Don't invent statistics, client results or quotes. Google policy claims must be ones Google's own help pages state (for example, review gating is against Google policy). If unsure, leave it out.
- No promises of rankings, calls or timelines. No jargon ("SEO", "NAP", "citations"). Australian spelling. 40–120 words. No emojis in the first line.
- At most one call to action. Rotate it: "Message me your business name for a free listing check" on every 3rd post; a question for comments on the others.
- Skip the day if a spotlight Reel is already scheduled for the same date (check `facebook_insights.scheduledpost_list`) or a post went out in the last 36 hours.
- Never repeat a topic from the last 20 posts (read `northside/post-log.csv` and `post_list`).

## Content pillars (rotate in order, continue from the last one logged)
1. **Myth vs fact** about Google listings (like the "only ask happy customers" post).
2. **Two-minute fix:** one thing an owner can fix on their listing tonight (hours for public holidays, adding services, a reply to a review, photo tips), with the exact steps.
3. **What customers see:** explain one thing a searcher notices, without naming or shaming any real business.
4. **Owner question:** a genuine question that gets tradies commenting ("What's the weirdest thing a customer asked you before booking?").
5. **Behind the work:** what Cooper actually checks in a free Listing Check (from the brief's 14-point checklist), with no client names.
6. **Local:** a northside event, season or moment (storm season and emergency hours, Christmas closures, EOFY), tied to one listing action.

## Steps
1. **Setup:** attach the repo, then read the brief rules in `northside/STRATEGY.md` and this file. Take the Master Brief from Cooper's Drive folder "Ai Operating system " (`1ZYFs5C-tYbrfxqdNvvZLy6iGEllzjvIp`, `MASTER-BRIEF.md`) if available.
2. **Check the page:** Porter `facebook-insights`, page `1401246633065923`: `post_list` (last 20) and `scheduledpost_list`. Apply the skip rules above.
3. **Write the post:** use the next pillar. Read it back as a sceptical 50-year-old plumber: if any line sounds like an ad agency or AI, rewrite it in Cooper's voice (a local young business owner who knows his stuff: plain, short, specific).
4. **Make an image:** a 1080×1350 card in the house style (navy #1b2633 or soil #3d2a1e ground, Inter 900 headline in pale #f5efe6 with one amber #f5b83d word, "Northside Local" mark, no gradients, no emoji, no stock photos). Build it as HTML and screenshot it with Playwright (`require('playwright')`, `chromium.launch()`), then look at the PNG before using it.
5. **Schedule it for 4:00 PM AEST today** (or tomorrow if that's under 2 hours away):
   - upload the image with `facebook_insights.photo_upload` (`published=false`), then `facebook_insights.post_create` with `attached_media=[{"media_fbid": <id>}]`, `published=false` and `scheduled_publish_time`
   - if that combination is refused, schedule a text-only `post_create` and say so in the notification
   - check that it's queued with `scheduledpost_list`
6. **Save the record:** append to `northside/post-log.csv` (date, slot, T2/T3, pillar, hook, CTA, post_id, scheduled), save the copy in `northside/posts/`, then commit and push.
7. **Tell Cooper** in one push notification: the hook line, the live time, how to cancel (Business Suite > Planner), and "reply to every comment in the first hour". If a comment or message on any recent post asks for a Listing Check, flag it as his top priority.
