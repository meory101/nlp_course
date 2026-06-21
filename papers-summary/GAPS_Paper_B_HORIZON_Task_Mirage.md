# 🕳️ GAPS extracted from Paper B — HORIZON / Long-Horizon Task Mirage
### (arXiv 2604.11978, Apr 2026 — see `Paper_B_HORIZON_Task_Mirage.md` for the full summary)

> ⚠️ RULE: a gap list is AMMUNITION, not a to-do list. Tags: 🎯 CORE · 🆓 FREE-RIDER
> · 🅿️ PARKED.

---

## From the judge — autopsy, never alarm
*(the judge reads trajectories AFTER death. Their own observation — killer errors
"arise early … convert RECOVERABLE local mistakes into IRREVERSIBLE failures" —
describes an intervention window. They measured that the window exists (as an
observation, NOT an intervention proof — my catch) and never measured the window.)*

- **GAP 1** 🎯⭐ Same empty seat, 4th paper circling it: nothing detects DURING the
  run, no alarm timing, no lead time. Full pattern now: D = real-time-not-forecast,
  E = no steps, K = post-mortem oracle, **B = post-mortem judge + observed-but-
  unmeasured recovery window.** Pitch line: "B observed the window, K proved repair
  in hindsight — nobody tested repair triggered by an early alarm in real time."
- **GAP 2** 🎯 They label WHY, never WHEN. Cause-of-death per trajectory, but NO
  onset step number (K has gold step labels; B doesn't) → their 3,100 trajectories
  can't yield lead time. Measuring the ONSET of drift in real environments =
  unclaimed.

## From the cliff — two rulers never connected
*(Paper A: per-step error rises SMOOTHLY (self-conditioning). Paper B: task success
collapses ABRUPTLY (cliff). Both plausible — a smooth per-step decay multiplies
into a sharp all-steps-must-succeed collapse — but nobody showed the smooth hidden
signal and the abrupt visible cliff on the SAME runs.)*

- **GAP 3** 🆓⭐ THE #16→#18 BRIDGE: show drift signals rising smoothly BEFORE the
  success cliff on my Dictionary-Sum runs → simultaneously (a) reconciles A's curve
  with B's cliff, (b) EXPLAINS B's headline finding, (c) proves early warning is
  possible (the signal moves before the cliff does). One plot, three claims.

## From depth/breadth — the separation leaks
*(breadth kills the LOGICAL snowball (data poisoning) but not the IMITATION
snowball — self-conditioning reads the transcript in both shapes (Paper A). They
never control for behavior-poisoning.)*

- **GAP 4** 🆓 Run a scrub-style control on breadth tasks: does removing past
  sloppy output change later jobs even with zero logical dependency? = measuring
  behavior-poisoning where data-poisoning is impossible. Uniquely my probe's home
  turf.

## From the ground truth — shaky foundations
- **GAP 5** 🅿️ Taxonomy from a 40-trajectory pilot; humans agree only κ=0.61;
  judge model unnamed; multi-label fuzzy. Defense ammo when told "just use
  HORIZON's judge" — and justification for Dictionary-Sum's FREE exact labels.

## From the missing treatment arm
- **GAP 6** 🅿️ 7 diseases named, zero cures tested. No rollback (K), no
  re-grounding (my old #17 — aimed straight at Catastrophic Forgetting), no
  checkpointing (#21). Each disease × each cure = an open intervention matrix.
  My #4 fills one cell (alarm-triggered rollback vs History Error Accumulation).

---

## The short list
| Use | Gaps |
|---|---|
| 🎯 Core of my arc | **1** (the empty seat, now 4-papers-strong) · **2** (onset/WHEN) |
| 🆓 Free riders | **3** ⭐ (smooth-signal-before-cliff plot) · 4 (breadth scrub control) |
| 🅿️ Parked | 5, 6 |

One-line memory hook:
> **B filmed 3,100 crashes in real worlds and named every cause of death — but its
> doctor only ever met dead patients. The wobble before the crash is still
> unmeasured. That's my seat, and now FOUR papers point at it.**
