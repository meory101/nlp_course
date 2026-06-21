# 📄 Paper I — Decomposing LLM Self-Correction
### *The Accuracy-Correction Paradox and the Error Depth Hypothesis*

| | |
|---|---|
| **arXiv** | 2601.00828 (Dec 2025, Yin Li — Univ. of Birmingham) |
| **My thread** | **#4 — REPAIR** (self-correct without external feedback?) |
| **Role in my project** | ⭐ ANCHOR for Repair — gives the *decomposition* + the metrics + the paradox |
| **API-only?** | ✅ Yes (black-box: GPT-3.5, DeepSeek, Claude via API) |
| **Code/data** | ✅ Code released (GitHub linked in paper); GSM8K-Complex is a filtered GSM8K subset |
| **Read status** | ✅ Understood via summary + discussion |

---

## 🎯 THE ONE-LINE POINT
> "Self-correction" is not ONE skill — it's **three** (detect → localize → correct).
> Split them apart and a paradox appears: **weaker models fix themselves MORE than
> stronger ones**, because strong models make **fewer but DEEPER** errors that
> resist fixing. And **detecting ≠ correcting** (Claude detects 10% but corrects 29%).

---

## ⭐ MY GRAB
> **Stop measuring "self-correction" as a single number. Decompose it into
> detect / localize / correct and measure each separately — they're independent.**
> Bonus: higher base accuracy → LOWER correction rate (the paradox), explained by
> error DEPTH (calculation = shallow/fixable, logic+setup = deep/unfixable).

---

## 🧱 HOW THEY GOT THE DATA (the setup)
- **GSM8K-Complex** = GSM8K filtered to HARD problems only: question > 100 chars,
  ≥ 4 computation steps, ≥ 3 distinct operations. 500 problems per model.
- Each model solves each problem ONCE. Every time `model answer ≠ gold answer` = a
  logged **error**. These errors are the "patients" the 3 skills are tested on.
- **346 total errors:** DeepSeek 30 (94% acc), GPT-3.5 168 (66% acc), Claude 148 (70% acc).
- Setting = **INTRINSIC** (no oracle, no ground-truth told to the model) = realistic,
  deploy-time, ✅ API-only.

---

## 🔬 THE THREE SKILLS — mechanism + measure + result

### 1️⃣ DETECT — "is something wrong at all?" (the yes/no alarm)
| | |
|---|---|
| **Mechanism (prompt)** | *"Look at this solution. Is it correct?"* → model returns VERDICT (correct/incorrect) + confidence + explanation. One pass, no hint. |
| **Measure** | **Detection rate = (errors flagged "incorrect") ÷ (total errors)** |
| **Result** | GPT-3.5 **81.5%**, DeepSeek 56.7%, Claude **10.1%** |
| **Conclusion** | Detection varies WILDLY across models (10%→82%). |

### 2️⃣ LOCALIZE — "WHICH step is wrong?"
| | |
|---|---|
| **Mechanism (prompt)** | *"Identify the step k where the first error occurs."* One pass, model's own guess (no answer key). |
| **Measure** | No clean accuracy %. Tested INDIRECTLY: feed the model's own location back as a HINT to correction → did it help or hurt? |
| **Result** | Hint HURT 2 of 3 models: GPT-3.5 26.8%→15.5%, Claude 29.1%→12.8%; only DeepSeek improved 16.7%→26.7%. |
| **Conclusion** | Self-localization is POOR — pointing at a step "anchors" the model to a wrong path and damages the fix. ⚠️ **clashes with Paper K** (which said location helps). |

### 3️⃣ CORRECT — "now actually FIX it" (3 conditions)
| Condition | Mechanism (prompt) | Result |
|---|---|---|
| **A. Intrinsic** | *"Verify your previous solution and correct any errors."* One pass, no hint. | GPT-3.5 **26.8%**, DeepSeek **16.7%**, Claude 29.1% |
| **B. With hint** | Same + the model's own localized step | GPT-3.5 15.5%, DeepSeek 26.7%, Claude 12.8% |
| **C. Iterative** | Repeat verify→re-solve **up to 3 rounds**, no external feedback; success = ANY round hits gold | GPT-3.5 **67.9%**, DeepSeek 20.0%, Claude **60.8%** |

