# 🕳️ GAPS extracted from Paper I — Decomposing LLM Self-Correction
### (arXiv 2601.00828, Yin Li, Dec 2025 — see `Paper_I_Decomposing_Self_Correction.md` for the full summary)

> Every gap below = something Paper I CLAIMED but could NOT prove,
> or a measurement it skipped. Each one is an open question I could own.
>
> ⚠️ RULE: a gap list is AMMUNITION, not a to-do list. A semester tests 1–2 gaps
> properly. Tags: 🎯 CORE (part of my arc) · 🆓 FREE-RIDER (same data, one extra
> pass/plot) · 🅿️ PARKED (future-work / defense ammo only).

---

## From Row 1 — the Accuracy-Correction Paradox
*(claim: smarter model fixes its own errors LESS — 26.8% weak vs 16.7% strong.
"Paradox" = the OPPOSITE of what everyone expects: accuracy ↑ should mean
self-repair ↑, but they moved in opposite directions.
Weakness: the strong-model side = only 30 errors → 16.7% = 5 fixes = noise.)*

- **GAP 1** 🆓 Does the paradox survive with REAL sample sizes?
  My long-horizon runs produce hundreds of errors per model → free re-test.
  If TRUE it's alarming: better models = LESS self-repair → external
  detect-and-repair (my arc) becomes MORE necessary as models improve.
- **GAP 2** 🅿️ Does it hold on modern (2025/26, thinking) models? They only
  tested small 2024 models (GPT-3.5-Turbo, DeepSeek-Chat, Claude-3-Haiku).
- **GAP 3** 🅿️ Does it hold in AGENTS at all? Only ever observed in one-shot math.

## From Row 2 — the Error Depth Hypothesis
*(claim: deep errors (misread problem / bad logic) resist self-fixing, shallow
ones (arithmetic slips) don't. Weaknesses: (a) each model labeled its OWN errors
= the blind grading its own blindness; (b) the key table — fix-rate PER error
type — was never made; (c) "depth" has no computable definition.)*

- **GAP 4** 🆓 Re-label error depth with an INDEPENDENT judge (not self-labeling)
  — does the hypothesis survive?
- **GAP 5** 🆓 Make the missing table: fix-rate BY depth. One table = new result.
- **GAP 6** 🅿️ Propose an actual METRIC for depth (e.g. how many later steps
  depend on the broken step — computable from my logged trajectories).
  Naming + measuring a fuzzy concept = classic paper contribution.
- **GAP 7** 🆓⭐ THE BRIDGE TO PAPER A: does self-conditioning make errors
  DEEPER over time? Nobody measured depth as a function of step number.
  Connects Paper A ↔ Paper I. Fully mine.

## From Row 3 — "hints hurt" (the localization mess)
*(claim: telling the model WHERE its error is makes fixing worse. Weaknesses:
their own table contradicts the abstract — DeepSeek improved 16.7→26.7%, but
that's 5→8 fixes of 30 = noise; AND their hints were the model's OWN WRONG
GUESSES, while Paper K used TRUE locations and found hints HELP. The combined
untested law: accurate pointer → helps; wrong pointer → worse than silence.)*

- **GAP 8** 🎯 The 3-way test nobody ran: no hint vs SELF-GUESSED hint vs TRUE
  hint (my Paper-A judge knows the true failure step for free). Resolves the
  published Paper I vs Paper K conflict in one table. → my #4 design.
- **GAP 9** 🎯 Is there a POINTER-ACCURACY THRESHOLD — how accurate must an
  alarm's pointing be before acting on it helps instead of harms?
  ← this question literally PRICES my #18 detector.
- **GAP 10** 🆓 Hint effect × error depth (2×3 grid): does a TRUE pointer rescue
  DEEP errors specifically? (Theory: a hint competes with the model's own
  search — handcuffs for shallow errors, the only flashlight for deep ones.)

## From Row 4 — nothing about detect/localize generalizes
*(detection = 10% / 57% / 82% across 3 models, no pattern, no explanation.
These are personality traits of individual models, not laws about LLMs.
The paper itself admits: "self-verification is not a universal capability.")*

- **GAP 11** 🅿️ WHAT MAKES a model good/bad at self-detection? Unknown — it's
  not size and not accuracy (the numbers don't sort that way).
- **GAP 12** 🆓 Replication test they skipped: same protocol on several models —
  which effects REPLICATE (= laws) vs which are idiosyncrasies?
- **GAP 13** 🎯⭐ MY STRONGEST: since built-in detection is unreliable AND
  unpredictable per model, an EXTERNAL, MODEL-AGNOSTIC detector is required —
  that IS my #18. This row is its justification paragraph.

## Bonus gaps — measurements the paper simply skipped
- **GAP 14** 🆓 False-alarm rate: they never showed models CORRECT solutions —
  a detector that says "incorrect" to everything scores 100% on their test.
- **GAP 15** 🆓 Over-correction: correct→wrong flips after self-correction —
  never measured (this was my idea #5; it remains 100% mine).
- **GAP 16** 🅿️ Confidence calibration: they collected HIGH/MED/LOW confidence
  in detection and never analyzed it.

---

## The short list (what actually enters the proposal)
| Use | Gaps |
|---|---|
| 🎯 Core of my arc | **13** (justifies #18) · **8, 9** (designs #4) |
| 🆓 Free riders on the same data | **1, 4, 5, 7, 10, 12, 14, 15** |
| 🅿️ Parked (defense ammo / future work) | 2, 3, 6, 11, 16 |

One-line memory hook:
> **They proved noticing ≠ fixing; everything else they claimed is an untested
> hypothesis — and my harness can test almost all of it for free.**
