# 🕳️ GAPS extracted from Paper E — DiverseAgentEntropy
### (arXiv 2412.09572, EMNLP 2025 Findings, Amazon Science — see `Paper_E_DiverseAgentEntropy.md` for the full summary)

> Every gap below = something Paper E could NOT show, skipped, or explicitly left
> for future work. Each one is an open question I could own.
>
> ⚠️ RULE: a gap list is AMMUNITION, not a to-do list. A semester tests 1–2 gaps
> properly. Tags: 🎯 CORE (part of my arc) · 🆓 FREE-RIDER (same data, one extra
> pass/plot) · 🅿️ PARKED (future-work / defense ammo only).

---

## From the task shape — single-turn ONLY
*(their own limitation, quotable: "we analyze short-form, query-based uncertainty…
we recognize the need to explore more complex scenarios in future work." Every
benchmark row = one question, one answer. No step 2 exists anywhere in the paper.)*

- **GAP 1** 🎯⭐ MY STRONGEST: the consistency signal has NEVER been run **per-step
  inside a long-horizon trajectory**. Nobody asked "does disagreement between
  rephrased 'what's your next action?' probes RISE before the true failure step —
  and how early?" = my ask-twice probe + LEAD TIME. E supplies the pedigree
  (signal class works, black-box, 0.725–0.947 AUROC); the transplant is mine.
  Pairs with Paper D's "does not forecast drift" hole: D = right setting, wrong
  timing; E = right signal, wrong setting. **The intersection is empty = my seat.**
- **GAP 2** 🅿️ Long-form answers + response-based (not query-based) uncertainty —
  their own named future work. Not my fight, but shows the field knows the hole.

## From the blind spot — confident-wrong (I caught this one myself)
*(consistency detects UNCERTAINTY, not FALSEHOOD: a solidly-stored wrong fact sends
all 5 doors to the same wrong room → zero spread → passes as success. Their own
TruthfulQA score (0.624, near coin-flip, their worst) is the smoking gun. They never
analyze WHICH errors escape the alarm.)*

- **GAP 3** 🎯 Split detector misses by error type: **guessing-type drift (alarmed
  early) vs confident-type drift (silent crash)**. In my Dictionary-Sum lab this is
  measurable for free — failed runs split by whether the alarm fired. Reporting that
  split is itself a finding nobody has. Also PRICES every consistency detector.
- **GAP 4** 🎯 The scrub-probe advantage, testable: scrub doesn't ask "are you
  consistent?" but "does removing your own history CHANGE you?" → can fire even
  under confidence, IF the confidence came from a contaminated transcript
  (Paper A's self-conditioning). Head-to-head ask-twice vs scrub on confident-type
  failures = direct evidence for my novel mechanism.

## From the evaluation — unfair compute + tiny model set
*(E gets ~25 API calls/question, self-consistency baselines get 5. Never
compute-matched. Only 2 models, both 2024-era.)*

- **GAP 5** 🆓 Equal-budget rematch: does E still beat self-consistency when SC
  also gets 25 samples? (My old idea #7 instinct; same fairness move as
  2310.01798's equal-budget critique of debate.) Nobody ran it.
- **GAP 6** 🅿️ Do the numbers hold on modern 2025/26 (incl. thinking) models?
  Cheap half-day sanity check: their repo on ~50 TruthfulQA questions with a
  current model — doubles as my pre-build validation.
- **GAP 7** 🆓 Cost-accuracy curve of the probe itself: their SeQ baseline
  (diversity, NO arguing) = 81.5% vs full 88.3% — so how much signal survives at
  2–3 variants and zero argument rounds? That cheap point on the curve is exactly
  what a PER-STEP probe must use; the curve was never mapped. My harness maps it
  free (vary probe size per run).

## From the interaction — herding never stress-tested properly
*(arguing fixes 18–27% of wrong answers but also breaks 2.5–8.9% of correct ones;
their adversarial ablation = ONE stubborn wrong agent, performance "declines
slightly," weaker model degrades more. No deeper analysis of when consensus is
manufactured rather than discovered.)*

- **GAP 8** 🆓 Over-correction accounting (my idea #5 again, still unclaimed):
  net effect of interaction = fixes minus breakages, BY question difficulty.
  Their numbers hint weak models herd more; never quantified.
- **GAP 9** 🆓 BRIDGE TO #4: peer-disagreement corrected wrong answers WITHOUT any
  oracle → a third feedback condition for my repair toggle: verifier ON vs OFF vs
  PEER-DISAGREEMENT-ONLY. E proves the channel exists in single-turn; nobody tried
  it as a mid-task repair signal.

---

## The short list (what actually enters the proposal)
| Use | Gaps |
|---|---|
| 🎯 Core of my arc | **1** (THE opening for #18) · **3, 4** (probe taxonomy + scrub advantage) |
| 🆓 Free riders on the same data | 5, 7, 8, 9 |
| 🅿️ Parked (defense ammo / future work) | 2, 6 |

One-line memory hook:
> **E proved the consistency alarm works — on standing-still questions. Nobody has
> mounted it on a moving agent and timed how early it fires. That timing (lead time)
> is my paper.**
