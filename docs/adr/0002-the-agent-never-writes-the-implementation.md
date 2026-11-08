# 0002 — The agent never writes the implementation

**Date:** 2026-11-08
**Status:** Accepted

## Context

The `implement` skill from the Matt Pocock engineering set says: implement the work,
call `tdd` at pre-agreed seams, run the typechecker, commit your work, then call
`code-review`. Applied literally to this repo, the agent would write the functions.

That contradicts the point of the repo. The purpose of `labkit/` is that the *learner*
writes every function, because writing it is the only thing that produces the
understanding the repo exists to build. A finished implementation is not a faster route
to understanding — it is the removal of understanding.

The same rule already governs `decision-arena` (`AGENTS.md` rule 8 there: "The learner
writes the exercise code").

## Decision

**The agent never writes an implementation.** Not the function body, not the reference
solution, not the body of a TODO, not "just this one function", not even when asked
directly.

If the learner insists twice, the agent gives a **worked trace** — inputs, intermediate
values, the reasoning at each step, in prose or a table — and never the finished
implementation. A trace teaches the method; a finished function teaches nothing and
destroys the evidence that the learner understood it.

The agent may scaffold files, explain, review the learner's code, quiz, hint at the
concept, and log progress.

## Consequences

- The `implement` skill is **not** used for learner code in this repo. It remains
  available for tooling and infrastructure changes, where the code is not the learning.
- The `code-review` skill **is** used, in session C: the agent reviews the learner's
  own code against the contract and the chapter's intent.
- Tests are also written by the learner (session C). An agent-written test can pass
  against a wrong implementation and teach the wrong thing.
- `AGENTS.md` carries the rule as the one line that overrides everything else.
