# LEARNING.md - the pointer index

This file is an **index, not a source of truth**. It answers one question: where is each
chapter's reading, its code, and its work item? It holds no progress state of its own.

| What is truth | Where |
|---|---|
| The teaching (34 chapters) | Obsidian vault: `Learning/Foundations/Book 1 - Foundations/` |
| Your progress | Vault: `Learning/Course - Decision Models/01 Progress.md` and `03 Build Log.md` |
| The work item | GitHub Issues in `aswathas/laya-try` |
| The API | `labkit/CONTRACT.md` - change it before you change a chapter |

## The loop

```
vault chapter  ->  session A (concept)  ->  session B (you write the code)
              ->  session C (you write the test, teach it back)  ->  close the issue
```

Start a session with `/learn` inside this repo. It finds the chapter, the issue, and the
module, and it never writes your implementation.

## Stages and gates

| Stage | Chapters | Gate | The gate proves you can |
|---|---|---|---|
| I - The Mathematics | 01-09 | G1 (after 03) | name every shape in any layer, from a sentence |
| | | G2 (after 09) | compute cross-entropy by hand; say why `log_sum_exp` exists |
| II - The One Idea | 10-16 | G3 (after 16) | explain every number on a training curve |
| III - Deep Learning | 17-22 | G4 (after 22) | backprop by hand and match your own code |
| IV - Language Models | 23-29 | G5 (after 29) | explain attention and sampling, no diagram |
| V - Decision Models | 30-34 | G6 (after 34) | defend a threshold, an abstention rule, a measurement set |

A gate is a separate check, not a formality. It re-asks questions from earlier chapters.

## Chapters

