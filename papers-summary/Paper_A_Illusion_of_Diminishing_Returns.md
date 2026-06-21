# 📄 Paper A — The Illusion of Diminishing Returns
### *Measuring Long-Horizon Execution in LLMs*

| | |
|---|---|
| **arXiv** | 2509.09677 (2025) |
| **My thread** | **#16 — MEASURE the drift** (linear vs exponential) |
| **Role in my project** | ⭐ ANCHOR / "insurance" paper — the foundation that can't fail |
| **API-only?** | ✅ Yes (black-box, I can replicate) |
| **Read status** | ✅ Understood via summary — do NOT need full re-read |

---

## 🎯 THE ONE-LINE POINT
> People think LLMs are plateauing (small yearly gains). That's an **illusion**.
> Small gains in **single-step accuracy** turn into **huge (exponential) gains in
> how LONG a task the model can finish**. But on long tasks the model still drifts —
> partly because it **sees and copies its own past mistakes**.

---

## ⭐ MY GRAB (the one thing to take)
> **Per-step accuracy DECLINES over a long task, and the model's own past mistakes
> accelerate the decline (self-conditioning). Small per-step gains → exponential
> task-length gains.**

That sentence **IS my #16 thesis.** Nothing else from this paper is needed to defend idea #16.

---

  ## 🤔 THE PROBLEM THEY STARTED FROM
  Two complaints about LLMs that seem to contradict each other:
  1. *"New models are barely better — scaling is dying (diminishing returns)."*
  2. *"Yet LLMs still fail at simple but LONG tasks a human could do with time."*

  Both feel true but don't fit together. The paper shows **both are misreadings of the
  same thing** — caused by measuring the wrong number.

---

## 🏆 THE 3 THINGS THEY WANTED TO ACHIEVE

### 1️⃣ Kill the "diminishing returns" story
- **Claim:** a *tiny* rise in single-step accuracy → an **exponential** rise in the
  task length the model can finish. Gains only *look* small because people use the
  wrong ruler (short benchmarks).
- **Simple math (steps chain, one wrong step breaks the task):**

  | Per-step accuracy | Finish 10 steps | Finish 100 steps |
  |---|---|---|
  | 90% | 0.9¹⁰ ≈ **35%** | ~0% |
  | 99% | 0.99¹⁰ ≈ **90%** | 0.99¹⁰⁰ ≈ **37%** |

  → 90% → 99% looks like "+9%", but task length jumps **~10× (10 → 100 steps)**.
- **Takeaway:** the gain isn't *diminishing*, it's **hiding**. Wrong ruler =
  single-step accuracy. Right ruler = **task length you can finish**.

### 2️⃣ Locate the REAL failure: execution, not reasoning
- Two very different reasons a long task fails:
  - **Reasoning failure** = didn't *know* the plan / lacked knowledge.
  - **Execution failure** = *knew* exactly what to do, but **slipped** during the
    long sequence of steps.
- **The isolation trick (← I copy this):** they **gave the model the full plan +
  knowledge upfront**, so there's nothing left to "think" about. The model still
  broke down on long tasks → therefore the failure is **pure execution drift**,
  NOT reasoning.
- **Takeaway:** LLMs don't fail long tasks because they're not smart enough — they
  fail because they can't **execute** a long chain without slipping.

### 3️⃣ Explain WHY execution rots: self-conditioning ⭐
- **Finding:** once the model's **own earlier errors** are sitting in its context,
  it becomes **more likely** to make NEW errors. It **copies its own bad behavior.**
- **Not just "long-context fatigue":** it's specifically the *presence of its own
  mistakes* that speeds the breakdown.
- **Drift is a snowball / vicious cycle:**

  ```
  1 small mistake → sits in context → next mistake more likely
       → 2 mistakes in context → even more likely → snowball → task collapses
  ```
- **How they proved it:** feed a history WITH its own errors vs a CLEAN history,
  watch per-step accuracy. With errors → drops faster. Scrubbed → holds up. The gap
  = self-conditioning.
- **Bonus:** "thinking" (test-time reasoning) partly **resists** it → lets the model
  go longer in one turn.

---

## 🤖 MODELS THEY USED (verified from the paper, 2026-06-08)
**Non-thinking / standard (← what I use — self-conditioning lives here):**
- Open: **Qwen3** (4B, 8B, 14B, 32B, 235B-Instruct) · **Gemma3** (4B, 12B, 27B) ·
  **DeepSeek-V3** (~670B) · **Kimi K2** (~1T)
- Frontier (non-thinking mode): **Claude-4 Sonnet** · **Gemini 2.5 Pro** · **Grok 4**

