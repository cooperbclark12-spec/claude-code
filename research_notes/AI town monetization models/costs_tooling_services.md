# Economics of Running AI Towns and "Picks and Shovels" Monetization (costs, infrastructure, tooling, services)

Research date: 2026-11-21. Method note: two official pricing hosts (benchlm.ai, convex.dev) could not be fetched from this research environment (network allowlist), so several prices come from search-result snippets of official docs pages or from aggregators. Each is flagged. Every "per agent-day" figure below is a calculation, marked ESTIMATE, built on one measured baseline (the open-source Generative Agents reproduction cost table).

---

## 1. What it costs to run an AI town (inference + hosting), per agent per day

### Takeaway
A Generative-Agents-style town agent uses about 1.2M tokens per simulated day, mostly input (ESTIMATE, back-calculated from a measured $18.50 / 25-agent / full-day run on gpt-3.5-turbo-0125). At late-2026 cheap-model prices that works out to about $0.06–$0.20 per agent-day (Groq Llama 8B, GPT-5 nano, Claude Haiku 5.5, Gemini Flash-Lite) and $0.50–$1.30 per agent-day on mid-tier "mini/Flash" models. A 25-agent town running around the clock costs roughly $600–$1,600 a year in inference on the cheapest tier, against the original 2023 paper's "thousands of dollars" for 2 days. Hosting (Convex) is small next to inference unless the town has many viewers.

### Cited Findings

**Original paper (2023) baseline**
- Park et al.'s Generative Agents (Smallville): 25 agents interacting for two simulated days. The researchers said it was expensive, "costing thousands of dollars in ChatGPT tokens to simulate two days." — [The Register](https://www.theregister.com/2023/04/11/sims_ai_generation/); same claim in [Windows Central](https://windowscentral.com/software-apps/heres-what-happened-when-stanford-created-a-virtual-world-full-of-chatgpt-powered-people); paper: [arXiv 2304.03442](https://ar5iv.labs.arxiv.org/html/2304.03442)
- "Thousands" is never broken down into tokens or an exact dollar figure in the coverage found. Treat it as an order of magnitude only.

