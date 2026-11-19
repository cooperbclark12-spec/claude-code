# Weekly Northside Business Spotlight: runbook

Runs every Sunday morning (Australia/Brisbane) as a scheduled task. The result is one finished, scheduled spotlight Reel on the Northside Local page, plus everything Cooper needs to do his part. Cooper is 14–15, on his phone, and has about 5 hours a week. Do the work; send him only what needs his hands.

## Hard rules (never break, from the Master Brief)
- Facts only. The business name, suburb, rating, review count and review quote must come from a source you actually read this run: a screenshot/details.json Cooper dropped in Drive, or a live listing you fetched. Never invent, round or "fix" a number or a quote. A quote may be shortened with "…" but no word is changed.
- No promises of rankings, calls or results. No naming Northside Local clients. Australian spelling, no jargon.
- Feature only owner-run businesses in the service area (Bald Hills, Bracken Ridge, Fitzgibbon, Carseldine, Bridgeman Downs, Brighton, Brendale, Lawnton first; then Sandgate, Strathpine, Bray Park, Warner, Petrie, Boondall, Geebung, Griffin, Aspley, Murrumba Downs, Zillmere, Chermside). Rating 4.7+ and 8–40 Google reviews (good reputation, still a possible client). No chains or franchises.
- Never feature the same business twice: check `northside/post-log.csv`.
- Never message a business from the page. Facebook blocks a page from starting a conversation, so Cooper sends the owner message himself.
- Nothing goes live sooner than 48 hours after this run, so Cooper can watch the preview and cancel it in Meta Business Suite > Planner.

## Steps

### 0. Setup (fresh container)
- Attach `cooperbclark12-spec/claude-code` with add_repo if it's not present, clone it, check out `claude/northside-facebook-strategy-zcax7r` (if its PR has merged, restart the branch from the default branch per the repo's git rules).
- `npm i hyperframes@0.8.207 gsap@3.15.0` in a scratch folder, then `npx hyperframes browser ensure`.
- Read `northside/STRATEGY.md` (Correction section), `.claude/skills/northside-post/SKILL.md`, the last 3 entries of `northside/post-log.csv`, and the newest `northside/posts/*spotlight*.md`.

### 1. Last week's results
Porter Metrics, `facebook-insights`, page `1401246633065923`:
- `facebook_insights.post_list` (last 14 days) and, for each spotlight post, `facebook_insights.postinsights_get` (views, reactions, clicks).
- Read the comments on the latest spotlight. Any business people tagged or named is a candidate for next week: note it.
Write `northside/reports/<date>-weekly.md`: each post's views, reactions and comments, and one recommendation for next week (one change, with the number behind it).

### 2. Pick this week's business (in this order)
a. Newest spotlight drop in Cooper's Drive folder (`1nW7dMPHizCTTu-LEw4zUQ6JHfMb-FYRi`) that isn't in post-log: a `details.json` plus listing and review screenshots. Read the screenshots and confirm every field in details.json matches them exactly.
b. Otherwise, a business tagged in last week's comments. Look it up with Composio `GETANYAPI_SEO_LOCAL_PACK` / `GETANYAPI_FACEBOOK_SEARCH_PAGES` (cap max_cost_usd at 0.10 per call, use an idempotency key, and never retry a keyless paid call). Use it only if you can read a real rating, review count and a real recent review.
c. Otherwise, the same Composio lookup for "<trade> <core suburb>": rotate trades that haven't been featured (electrician, plumber, dog groomer, mobile mechanic, landscaper, cleaner, barber, physio, cafe, carpenter).
d. If nothing passes the rules with verified facts: stop building. Send Cooper (a push notification, plus a file if you can) the terminal prompt below so his computer can find one, and finish steps 1 and 6.

Terminal prompt for Cooper (fill in the next unused trades and suburbs):
> Find the business for the next Northside Business Spotlight. Search Google Maps for "<trade> <suburb>" (5 searches max). Keep owner-run, 4.7★+, 8–40 reviews, phone shown, Facebook page if possible. Pick a recent (3 months) specific review that names the owner or the job and copy it word for word. Screenshot the listing and the review, write details.json (business, trade, suburb, street, rating, reviews, quote, reviewer, owner_name, facebook_url) and upload all 3 to the Drive spotlight folder. Don't contact the business.

### 3. Build the Reel
- Copy the newest spotlight folder in `northside/renders/` into `northside/renders/<date>-spotlight-<slug>/`. Keep the structure: hook on screen at frame 0, a one-take scene that *shows the trade's actual job* (design a new one for each trade, never reuse the last scene), the name slam, the rating (draw partial stars for decimals), the review line by line with the owner's name in amber, and the amber end card. Brand: Northside Local mark, Inter, amber #f5b83d, grain.
- Make it better than last week in one specific way, and name it in the report.
- `npx hyperframes check` must pass with 0 errors (fix contrast, overlap and reading-time warnings), then snapshot 8+ frames and look at every one. Fix anything clipped, overlapping or empty, then render (`--quality delivery`).
- Soundtrack: `northside/automation/make_soundtrack.sh in.mp4 out.mp4 <duration> "<scene-change times>" "<star times>"`. Integrated loudness should land around -20 LUFS.

### 4. Schedule it
- The slot is the coming Wednesday, 4:00 PM AEST (at least 48 h away). Never post after 7 PM.
- Porter `prepare_upload(purpose="action", action="facebook_insights.video_upload", account_id=<Northside Local>)`, then POST from Bash with `published=false`, `scheduled_publish_time=<epoch>`, a title of "Northside Business Spotlight: <Business>", and a description in the house format (number the spotlight from post-log, give the facts, a short quote, "Know a northside business that deserves a shout-out? Tag them below.", and 3 local hashtags).
- Verify with `facebook_insights.post_get` that the title, description, time and length are right. If the upload host is blocked, stop and tell Cooper exactly which host to allow.

### 5. Save the record
Write `northside/posts/<date>-spotlight-<slug>.md`, containing:
- the facts and where they came from
- title, description and group version
- the owner message
- the groups checklist

Then append to `post-log.csv`, commit and push to the branch.

### 6. Hand Cooper his part (one push notification + the files)
- **Preview:** the MP4 (SendUserFile, proactive) plus "goes live Wed 4 PM; cancel in Business Suite > Planner".
- **After it's live, he needs to:**
  1. tag the business's page (give the URL if you found it)
  2. send this owner message (filled in, under 300 characters, no pitch)
  3. share to 2–3 North Brisbane groups using the group version
- **Last week's numbers:** one line, plus the one recommendation.
- **If the business is also a Listing Check prospect:** say so, but never pitch them in the spotlight.
