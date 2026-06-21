# 📄 Paper B — HORIZON
### *The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break*

| | |
|---|---|
| **arXiv** | 2604.11978 (v1 Apr 2026 — FRESH) — Wang et al., UW-Madison + Berkeley (incl. Dawn Song, Rob Nowak) |
| **My thread** | **#16 — MEASURE** (the messy-real-world version of Paper A) |
| **Role in my project** | The judge blueprint + the official failure VOCABULARY + modern-model proof that drift kills. Like A it's a lab paper — but A stays my primary lab. |
| **API-only?** | ✅ All prompting/evaluation; no training. |
| **Code/data** | ⚠️ Leaderboard site only (`xwang2775.github.io/horizon-leaderboard`); full code/data release UNCLEAR from the paper. Scaffold details + judge model + exact s values undisclosed (thin appendix). |
| **Read status** | ✅ Understood via web-pull + discussion (2026-06-06) |

---

## 🎯 THE ONE-LINE POINT
> Stretch the SAME task to controlled lengths in 4 real agent environments, autopsy
> 3,100 runs with a validated LLM-judge (κ=0.84 vs humans), and you find: agents
> don't fade — they fall off a CLIFF; bigger models only MOVE the cliff; and past it
> the CAUSE of death changes — from planning slips to **forgetting + snowballing**.

---

## ⭐ MY GRAB
> **Long-horizon failure is "a structural shift in failure composition," not just a
> score drop — and the killer mistakes happen EARLY, as recoverable local slips that
> later become irreversible. They OBSERVED that window. They never measured it,
> never fired an alarm in it. (⚠️ observed ≠ proved — see the correction box.)**

---

