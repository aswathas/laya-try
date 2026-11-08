# GLOSSARY.md — the vocabulary of this repo

Use these words, not synonyms, in issue titles, code, tests and notes. If a concept
you need is missing, that is a signal: either you are inventing language the project
does not use, or there is a real gap worth closing with `/domain-modeling`.

## The learner and the agent

**Learner** — Aswath. The person who writes every function in `labkit/`.

**Agent** — Claude Code. Explains, reviews, quizzes, hints, scaffolds. Never writes
an implementation.

**Chapter** — one of the 34 chapters of *Book 1 - AI Foundations*, in the Obsidian
vault at `Learning/Foundations/Book 1 - Foundations/`.

**Session** — one of the three passes over a chapter: **A - Concept**, **B - Build**,
**C - Verify + teach back**. A chapter is grasped only when all three hold.

**Gate** — a checkpoint that proves a stage is understood (G1-G6). A gate re-asks
questions from earlier chapters. Passing a gate is a separate check, not a formality.

**Contract** — `labkit/CONTRACT.md`. Fixes every public name and signature. Change it
before changing a chapter.

**Tracer bullet** — one vertical slice that works end to end, small enough to finish
and prove something. Every chapter ticket is one.

## The mathematics

**Scalar** — one number. `0.9`, not `[0.9]`.

**Vector** — an ordered list of floats. Order is the whole point: `[0.9, 0.1]` means
something, the same two numbers as a set do not.

**Shape** — the size of each axis of a vector or matrix. `(3,)` is a 3-vector;
`(2, 3)` is a 2-row, 3-column matrix. Shapes are contracts.

**Matrix** — a list of lists of floats, all rows the same length.

**Dot product** — `sum(a[i] * b[i])`. One number from two vectors. Exactly what a
neuron computes.

**Norm** — the length of a vector, `sqrt(sum(x*x))`.

**Linear map** — a matrix acting on a vector. `y = W x`. The matrix is the map;
`apply_linear` is the function that applies it.

**Rank-1 matrix** — a matrix that can only stretch or flatten along one direction.
What it forbids is the point of studying it.

**Derivative** — a rate: whose rate, about what, per what unit.

**Gradient** — the vector of partial derivatives. A direction, not a number.

**Chain rule** — how a nudge to one early weight becomes a nudge to the final loss.

**Numerical derivative** — `(f(x+h) - f(x-h)) / (2h)`. A finite difference, used to
check an analytic derivative, never as the definition.

## Probability and information

**Probability** — a number in `[0, 1]`. A distribution's entries sum to 1.

**Expectation** — the probability-weighted average. It averages *over* the
distribution, which is not the same as the most likely outcome.

**Entropy** — `-sum(q * ln(q))`. Uncertainty, in nats.

**Cross-entropy** — `-sum(p[i] * ln(q[i]))`. How surprised you are by the truth `p`
under your belief `q`. A confidently wrong answer costs far more than an uncertain one.

**KL divergence** — `sum(p[i] * ln(p[i] / q[i]))`. How far `q` is from `p`.

**Logit** — an unnormalised score from the last layer of a model, one per candidate
option. Any real number. Not a probability.

**Softmax** — turns logits into a distribution: exponentiate, divide by the sum.
Preserves ordering, always positive.

**Temperature** — divides the logits before softmax. Low sharpens, high flattens.
At 1 the model is native. It changes *which* option a thresholded decision picks.

**Log-sum-exp** — `ln(sum(exp(x)))`, computed stably by subtracting the max. Exists
because `exp(1000)` overflows.

**Calibration** — a model that says 70% is right 70% of the time.

**ECE** — expected calibration error. Bins predictions by confidence, averages the
gap between confidence and accuracy, weights by bin count.

**Reliability curve** — per bin: `(mean confidence, accuracy, count)`.

**Brier score** — mean squared error of the predicted probabilities.

## The machine

**Tensor** — a nested list of floats with named axes.

**Parameter** — a number the model learned. The model stores parameters, not answers.

**Loss** — the scoreboard. The only honest measure of how a model is doing. A number
measured on training data is not evidence.

**Gradient descent** — `x <- x - lr * grad(x)`. The learning rate decides between
learning and divergence.

**Momentum** — `v = momentum * v + grad`. The effective step is `lr / (1 - momentum)`,
so momentum usually needs a smaller learning rate.

**Autograd** — a tape of operations that replays the chain rule to fill `.grad` on
every node.

**Backpropagation** — the chain rule, applied in code, reusing partial results.

**Embedding** — a vector that stands for a token. Meaning becomes geometry.

**Attention** — each position looks at every other position and decides how much to
take from each. A weighted sum of values, with the weights from a softmax over
scaled dot products.

**Head** — one of the parallel attention sub-computations inside a multi-head layer.

**KV cache** — the stored keys and values from previous steps. The reason long
contexts are slow.

**Layer norm** — zero mean, unit variance, then scale and shift.

**Residual connection** — adding a sub-layer's input to its output.

**Transformer block** — attention, residual, layer norm, feed-forward, residual,
layer norm. The order matters.

**Next-token prediction** — the training objective. One training example is a
sequence and its shifted copy.

**Temperature sampling** — sample from the softmax of `logits / temperature`.

**Top-p** — keep the smallest set of candidates whose cumulative probability reaches
`p`, renormalise, then sample.

## The decision model

**Decision model** — a model that takes a *state* and returns a probability over a
small set of *typed options*. It chooses; an LLM writes.

**Decision head** — a softmax over the option set. The same maths as a language
model's head, with a different number of outputs.

**Schema** — the ordered list of fields the model is allowed to see. The most
important artifact in the system, and it is not code.

**Abstention** — declining to act because confidence is below the threshold. The
system needs a queue behind the abstentions.

**Threshold** — where "not sure enough" becomes "a human looks at it". Defensible
only against the cost of being wrong.

**Swap safety** — does the decision survive changing the provider? Choices agreeing is
weaker evidence than the action agreeing.
