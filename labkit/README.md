# labkit

A from-scratch AI library, built one chapter at a time alongside *Book 1 -
AI Foundations* in the Obsidian vault
(`Learning/Foundations/Book 1 - Foundations/`).

**Rule: you write the code.** The agent scaffolds the files, explains, reviews,
quizzes and hints. It does not write the implementations.

**Stdlib only.** No numpy, no torch. If a chapter seems to need a library, either
prove it does not, or write the piece you need.

## How it grows

| Chapter | Module | What it ends up doing |
|---|---|---|
| 01-03 | `linalg.py` | vectors, dot products, matrix multiplication, linear maps |
| 04-06 | `calculus.py` | derivatives, gradients, the chain rule |
| 07-09 | `probability.py` | distributions, expectation, entropy, cross-entropy, stable softmax |
| 10-16 | `data.py` | examples, labels, batching, the train/val/test split |
| 12, 13, 20 | `optim.py` | loss functions, gradient descent, optimizers |
| 17 | `tensors.py` | n-dimensional arrays with named axes, broadcasting |
| 18, 21-22 | `nn.py` | layers, the model, the training loop |
| 19 | `autograd.py` | automatic differentiation, built on your own calculus code |
| 23 | `tokenizer.py` | a byte and word-level tokenizer |
| 24-29 | `transformer.py` | embeddings, attention, the block, sampling |
| 30, 32, 34 | `decision.py`, `router.py` | the decision head, the schema, the threshold policy |
| 31, 33 | `metrics.py` | accuracy, ECE, reliability curves, the seven measurements |

**Nothing here exists yet.** Each module is created in the chapter that needs it.
There are no stub files waiting to be filled in — a module appears when the chapter
that builds it arrives.

## The contract

`CONTRACT.md` fixes every public name and signature. **Change it before you change a
chapter**, never after. If a chapter and the contract disagree, the contract wins and
the contract is what gets fixed first.

## Rules

- Functions are pure, deterministic, and raise `ValueError` for shape mismatches.
- Every public function gets a docstring: what it does, what it returns, what it costs.
- Tests live in `labkit/tests/test_<module>.py` and use `unittest`.

## Run the checks

```bash
python -m unittest discover -s labkit/tests -v
```

## The map

`../LEARNING.md` — where each chapter's reading, module and GitHub issue live.
