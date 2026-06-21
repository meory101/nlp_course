# 🧰 CROSS-PAPER TABLE — what I USE from each paper
### (the owed table — done 2026-06-07, day before the presentation)

## The one-glance table

| Paper | Role | Dataset/code downloadable? | What I actually USE |
|---|---|---|---|
| **A** Illusion of Diminishing Returns (ICLR 2026, 2509.09677) | 🧪 **The LAB** | ✅ HF dataset `arvindh75/Long-Horizon-Execution` + task recipe | The environment + **free answer key** (auto-labeled failure step at every length); the scrub experiment; ⚠️ use **non-thinking** models (thinking models are immune to self-conditioning) |
| **B** HORIZON / Task Mirage (2604.11978) | 📖 **The VOCABULARY** | ❌ Leaderboard site only — no usable data | Official names ("History Error Accumulation" = my drift); judge **protocol** (pilot → κ-validate → mass-label); depth/breadth defense trick; pitch quotes (cliff moves, never disappears; recoverable→irreversible — observed, NOT proved) |
| **D** Nautilus Compass (2605.09863) | 🥊 **COMPETITOR #1** (detects NOW, not BEFORE) | ✅ Full code + labeled drift traces (MIT, GitHub) | Anchor-similarity **detector skeleton** (embed + cosine vs goal anchor); labeled traces = validation set + **0.83 AUROC baseline to beat** |
| **E** DiverseAgentEntropy (EMNLP 2025, 2412.09572) | 🥊 **COMPETITOR #2** (single questions, no steps) | ✅ Code (Apache 2.0); their QA datasets = skip (wrong shape) | **Ask-twice probe**: rephrase "next action?" 2–3 ways, log disagreement; harvest variant-generation prompt + entropy-scoring code; caveat: "consistency detects UNCERTAINTY, not FALSEHOOD" |
| **I** Decomposing Self-Correction (2601.00828) | 📋 **The METRICS** for Repair | ✅ Code on GitHub; GSM8K-Complex = filtered GSM8K (rebuildable) | 3-way readout (**detect / localize / correct** logged separately); error-depth axis (shallow vs deep); detection–correction gap; ⚠️ wrong pointer HURTS |
| **K** Find vs Fix (ACL 2024, 2311.08516) | 🔧 **The REPAIR mechanism** + gold data | ✅ **BIG-Bench Mistake** (Apache 2.0): 2,186 traces, gold first-error-step labels + prompts (⚠️ their trained detector NOT released) | **Backtracking** recipe (rollback → regenerate-different); random-step control + over-correction guard; **60–70% detector-good-enough threshold**; offline validation bed for my probes |

## Data inventory in one breath
- **Develop on:** A (unlimited synthetic runs, free clean labels)
- **Validate on:** K's BIG-Bench Mistake (gold human labels) + D's real Claude traces (0.83 baseline)
- **No data from:** B (vocabulary only), E/I (wrong task shape — copy code/metrics, not datasets)

## How each feeds the three RQs

| | #16 Measure | #18 Detect | #4 Repair |
|---|---|---|---|
| **A** | the drift curve itself | scrub probe idea | scrub-as-repair idea |
| **B** | cliff finding to connect to | "window exists" quotes | taxonomy = target list |
| **D** | — | detector skeleton + baseline | — |
| **E** | — | ask-twice probe + code | peer-disagreement fixes 18–27% w/o oracle |
| **I** | error-depth axis | "detection ≠ fixing" sharpener | 3-way metrics + paradox |
| **K** | labeled steps complement A | 60–70% target bar | backtracking + controls |

## Professor-proof sentence
> "A is my lab, K is my gold-labeled validation set, D is the baseline to beat,
> E gives me a second probe, I gives me the repair metrics, and B gives me the
> field's vocabulary. Every paper contributes a part; none of them ran the
> pipeline: **alarm → rollback → recovery vs lead time.**"
