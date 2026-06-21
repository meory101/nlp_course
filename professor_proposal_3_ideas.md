# Research Proposal — 3 Ideas on Long-Horizon LLM Agents
Prepared for: professor meeting.  Solo, API-only (no GPU/training), one semester.
Author: M. Khair.  Date: 2026-06-04.

Each idea below is stated as: QUESTION -> MECHANISM (what I build) ->
EVALUATION (how I measure) -> RISK. The three share ONE agent harness,
so building one builds most of all three.

---------------------------------------------------------------------
ONE-LINE FRAMING (say this first)
---------------------------------------------------------------------
"All three ideas are one story about long-horizon agents:
 DETECT -> DIAGNOSE -> REPAIR. They run on a single ReAct agent harness
 that logs every step, so I can answer all three from the same runs.
 I propose we pick one to go deep on; the other two come nearly free."

=====================================================================
 IDEA 1  (MEASURE) — How does agent error grow over long tasks?
=====================================================================
QUESTION:
  As a task gets longer, does the per-step error rate stay constant
  (linear drift) or accelerate (exponential drift)?

MECHANISM (what I build):
  A ReAct agent on a multi-step environment. I give it the plan and
  knowledge up front, so any failure is pure EXECUTION drift, not lack
  of knowledge. I log every step (action, observation, correct y/n).
  Run tasks of increasing length (e.g. 5, 10, 20, 40 steps).

EVALUATION (how I measure):
  - Plot per-step success rate vs step number: straight line = linear,
    upward curve = exponential.
  - Plot P(finish whole task) vs task length.
  - Ablation: keep vs scrub the agent's own past errors from context
    -> tests "self-conditioning" (errors breeding more errors).

RISK: lowest. This produces a real result no matter what -> insurance.
BASIS: Illusion of Diminishing Returns (arXiv 2509.09677).

=====================================================================
 IDEA 2  (DETECT) — Can an agent flag its own drift BEFORE it fails?
=====================================================================
QUESTION:
  Using only API-visible signals (black-box), can the agent raise an
  alarm that it has drifted off-task BEFORE the visible failure?

MECHANISM (what I build):
  On the same harness, add ONE cheap self-signal per step. Options:
   (a) a "still on task? confidence 0-1" self-rating each step, or
   (b) sample the next action k times and measure disagreement
       (action entropy) -> high disagreement = drift alarm.
  No model internals used (API-only by design).

EVALUATION (how I measure):
  Idea 1 already gives me the TRUE failure step of each run. So I score
  the alarm as an early-warning detector:
   - lead time = failure step - first alarm step (want > 0),
   - AUROC: does the alarm separate doomed runs from healthy runs early,
   - precision/recall of "alarm fired before failure."

RISK: medium. Signal might be weak -> but a negative result is still
  publishable ("black-box self-monitoring is/ isn't enough").
BASIS: DiverseAgentEntropy (arXiv 2412.09572); SelfCheckGPT family.

=====================================================================
 IDEA 3  (REPAIR) — Self-correct without feedback, or only with a verifier?
=====================================================================
QUESTION:
  Can the agent fix its own mistakes with NO external feedback
  (intrinsic), or only when a verifier/oracle is present? And does
  "correcting" ever BREAK answers that were already right?

MECHANISM (what I build):
  On the same harness, add a critique -> redo step with a VERIFIER
  TOGGLE:
   - OFF (intrinsic): agent must self-diagnose, no signal shown.
   - ON: show a real signal. For a CODE task this is FREE -
     run_tests()/error message acts as the verifier.
  Compare OFF vs ON at the SAME token budget (fair comparison).

EVALUATION (how I measure):
  - recovery rate = fraction of failing runs fixed,
  - over-correction rate = fraction of CORRECT answers it BREAKS,
  - net = recovered - broken,
  - recovery by error depth (shallow vs deep errors).

RISK: medium. Prior work says intrinsic self-correction often HURTS;
  reproducing/refining that is itself a clean result.
BASIS: LLMs Cannot Self-Correct Yet (2310.01798); Cannot Find Errors
  but Can Correct Given Location (2311.08516); Kamoi survey (2406.01297).

=====================================================================
 WHY THESE THREE TOGETHER (the pitch)
=====================================================================
- ONE harness, three readouts -> efficient for a solo semester.
- Idea 1 hands Ideas 2 & 3 the ground-truth failure step for free.
- Spans the risk spectrum: Idea 1 can't fail; 2 & 3 are higher-interest
  and publishable even as negative/ refutation results.
- Fully API-only: no GPUs, no training, finishable in a semester.

QUESTIONS FOR YOU (professor):
  1. Is a measurement / refutation result publishable in our target venue?
  2. Do we have an API budget, or is it on me?
  3. Which thread do you want me to go deepest on — Detect (2) or Repair (3)?

=====================================================================
 30-MINUTE READING TO DEFEND THIS (only if you have time)
=====================================================================
Read the ABSTRACT + first FIGURE + CONCLUSION of these, 10 min each:
  - Idea 1: 2509.09677  (confirm: failure grows exponentially w/ length)
  - Idea 3: 2311.08516  (confirm: can't FIND the error, CAN fix if given it)
  - Idea 2: 2412.09572  (confirm: disagreement across rephrasings = wrongness)
If a paper comes up and you haven't read it: say "the mechanism I take
from it is X" (from the boxes above). That is the only thing he cares about.
=====================================================================
