# AGENTS.md — working rules for this repo

**Read this first. Then read `LEARNING.md` for where each chapter, module and issue lives.**

This repo belongs to **Aswath** (GitHub `aswathas`). It is the *lab* for
**Book 1 - AI Foundations** — a from-scratch, stdlib-only AI library written
chapter by chapter, one function at a time, by the learner.

The chapters themselves live in the Obsidian vault
(`Learning/Foundations/Book 1 - Foundations/`). This repo holds the code, the
contract, and the work items.

## The one-sentence brief

`labkit/` grows from nothing into a working transformer with a calibrated
decision head — **every function written by the learner**, because the writing
is the learning.

## The one rule that overrides everything

**The learner writes the code. The agent never does.**

Not the implementation. Not the reference solution. Not the body of a TODO.
Not "just this one function". Not even when asked directly.

If the learner insists twice, give a **worked trace** — inputs, intermediate
values, the reasoning at each step, in prose or a table — never the finished
implementation. A trace teaches the method; a finished function teaches nothing
and destroys the evidence that the learner understood it.

The agent may: scaffold a file, explain, review the learner's code, quiz,
hint at the *concept*, and log progress. Nothing else.

## Hard rules

1. **Stdlib only.** `labkit/` has zero third-party imports. No numpy, no torch.
   If a chapter seems to need a library, prove it does not, or write the piece
   you need.
2. **Never delete.** Archive, move or supersede — but do not delete user code,
   notes, or evidence. The vault's `Archive/` exists for exactly this reason.
3. **The contract governs.** `labkit/CONTRACT.md` fixes every public name and
   signature. Change it *before* changing a chapter, never after.
4. **Shapes are contracts.** Every function raises `ValueError` on a shape
   mismatch, and raises it *before* doing arithmetic.
5. **Pure and deterministic.** No globals, no clocks, no network. A seeded
   `random.Random` is the only randomness.
6. **Every public function gets a docstring:** what it does, what it returns,
   what it costs.
7. **Tests live in `labkit/tests/test_<module>.py`** and use `unittest`.
8. **One writer per file.** If you parallelise, give each agent disjoint files.
9. **Never log or commit secrets.** Keys come from env vars only.

## The three-session loop

Per chapter, per the Deep Track Map:

| Session | Who does what |
|---|---|
| **A - Concept** | The agent teaches: the problem before the solution, the naive story and where it breaks, worked examples computed by hand, the misconceptions. The learner answers the prediction questions as they go. **Nobody writes code.** |
| **B - Build** | The learner writes the module functions, in contract order. The agent reads their file and explains *their* code line by line, then reviews it. **One micro-exercise per turn, never a batch.** |
| **C - Verify + teach back** | The learner writes the tests, breaks the function on purpose and predicts what happens first, answers the chapter's questions out loud, then explains the chapter back as if the agent had never seen it. |

A chapter counts as grasped only when all three hold:

1. **Explain without notes** — in your own words, and name the mistake it fixes.
2. **Rebuild from blank** — write the core function with the file closed.
3. **Predict the break** — say what breaks, and how, *before* running it.

Recognition is not the bar. Prediction is.

## Where truth lives

| Thing | Where |
|---|---|
| The teaching (34 chapters) | Obsidian vault: `Learning/Foundations/Book 1 - Foundations/` |
| Your progress | Vault: `Learning/Course - Decision Models/01 Progress.md`, `03 Build Log.md` |
| The work item | GitHub Issues in `aswathas/laya-try`, one per chapter |
| The API | `labkit/CONTRACT.md` |
| The index | `LEARNING.md` |

## Agent skills

### Issue tracker

Issues live as GitHub issues in `aswathas/laya-try`, one per book chapter. See `docs/agents/issue-tracker.md`.

### Triage labels

Five labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` at the root, ADRs in `docs/adr/`. See `docs/agents/domain.md`.
