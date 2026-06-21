# How an LLM Agent Actually Works — Plain Explainer
*(Built up from scratch on 2026-06-03. Read this to refresh the whole picture
before designing the experiments. Written in simple language on purpose.)*

---

## The 1 core idea (everything sits on this)
> **An LLM can ONLY write text. It cannot DO anything.**
> A small program around it ("your code") is the HANDS that actually run things.

- **The LLM** = Claude/GPT, lives on a server far away, only writes words.
- **"Your code"** = a small Python program on your laptop. It sends text to the
  LLM, reads the reply, and *actually does* what the reply says (open files,
  run tests). When you use **Claude Code in the terminal, Claude Code itself
  is this "your code"** — Anthropic already wrote it for you.

Picture:
```
   YOUR CODE (laptop)  <--internet-->  THE LLM (server)
   - sends the question                 - reads it
   - reads the answer                   - writes an answer (text only)
   - DOES the action (hands)
```
The LLM is a very smart friend on the phone who can't move. It only *tells* you
what to do. Your code has the hands.

---

## PART A — How the LLM "completes the sentence" (understands)
The LLM only ever does ONE trick: **guess the next tiny piece of text.**

1. **Tokens** — text is chopped into small pieces (token = ~3/4 of a word).
   "find an apple" -> ["find", " an", " apple"]. Each token is a number.
2. **Embedding** — each token becomes a long list of numbers that captures its
   meaning. Similar meanings sit near each other (apple near fruit, far from truck).
3. **Attention** — every token looks at the others and decides which matter for
   what comes next. This is how it "uses context."
4. **Probability table** — it outputs a % for EVERY possible next token:
   after "find an ___":  apple 71% | object 9% | item 6% | ...
   **This table IS understanding** — it understood well if the sensible token
   gets high %.
5. **Sampling** — pick one token from the table. **Temperature** = randomness
   knob (0 = always top choice, predictable; high = more varied). Agents use
   LOW temperature so results are stable/reproducible.
6. **Autoregression** — append the picked token, re-read everything, predict the
   next. Repeat hundreds of times until a stop token.

> "Completing the sentence" = looping steps 3-5 hundreds of times, one token
> each. There is no other magic.

---

## PART B — The agent loop (one full pass)
```
  1. SEND    -> your code sends the WHOLE transcript to the LLM
  2. THINK   -> LLM writes "Thought: ..." + "Action: ..." (just text, Part A)
  3. PARSE   -> your code finds the Action inside that text
  4. DO      -> your code runs the real tool (Read / Edit / Bash) = the HANDS
  5. OBSERVE -> your code pastes the result back as "Observation: ..."
  6. REPEAT  -> go to 1 with the now-longer transcript
            ... until the LLM writes finish()
```

---

## TWO key words

