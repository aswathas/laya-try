# laya-try

**The lab for *Book 1 - AI Foundations*.** A from-scratch, stdlib-only AI library,
written one function at a time by the learner — from nothing, through vectors,
derivatives and probability, to a transformer with a calibrated decision head.

## What is here, and what is not

| | |
|---|---|
| **The teaching (34 chapters)** | Obsidian vault: `Learning/Foundations/Book 1 - Foundations/` |
| **The code you write** | `labkit/` — in this repo |
| **The API contract** | `labkit/CONTRACT.md` |
| **The work items** | GitHub issues in this repo — one per chapter, #1 to #34 |
| **The map** | [`LEARNING.md`](LEARNING.md) |
| **The rules** | [`AGENTS.md`](AGENTS.md) |
| **The vocabulary** | [`GLOSSARY.md`](GLOSSARY.md) |

`labkit/` is **empty on purpose**. Every module is created in the chapter that
needs it. There are no stub files waiting to be filled in.

## The rule

**You write the code.** The agent scaffolds the files, explains, reviews, quizzes and
hints. It does not write the implementations. That is the whole point — the writing is
the learning.

Stdlib only. No numpy, no torch. If a chapter seems to need a library, either prove it
does not, or write the piece you need.

## The loop

One chapter, three sessions:

- **A — Concept.** The problem before the solution. The naive story and where it
  breaks. Worked examples computed by hand. Nobody writes code.
- **B — Build.** You write the module functions, in contract order. The agent reads
  *your* code and explains it line by line, then reviews it. One micro-exercise per
  turn.
- **C — Verify + teach back.** You write the tests, break the function on purpose and
  predict what happens first, then explain the chapter back as if the agent had never
  seen it.

A chapter is grasped only when all three hold: you can **explain without notes**,
**rebuild from blank**, and **predict the break**. Recognition is not the bar.
Prediction is.

Start with `/learn` in this repo.

## Run the checks

```bash
python -m unittest discover -s labkit/tests -v
```

## The gates

Six checkpoints across five stages. A gate re-asks questions from earlier chapters —
passing one is a separate check, not a formality.

| Stage | Chapters | Gate |
|---|---|---|
| I — The Mathematics | 01-09 | G1 after 03, G2 after 09 |
| II — The One Idea | 10-16 | G3 after 16 |
| III — Deep Learning | 17-22 | G4 after 22 |
| IV — Language Models | 23-29 | G5 after 29 |
| V — Decision Models | 30-34 | G6 after 34 |

## Decisions worth knowing

- [`docs/adr/0001-repo-is-a-lab-not-an-engine.md`](docs/adr/0001-repo-is-a-lab-not-an-engine.md) —
  why there is no learning engine here, and where the one that exists lives.
- [`docs/adr/0002-the-agent-never-writes-the-implementation.md`](docs/adr/0002-the-agent-never-writes-the-implementation.md) —
  why the agent never writes your code, and what it gives you instead.

## A note on the history

The first commit on `main` is a baseline of the previous contents, and the second is
the wipe that started this. Everything from that earlier state is still recoverable:

```bash
git show 34affdf:labkit/CONTRACT.md
```
