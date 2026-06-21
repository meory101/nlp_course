# 🕳️ GAPS extracted from Paper K — Find vs Fix / Backtracking
### (arXiv 2311.08516, ACL 2024 Findings, Google — see `Paper_K_Find_vs_Fix_Backtracking.md` for the full summary)

> Every gap below = something Paper K could NOT show, skipped, or assumed.
>
> ⚠️ RULE: a gap list is AMMUNITION, not a to-do list. A semester tests 1–2 gaps
> properly. Tags: 🎯 CORE (part of my arc) · 🆓 FREE-RIDER (same data, one extra
> pass/plot) · 🅿️ PARKED (future-work / defense ammo only).

---

## From the oracle — perfect hindsight, zero foresight
*(the error location is handed over AFTER the trace is complete. Nobody connected
a real-time detector firing MID-RUN to the repair.)*

- **GAP 1** 🎯⭐ MY STRONGEST: **alarm → rollback → recovery as a function of LEAD
  TIME.** Does backtracking work better the EARLIER the alarm fires (before the
  error cascades / self-conditions per Paper A)? Completely unmeasured. This is
  the #18+#4 pipeline in one experiment — K proved the repair with hindsight; I
  supply the foresight.
- **GAP 2** 🎯 The pointer-accuracy price curve: their simulation gives ONE point
  (~60–70% detector accuracy suffices, on their artificial tasks). The full curve —
  at what accuracy does a pointer flip from helping to harming (the I-vs-K
  combined law) — was never mapped. This curve PRICES my detector (= Paper I
  GAP 9, now with a published starting point).

## From the task shape — reasoning text, not agents
*(CoT traces: no tools, no observations, no environment feedback, no
self-conditioning pressure. Their own limitation: "artificial and unrealistic".)*

- **GAP 3** 🎯 Does find ≪ fix survive in a LONG-HORIZON ACTING agent, where
  errors come from execution (Paper A) and contaminate later steps? My
  Dictionary-Sum harness answers it for free once #18 logging exists.
- **GAP 4** 🆓 Multi-error traces: labels mark the FIRST error only; backtracking
  assumes the rest is clean after one regeneration. Real long runs cascade —
  does one rollback fix a cascade, or does a second error wait behind the first?
  (Bridge to Paper A's error-breeding + Paper I GAP 7 error-deepening.)

## From the evaluation — missing controls
- **GAP 5** 🆓 No equal-budget baseline: backtracking (≤8 retries + completion)
  vs simply RERUNNING the whole task from scratch at the same token cost. If a
  full rerun recovers as much, backtracking is pointless. (Third paper in a row
  missing equal-budget — 2310.01798's lesson keeps applying. Easy table, fully
  mine.)
- **GAP 6** 🆓 Rollback DEPTH: they regenerate AT the error step only. Never
  tested backing up k steps BEFORE it (maybe contamination starts earlier than
  the visible error — scrub-probe logic). One knob, new result.
- **GAP 7** 🅿️ Skew/size: 85% failing traces, small per-task cells; detector
  simulation evaluated on the same 5 artificial tasks.

## From the era — old models, and the thinking-model question
- **GAP 8** 🅿️→🆓 The 53%/+44 NUMBERS are 2023-era; the durable claim is the
  SPLIT. Real 2026 question: are THINKING models (immune to self-conditioning per
  Paper A) also finally good at FINDING errors? If yes, K's bottleneck dissolves
  for them and the premise of self-correction research shifts. Free bonus
  experiment in my harness (one model-swap run).

---

## The short list (what actually enters the proposal)
| Use | Gaps |
|---|---|
| 🎯 Core of my arc | **1** (lead-time × repair = the pipeline) · **2** (price curve) · **3** (agents) |
| 🆓 Free riders | 4, 5, 6, (8 as bonus run) |
| 🅿️ Parked | 7 |

One-line memory hook:
> **K proved repair works with a perfect post-mortem pointer. Nobody measured
> repair with a LIVE, EARLY, imperfect pointer — that's my experiment.**
