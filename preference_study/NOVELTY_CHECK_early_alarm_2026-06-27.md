# NOVELTY CHECK — Early-Alarm / Lead-Time Idea (prior-art sweep)

**Date:** 2026-06-27
**Why:** Professor approved the presentation and asked for a *preference study*; the
EARLY-ALARM idea (#18 detect) is the chosen direction. Before committing, ran a deep
multi-source prior-art sweep (17 papers fetched, 78 claims extracted, 24 adversarially
verified 3-vote) to confirm the idea is not already taken.

**My proposed contribution (the thing being checked):**
A LIVE, black-box (API-only), self-monitoring early-alarm signal that fires BEFORE
failure + a LEAD-TIME metric = (true failure step) − (first alarm step) + a
recovery-rate-vs-lead-time curve.

---

## ⚠️ VERDICT: PARTIALLY TAKEN — not fully novel (but a defensible gap remains)

The abstract combination of (forecast failure BEFORE it happens) + (a steps-in-advance
lead-time metric) is **no longer untouched** — one 2026 paper does both. Do NOT claim
"nobody has done early warning." Reframe the pitch around the defensible gap below.

---

## 🔴 PRINCIPAL THREAT — SafetyDrift (arXiv:2603.27148, Dhodapkar & Pishori, 28 Mar 2026)
- **Link:** https://arxiv.org/abs/2603.27148
- **Mechanism:** models agent trajectories as **absorbing Markov chains**, computes the
  probability a trajectory reaches a violation within N future steps.
- **The damaging sentence:** "a lightweight monitor… **detects 94.7% of violations with
  3.7 steps of advance warning** at negligible computational cost" (>60,000× faster than
  per-step LLM judges).
- **Why it threatens me:** that is forecasting-before-failure **+** an explicit
  steps-in-advance lead-time number = my two core pillars, already in print.
- **Why I'm still alive (memorize these 3 differences — this is the whole defense):**
  1. It targets **SAFETY / policy violations** (data-leak, capabilities, reversibility),
     **NOT general off-task / task-failure drift** (my target).
  2. It uses a **structured Markov state model**, NOT a **black-box, API-only, per-step
     self-monitoring** signal.
  3. It has **NO recovery-rate-vs-lead-time curve** — nobody does.

---

## OTHER CLOSE WORK (know these — don't get surprised in defense)

- **InferAct** (arXiv:2407.11843, EMNLP 2025) — genuinely preemptive (Theory-of-Mind,
  catches a misaligned action *before execution*), BUT only the immediate **next action**;
  **no lead-time / steps-in-advance metric**. Different granularity from mine.
  Link: https://arxiv.org/abs/2407.11843
- **Agentic Overconfidence** (arXiv:2602.06948, Feb 2026) — CLOSEST IN SPIRIT. Elicits the
  agent's success probability before / DURING (25%, 50%, 75% of steps) / after a run.
  ⚠️ **KEY NEGATIVE RESULT:** mid-run self-doubt is **uninformative — fires equally for
  successes and failures.** → A naive "are you still on track?" prompt will NOT work.
  **This is now my real scientific risk (not novelty): my scrub-probe / ask-twice signal
  must BEAT this baseline.**
  Link: https://arxiv.org/abs/2602.06948
- **The Intervention Paradox** (arXiv:2602.03338, Feb 2026) — a 0.94-AUROC critic still
  caused a **26-point performance collapse** when used to intervene (disruption-recovery
  tradeoff). HELPS me: proves a recovery-vs-lead-time curve is a real, non-trivial result.
  Link: https://arxiv.org/abs/2602.03338

## NOT A THREAT (post-hoc / white-box — preserve my novelty)
- **HTC / Agentic Confidence Calibration** (2601.15778) — needs the COMPLETED run +
  token log-probs (white-box). Post-hoc, no lead-time. https://arxiv.org/abs/2601.15778
- **HORIZON / Task Mirage** (2604.11978) — LLM-as-judge failure *attribution* over
  finished trajectories. Answers where/why, not *when during* the run.
  https://arxiv.org/abs/2604.11978
- **Entropy-trajectory-shape** (2603.18940) — diagnostic study of single-instance CoT,
  not long-horizon agents. https://arxiv.org/abs/2603.18940