**Measured reproduction costs (key baseline)**
- The open-source reproduction (drudilorenzo/generative_agents) publishes a cost table — [GitHub](https://github.com/drudilorenzo/generative_agents):
  - 3 agents, ~5,000 steps: ~$0.31 (gpt-3.5-turbo-0125 + text-embedding-3-small)
  - 25 agents, ~3,000 steps (until ~8 a.m. game time): ~$1.30
  - 25 agents, ~8,650 steps (one full game day): ~$18.50
  - The configured prices are $0.50/M input and $1.50/M output for generation, and $0.02/M for embeddings. The repo has a `cost-upperbound` setting that stops a run at a spending cap.
- Affordable Generative Agents (AGA, Tencent; TMLR 2024) brings a 25-agent town's token cost down to 42.7% of the Generative Agents baseline (31.1% in a 3-agent setup) and down to 3.4% in VirtualHome. Its main method is replacing repeated LLM calls with learned/cached policies. The paper says most token use is **input** tokens. — [arXiv 2402.02053](https://arxiv.org/abs/2402.02053v2); [arXiv HTML v1](https://arxiv.org/html/2402.02053v1). (The 3.4% and 96.6% figures were confirmed only via a secondary summary in search results.)

**Current model prices (per 1M tokens, input / output)**
- Claude Haiku 5.5 (current Haiku): $0.10 / $0.50 for prompts up to 100K tokens; $0.50 / $2.50 above that. Cache reads are $0.01/M. Batch processing is 50% off. Haiku 4.5 is now legacy at $1 / $5. — [Claude Platform pricing docs](https://platform.claude.com/docs/en/about-claude/pricing); [Haiku 5.5 overview](https://platform.claude.com/docs/en/models/haiku-5-5/overview)
- GPT-5 mini: $0.25 / $2.00 (cached input $0.025). GPT-5 nano: $0.05 / $0.40 (cached $0.005). OpenAI's docs now mark both deprecated and point new high-volume work to "GPT-6.1 Terra", whose price I could not verify. GPT-5.4 nano is listed at $0.20 / $1.25. — [OpenAI GPT-5 mini model page](https://developers.openai.com/api/docs/models/gpt-5-mini); [GPT-5 nano page](https://developers.openai.com/api/docs/models/gpt-5-nano); [Introducing GPT-5 for developers](https://openai.com/index/introducing-gpt-5-for-developers/); [GPT-5.4 nano page](https://developers.openai.com/api/docs/models/gpt-5.4-nano)
- GPT-5.4 mini: $0.75 / $4.50 (aggregator) — [intuitionlabs](https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025)
- Gemini 3.8 Flash: $0.75 / $3.75 through 2026-12-31, rising to $1.50 / $7.50 on 2027-01-01. Gemini 3.5 Flash-Lite: $0.30 / $2.50. Gemini 2.5 Flash-Lite: $0.10 / $0.40. (Aggregators only; not confirmed on Google's page.) — [benchlm.ai via search](https://benchlm.ai/llm-pricing); [qubax](https://qubax.ai/blog/2026-07-28-ai-model-pricing-compared-cheapest-llm-apis-2026)
- Open-weight via hosts (aggregators, 2026): Groq Llama 3.1 8B $0.05 / $0.08; Groq Llama 3.3 70B $0.59 / $0.79; Together Llama 3.3 70B ~$0.88 / $0.88; Together 8B ~$0.18 / $0.18; DeepInfra 70B ~$0.23 / $0.40 (cheapest 70B host). Groq is fastest (500+ tok/s on 8B). — [aipricing.guru Groq](https://www.aipricing.guru/groq-pricing/); [costbench Groq vs Together](https://www.costbench.com/compare/groq-vs-together-ai/); [aipricing.guru Meta Llama hosted](https://www.aipricing.guru/meta-pricing/). One page says some Groq Llama models are now "contact sales", which conflicts with the published rates.
- Aggregators disagree on GPT-5 mini (some list $0.50/$2.00 or $1.50/$6.00). The OpenAI model page ($0.25/$2.00) wins here. — [intuitionlabs](https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025)

**AI Town (a16z) stack and hosting**
- a16z-infra/ai-town defaults to **local Ollama** (`llama3` for chat, `mxbai-embed-large` for embeddings). It also supports OpenAI, Together.ai, or any OpenAI-compatible API (Anthropic, Groq, Azure) via `LLM_API_URL`. The backend is Convex, which needs a free account; the whole thing can also run self-hosted with Docker Compose, deploy on Fly.io, or put the frontend on Vercel. — [AI Town README](https://raw.githubusercontent.com/a16z-infra/ai-town/main/README.md)
- Built-in cost controls: the simulation pauses after 5 minutes without browser activity (a "stop inactive worlds" cron), and there are manual freeze and `npx convex run testing:stop` options. — [AI Town README](https://raw.githubusercontent.com/a16z-infra/ai-town/main/README.md)
- AI Town is described as MIT-licensed — [brightcoding blog](https://prompts.brightcoding.dev/blog/ai-town-build-your-own-autonomous-ai-agent-society) (third party; the README fetch did not show the license).
- Convex pricing (search snippets of official docs/pricing pages): free Starter tier with 1M function calls/month and 1 GiB database bandwidth; Professional at $25/developer/month with 25M function calls and 50 GiB bandwidth included; overage $2 per extra 1M calls and $0.20/GiB; Business/Enterprise from a $2,500/month minimum. A third-party calculator lists 250M calls on Pro, which conflicts with the official 25M. Database I/O is billed by documents *scanned*, not returned, and is the meter that "most often surprises" users. — [Convex pricing](https://www.convex.dev/pricing); [Convex limits docs](https://docs.convex.dev/production/state/limits); [activepieces guide](https://www.activepieces.com/blog/how-to-choose-a-convex-pricing-plan-in-2026); [budgetforge](https://www.budgetforge.dev/tools/convex-pricing-2026)
- A Convex Discord user asked what AI Town's Convex bill would be per hour at a given concurrent-user count. No published answer was found. — [Convex Discord thread](https://discord-questions.convex.dev/m/1140994230022582312)

### Inferences (calculations — all ESTIMATES)

**Step 1: tokens per agent-day (sim day).** $18.50 / 25 agents = **$0.74 per agent per simulated day** on gpt-3.5-turbo-0125. Assume a 90% input / 10% output token split (AGA says input dominates; 90/10 is my assumption). Blended price = 0.9 × $0.50 + 0.1 × $1.50 = $0.60/M. So $18.50 / $0.60 ≈ 30.8M tokens per town-day, or **≈1.23M tokens per agent-day (≈1.11M input, ≈0.12M output)**. Embedding cost is negligible at $0.02/M.

**Step 2: cost per agent-day at 2026 prices** (1.11M input + 0.12M output, no caching):

| Model / host | $ in / out per M | Cost per agent-day | 25-agent town per day | 25 agents × 365 days |
|---|---|---|---|---|
| Groq Llama 3.1 8B | 0.05 / 0.08 | ~$0.065 | ~$1.6 | ~$590 |
| GPT-5 nano | 0.05 / 0.40 | ~$0.10 | ~$2.6 | ~$950 |
| Gemini 2.5 Flash-Lite | 0.10 / 0.40 | ~$0.16 | ~$4.0 | ~$1,450 |
| Claude Haiku 5.5 | 0.10 / 0.50 | ~$0.17 | ~$4.3 | ~$1,560 |
| DeepInfra Llama 70B | 0.23 / 0.40 | ~$0.30 | ~$7.6 | ~$2,760 |
| GPT-5 mini | 0.25 / 2.00 | ~$0.52 | ~$13 | ~$4,730 |
| gpt-3.5-turbo-0125 (baseline) | 0.50 / 1.50 | $0.74 (measured) | $18.5 | ~$6,750 |
| Groq Llama 3.3 70B | 0.59 / 0.79 | ~$0.75 | ~$19 | ~$6,850 |
| Together Llama 3.3 70B | 0.88 / 0.88 | ~$1.08 | ~$27 | ~$9,860 |
| Gemini 3.8 Flash (2026 promo) | 0.75 / 3.75 | ~$1.28 | ~$32 | ~$11,700 (doubles in 2027) |
| Claude Haiku 4.5 (legacy) | 1.00 / 5.00 | ~$1.71 | ~$43 | ~$15,600 |

- Per agent-**hour** (24 sim hours per sim day): about $0.003 (Groq 8B) to $0.007 (Haiku 5.5) to $0.02 (GPT-5 mini).
- **Caching:** with Haiku 5.5, if 70% of input is cache reads (persona and memory prefixes; my assumption): 0.33M × $0.10 + 0.78M × $0.01 + output $0.06 ≈ **$0.10/agent-day**, down about 40%.
- **AGA-style optimization:** multiply by 0.427 (25-agent result). Haiku 5.5 ≈ $0.07, GPT-5 mini ≈ $0.22 per agent-day.
- **Batch API (50% off)** suits offline research sims, not live interactive towns.
- **Caveats:** (a) GPT-5-family "mini/nano" are reasoning models. Hidden reasoning tokens are billed as output and could raise their figures several-fold, so their cost depends on the effort setting. (b) Token use depends on implementation: AI Town's conversation-centric design differs from Smallville's planning/reflection loop. (c) "Sim day" ≠ wall-clock day. A town shown in real time (1 sim day per 24h) matches the table; a town fast-forwarded 10× costs 10× per wall-clock day. (d) Cost scales with interactions: conversation calls grow with agent density, so 25 → 1,000 agents is not exactly linear.

**Step 3: reconciling with "thousands of dollars".** In 2023 gpt-3.5-turbo cost about $2/M (from memory, not re-verified here). 30.8M tokens/day × 2 days × $2 ≈ $125, far below "thousands". The gap likely comes from development and debug runs, evaluation interviews, less-optimized prompts, or partial GPT-4 use (INFERENCE, not confirmed). In any case, the cost of the same workload per agent-day has fallen from **~$40–$100+ (2023, implied by "thousands"/50 agent-days)** to **~$0.10–$0.20 (2026 cheap tier)**, a drop of roughly 200–1,000×.

**Step 4: hosting.** A 25-agent town on Convex Pro ($25/dev/mo + 25M calls) is a fixed cost of about $25–$75/month for a hobby or medium-traffic town (ESTIMATE; assumes the game loop and viewers stay near the included quota; I found no measured AI Town call counts). Hosting becomes significant only with many concurrent viewers, because database bandwidth and scanned documents grow with traffic. Local Ollama shifts the cost to hardware and electricity: the marginal token is free, and throughput is limited by the GPU.

**Bottom line:** a 25-agent public town on a cheap API costs about $5–$15/day all-in (ESTIMATE), roughly $150–$450/month. That bill is the reason builders sell tooling and services instead of running towns themselves (see section 2).

### Gaps
- The original paper's exact dollar figure and token counts were not published in any source found.
- No measured token/day figure exists for a16z AI Town (vs. Smallville). No measured Convex function-call counts for AI Town.
- Official Google Gemini pricing page not verified (aggregator figures only); GPT-6.1 Terra pricing unverified.
- Wall-clock vs. sim-time ratio of AI Town's default engine not documented in sources fetched.
- Local GPU cost per million tokens: no reliable source captured (a Findstack "Ollama on a VPS" article exists but was not read).
- OASIS (1M agents) compute/GPU cost not extracted from the paper.

---

## 2. Tooling / SaaS platforms selling agent-world infrastructure: pricing and revenue

### Takeaway
The companies capturing value are general infrastructure (Convex as a backend, Inworld as a character/voice API, Fetch.ai and Virtuals as crypto agent rails), not "AI town" products. Most simulation frameworks (TinyTroupe, Concordia, OASIS/CAMEL, AI Town) are free and open source and make no direct revenue. Disclosed revenue is small: Inworld is estimated at $1–10M, and Virtuals runs about $3M/yr protocol revenue on a trailing basis.

### Cited Findings
- **Convex** (AI Town's backend; a16z-backed): raised a $24M round in Nov 2025 led by a16z with Spark co-leading, then a **$57M Series B (Aug 4, 2026) led by Insight Partners**, bringing total funding to **$110.5M**. It is positioned as an "AI-optimized application backend". Sources disagree on earlier rounds (one cites a $26M Series A led by a16z). — [Convex blog: raises $24M](https://news.convex.dev/convex-raises-24m/); [SiliconANGLE 2026-08-04](https://siliconangle.com/2026/08/04/convex-reels-57m-ai-optimized-application-backend/); [Pulse 2.0](https://pulse2.com/convex-raises-57-million-series-b-bringing-total-funding-to-110-5-million/); [Sacra](https://sacra.com/c/convex/). Pricing is in section 1.
- **Inworld AI** (character engine / voice for NPCs): ~$50M round in Aug 2023 led by Lightspeed at a >$500M valuation; total funding is cited anywhere from ~$117M to ~$153M by different aggregators. In June 2026 Inworld cut prices by more than 50% across TTS, STT, and LLMs. It reportedly acquired Ultravox (closed 2026-09-30, per a secondary source). Dealroom estimates revenue at **$1–10M** (unverified estimate). — [BusinessWire 2023](https://www.businesswire.com/news/home/20230802502983/en/); [BusinessWire June 2026 price cut](https://www.businesswire.com/news/home/20260610968386/en/); [Dealroom](https://dealroom.co/companies/inworld-ai/); [GamesBeat](https://gamesbeat.com/inworld-ai-raises-new-round-at-500m-valuation-for-ai-game-characters)
- **Fetch.ai Agentverse:** no official price list was found. A third party lists Basic $0, Premium $25/month, and custom Enterprise (unverified). Official docs require an active subscription for agent mailboxes; on the free tier that means logging in at least once every 30 days. Paying in FET/ASI gives 15% off. Agentverse reportedly hosts ~2.7–3M registered agents. — [Agentverse docs: subscriptions & quotas](https://docs.agentverse.ai/documentation/advanced-usages/agentverse-subscriptions-and-quotas); [aimojo](https://aimojo.io/tools/agentverse/); [Crypto Briefing](https://cryptobriefing.com/fetch-ai-agent-marketplace-3-million-agents/)
- **Virtuals Protocol** (crypto agent launchpad): DefiLlama trailing-year annualized **~$9.64M fees / ~$3M revenue**; the latest 30 days show only ~$120K fees and ~$37K revenue, a steep decline. Revenue comes from a 1% fee on agent-token trades plus a 100 $VIRTUAL launch fee. Virtuals said it spends >$1M/month on agent incentives (Feb 2026). Agent-to-agent commerce revenue passed $3M (Mar 2026, secondary). — [DefiLlama](https://defillama.com/protocol/virtuals-protocol); [Blockworks income statement](https://blockworks.com/analytics/virtuals/virtuals-financials-new/virtuals-income-statement-2); [KuCoin flash](https://www.kucoin.com/news/flash/virtuals-protocol-allocates-over-1m-monthly-for-agent-incentives); [Forkast "real fees, elastic numbers"](https://forkast.news/state-of-virtuals-real-fees-elastic-numbers/)
- **CAMEL-AI / OASIS / Eigent:** OASIS is an open-source social-media simulator that supports up to 1M LLM agents. — [arXiv 2411.11581](https://arxiv.org/html/2411.11581v3); [GitHub camel-ai/oasis](https://github.com/camel-ai/oasis). Monetization goes through **Eigent** (a subscription product); 10% of Eigent's subscription fee funds the CAMEL Open Source Foundation, alongside GitHub Sponsors. — [Eigent open-source fund](https://www.eigent.ai/es/open-source-fund). Dealroom lists no known external funding for Eigent. — [Dealroom](https://app.dealroom.co/companies/eigent_ai)
- **Microsoft TinyTroupe:** open source, persona-based simulation for "virtual focus groups" and product testing. The README says it is for research and simulation only; Microsoft called it experimental and not ready for professional use. It has no paid offering. — [TinyTroupe README](https://raw.githubusercontent.com/microsoft/TinyTroupe/main/README.md); [The Decoder](https://the-decoder.com/microsofts-tinytroupe-library-creates-ai-powered-virtual-focus-groups-for-product-testing/); [arXiv 2507.09788](https://arxiv.org/html/2507.09788v1)
- **Concordia (Google DeepMind), AgentVerse (OpenBMB):** no pricing or commercial info found; both are presumed free research libraries (unverified here).

### Inferences
- The "picks and shovels" layer that actually earns money is (a) generic backend, inference, and voice APIs paid per usage, and (b) crypto launchpads that take trading fees. Simulation-specific frameworks are mostly free and paid for by big companies or research labs, so a solo builder cannot easily charge for a framework.
- Inworld cutting prices by more than 50% in 2026 points to commoditization pressure on "AI character" APIs as base-model prices fall.
- Virtuals' revenue is closely tied to speculation (a 30-day run-rate of ~$0.45M/yr against ~$3M trailing), so crypto-rail income is volatile.

### Gaps
- No pricing page fetched for Inworld (post-cut), Concordia, AgentVerse.
- No revenue figures for Convex (Sacra may have an estimate; not retrieved).
- Fetch.ai official subscription prices unverified.

---

## 3. Freelance/dev services, templates/courses, hackathons, grants, sponsorships

### Takeaway
Services pay modestly on marketplaces: about $25–$45/hr for posted multi-agent (LangGraph/CrewAI) work on Upwork. "AI town" templates and courses are a thin niche, with no Gumroad listing found that is specifically an AI-town kit; adjacent agent kits sell for $19–$345. Hackathon prizes are mostly small ($750 at a college hackathon), with crypto agent hackathons reaching ~$100K total pools. a16z Open Source AI Grants are non-dilutive but by invitation only.

### Cited Findings
- **Upwork budgets:** "AI Engineer for Multi-Agent Orchestration" (LangGraph/CrewAI/AutoGen, expert level, 1–3 months): **$30/hr**. "Senior AI Agent Engineer (OpenAI, LangGraph, FastAPI)": **$25–$35/hr**, 30+ hrs/week. "AI Systems Architect – LangGraph & RAG" (intermediate, 3–6 months): **$25–$30/hr**. A multi-agent/LangGraph agency profile: **$25–$45/hr**. — [Upwork job 1](https://www.upwork.com/jobs/~022066934148697692363); [Upwork job 2](https://www.upwork.com/freelance-jobs/apply/Senior-Agent-Engineer-OpenAI-LangGraph-Python-FastAPI_~022074827809015794397/); [Upwork job 3](https://www.upwork.com/jobs/~022093632251730338229); [Upwork agency](https://www.upwork.com/agencies/2103936255231378932/)
- Upwork also sells fixed-price "project catalog" services such as "Multi-Agent AI Systems with CrewAI, LangGraph & AutoGPT" (price not captured). — [Upwork service](https://www.upwork.com/services/product/development-it-multi-agent-ai-systems-with-crewai-langgraph-autogpt-2054672277658179854)
- A 2026 consultant-rate guide says multi-agent and RAG skills add **20–30%** to base rates, and that most "AI agent" work on Upwork is template-based, not custom production work. — [DEV Community](https://dev.to/jahanzaibai/ai-automation-consultant-hourly-rate-what-youll-actually-pay-in-2026-and-when-its-worth-it-55ln)
- **Templates/courses:** Gumroad "2 Course Bundle: Generative design & Agent Simulation" sells for **$345**. — [Gumroad arsiliath](https://arsiliath.gumroad.com/l/bundle). A multi-agent ADK builder pack (ADK, A2A, MCP, Cloud Run scripts) sells for **$29**. — [Gumroad chongdashu](https://chongdashu.gumroad.com/l/adk-builder-pack-1). A generic agent starter kit sells for **$19.99**. — [DEV Community](https://dev.to/_df5259e5cebd3a923371e/build-your-first-ai-agent-in-one-afternoon-complete-starter-kit-for-1999-48bn). No Gumroad product specifically for an "AI town" was found. Sales volumes were not visible.
- **Hackathons:** Hack@Brown 2026 (Fetch.ai sponsor) "Best Overall AI Agent Solution": **$750**. — [Fetch.ai Innovation Lab](https://innovationlab.fetch.ai/events/hack-brown-2026). Colosseum Solana Agent Hackathon: total prizes capped at **$100,000** in USDC. — [Colosseum](https://colosseum.com/agent-hackathon/). A UCL AI Festival team won Anthropic's prize for best use of the Claude Agent SDK with an AI-town-like simulation: 100+ autonomous agents with avatars in a pixel-art office running a simulated hackathon (prize amount not stated). — [EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/ucl-team-wins-anthropic-prize-after-simulating-hackathon-with-ai-agents). HackSim (ETHGlobal showcase) is a multi-agent simulation of a hackathon on Gensyn AXL. — [ETHGlobal](https://ethglobal.com/showcase/hacksim-nyk7y)
- **Grants:** a16z Open Source AI Grant gives grant funding, not an investment or SAFE. Batches were announced in Aug 2023, Dec 2023, and June 26, 2025 (e.g., Open WebUI). There is no public application; a16z selects recipients. — [a16z: supporting the open source AI community](https://a16z.com/supporting-the-open-source-ai-community/); [a16z latest grants](https://a16z.com/announcing-our-latest-open-source-ai-grants); [Superscout](https://superscout.co/program/a16z-open-source-ai-grant). (a16z also released AI Town itself, which shows its interest in this category — [AI Town repo](https://github.com/a16z-infra/ai-town/).)
- **Ecosystem incentives:** Virtuals spends >$1M/month on agent incentives (crypto). — [KuCoin flash](https://www.kucoin.com/news/flash/virtuals-protocol-allocates-over-1m-monthly-for-agent-incentives)
- **Open-source sponsorship model:** CAMEL uses GitHub Sponsors plus a 10% share of its subscription product. — [Eigent open-source fund](https://www.eigent.ai/es/open-source-fund)

### Inferences
- **Freelancer unit economics (ESTIMATE):** at $30/hr and 30 hrs/week for 3 months (~390 hrs), one gig is worth ≈ $11.7K gross, or ≈ $10.5K after Upwork's fee (fee level assumed ~10%, not verified here). By comparison, a 25-agent town costs ~$4/day in Haiku 5.5 inference. One medium contract pays for about 7 years of running a cheap town, so services clearly beat running a town on cash flow.
- **Templates (ESTIMATE):** at $29–$345 per sale, reaching $1K/month takes about 3–35 sales a month. With MIT-licensed AI Town free on GitHub, a paid template has to offer customization, deployment, or a course, not just code.
- **Hackathons:** good for visibility and portfolio, not income. Prizes are $750 at the typical college event, and the largest pools are on crypto-sponsored hackathons.
- **Is the picks-and-shovels side profitable?** For individuals, yes at a modest scale: freelance work runs $25–45/hr, and inference costs are trivial next to that. For platforms, the evidence is weak. Inworld's estimated revenue is $1–10M against over $100M raised, Virtuals' revenue is falling, and simulation frameworks are free. Convex's $57M Series B shows investors back general AI backend infrastructure, not town-specific tooling.

### Gaps
- No Fiverr listings found specifically for "AI town" or agent-simulation gigs. No top-tier (>$100/hr) multi-agent rates captured.
- No Gumroad sales counts or revenue for agent templates and courses.
- No crypto-foundation grant programs (e.g., Solana, Base, NEAR, Fetch.ai) with amounts for agent-simulation projects were confirmed.
- No sponsorship deals (brand-sponsored towns, streamer sponsorships) found.
- No case study of a builder disclosing profit from AI-town tooling or services.
