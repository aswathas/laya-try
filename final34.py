import io

OUT = r"C:\Users\aswat\Projects\laya-try\final34.py.tmp"

body = r'''---
title: "34 - Building Your First Decision Model, End to End"
type: book-chapter
part: "Part V - Decision Models"
order: 34
status: draft
tags: [ai-foundations, book-1, decision-models, capstone]
created: 2026-11-07
updated: 2026-11-07
---

# 34 - Building Your First Decision Model, End to End

## How to use this chapter

Read it once with a calculator. Then write `labkit/router.py` and `labkit/tests/test_router.py`, run the tests, answer the five questions at the end out loud. Every number is hand-checkable: four flags, six exponentials, one softmax.

**Build target:** `labkit/router.py` (one function), `labkit/tests/test_router.py` (2 checks).

## Why this matters

The pieces are easy: `decision_head` is a softmax, `decide` is a comparison, `state_to_features` is a loop. You wrote all three.

The system is not code. Four decisions decide whether it works, none with an answer you can look up: **the schema** (what the model may see), **the threshold** (where "not sure enough" becomes "a human looks at it"), **the abstention rule** (what happens to a declined ticket), and **the measurement** (what you check before believing any of it). Get all four wrong and the system scores beautifully on the tickets you looked at while quietly misrouting the ones you did not.

## The naive story

The naive story: *I understand the pieces, so I understand the system.* You know what a head does, what a threshold does, what a metric does - therefore you know what a decision model does. The rest is plumbing: write the head, pick a threshold (0.5, the default), wire it up, ship.

It breaks because every piece you understand is *local*: it takes numbers and returns numbers. The system is the decisions made *around* those objects, and those decisions are invisible in all of them. The threshold's number is not in the head. The schema's meaning is not in the vector. The queue that receives your abstentions is not in your code at all. So a router with a perfect head and a bad schema fails for reasons no head can fix - the failure is in the *inputs* - and so does one with no queue behind the abstentions.

## The real thing

### Step 1 - the schema

Write it down before you write any code:

```
SCHEMA = ["mentions_billing", "is_paying_tier", "has_prior_ticket", "is_email_channel"]

is_billing: ["yes", "no"]
team:       ["billing", "technical", "sales", "other"]
```

This is the most important artifact in the project, and it is not code. The vector, the weights, the thresholds and the cost of every mistake follow from those lines. Each flag comes from one field of the record: `mentions_billing` from the message text (it contains charged, refund, invoice, bill, billing, card or price as a whole word); `is_paying_tier` from the tier (`pro` or `enterprise`); `has_prior_ticket` from the prior ticket count (above zero); `is_email_channel` from the channel (`email`). Two questions, one forward pass: the same vector feeds two heads - Chapter 30's "same body, different head", twice over.

### Step 2 - the features

`state_to_features(state, SCHEMA)` turns the flags into the vector.

The honest limit: **a bag of flags throws away the text.** Three different billing complaints collapse to `[1.0, 1.0, 1.0, 1.0]` - three problems, three humans, one input. And Chapter 16's ceiling applies without mercy ([[Learning/Foundations/Book 1 - Foundations/16 - features]]): two tickets with the same flags and different labels cannot both be answered correctly, however good the model is.

### Step 3 - the head and the policy

`decision_head` gives probabilities; `decide` applies the threshold and abstains. The head is one weight per option per field, plus a bias - Chapter 32's shape, so every number below is checkable with a pencil:

| head | option | billing-word | paying-tier | prior-ticket | email | bias |
|---|---|---|---|---|---|---|
| billing | yes | 6.0 | 0.5 | 0.3 | -0.2 | -3.0 |
| billing | no | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| team | billing | 5.0 | 0.0 | 0.0 | 0.0 | -1.6 |
| team | technical | 0.0 | 1.5 | 1.2 | 0.0 | -1.2 |
| team | sales | 0.0 | 0.0 | 0.0 | 1.8 | -1.6 |
| team | other | 0.0 | 0.0 | 0.0 | 0.0 | -2.2 |

The thresholds are yours, and here is why. **`is_billing` at 0.95:** saying "yes" opens the billing workflow, where a person may issue a refund - expensive to undo, visible to a customer. **`team` at 0.50:** naming the wrong queue is cheap; a human moves it in two seconds. Write the reason next to the number.

### Step 4 - the measurement

Run the seven measurements of [[Learning/Foundations/Book 1 - Foundations/33 - seven-measurements]] on held-out data. Four of the ten tickets below are the development set you fitted against; six are held out.

| measurement | result on the held-out six | read it as |
|---|---|---|
| accuracy | is_billing 6/6 = 1.000; team 5/6 = 0.833 | team is **at the ceiling**; a constant "no" also scores 6/6 on is_billing |
| calibration | ECE 0.055386 (billing), 0.284811 (team) | *under*-confident in every bin; the ceiling error sits in the lowest bin |
| cost | 18 min per 10 tickets (6 escalations x 3 min, 0 misroutes x 12 min) | half the decisions escalated, none wrong |
| latency | head = 24 multiply-adds, 6 exponentials | p95 is set by the ticket fetch, not the model |
| determinism | 10/10 tickets reproduce exactly | no RNG in the path |
| injection | 1 of 1 attack succeeded | the flag flipped, and confidence went **up** |
| swap safety | choices agree 9/10; actions 9/10 at 0.50, 10/10 at 0.60 | the disagreement lives in the low-confidence band |

### Step 5 - the swap test

Build a second candidate: same schema, same code, different team-head weights. Run the same battery and report what changed, not what improved. That is what you ship: not "my model is good" but "here is what changes if we swap, and what it costs".

### The end-to-end check

Does it behave as one system? Four failure modes earn their names here, all visible in the numbers above.

- **A threshold that flips on rounding.** T3 clears 0.95 by 0.0026; T7 misses by 0.0022. Move the billing head's bias from -3.0 to -3.1 and T7 flips to an action.
- **An abstention nobody handles.** A declines the team on three of six held-out tickets. With no queue and service level behind "abstained", those tickets do not become someone's job - they vanish.
- **A schema field that is usually empty.** `has_prior_ticket` is missing for a brand-new account, so the flag reads 0.0 - identical to "no prior tickets". T10's vector becomes `[0.0, 0.0, 0.0, 0.0]`: the team answer drops from technical 0.660242 to technical 0.369205 and now abstains, while the billing answer goes from a 0.937027 abstention to a 0.952574 action. Two decisions flipped, one missing key, no error.
- **Latency at the 95th percentile.** The head's cost is fixed at 24 multiply-adds per ticket, so no model optimisation moves p95 - the account lookup does.

### Where you stand

You have built, from nothing and in plain Python: matrices and dot products, derivatives and the chain rule, autograd, gradient descent, a training loop with a three-way split, a tokenizer, embeddings, attention, a transformer block, next-token training, sampling, a decision head, calibration metrics and an evaluation battery. You can explain why a matrix is a shape contract, why backpropagation is the chain rule with bookkeeping, why a softmax is a distribution and not a score, and why identical features cap your accuracy. The harder skill - saying what each of those does *not* tell you - is what this book was for.

### What you would do next with real data

**Get real labelled tickets** (ten hand-written rows are a diagram, not a dataset). **Fix the label quality** (two humans must agree on the team before a label is worth training on; bad labels are not noisy labels - they are a different task than the one you think you are doing). **Then fix the schema** - this is where the accuracy lives, since T3 and T8 have identical flags and different labels, so no model passes 5/6 on the held-out six; a flag separating "app crashes" from "password reset email" raises the ceiling. **Then measure.** A better model on a bad schema loses to a worse model on a good one, every time.

## Worked examples

### Example 1 - one ticket, end to end

T1: `"charged twice for order 8812, please refund"`, tier `pro`, 1 prior ticket, channel `email` -> flags `[1.0, 1.0, 1.0, 1.0]`.

**Billing head.** Logits: yes = `6.0(1) + 0.5(1) + 0.3(1) - 0.2(1) - 3.0 = 3.6`; no = `0.0`. Softmax: `e^3.6 = 36.5982`, `e^0 = 1`, sum `37.5982` -> yes = `0.973403`, no = `0.026597`. At 0.95, `0.973403 >= 0.95` -> `{"choice": "yes", "confidence": 0.973403, "abstained": False}`.

**Team head.** Logits: billing = `5.0(1) - 1.6 = 3.4`; technical = `1.5(1) + 1.2(1) - 1.2 = 1.5`; sales = `1.8(1) - 1.6 = 0.2`; other = `-2.2`. Exponentials `29.9641`, `4.4817`, `1.2214`, `0.1108`; sum `35.7780`.

```
billing   = 29.9641 / 35.7780 = 0.837501
technical =  4.4817 / 35.7780 = 0.125264
sales     =  1.2214 / 35.7780 = 0.034138
other     =  0.1108 / 35.7780 = 0.003097
```

At 0.50, `0.837501 >= 0.50` -> `{"choice": "billing", "confidence": 0.837501, "abstained": False}`. Two questions, one forward pass, one vector.

### Example 2 - the ten tickets, and what the model did with them

Each row is one ticket: its four state fields, and the two labels the model had to produce. "dev" is the set you fitted against; "held" is the set you did not.

| # | message | tier/prior/ch | is_billing | team pick (conf) | action | truth |
|---|---|---|---|---|---|---|
| T1 | charged twice | pro/2/email | yes 0.973403 | billing 0.837501 | billing | yes / billing |
| T2 | March invoice too high | ent/7/email | yes 0.973403 | billing 0.837501 | billing | yes / billing |
| T5 | change card on file | pro/1/chat | yes 0.978119 | billing 0.862066 | billing | yes / billing |
| T9 | wrong plan charged | pro/2/email | yes 0.973403 | billing 0.837501 | billing | yes / billing |
| T3 | app crashes, reports tab | free/0/chat | no 0.952574 | technical 0.369205 | **abstain** | no / technical |
| T4 | API returns 500 | ent/3/email | no 0.916827 | technical 0.744987 | technical | no / technical |
| T6 | quote for 50 seats | free/0/email | no 0.960834 | sales 0.665507 | sales | no / sales |
| T7 | add a teammate | free/2/email | no 0.947846 | sales 0.481986 | **abstain** | no / sales |
| T8 | reset email never arrived | free/0/chat | no 0.952574 | technical 0.369205 | **abstain** | no / other |
| T10 | white-screen after update | free/1/chat | no 0.937027 | technical 0.660242 | technical | no / technical |

**Accuracy.** All ten: is_billing 10/10, team 9/10 (T8 is the miss). Held-out six: is_billing 6/6, team 5/6.

**The ceiling, checked by hand.** T3 and T8 are both free tier, zero prior tickets, chat, and neither message contains a billing word - so both produce the vector `[0.0, 0.0, 0.0, 0.0]` - and they disagree on the team (technical vs other). One of them must be wrong, so team accuracy on the held-out six cannot exceed **5/6 = 0.833** - and A scores exactly 5/6. Chapter 16's rule, unchanged: a better model cannot help, only a better schema can. (The is_billing labels never conflict, so its ceiling is 6/6 - and a constant "no" also gets 6/6, so that 1.000 says nothing about the model.)

**ECE, by hand (held-out six, team), 10 bins**, bucketed by the team's top confidence:

| bin | count | mean conf | accuracy | gap | weighted |
|---|---|---|---|---|---|
| [0.3, 0.4) | 2 | 0.369205 | 0.5 | 0.130795 | 0.043598 |
| [0.4, 0.5) | 1 | 0.481986 | 1.0 | 0.518014 | 0.086336 |
| [0.6, 0.7) | 2 | 0.662874 | 1.0 | 0.337126 | 0.112375 |
| [0.7, 0.8) | 1 | 0.744987 | 1.0 | 0.255013 | 0.042502 |

`ECE = 0.043598 + 0.086336 + 0.112375 + 0.042502 = 0.284811`. Every bin's accuracy sits above its stated confidence - the model is *under*-confident. The first row is the ceiling error: it said 0.37 and was right half the time.

**Abstentions.** Six of the twelve held-out decisions abstain: billing on T4, T7, T10; team on T3, T7, T8. Zero wrong actions. At 3 minutes per escalation and 12 per misroute: `6 x 3 + 0 x 12 = 18` minutes per ten tickets.

### Example 3 - the swap test

Candidate B: same schema, same code, same billing head, different team-head weights. A pick acts at confidence 0.50 or above, otherwise it abstains.

| # | A: pick (conf) | B: pick (conf) | verdict |
|---|---|---|---|
| T1 | billing 0.837501 | billing 0.749013 | agree |
| T2 | billing 0.837501 | billing 0.749013 | agree |
| T5 | billing 0.862066 | billing 0.762783 | agree |
| T9 | billing 0.837501 | billing 0.749013 | agree |
| T3 | technical 0.369205 | technical 0.332350 | agree (both abstain) |
| T4 | technical 0.744987 | technical 0.881130 | agree |
| T6 | sales 0.665507 | sales 0.618002 | agree |
| T7 | sales 0.481986 | technical 0.550618 | **differ** |
| T8 | technical 0.369205 | technical 0.332350 | agree (both abstain) |
| T10 | technical 0.660242 | technical 0.750714 | agree |

**Where they agree.** Nine of ten team choices, ten of ten billing choices - on this batch the two models are the same model.

**Where the actions differ.** One ticket: T7. A is 0.481986 on sales and abstains; B is 0.550618 on technical and acts - and technical is wrong, because T7's true team is sales. B routes one ticket wrongly and A routes none. On the held-out six A scores 5/6, B scores 4/6.

**Which threshold absorbed the difference.** Raise the team threshold from 0.50 to 0.60 and the two agree on **all ten**: B's 0.550618 falls below the line and both abstain on T7. The disagreement lived in the band between 0.48 and 0.56, where the threshold decides. A threshold set inside that band turns a model difference into a production incident; outside it, the same difference is nothing at all.

**And the cost.** At 12 minutes per misroute and 3 per escalation, A costs 18 minutes per ten tickets and B costs 27. Swap in B and you pay 50% more human time, route one ticket wrongly, and lower the team ECE from 0.284811 to 0.272679. The better-calibrated model is the worse system: calibration averages over the tickets you got right and the one you got wrong.

## Where this sits in the code

This chapter adds no new library functions. It assembles what you already wrote: `state_to_features`, `decision_head` and `decide` from `labkit/decision.py` (Chapters 30 and 32), `apply_linear` from `labkit/nn.py`, `accuracy` from `labkit/data.py`, and `brier_score`, `ece`, `reliability_curve` and `agreement` from `labkit/metrics.py`. The build target is a **script**: `labkit/router.py` plus `labkit/tests/test_router.py`.

**Signature:** `route(state: dict) -> dict`

**Inputs:** `state` has four keys - `message` (str), `tier` (str), `prior_tickets` (int), `channel` (str).

**Outputs:** one dict with `features` (the vector) and `is_billing` and `team`, each the three-key dict `decide` returns (`choice`, `confidence`, `abstained`; `choice` is `None` when abstained).

**Expected outputs, exactly:**

| input | `features` | `is_billing` | `team` |
|---|---|---|---|
| T1 | `[1.0, 1.0, 1.0, 1.0]` | `"yes"`, 0.973403, False | `"billing"`, 0.837501, False |
| T3 | `[0.0, 0.0, 0.0, 0.0]` | `"no"`, 0.952574, False | `None`, 0.369205, True |
| T4 | `[0.0, 1.0, 1.0, 1.0]` | `None`, 0.916827, True | `"technical"`, 0.744987, False |

**Run.** From `C:\Users\aswat\Projects\laya-try`:

```bash
python -m unittest discover -s labkit/tests -v
```

**Hint (one idea, not code):** the threshold belongs to the caller, and now *you* are the caller. Before you pick a number, finish this sentence out loud: *"a ticket the model is 0.50 sure about goes to \_\_\_\_ because \_\_\_\_."* If you cannot finish it, you have a guess with a decimal point, not a threshold.

## Your turn - build it

**File: `labkit/router.py`** - one function, `route(state)`. Inside, in this order:

1. Derive the four flags from the record using the schema rules, then call `state_to_features` with `SCHEMA` in that exact order.
2. Build the two heads with `apply_linear`, using the weight table above so your numbers match this chapter.
3. Call `decision_head` on each set of logits, then `decide` twice: `["yes", "no"]` at 0.95, the four teams at 0.50.
4. Return `{"features": ..., "is_billing": ..., "team": ...}`.

Keep the thresholds in named constants.

**File: `labkit/tests/test_router.py`** - two checks, `unittest` style like `labkit/tests/test_linalg.py`:

1. **The abstention path.** Route T3's record. Assert `result["team"]["abstained"] is True`, `result["team"]["choice"] is None`, `result["team"]["confidence"]` is `0.369205` to six places, and `result["features"] == [0.0, 0.0, 0.0, 0.0]`.
2. **One threshold boundary.** Route T4's record: `is_billing` must abstain with confidence `0.916827`, and `team` must act with choice `"technical"` and confidence `0.744987`. That pins the boundary from both sides - just above 0.95 acts, just below does not.

Do not build the evaluation battery yet; that is Chapter 33's job.

## Check yourself

1. T3 and T8 produce the same four flags. What is the highest team accuracy any model with this schema can reach on the held-out six, and what would you add to the schema to raise it?
2. T3's billing confidence clears 0.95 by 0.0026 and T7's misses by 0.0022. Move the billing head's bias from -3.0 to -3.1. Which decisions change, and what does a decision made in the third decimal place tell you about where to put a threshold?
3. A escalates more and misroutes less; B escalates less and misroutes once, with a lower ECE. At 3 minutes per escalation and 12 per misroute, which is cheaper - and at 5 and 3, which would be? What did you just decide, and whose decision is it?
4. The injected ticket flips exactly one flag and the model's confidence goes *up* afterwards, to 0.979924. Which part of your pipeline was attacked, and why is a confident wrong answer worse than an abstention?
5. The is_billing head scores 6/6 on the held-out six - and so does a constant "no". What measurement would tell those two apart, and why does accuracy alone not?

## Where this goes next

Book 2 leaves the lab and enters the decision-model field: Jev, Clef and Laya as they exist in practice - what each one is, who runs them, what they cost per call and per month, what the open-weight options look like, and what you can build on top of them. Here you built the thing from scratch; there the model arrives ready-made and the work moves to the edges: choosing a provider, pricing a call, wiring a schema into a request path, and defending a threshold to the people paged when it misfires.

**What you can now explain, one line each:**

- A vector is a shape contract; most ML bugs are shape violations.
- A matrix is a function; a layer is a multiply plus a nonlinearity.
- A derivative is a local slope; a gradient is all of them at once.
- The chain rule lets you reuse one idea, not a derivative per function.
- Autograd is the chain rule with a tape; backpropagation is the tape backwards.
- Gradient descent is walking downhill; the optimizer is how big and which way.
- Overfitting is learning the sample; the split is how you notice.
- Features set the accuracy ceiling, and the ceiling belongs to the data.
- Tensors are numbers with named axes; the names are documentation.
- An embedding is meaning as geometry; similarity is a dot product.
- Attention is every position asking every other position a question.
- A transformer block is attention, residual, norm, feed-forward, residual, norm.
- Next-token training is the objective; the rest is engineering around it.
- A decision model is the same machine with a different head and objective.
- Calibration is a claim about a conditional, and it can be checked.
- A decision model sees only the state you give it; silence looks like confidence.
- A decision model is judged by seven numbers, and each hides something.
- A schema is a decision about what a system is allowed to know.

[[Learning/Foundations/Book 1 - Foundations/00 - Book Index]]
'''

io.open(OUT, "w", encoding="utf-8").write(body)
lines = body.split("\n")
tbl = sum(len(l.split()) for l in lines if l.strip().startswith("|"))
allw = sum(len(l.split()) for l in lines)
print("total", allw, "tables", tbl, "prose", allw - tbl)