| | |
|---|---|
| **Measure** | **Correction rate = (errors fixed to gold) ÷ (total errors)**; a fix counts only if `A' = A*` (exact gold). Iterative = best rate across ≤3 rounds. |
| **Conclusion** | (a) **PARADOX**: weak GPT-3.5 (26.8%) > strong DeepSeek (16.7%). (b) **Iterative rescues weak detection**: Claude detects 10% but corrects 61% over 3 rounds → just *re-trying* beats consciously *finding* the bug. |

---

## 🕳️ THE EXPLANATION — Error Depth Hypothesis
| | |
|---|---|
| **Mechanism** | Each model classifies its OWN error type: CALCULATION (arithmetic = *shallow*), LOGIC (bad reasoning = *deep*), SETUP (misread problem = *deep*). |
| **Measure** | Distribution of error types per model + correction rate within each type. (No single "depth" number — inferred from the mix.) |
| **Result** | GPT-3.5: **62% calculation** (shallow). DeepSeek: **77% setup+logic** (deep). Shallow fixes >> deep fixes. |
| **Conclusion** | Strong models fail LESS, but when they do it's deep/structural → unfixable by self-correction → that's WHY accuracy ↑ goes with correction ↓. |

---

## ⚖️ THE TENSION WITH PAPER K (use this in the pitch)
- **Paper K** (2311.08516): "bottleneck is FINDING the error — give the location and it fixes fine."
- **Paper I**: giving the location **HURTS**, and detection does **NOT** predict correction.
- → The "just tell it where the bug is" fix is **not universal**. This is a live, unsettled
  question my project can speak to directly. Good — a real opening, not a settled fact.

---

## 🛠️ WHAT I COPY FOR MY BUILD (the #4 Repair readout)
- Don't log ONE "did it recover?" bit. Log **THREE**: detected? localized? corrected? —
  their decomposition, applied to MY mid-task agent.
- Keep the **verifier toggle** (feedback ON vs OFF), AND add an **error-depth axis**:
  label each error shallow (calculation-like) vs deep (logic/setup-like) and report
  recovery **by depth** → directly tests their hypothesis on my agent.
- New metric: **detection–correction gap** (does my agent fix things it never flagged?
  does flagging / locating help or hurt — replicate the hint effect).
- Add the **iterative knob**: 1 pass vs ≤N reflection rounds at EQUAL token budget
  (ties back to 2310.01798's fairness point — gains must survive equal-budget).

---

## 🔗 HOW IT CLOSES MY ARC (Detect → Diagnose → Repair)
| Thread | What Paper I gives it |
|---|---|
| **#16 Measure** | "Deep vs shallow error" = another axis of drift to measure. |
| **#18 Detect** | Detection ≠ fixing → early detection (my lead-time idea) only pays off if the error is shallow enough to fix → sharpens the claim. |
| **#4 Repair** | The decomposition + paradox + error-depth = my Repair mechanism AND metrics, ready-made. |

---

## ⚠️ THE GAP / WHAT'S MISSING (my contribution angle)
- This is **single-shot MATH QA** (GSM8K), one-and-done correction. **My agent is
  LONG-HORIZON** and repairs **mid-task**, in context, where self-conditioning
  (Paper A) is also acting. Nobody has measured the detect/localize/correct
  decomposition + error depth **inside a running long-horizon agent.** ← my opening.
- Error depth has **no formal metric** yet (inferred from type mix) → I could propose
  a cleaner shallow/deep operationalization for agent steps.

---

## 🗣️ SAY-IT-TO-THE-PROFESSOR VERSION
> "This paper breaks 'self-correction' into three measurable skills — detect, localize,
> correct — and shows they're independent: a model can detect 10% of its errors yet
> correct 29%. It finds an Accuracy-Correction Paradox (weaker GPT-3.5 self-corrects
> 1.6× more than stronger DeepSeek) and explains it with error DEPTH — strong models
> make fewer but deeper (logic/setup) errors that resist fixing. It even finds that
> giving the model its error location HURTS, contradicting earlier work. My #4 takes
> this decomposition into a LONG-HORIZON agent doing mid-task repair, scored by
> recovery vs over-correction at equal budget, split by error depth."