**Thinking / reasoning (immune to self-conditioning — DON'T use for drift):**
- **GPT-5** (codename "Horizon") · **DeepSeek-R1** · **Qwen3 (thinking on)**

**Self-conditioning experiment:** run mainly on non-thinking Qwen3 + Gemma3
(plus Kimi-K2, DeepSeek-V3). A larger non-thinking model managed **~15 steps before
accuracy fell below 50%** at the simplest setting — and that number **dropped sharply
when errors were INJECTED into the history.** That clean-vs-injected gap = self-
conditioning, measured. ➡️ I can develop on tiny cheap models (Qwen3-4B / Gemma3-4B),
then one confirmation run on Claude-4-Sonnet or Gemini-2.5-Pro (both non-thinking).

## 🛠️ WHAT I COPY FOR MY BUILD
- **Mechanism:** give my ReAct agent the **plan + knowledge**, log every step, run
  tasks of increasing length (**5 / 10 / 20 / 40 steps**).
- **The plot:** per-step success **vs** step-number.
  - straight line = **linear** drift
  - curve bending up = **exponential** drift (self-conditioning)
  - also plot **P(finish whole task) vs task length**.
- **Free, can't-fail experiment:** run twice — errors **KEPT** in context vs
  **SCRUBBED** out. If scrubbed does better → I reproduced self-conditioning myself.

---

## 🧪 SCRUB-PROBE — what's NEW vs what A already did (clarified 2026-06-08)
A's injection experiment ALREADY shows the *effect*: add errors to history → accuracy
drops; clean (0%) history drifts least. So "does a cleaner context reduce self-
conditioning?" = **already answered yes** (with KNOWN, planted errors). Do NOT pitch
that — professor will say "A showed it."
**The NEW part = using scrub as a REPAIR tool on UNLABELED runs (A never intervened):**
- **Scrub as REPAIR (RQ3/RQ4):** on alarm, ERASE the poisoned step from context +
  regenerate — vs the naive repair of leaving it in and appending a correction (which
  keeps poisoning, per A's own finding). = the injection experiment run BACKWARDS.
- ⚠️ **Scrub is NOT a detector** (corrected 2026-06-08): removing a step only shows it
  was INFLUENTIAL, not WRONG — removing a GOOD step also changes the output, so you'd
  need a quality signal to interpret it = circular. Detection comes from D (anchor
  similarity) / E (ask-twice), not scrub. Scrub's home is REPAIR.

## 🔗 WHY THIS FEEDS ALL 3 OF MY THREADS
| Thread | What this paper gives it |
|---|---|
| **#16 Measure** | Self-conditioning is *why* drift may be **exponential**, not linear = my curve question. |
| **#18 Detect** | If errors snowball, catching the **first** one early = huge payoff → motivates the early-warning detector. |
| **#4 Repair** | Suggests a repair: **scrub the bad step out of context** (backtrack), not just add a correction on top. |

---

## 📦 DATA / BENCHMARK — what I can actually use
> ✅ CORRECTED 2026-06-08: they DO release everything. Repo:
> **github.com/long-horizon-execution/measuring-execution** — contains (a) task
> generator `generate_dataset_json.py`, (b) the **fake/injected-history code** for the
> self-conditioning counterfactual ("inject output histories with a chosen error
> rate" — 0/10/25/50%), AND a 100-sample starter set on HF
> (arvindh75/Long-Horizon-Execution). I do NOT have to reverse-engineer the
> fake-history procedure — it's published. "Contamination-free: new examples generated
> programmatically." (Earlier note below said "recipe only / no dataset" — that was WRONG.)

**Older (superseded) note: Paper A gives a RECIPE that produces labels for FREE.**

- Their tasks are **synthetic + deterministic** → they *built* the task, so the
  **correct answer at every step is already known by a simple program.**
- To label a step right/wrong, just compare:
  `model's step output  vs  the known-correct output` → match ✅ / differ ❌ (= the failure step).
- **No human labeling, no download.** I can generate **unlimited** runs at any
  length (5/10/20/40 steps), every step **auto-labeled**, perfectly clean.

| What I want | Where to get it |
|---|---|
| Auto-generated clean labels from tasks I control | **Paper A's method** (I build it; labels are free) |
| A ready-made, already-labeled dataset to download | **Paper K — BIG-Bench Mistake** (traces with the first wrong step labeled) |

➡️ **Recommended:** build A-style auto-labeled tasks (clean, unlimited) for development;
optionally validate on **BIG-Bench Mistake** (K) to show it works on a published set.

> ⚠️ Paper A gives the **answer key** (true failure step), NOT a detector and NOT a
> detection benchmark. The detector + its benchmark come from my #18 papers (D / E / K).

---

## ⚠️ THE ONLY REASON TO OPEN THE PDF
- **The main figure** (the drift curve) — 30 sec, just to *see* the shape, so I'm
  fluent if the professor asks "what does the result look like?"
- **The 4 metrics definitions** (Step / Turn / Task accuracy + complexity) — only if
  the professor asks "how exactly did you define a 'step'?" I'd reuse them exactly.
- Everything else (math, related work, appendix, hyperparameters) → **skip**.

---

## 🗣️ SAY-IT-TO-THE-PROFESSOR VERSION
> "This paper shows long-horizon performance — not single-step accuracy — is the
> right thing to measure: tiny per-step gains compound exponentially into task
> length. It proves the bottleneck is **execution**, not reasoning, by handing the
> model the plan and watching it still drift. And it finds **self-conditioning** —
> the model copies its own past errors, so drift snowballs. My #16 builds directly
> on this by measuring the **shape** of that drift, which then sets up Detect (#18)
> and Repair (#4)."