### Transcript = the agent's ONLY memory
The whole conversation written in one growing document: hidden rules + task +
every Thought/Action/Observation so far. The LLM **forgets everything between
steps**, so your code re-sends the entire transcript every step. The transcript
IS the agent's mind. Like a notebook you show an amnesiac before every move.
(Long tasks => huge transcript => attention spreads thin => goal fades =>
errors rise. That is literally research idea #16.)

### Observation = the agent's eyes
The result of an action, pasted back so the LLM can SEE what happened.
- Without it: it says "Read the file" but never sees the contents -> edits blind.
- With it: it sees the code/test result -> makes the correct next move.
Action = reach out and do something. Observation = see what happened.
The seeing-and-adjusting is what makes it look intelligent.

---

## Worked example — fixing a bug (mobile dev / Claude Code)
Bug: app crashes, "undefined is not an object (user.name.toUpperCase)".

| Loop | LLM writes (brain)            | Your code does (hands)      | Result            |
|------|-------------------------------|-----------------------------|-------------------|
| 1    | Grep / Read(LoginScreen.js)   | searches + opens real file  | sees the bug      |
| 2    | Edit(add safe check ?? 'Guest')| changes the real file       | bug fixed on disk |
| 3    | Bash(npm test)                | runs the real tests         | learns pass/fail  |
| 4    | finish()  (or fix again)      | stops loop (or loops back)  | done              |

In the terminal, the lines `● Read(...)`, `● Update(...)`, `● Bash(...)` =
Claude writing an Action and Claude Code executing it. The `└ result` lines =
the Observation. Several in a row = the loop. Final message = finish().

---

## Why it "knows" to open the file first
Two things make `Read(file)` the highest-probability first action:
1. **A hidden system prompt** you never see, sent before your message. It lists
   the tools and the rules, e.g. "When given a bug, FIRST find and READ the
   relevant code. Never edit a file you have not read. Verify with tests."
2. **Training habits** — millions of examples where humans look before editing.

Both push the same way -> "read first" wins. **No human-like memory** — every
step it just re-reads the rules + transcript and writes the most likely action.
**Change the rules -> change the behavior.** (Real published examples of such
prompts: OpenHands, Aider, SWE-agent, Cline on GitHub.)

> This is the whole API-only experiment lever: edit the hidden rules / add
> self-check steps, and MEASURE how behavior changes. No GPUs needed.

---

## The 4 truths to remember
1. The LLM only WRITES TEXT (highest-probability next words).
2. Your code is the HANDS (parse + run the real tool).
3. The TRANSCRIPT is the only memory (re-sent every step).
4. The OBSERVATION is the eyes (feedback closes the loop = looks smart).

One sentence:
> An agent = an LLM that writes one action as text -> your code runs it ->
> the result is pasted back -> repeat, until it says "done."

---

## What I build for each research idea

### PART 0 — shared base (build ONCE, ~60% of all 3 ideas)
- the agent loop (transcript + Thought/Action/Observation)
- an environment (ALFWorld / WebArena, OR a code agent with buggy files)
- logging of EVERY step (thought, action, observation, tokens, time)
- a budget kill-switch (never overspend the API)

### #16 MEASURE — is drift linear or exponential? (lowest risk, can't fail)
Add: (1) a **judge** that labels each step right/wrong (rule or LLM-as-judge);
(2) a **runner** over many task lengths; (3) **plot error-rate vs step-number**
— straight line = linear, bending up = exponential.
Output: one graph + one sentence. Hardest part: the judge.

### #18 DETECT — can it catch its own drift early?
Add: (1) a **self-monitor prompt** each step ("reading your last 3 thoughts,
are you still on the original task? confidence 0-1") = 1 extra LLM call/step;
(2) **mark the true failure step** (ground truth); (3) check if the **alarm
fires BEFORE the failure**.
Output: "the self-alarm fired N steps before failure X% of the time."
Hardest part: defining drift + marking the true failure point.

### #4 REPAIR — self-correct with vs without a verifier?
Add: (1) a **critique + redo** step ("what was wrong?" then "redo it");
(2) a **verifier TOGGLE** — condition A feedback ON (show test/error) vs
condition B feedback OFF (hide it, self-reflect only); (3) **compare recovery
rates** + measure **over-correction** (made correct things wrong?).
Output: "with verifier recovers X%, without only Y%."
Best feature: a code agent gives a FREE verifier via run_tests() — just hide
or show the test output.

### Picture
```
        SHARED BASE (build once): loop + environment + logging + budget cap
                 |
   #16 adds: judge + many lengths + plot the curve
   #18 adds: self-check prompt + mark true failure + check alarm timing
   #4  adds: critique+redo step + verifier ON/OFF toggle + compare recovery
```

### Agreed plan
1. Build PART 0 + #16 first (insurance result + shared data the others reuse).
2. Then go DEEP on ONE of #18 or #4 (pick after reading the 3 anchor papers).
3. Show professor: insurance result (#16) + the one interesting question chased
   on the same harness. Clean, low-risk, API-only, one semester.
