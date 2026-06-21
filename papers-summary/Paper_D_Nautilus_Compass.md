# 📄 Paper D — Nautilus Compass
### *Black-box Persona Drift Detection for Production LLM Agents*

| | |
|---|---|
| **arXiv** | 2605.09863 (2026) |
| **My thread** | **#18 — DETECT the drift** (black-box, before failure) |
| **Role in my project** | Method skeleton for my detector + a usable labeled dataset |
| **API-only?** | ✅ Yes (works on closed APIs — Claude, GPT-4) |
| **Code/data** | ✅ ALL released (MIT): https://github.com/chunxiaoxx/nautilus-compass |
| **Read status** | ✅ Understood via summary |

---

## 🎯 THE ONE-LINE POINT
> You can catch an agent **drifting** using **only its text outputs** (no model
> internals). Compare what the agent is saying NOW against a fixed "intended-behavior"
> anchor; when they stop matching → **drift alarm**. AUROC 0.83 on real Claude traces.

---

## ⭐ MY GRAB
> **Detect drift black-box: embed the agent's current output, compare (cosine
> similarity) to a fixed intended-behavior anchor. Score drops → drift alarm.**

---

## 🛠️ THE MECHANISM (what I copy)
| Step | What they do | Plain meaning |
|---|---|---|
| 1 | Write **anchor texts** | Short descriptions of how the agent *should* behave (rules/persona/goal). |
| 2 | **Embed** anchors + current output (BGE-m3) | Turn text into number-vectors that capture *meaning*. |
| 3 | **Cosine similarity** | A 0→1 score of how close-in-meaning output is to the anchor. |
| 4 | **Weighted top-k mean** | Combine best-matching anchor scores into one "on-track" number. |
| 5 | Score **drops** → **alarm** | Behavior stopped matching intent → flag drift. |

> 💡 "embedding + cosine similarity" = turn both texts into number-vectors, measure
> the angle. Small angle = same meaning = on task. Big angle = drifted.

---

## ⚖️ WHAT IT CATCHES vs MISSES (important honesty)
| Drift type | Example (Flutter "login cubit" task) | Caught? |
|---|---|---|
| **Topic / goal drift** | starts editing theme / API client instead of login cubit | ✅ YES (its strength) |
| **Constraint drift** | I said "use cubit", later switches to Bloc | ✅ YES |
| **Subtle correctness drift** | cubit looks on-topic but has a logic bug | ❌ NO (meaning still matches) |

➡️ Cosine similarity measures **meaning-closeness, NOT correctness.** Good for
"agent wandered off", weak for "on-topic but wrong" → I may need a **2nd alarm**
(Paper E — DiverseAgentEntropy, consistency-as-uncertainty).

---

## 📦 DATASET — what it is & how they used it
Nautilus is **2 tools in one** (a drift detector **and** a memory layer), so it has
two kinds of benchmark:

| Dataset | Tests which job | Score | Useful to me? |
|---|---|---|---|
| **Own drift test set** ⭐ — real Claude Code traces, labeled drift/no-drift by an LLM judge | **Drift detection** (output level) | **AUROC 0.83** | ✅ **THE one** — ready-made labeled drift benchmark + a baseline to beat |
| LongMemEval-S (public, ICLR'25) | **Memory recall** (not drift) | 56.6% | ⚠️ memory, mostly ignore |
| EverMemBench-Dynamic (public) | **Memory recall** | 44.4% | ⚠️ memory, ignore |

⚠️ **Label caveat:** drift labels come from an **LLM judge** (another model's
opinion) = slightly noisy. Paper A's labels are deterministic/clean → so:
**develop on A-style clean labels, then VALIDATE on D's real traces + cite 0.83.**

---

## 🕳️ THE GAP = MY IDEA #18 (the key insight)
**There is NO standard public benchmark OR metric for drift/failure detection.**
Nautilus had to invent its own. And more importantly:

> Nautilus detects drift **while it's ALREADY happening** (smoke detector beeping when
> the room is full of smoke). My #18 is the **sharper, harder** version: detect failure
> **BEFORE it happens** (beep at the first wisp) — measured by **LEAD TIME**.

| | Nautilus (detect NOW) | My #18 (detect BEFORE) ⭐ |
|---|---|---|
| Question | "Is it drifting already?" | "**Will** it fail soon, while it still looks fine?" |
| Timing | damage in progress | **early warning** |
| Metric | drift/no-drift (AUROC 0.83) | **lead time** + AUROC vs the TRUE failure step |
| Standard exists? | own dataset only | ❌ **No → my opportunity** |

**Why my order works:**
```
Paper A → gives the TRUE failure step (answer key)   ✅ free, clean, deterministic
Paper D → gives the black-box drift SIGNAL (alarm)   ✅ method to copy
MY #18  → fire alarm, then measure:
            lead time = (true failure step) − (first alarm step)
            AUROC: can it separate doomed vs healthy runs EARLY?   ⭐ the contribution
```
Proposing a clean, reproducible **early-warning benchmark + lead-time metric** is a
real contribution, because nobody has standardized it.

---

## 🧰 COMMON METHODS TO DETECT DRIFT / EARLY FAILURE (check later)
All are black-box (API-only). ⭐ = my candidate NEW idea (not yet published).

| Method | How it works (simple) | Catches | Weakness |
|---|---|---|---|
| **Self-rating** | Ask the agent each step "are you still on track? 0–1" | cheap gut-check | models are **overconfident** → weak alone |
| **Action entropy** (sample-k) | Ask "next action?" k times at temperature → measure disagreement | confused/uncertain steps (on-topic but wrong) | costs k× calls; do every N steps |
| **Goal/anchor similarity** (Nautilus) | Embed output, cosine-compare to fixed goal anchor; score drops = drift | off-topic / broke-the-rules drift | misses subtle on-topic errors |
| **Behavioral smells** | Watch the log: repetition 🔁, hedging words, rising length | stuck loops, early wobble | noisy; heuristic |
| **Self-contradiction** | Check if a step contradicts the agent's OWN earlier (correct) statement | internal inconsistency | needs tracking past claims |
| ⭐ **Scrub probe** (mine) | Run next action WITH vs WITHOUT last step in context; big disagreement = recent step is contaminating → drift incoming | **self-conditioning, EARLY** (the snowball starting) | 2× calls; novel = unproven |
| ⭐ **Time-to-failure gauge** (mine) | Predict *how many steps until failure* (a number), not just yes/no | tells you *when*, not just *if* | regression is harder to train |
| ⭐ **Drift velocity** (mine) | Track the *rate/acceleration* of a drift signal, not its level | fires earlier (momentum, not position) | derivative is noisy |

**How to choose:** start by LOGGING several signals on Paper-A runs, then rewind from
real failures and see which signal rose EARLIEST → that's the empirical winner.
My primary bet = **action entropy** (strong, cited) + ⭐ **scrub probe** (novel, tied
to self-conditioning). Score all by **lead time** vs the true failure step.

---

## 🗣️ SAY-IT-TO-THE-PROFESSOR VERSION
> "Nautilus shows drift IS detectable black-box — embed the output, compare to an
> intended-behavior anchor, AUROC 0.83 on real agent traces, all code/data public.
> But it detects drift *as it happens* and there's no standard early-warning benchmark.
> My #18 sharpens this: detect failure **before** it happens, scored by **lead time**
> against the true failure step — which Paper A gives me for free. Nautilus is my
> method skeleton; the early-warning framing + lead-time metric is the new part."
