# 0001 — This repo is a lab, not a learning engine

**Date:** 2026-11-08
**Status:** Accepted

## Context

`aswathas/decision-arena` already contains a complete, gated learning engine: 46
authored lessons, 199 auto-graded questions with per-concept mastery, a review queue,
an append-only build log, an adaptive coach skill, and a format gate that fails the
build on a malformed lesson.

That engine is also **cold** — `progress.json` has zero lessons done, `build_log.md`
has zero entries, `exercises/` does not exist.

Its content gap is precisely *Book 1 - AI Foundations*: no matmul, no backprop through
a network, no autodiff, no end-to-end transformer. The Academy teaches concepts and
exercises against the existing `decisionarena/` package; it does not teach the
numerics from scratch.

Two candidate shapes for this repo were on the table:

- **(A)** code + tracker only. The vault chapters are the curriculum; GitHub issues are
  the work items; no engine here.
- **(B)** a full second engine — `course/`, `learn_state.py`, `progress.json` — with
  the 34 chapters converted to the 8-section lesson format.

## Decision

**(A).** This repo holds the code, the contract, and the work items. It has no learning
engine.

The full engine already exists, in a repo that is public, gated and working. A second
copy of `learn_state.py` would be ~600 duplicated lines and a second `progress.json`
that would drift from the first. The machinery is not the gap; the content is.

The session loop is driven by a repo-local `.claude/skills/learn/` skill that reads the
vault chapter and the GitHub issue directly. No progress database: progress lives in the
vault (`01 Progress.md`, `03 Build Log.md`), which is where it already lives and where
it is already written by hand.

## Consequences

- `decision-arena` remains the home of the Academy engine. If it ever needs the
  numerics curriculum, the right move is to add lessons there, not to fork the engine.
- This repo has no machine-readable progress state. An agent picking this up cold reads
  `LEARNING.md` for the map and the GitHub issues for status.
- The repo-local `learn` skill shadows the global `learn` skill (the 523-lesson
  `rohitg00/ai-engineering-from-scratch` curriculum) inside this directory only,
  exactly as `decision-arena` does with its own copy. Outside this directory, `/learn`
  still means the other course.
