# FRESH Reading Cheat-Sheet — 2025/2026 papers only
*(Re-search done 2026-06-03. Newer + deeper than the first cheat-sheet.
Only papers that talk DIRECTLY about your 3 ideas are here — no filler.)*

=====================================================================
 ⭐ START HERE — TODAY'S READING PLAN (read these 3, in THIS order)
=====================================================================
Read one paper per idea, in this order — it tells the STORY of your
project (Problem -> Detect -> Repair) so you can FEEL which thread pulls
you. ~10 min each, ~30-40 min total. Hunt only the GRAB/LOOK FOR line.

  1st →  A. Illusion of Diminishing Returns   (#16 Measure)
         the PROBLEM: errors compound, per-step accuracy falls.
         GRAB: their 4 metrics (Step/Turn/Task Accuracy).

  2nd →  D. Nautilus Compass                  (#18 Detect)
         can we CATCH the drift early, black-box? yes.
         GRAB: the black-box drift signal (output-vs-goal compare).

  3rd →  I. Decomposing Self-Correction       (#4 Repair)
         can it FIX itself? when repair helps vs hurts.
         GRAB: the over-correction finding (strong models flip
         correct -> wrong).

THE ONE DECISION after reading: "Which paper did I NOT want to put down?"
   pulled to A / measuring        -> lean #16 (safest)
   pulled to D / catching early   -> lean #18
   pulled to I / fixing it        -> lean #4
That gut feeling = your thread. Bring it back -> we go deep + build plan.

TOMORROW (second paper of whichever thread you picked):
   picked #16 -> read B (HORIZON = your method blueprint)
   picked #18 -> read E (DiverseAgentEntropy = 2nd alarm signal)
   picked #4  -> read K (Find-vs-Fix = proves detect must precede repair)
=====================================================================


How to read each (~10 min): **Abstract → main figure → Intro contributions →
Limitations → Conclusion → "API-only? yes/no".**
For each paper below: **GRAB** = the ONE thing to take. **LOOK FOR** = the exact
section/number to hunt while reading, then close the paper.

Legend:  ✅ API-only (black-box, you can replicate)   ⚠️ uses model internals
(read for framing/definition only, NOT as your method)   🔑 = verified abstract.

To open a paper: paste the title into Google Scholar, or use the arXiv ID.

---

## THREAD #16 — MEASURE the drift (linear vs exponential error growth)

### A. The Illusion of Diminishing Returns: Measuring Long Horizon Execution in LLMs  ⭐ANCHOR ✅
- arXiv 2509.09677 (2025)
- 🔎 https://scholar.google.com/scholar?q=The+Illusion+of+Diminishing+Returns+Measuring+Long+Horizon+Execution+in+LLMs
- **GRAB:** Per-step accuracy FALLS as the task gets longer ("self-conditioning":
  seeing its own past errors makes it err more) → task length grows but errors
  compound. This IS your #16 thesis.
- **LOOK FOR:** their 4 metrics — **Step Accuracy, Turn Accuracy, Turn Complexity,
  Task Accuracy**. Copy these definitions; you will reuse them exactly.

### B. The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break  🔑 ✅(behavioral)
- arXiv 2604.11978 (2026) — the **HORIZON** benchmark, 3,100+ trajectories,
  GPT-5 + Claude families, 4 domains.
- 🔎 https://scholar.google.com/scholar?q=Long-Horizon+Task+Mirage+Diagnosing+Where+and+Why+Agentic+Systems+Break
- **GRAB:** They treat **horizon (number of steps) as a CONTROLLED VARIABLE** and
  do trajectory-level failure attribution — exactly the experimental shape you need.
- **LOOK FOR:** their **"trajectory-grounded LLM-as-a-Judge" pipeline** (how they
  auto-label each step right/wrong) and the **horizon-dependent degradation curves**.
  This is your blueprint for the #16 "judge" + the plot. (Agreement: κ=0.84 vs humans.)

### C. AgentRx: Diagnosing AI Agent Failures from Execution Trajectories  ✅
- arXiv 2602.02475 (2026)
- 🔎 https://scholar.google.com/scholar?q=AgentRx+Diagnosing+AI+Agent+Failures+from+Execution+Trajectories
- **GRAB:** A method to read a trajectory log and pinpoint the failing step.
- **LOOK FOR:** their **failure categories / step-labeling scheme** — borrow it to
  DEFINE "step" and "error" precisely before you run anything. (Skim; method optional.)

---

## THREAD #18 — DETECT the drift (self-monitoring BEFORE failure, black-box)

### D. Nautilus Compass: Black-box Persona/Task Drift Detection for Production LLM Agents  🔑 ✅
- arXiv 2605.09863 (2026)  ← **best new #18 lead, fully API-only**
- 🔎 https://scholar.google.com/scholar?q=Nautilus+Compass+Black-box+Persona+Drift+Detection+Production+LLM+Agents
- **GRAB:** You CAN detect drift from outputs alone (prompt-response space, no
  weights) using **embedding + consistency** between current output and the
  intended goal/persona. This is a working black-box detector you can imitate.
- **LOOK FOR:** the exact **drift signal** (how they embed and compare) and the
  **detection-before-failure** results. This is your #18 method skeleton.

### E. Rethinking LLM Uncertainty: A Multi-Agent Approach (DiverseAgentEntropy)  ✅
- arXiv 2412.09572 (late 2024/2025)
- 🔎 https://scholar.google.com/scholar?q=Rethinking+LLM+Uncertainty+Multi-Agent+Approach+Estimating+Black-Box+Model+Uncertainty
- **GRAB:** Estimate confidence WITHOUT internals — ask the SAME question many
  ways; if answers are inconsistent → the model is uncertain → likely drifting.
- **LOOK FOR:** the **consistency-as-uncertainty metric**. A cheap, API-only alarm
  signal you can compute every N steps for #18.

### F. Generalized Correctness Models  ✅
- arXiv 2509.24988 (2025)
- 🔎 https://scholar.google.com/scholar?q=Generalized+Correctness+Models+Calibrated+Model-Agnostic+Correctness+Predictors
- **GRAB:** Whether a step is correct can be predicted from **historical patterns**,
  model-agnostically — i.e. self-monitoring is a learnable, transferable skill.
- **LOOK FOR:** what **black-box features** they feed the correctness predictor.
  Those features = candidate inputs for your drift alarm.

### G. Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits (Gnosis)  ⚠️
- arXiv 2512.20578 (2025)
- 🔎 https://scholar.google.com/scholar?q=Can+LLMs+Predict+Their+Own+Failures+Self-Awareness+via+Internal+Circuits
- **GRAB:** Framing only — "can a model see its own failure coming?" Yes, but via
  HIDDEN STATES.
- **LOOK FOR:** just the Intro framing + the Limitations (why black-box is harder).
  ⚠️ Needs internals → use as motivation/contrast, NOT your method.

---

## THREAD #4 — REPAIR the drift (self-correct WITH vs WITHOUT a verifier)

### H. Large Language Models Cannot Self-Correct Reasoning Yet  ⭐ANCHOR ✅
- arXiv 2310.01798 (keep — the foundation claim)
- 🔎 https://scholar.google.com/scholar?q=Large+Language+Models+Cannot+Self-Correct+Reasoning+Yet
- **GRAB:** Intrinsic self-correction (no external feedback) does NOT help, often
  HURTS. Copy their exact setup; it's your "feedback OFF" condition.

### I. Decomposing LLM Self-Correction: Accuracy-Correction Paradox & Error Depth  🔑 ✅
- arXiv 2601.00828 (2026)  ← **best new #4 paper, prompting-based**
- 🔎 https://scholar.google.com/scholar?q=Decomposing+LLM+Self-Correction+Accuracy-Correction+Paradox+Error+Depth+Hypothesis
- **GRAB:** Two gold results: (1) **Accuracy-Correction Paradox** — weaker models
  self-correct MORE; strong models risk **flipping correct→wrong** (over-correction).
  (2) **Error Depth Hypothesis** — self-correction fixes SHALLOW errors but not DEEP
  ones (it can't see flaws it doesn't understand).
- **LOOK FOR:** how they **separate shallow vs deep errors**, and the **over-correction
  rate**. This directly gives you a way to measure your #4 (and idea #5 over-correction).

### J. Confidence vs. Critique: A Decomposition of Self-Correction Capability  ✅
- arXiv 2412.19513 (2025)
- 🔎 https://scholar.google.com/scholar?q=Confidence+v.s.+Critique+Decomposition+of+Self-Correction+Capability+LLMs
- **GRAB:** Self-correction = two skills: knowing it's wrong (confidence) + fixing it
  (critique). Failure is usually in DETECTING, not fixing.
- **LOOK FOR:** their **split metric** (detect-rate vs fix-rate). Use it to report
  WHERE your agent fails in the repair loop.

### K. LLMs Cannot Find Reasoning Errors, but Can Correct Them Given the Error Location  ✅
- arXiv 2311.08516 (2023 — older but PIVOTAL, bridges #18↔#4)
- 🔎 https://scholar.google.com/scholar?q=LLMs+cannot+find+reasoning+errors+but+can+correct+them+given+the+error+location
- **GRAB:** The bottleneck is **FINDING** the error, not fixing it. Tell the model
  WHERE the error is → it fixes well. This is exactly why #18 (detect) must come
  before #4 (repair).
- **LOOK FOR:** the gap between **error-finding accuracy** and **given-location
  correction accuracy**. One table; it justifies your whole Detect→Repair arc.

### L. ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification  ⚠️(training)
- arXiv 2502.14565 (2025)
- 🔎 https://scholar.google.com/scholar?q=ReVISE+Learning+to+Refine+at+Test-Time+via+Intrinsic+Self-Verification
- **GRAB:** A "self-verify then refine" loop that DOES work — but via fine-tuning.
- **LOOK FOR:** only the **loop design** (verify→refine→repeat). ⚠️ Needs training →
  borrow the structure, not the method (you're API-only).

---

## What to read FIRST (don't read all 12)
1. **B (Long-Horizon Mirage)** + **A (anchor)** → your #16 method + the judge/plot.
2. **D (Nautilus Compass)** + **E (DiverseAgentEntropy)** → your #18 black-box alarm.
3. **I (Decomposing Self-Correction)** + **K (Find-vs-Fix)** → your #4 with/without verifier.
That's 6 papers = enough to design all three experiments.

## The one question to answer after reading
> Which thread excites me most — **Measure (#16)**, **Detect (#18)**, or **Repair (#4)**?
The Detect→Repair bridge (paper K) suggests #18 and #4 are two halves of one story.
Bring your pick back and we build the week-by-week experiment plan.

---
### ⚠️ Note on arXiv IDs
Titles are exact (paste into Google Scholar to open). The 2026 arXiv IDs
(26xx.xxxxx) for B, C, I, D were taken from live search; A, H, K, J, E, F, L, G
are well-established. If any numeric ID 404s, search the TITLE — the paper is real.
Verified abstracts (🔑): B, I, D.