## 🧱 WHAT THEY DID — the lab protocol (7 stages)
1. **4 borrowed worlds + ~700 base tasks:** Web (WebArena: "buy headphones under
   $200"), OS (AgentBench: permissions "except mine"), Embodied (Isaac Sim: "block
   in the MISmatching bowl"), Database (MAC-SQL: "show churned users").
2. **The ruler — intrinsic horizon H\*** = minimum actions a perfect agent needs
   (headphones task: H\*=8: search → filter → sort → … → checkout).
3. **Stretch each task at level s, TWO ways** (see depth/breadth box below), with
   the NESTING trick: level s+1 contains all tasks of level s plus longer ones →
   success drop between levels = pure added length, not changed content.
4. **Run modern agents:** GPT-5, GPT-5-mini, Claude-4-Sonnet × every task × every
   level × 3 runs → **3,100+ full trajectories**, pass/fail per task checker.
5. **Build the death-list via FMEA** (the aerospace/manufacturing failure-catalog
   method) from a pilot of 40 hand-read failures, by 2 experts (κ=0.61 with each
   other — cause-of-death is genuinely arguable). Two families: PROCESS failures
   (during the run) = **72.5%**, DESIGN failures (built-in limits) = **27.5%**.
6. **Certify the robot doctor:** LLM judge reads a full trajectory, assigns failure
   type(s) (multi-label allowed). vs humans on the 40: **κ=0.84** — agrees with
   humans MORE than they agree with each other → unleashed on all 3,100.
7. **Analyze** → the 3 findings.

## ☠️ THE 7 WAYS AGENTS DIE (the taxonomy = my new vocabulary)
| Failure | Plain meaning | Long-horizon native? |
|---|---|---|
| **Catastrophic Forgetting** | early constraint STILL IN the context window but no longer attended to — list in hand, stopped reading it | **L** |
| **History Error Accumulation** | small early mistake snowballs through later steps **= MY DRIFT, official name** | **L** |
| **Memory Limitation** | context truncation — early info literally GONE (≠ forgetting above!) | **L** |
| Planning Error | bad subplan / step ordering | amplified |
| Instruction Error | misreads the (long) instruction | amplified |
| False Assumption | assumes what it never checked | amplified |
| Environment Error | misses that the world changed | amplified |

## 📐 DEPTH vs BREADTH — why TWO stretch directions (took me a while; keep the example)
- **DEPTH = a chain.** Each step needs the previous answer: 2+3=5 → ×2=10 → +1=11
  → ×3=33. One slip at step 1 (says 6) poisons EVERYTHING after: 6→12→13→39. ☣️
- **BREADTH = a pile.** Independent jobs bundled in one instruction: "2+3? capital
  of France? 7×2? translate hello." A slip in job A stays in its box — jobs don't
  use each other's results. 📦
- **Why both:** the snowball needs dependencies to roll → only depth feeds it. But
  forgetting/memory-full only care about LOAD → both shapes feed them. So:
  fails on chains but survives piles → killer = snowball; fails on piles too →
  killer = memory/attention load. One test tangles the diseases; two tests
  separate them (same logic as Paper A's injection experiment).
- **⚠️ MY REFINEMENT (from discussion): the separation LEAKS.** Breadth kills the
  *logical* snowball (data poisoning) but NOT the *imitation* snowball — the model
  still reads its own sloppy job-2 output in the transcript and copies the style
  into job 5 (Paper A's self-conditioning = behavior poisoning, acts in BOTH
  shapes). They never control for it. My scrub probe tests it directly.
- Other breadth-killers beyond memory/forgetting: bookkeeping (finishes 7/10,
  declares victory), misreading the bundle, constraint BLEEDING between jobs
  ($200 limit applied to the wrong job), coordination overhead (their ϵ term).

## 📊 THE 3 FINDINGS
1. **The cliff, not the slope.** Success stays flattish then COLLAPSES abruptly
   past a breaking region. Web collapses first; OS/Database last; Embodied fastest.
2. **Better model = cliff moves, never disappears.** Past the breaking region all
   models converge near zero. Scale buys runway, not safety.
3. **Headline:** "Long-horizon failure is … a structural shift in failure
   composition" — short failures die of planning/instruction slips; long failures
   die of forgetting + snowball + memory-full. Different sickness, not just more
   death. Plus: killer errors "arise early, propagate through downstream actions,
   and convert RECOVERABLE local mistakes into IRREVERSIBLE trajectory-level
   failures."

## ⚠️ CORRECTION BOX — "recoverable" is OBSERVED, NOT PROVED (I caught this)
They never intervened at the early step and showed the run gets saved. The
recoverable→irreversible line = a description from reading autopsies. Who proved
fixability? Paper K (+18..+44 via backtracking) — but post-mortem, with oracle.
| | B | K |
|---|---|---|
| Shows early errors LOOK fixable | observes (no test) | — |
| Proves errors ARE fixable | — | yes, AFTER the run, oracle pointer |
| Proves fixable MID-RUN, alarm-triggered | ❌ nobody | ❌ nobody |
Pitch phrasing: **"B observed the window, K proved repair in hindsight — nobody has
tested repair triggered by an early alarm in real time."**

## ⚠️ HONEST LIMITS (theirs)
- Breaking point = fuzzy REGION, differs per domain (same s ≠ same difficulty).
- Taxonomy from a 40-trajectory pilot; humans only κ=0.61; judge model unnamed;
  multi-label = fuzzy boundaries.
- Diagnostic only — 7 diseases named, ZERO cures tested (no rollback, no
  re-grounding, no intervention).
- Scaffold/loop/max-steps/s-values undisclosed; no cost/token reporting;
  code/data release unclear.

## 🛠️ WHAT I USE
1. **The vocabulary:** my "drift" = their *History Error Accumulation* (+
   *Catastrophic Forgetting*) — official names in a 2026 Berkeley-coauthored paper.
2. **Two pitch quotes:** (a) bigger models move the cliff, don't remove it → scale
   won't fix this → detection necessary; (b) recoverable→irreversible (phrased as
   "observed, not proved" + K's hindsight proof) → the early-warning window.
3. **The judge recipe** (pilot human labels → κ-validate LLM judge → mass-label)
   = my labeling tool for ANY messy environment without a free answer key.
   Copy the protocol, not the artifact.
4. **The depth/breadth control trick** for defense: "is your alarm detecting drift
   or just context length?" → breadth-shaped control run (same length, no chain):
   alarm quiet there = it's really the snowball.
5. **Modern-model proof:** GPT-5/Claude-4 still die of drift — nobody can say
   "newer models solved it."

## 🔗 HOW IT FITS MY ARC
| Thread | What Paper B gives it |
|---|---|
| **#16 Measure** | The messy-world validation of horizon-as-controlled-variable + the cliff finding my drift curves must connect to (see GAP 3: smooth hidden drift → abrupt visible cliff). |
| **#18 Detect** | The motivation quotes + proof the early window exists (observed) + WHY autopsy-judges aren't enough. |
| **#4 Repair** | The taxonomy = a target list per cure; their zero-interventions = open field. |

## 🗣️ SAY-IT-TO-THE-PROFESSOR VERSION
> "April 2026, Berkeley/Wisconsin: they stretch identical tasks to controlled
> lengths across four real agent environments — web, OS, robot, SQL — run GPT-5 and
> Claude-4 on 3,100 trajectories, and autopsy every failure with an LLM judge
> validated at κ=0.84 against humans. Three results: success doesn't decline, it
> falls off a cliff; bigger models only move the cliff; and past it the failure
> composition shifts structurally — long runs die of history error accumulation and
> catastrophic forgetting, diseases that barely exist in short runs. They also
> observe the killer mistakes arise EARLY, as recoverable local slips that turn
> irreversible. But their judge only does autopsies: nothing detects during the
> run, and the recovery window they describe is never measured. My project measures
> exactly that window — lead time — and tests repair triggered inside it."
