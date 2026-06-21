# 📄 Paper E — DiverseAgentEntropy
### *Rethinking LLM Uncertainty: A Multi-Agent Approach to Estimating Black-Box Model Uncertainty*

| | |
|---|---|
| **arXiv** | 2412.09572 (v2 Oct 2025) — **EMNLP 2025 Findings** (Yu Feng et al., Amazon Science + Dan Roth) |
| **My thread** | **#18 — DETECT** (consistency / ask-twice signal) |
| **Role in my project** | ⭐ THE CITATION for my "ask-twice" probe — proves the consistency-signal class works, black-box. Like Paper D it is a **competitor/feasibility proof**, NOT a tool I run directly. |
| **API-only?** | ✅ 100% — title says "black-box"; needs only prompt→text. No logits, no weights, no training. |
| **Code/data** | ✅ Code Apache 2.0: `github.com/amazon-science/DiverseAgentEntropy` (full pipeline, wired to AWS Bedrock, swappable in `utils.py`). Datasets all public (links below) but their exact sampled subsets NOT included — sample my own. |
| **Read status** | ✅ Understood via web-pull + discussion (2026-06-06) |

---

## 🎯 THE ONE-LINE POINT
> Asking the SAME question 5 times (self-consistency) can fool you — the model can be
> consistently wrong on one phrasing yet right on another. Ask **5 DIFFERENTLY-PHRASED
> versions**, let the answers **argue**, and the leftover disagreement is the real
> uncertainty signal. Scattered ending = the model is guessing → abstain.

---

## ⭐ MY GRAB
> **Consistency-across-rephrasings is a working, black-box, API-only hallucination
> alarm (AUROC up to 0.95 on long-tail facts) — but it has ONLY ever been run on
> single, standalone questions. Never per-step inside a trajectory.** It is the
> pedigree for my ask-twice probe; the per-step transplant + lead time is mine.

---

## 🚪 THE CORE DISCOVERY (why same-question-5× lies)
The model's memory = a room with **5 doors**. The fact is inside, but door #1 (the
original phrasing) can be JAMMED — the wording pulls up a wrong stored answer.
Re-asking the same question = banging the same jammed door 5× → 5× the same wrong
answer → looks confident-and-consistent → self-consistency says "trust it." WRONG.

**Their proof:** among cases where agents eventually converged on the CORRECT answer,
the model's first answer to the ORIGINAL phrasing was wrong **11–33%** of the time
(worst: TruthfulQA ~30%). The knowledge was IN the weights; retrieval failed.
They call the cause **contextual bias**: small wording shifts change which stored
answer gets pulled.

> 🔗 ECHO OF PAPER A: this is *retrieval* failing, not *knowledge* — the
> single-question cousin of "execution fails, not reasoning." Their contextual bias
> = prompt wording contaminating retrieval; Paper A's self-conditioning = your own
> error history contaminating the next step. **Same disease, different context window**
> → my scrub probe and ask-twice probe are provably cousins.

---

## 🧱 THE MECHANISM — 4 steps (Eiffel Tower example, true answer 1889)