| Ch | Read (vault) | Module | Issue | Gate |
|---|---|---|---|---|
| 01 | [01 - vectors-and-shapes](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/01 - vectors-and-shapes.md) | `labkit/linalg.py` | [#1](https://github.com/aswathas/laya-try/issues/1) |  |
| 02 | [02 - dot-products](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/02 - dot-products.md) | `labkit/linalg.py` | [#2](https://github.com/aswathas/laya-try/issues/2) |  |
| 03 | [03 - matrices-as-maps](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/03 - matrices-as-maps.md) | `labkit/linalg.py` | [#3](https://github.com/aswathas/laya-try/issues/3) | **G1** |
| 04 | [04 - derivatives](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/04 - derivatives.md) | `labkit/calculus.py` | [#4](https://github.com/aswathas/laya-try/issues/4) |  |
| 05 | [05 - gradients](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/05 - gradients.md) | `labkit/calculus.py` | [#5](https://github.com/aswathas/laya-try/issues/5) |  |
| 06 | [06 - chain-rule](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/06 - chain-rule.md) | `labkit/calculus.py` | [#6](https://github.com/aswathas/laya-try/issues/6) |  |
| 07 | [07 - probability](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/07 - probability.md) | `labkit/probability.py` | [#7](https://github.com/aswathas/laya-try/issues/7) |  |
| 08 | [08 - information-theory](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/08 - information-theory.md) | `labkit/probability.py` | [#8](https://github.com/aswathas/laya-try/issues/8) |  |
| 09 | [09 - numerics](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/09 - numerics.md) | `labkit/probability.py` | [#9](https://github.com/aswathas/laya-try/issues/9) | **G2** |
| 10 | [10 - the-one-idea](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/10 - the-one-idea.md) | `labkit/data.py` | [#10](https://github.com/aswathas/laya-try/issues/10) |  |
| 11 | [11 - data-and-labels](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/11 - data-and-labels.md) | `labkit/data.py` | [#11](https://github.com/aswathas/laya-try/issues/11) |  |
| 12 | [12 - parameters-and-loss](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/12 - parameters-and-loss.md) | `labkit/optim.py` | [#12](https://github.com/aswathas/laya-try/issues/12) |  |
| 13 | [13 - training-loop](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/13 - training-loop.md) | `labkit/optim.py` | [#13](https://github.com/aswathas/laya-try/issues/13) |  |
| 14 | [14 - overfitting](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/14 - overfitting.md) | `labkit/data.py` | [#14](https://github.com/aswathas/laya-try/issues/14) |  |
| 15 | [15 - four-flavors](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/15 - four-flavors.md) | `labkit/data.py` | [#15](https://github.com/aswathas/laya-try/issues/15) |  |
| 16 | [16 - features](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/16 - features.md) | `labkit/data.py` | [#16](https://github.com/aswathas/laya-try/issues/16) | **G3** |
| 17 | [17 - tensors](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/17 - tensors.md) | `labkit/tensors.py` | [#17](https://github.com/aswathas/laya-try/issues/17) |  |
| 18 | [18 - layers](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/18 - layers.md) | `labkit/nn.py` | [#18](https://github.com/aswathas/laya-try/issues/18) |  |
| 19 | [19 - backpropagation](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/19 - backpropagation.md) | `labkit/autograd.py` | [#19](https://github.com/aswathas/laya-try/issues/19) |  |
| 20 | [20 - gradient-descent](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/20 - gradient-descent.md) | `labkit/optim.py` | [#20](https://github.com/aswathas/laya-try/issues/20) |  |
| 21 | [21 - from-scratch](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/21 - from-scratch.md) | `labkit/nn.py` | [#21](https://github.com/aswathas/laya-try/issues/21) |  |
| 22 | [22 - representation-learning](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/22 - representation-learning.md) | `labkit/nn.py` | [#22](https://github.com/aswathas/laya-try/issues/22) | **G4** |
| 23 | [23 - tokens](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/23 - tokens.md) | `labkit/tokenizer.py` | [#23](https://github.com/aswathas/laya-try/issues/23) |  |
| 24 | [24 - embeddings](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/24 - embeddings.md) | `labkit/transformer.py` | [#24](https://github.com/aswathas/laya-try/issues/24) |  |
| 25 | [25 - attention](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/25 - attention.md) | `labkit/transformer.py` | [#25](https://github.com/aswathas/laya-try/issues/25) |  |
| 26 | [26 - heads-and-cache](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/26 - heads-and-cache.md) | `labkit/transformer.py` | [#26](https://github.com/aswathas/laya-try/issues/26) |  |
| 27 | [27 - transformer-block](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/27 - transformer-block.md) | `labkit/transformer.py` | [#27](https://github.com/aswathas/laya-try/issues/27) |  |
| 28 | [28 - next-token-training](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/28 - next-token-training.md) | `labkit/transformer.py` | [#28](https://github.com/aswathas/laya-try/issues/28) |  |
| 29 | [29 - sampling](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/29 - sampling.md) | `labkit/transformer.py` | [#29](https://github.com/aswathas/laya-try/issues/29) | **G5** |
| 30 | [30 - different-head](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/30 - different-head.md) | `labkit/decision.py` | [#30](https://github.com/aswathas/laya-try/issues/30) |  |
| 31 | [31 - calibration](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/31 - calibration.md) | `labkit/metrics.py` | [#31](https://github.com/aswathas/laya-try/issues/31) |  |
| 32 | [32 - what-it-is-not](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/32 - what-it-is-not.md) | `labkit/decision.py` | [#32](https://github.com/aswathas/laya-try/issues/32) |  |
| 33 | [33 - seven-measurements](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/33 - seven-measurements.md) | `labkit/metrics.py` | [#33](https://github.com/aswathas/laya-try/issues/33) |  |
| 34 | [34 - build-one](file:///C:/Users/aswat/Aswaths%20Obsidian%20Den/Aswaths%20Mountain%20Den/Learning/Foundations/Book%201%20-%20Foundations/34 - build-one.md) | `labkit/router.py` | [#34](https://github.com/aswathas/laya-try/issues/34) | **G6** |

## Rules

1. **You write the code.** The agent scaffolds, explains, reviews, quizzes and hints. It never
   writes an implementation, never pastes a reference solution, and never completes a TODO you
   left - not even if you ask for just the answer. If you insist twice, it gives a worked trace
   (inputs, intermediate values, reasoning at each step) instead.
2. **Stdlib only.** No numpy, no torch. If a chapter seems to need a library, either prove it does
   not, or write the piece you need.
3. **The contract governs.** `labkit/CONTRACT.md` fixes every name and signature. Change it
   before you change a chapter, never after.
4. **Shapes are contracts.** `ValueError` on any shape mismatch, raised before arithmetic.
5. **Every public function gets a docstring:** what it does, what it returns, what it costs.
6. **Tests live in `labkit/tests/test_<module>.py`** and use `unittest`.
7. **Run the checks:** `python -m unittest discover -s labkit/tests -v`

## Current state

Chapter 01 is the next one. Nothing in `labkit/` is written yet - every module is created by you,

in the chapter that needs it.