- **UProp** (2506.17419, https://arxiv.org/abs/2506.17419), **AUQ** (2601.15703,
  https://arxiv.org/abs/2601.15703) — live per-step uncertainty (my category 4)
  but reactive in-the-moment, no lead-time metric.
- **Runaway is Ashamed but Helpful** (2505.17616) — efficiency-oriented early-exit, not
  failure forecasting. https://arxiv.org/abs/2505.17616

---

## ✅ DEFENSIBLE GAP — the reframed pitch for the professor
> A **live, black-box (API-only), self-monitoring** early alarm for **GENERAL
> task-failure / off-task drift** (not safety-policy violations), evaluated with a
> **recovery-rate-vs-lead-time curve** — no single existing paper delivers all three
> together. SafetyDrift is the nearest neighbor: cite it, then pivot on these 3 points.

## CAVEATS / TODO
- ⚠️ Those 2026 arXiv IDs (2602/2603/2604-series) are real but VERY fresh. **Re-run this
  sweep right before submission** — this area is producing directly-relevant papers
  monthly (SafetyDrift, AUQ, HTC, Agentic Overconfidence all Jan–Mar 2026).
- Add a pitch sentence on WHY my signal would beat naive self-doubt (counters 2602.06948).
- Open question: does SafetyDrift's Markov state abstraction generalize to task-failure
  drift, or is it fundamentally safety-specific? (My differentiation hinges on this.)

## SOURCES (all primary arXiv, verifier-confirmed)
- SafetyDrift — https://arxiv.org/abs/2603.27148
- InferAct — https://arxiv.org/abs/2407.11843
- Agentic Overconfidence — https://arxiv.org/abs/2602.06948
- Intervention Paradox — https://arxiv.org/abs/2602.03338
- HTC — https://arxiv.org/abs/2601.15778
- HORIZON — https://arxiv.org/abs/2604.11978
- Entropy-shape — https://arxiv.org/abs/2603.18940
- UProp — https://arxiv.org/abs/2506.17419
- AUQ — https://arxiv.org/abs/2601.15703
- Runaway — https://arxiv.org/abs/2505.17616

---

## FULL 10-PAPER ROSTER (the sweep: 17 fetched -> 78 claims -> 25 verified -> 10 relevant)

Sorted by how directly they detect the error BEFORE the final failure.

GENUINELY EARLY-WARNING / PRE-FAILURE (3 — the ones that matter):
  1. SafetyDrift                       2603.27148  Mar 2026   forecast + lead-time (MAIN THREAT)
       https://arxiv.org/abs/2603.27148
  2. InferAct (Preemptive Detection)   2407.11843  Jul 2024   preemptive, next-action only
                                                   (EMNLP'25)
       https://arxiv.org/abs/2407.11843
  3. Agentic Overconfidence            2602.06948  Feb 2026   asks mid-run; NEGATIVE result
       https://arxiv.org/abs/2602.06948

LIVE PER-STEP MONITORING, BUT REACTIVE (not forecasting) (3):
  4. UProp (Uncertainty Propagation)   2506.17419  Jun 2025
       https://arxiv.org/abs/2506.17419
  5. AUQ (Agentic Uncertainty Quant.)  2601.15703  Jan 2026
       https://arxiv.org/abs/2601.15703
  6. Runaway is Ashamed, But Helpful   2505.17616  May 2025
       https://arxiv.org/abs/2505.17616

POST-HOC / DIAGNOSTIC — adjacent, NOT early warning (4):
  7. The Intervention Paradox          2602.03338  Feb 2026   (relevant to recovery curve)
       https://arxiv.org/abs/2602.03338
  8. HTC (Agentic Conf. Calibration)   2601.15778  Jan 2026   white-box
       https://arxiv.org/abs/2601.15778
  9. HORIZON / Long-Horizon Mirage     2604.11978  2026       *** ALREADY MINE = Paper B ***
       https://arxiv.org/abs/2604.11978
 10. Entropy-trajectory-shape          2603.18940  Mar 2026   single-instance CoT, not agents
       https://arxiv.org/abs/2603.18940

NEW vs KNOWN: 9 are genuinely NEW finds; #9 HORIZON is NOT new — it is my existing anchor
  Paper B, which the search re-surfaced on its own (good sign the sweep was on-target).
  8 of the 9 new ones are 2025-2026; only InferAct (Jul 2024) is older but still relevant.

⚠️ VERIFY-BEFORE-CITE: the 2026 arXiv IDs (2601-2604 range) were confirmed by verifier
  agents but are very fresh -> open each arXiv page and eyeball title+abstract before
  citing in writing, to be 100% sure the ID and claim line up. Priority to verify by hand:
  SafetyDrift (2603.27148), Agentic Overconfidence (2602.06948), Intervention Paradox
  (2602.03338).

OTHER 7 FETCHED BUT DROPPED (verification/budget — added nothing to early-alarm picture):
  2603.13325 (https://arxiv.org/abs/2603.13325) · 2603.20260 (https://arxiv.org/abs/2603.20260) ·
  2606.01365 (https://arxiv.org/abs/2606.01365) ·
  2605.09863 (Nautilus Compass = my Paper D, https://arxiv.org/abs/2605.09863) ·
  2606.00765 (https://arxiv.org/abs/2606.00765) · 2605.06788 (https://arxiv.org/abs/2605.06788) ·
  2602.11409 (https://arxiv.org/abs/2602.11409)