### 1️⃣ VARY — make 5 disguises of the question
The model ITSELF auto-generates ~5 variants that all require the same one fact:
paraphrase ("construction finished in?"), perspective flip ("Gustave Eiffel finished
his tower in?"), composition ("how old was it in 2000?" → must know 1889).
Checked quality: ~95% really preserve the knowledge, ~97% genuinely diverse.

### 2️⃣ ANSWER — 5 agents answer ALONE
"Agent" = a separate fresh chat with the SAME model. **Each agent gets ONE variant
only** (never all 5 — one variant's wording would contaminate the others).
E.g.: A1→1887 ❌, A2→1889 ✅, A3→1889 ✅, A4→"111 yrs"=1889 ✅, A5→1887 ❌.

### 3️⃣ ARGUE — one-on-one rounds with the strongest disagreer
Each round, agent Aᵢ is paired with the agent whose answer differs MOST. Aᵢ is shown
the other's question+answer inside its own chat and asked to reconsider — but it only
ever ANSWERS its own question. Seeing the fact through the other door often un-jams
the memory (A1 switches 1887→1889). Stop when: all agree / nobody changes for 2
rounds / max rounds. Ablation: one-on-one beats group chat.
⚠️ NOT majority-bullying: if the model truly lacks the fact, agents keep flip-flopping
and never settle — **the failure to settle IS the signal.**

### 4️⃣ SCORE — stability-weighted spread
Each agent's final answer is weighted by **how steady it was**:
- weight ∝ (total rounds − times it changed its answer + 1), normalized.
- Never changed = full weight (pulled the fact cleanly). Flip-flopped every round =
  tiny weight (was guessing; usually just echoed its last partner).
- Why not plain voting? **Vote % measures agreement; stability measures whether the
  agreement came from knowledge or from herding.** 4 flip-floppers herding onto the
  same answer ≠ 4 knowers.
Then: probability of each distinct answer = sum of its agents' weights; **score =
Shannon entropy of that distribution** (0 = all weight on one answer, big = scattered).
Worked example: weights 0.88/0.12 → entropy ≈ 0.37 → low → answer "1889".
Spread 0.4/0.35/0.25 → entropy ≈ 1.07 → high → **ABSTAIN** ("I don't know").
Abstain rule: entropy above threshold OR top answer = "don't know".

---

## 📊 THE NUMBERS THAT MATTER
**Models: only 2, both old 2024:** Claude-3-Sonnet + Llama-3-70B-Instruct (via API).
Never say just "Claude" (same rule as Paper I). They admit "budget constraint".

**Detection (AUROC, Claude-3-Sonnet):**
| vs best self-consistency baseline | SC | E |
|---|---|---|
| Average | 0.693 | **0.725** |
| PopQA long-tail entities | 0.887 | **0.947** |
| FreshQA (time-sensitive facts) | 0.694 | **0.836** |
| TruthfulQA (misconceptions) | 0.568 | 0.624 ⚠️ worst |

→ Pattern: wins BIG exactly where the model is *guessing* (thin/stale knowledge);
nearly useless where the model is *confidently wrong* (misconceptions).

**Abstention (Claude):** accuracy on answered questions 80.8% → **88.3%** (abstaining
21.6%); "truthfulness" (right or honestly silent) 0.846 → **0.908**.

**Free bonus for #4:** the argument rounds also FIX answers — **18–27% of wrong
answers got corrected** through peer interaction, while only 2.5–8.9% of correct ones
broke. Peer-disagreement = a feedback signal that works WITHOUT an oracle.

**Key ablations:** both halves needed (diverse questions alone < full; arguing alone
< full); ~5 agents enough, more plateaus; one-on-one > group; a stubborn wrong agent
degrades it slightly (weaker model degrades more).

---

## ⚔️ THE BASELINES (what it had to beat)
| Baseline | What it does | Acc (Claude) | Abstain |
|---|---|---|---|
| Greedy | answer once, never abstain | 80.8% | 12.6% |
| Self-Consistency 3/5 vote | same question 5×, answer if ≥3 agree | 82.3% | 12.9% |
| **SeQ** | diverse phrasings, NO argument rounds | 81.5% | 14.9% |
| **E (Agent)** | full machine | **88.3%** | 21.6% |
| E (Agent_L, lenient) | same, abstains less | 85.2% | 14.2% |

**SeQ is the row to remember** — it's E's Step 1 without Step 3 → only 81.5 vs 88.3.
So the ARGUMENT ROUNDS carry a big share of the gain, not just the diverse phrasings.
⚠️ Missing from the line-up: no verbalized-confidence baseline; and the comparison is
**not compute-matched** — E gets ~25 calls, self-consistency gets 5. Nobody checked
equal-budget (my old idea #7 instinct → see GAPS).

---

## ⚠️ HONEST LIMITS (say them before the professor does)
1. **The confident-wrong blind spot (I found this one myself):** if a wrong fact is
   stored SOLIDLY (popular misconception), all 5 doors lead to the same wrong room →
   zero spread → passes as confident success. Proof: TruthfulQA = their worst score
   (0.624, near coin-flip). One-liner: **consistency detects UNCERTAINTY, not
   FALSEHOOD — confidently-wrong is invisible to ANY self-consistency method, by
   construction.** (Nautilus shares this; my scrub probe is PARTIALLY immune — it asks
   "does removing your own history CHANGE you?", which can fire even under confidence.)
2. **Cost:** ~25 API calls per question = 5× self-consistency.
3. **Old, small models** (2024), only 2 of them.
4. **Single-turn factual QA ONLY** — their own words: *"we analyze short-form,
   query-based uncertainty… we recognize the need to explore more complex scenarios
   in future work."* No agents, no steps, no trajectories. ← quotable gap.
5. The convergence theorem rests on strict assumptions the authors call intuition-only.

---

## 🛠️ WHAT I COPY FOR MY BUILD (#18)
- **The cheap per-step transplant:** per step of a long run, rephrase "what's your
  next action?" 2–3 ways (their Step 1), answer fresh (Step 2), **SKIP the argument
  rounds** (too expensive per step), log disagreement rate (Step 4). Disagreement
  rising BEFORE the true failure step = my early alarm = lead time.
- **Harvest their repo:** (a) the variant-generation prompt (the hard-to-get-right
  part — Paper D's lesson: phrasing is everything), (b) the answer-clustering +
  stability-weighting + entropy scoring code, reusable for scoring my probe.
- **Optional half-day sanity check:** their pipeline on ~50 TruthfulQA questions with
  a current cheap model — confirms the signal exists on 2026 models before I build.
- **Their datasets = SKIP for the main project** (single-turn = no step 2 = no lead
  time to measure). Links if ever needed:
  PopQA `huggingface.co/datasets/akariasai/PopQA` · FalseQA `github.com/thunlp/FalseQA`
  · TruthfulQA `huggingface.co/datasets/truthful_qa` · FreshQA
  `github.com/freshllms/freshqa` (gold answers age — updated weekly).

---

## 🔗 HOW IT FITS MY ARC
| Thread | What Paper E gives it |
|---|---|
| **#16 Measure** | Nothing direct (wrong task shape). |
| **#18 Detect** | THE cited consistency mechanism + proof the signal class works black-box (0.725–0.947 AUROC) + the quotable "single-turn only" hole = my opening. |
| **#4 Repair** | Free evidence: peer-disagreement corrected 18–27% of wrong answers with NO oracle → a non-oracle feedback channel to test. |

**Updated role-casting:** A = laboratory · D = competitor (real-time, no forecast) ·
E = competitor (single-turn, no trajectory) · I = customer. The empty seat between
D and E = **per-step early warning with measured lead time = me.**

---

## 🗣️ SAY-IT-TO-THE-PROFESSOR VERSION
> "EMNLP 2025 paper from Amazon: self-consistency is a misleading uncertainty signal
> because models can be consistently wrong on one phrasing yet right on another —
> retrieval failure, not knowledge failure. Their fix: ask 5 knowledge-preserving
> rephrasings to 5 independent copies, let them argue pairwise, weight final answers
> by stability, and use the entropy of that weighted vote as the hallucination alarm —
> fully black-box, AUROC up to 0.95 on long-tail facts, and abstention lifts answered
> accuracy from 81% to 88%. Two limits matter for me: it's blind to confidently-stored
> wrong facts (their own worst score is the misconception benchmark), and it has only
> ever been run on standalone single-turn questions — never per-step inside a long
> agent trajectory. My #18 transplants exactly this signal into a running long-horizon
> agent and measures how EARLY it fires before the true failure step — lead time."
