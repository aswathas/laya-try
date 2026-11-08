# labkit API contract

The names and behaviours every chapter adds. The learner writes all of them.
Chapters must use exactly these names, or the code and the book drift apart.

Stdlib only. A vector is a `list[float]`. A matrix is a `list[list[float]]`.

## linalg.py - chapters 01-03

| Function | Signature | Behaviour |
|---|---|---|
| `add` | `add(a: list[float], b: list[float]) -> list[float]` | elementwise sum; `ValueError` if lengths differ |
| `scale` | `scale(a: list[float], k: float) -> list[float]` | every element times `k` |
| `dot` | `dot(a: list[float], b: list[float]) -> float` | `sum(a[i] * b[i])`; `ValueError` if lengths differ |
| `norm` | `norm(a: list[float]) -> float` | `sqrt(sum(x * x))` |
| `matvec` | `matvec(W: list[list[float]], x: list[float]) -> list[float]` | `y[i] = sum(W[i][j] * x[j])`; `ValueError` if `len(W[i]) != len(x)` for any row, or if rows have differing lengths |
| `matmul` | `matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]` | `(m,k) x (k,n) -> (m,n)`; `ValueError` if `len(A[0]) != len(B)` |
| `apply_linear` | `apply_linear(W: list[list[float]], b: list[float], x: list[float]) -> list[float]` | `matvec(W, x) + b`; `ValueError` if `len(b) != len(W)` |
| `zeros` | `zeros(rows: int, cols: int) -> list[list[float]]` | rows of cols zeros |
| `identity` | `identity(n: int) -> list[list[float]]` | `n x n` identity |

## calculus.py - chapters 04-06

| Function | Signature | Behaviour |
|---|---|---|
| `derivative` | `derivative(f, x: float, h: float = 1e-7) -> float` | central difference `(f(x+h) - f(x-h)) / (2h)` |
| `square` | `square(x: float) -> float` | `x * x` |
| `cube` | `cube(x: float) -> float` | `x * x * x` |
| `numeric_gradient` | `numeric_gradient(f, xs: list[float], h: float = 1e-7) -> list[float]` | one partial derivative per entry of `xs` |
| `compose` | `compose(f, g) -> callable` | returns `lambda x: f(g(x))` |
| `chain_grad` | `chain_grad(f, g, x: float, h: float = 1e-7) -> float` | numeric derivative of `f(g(x))` |

## probability.py - chapters 07-09

| Function | Signature | Behaviour |
|---|---|---|
| `mean` | `mean(xs: list[float]) -> float` | arithmetic mean; `ValueError` on empty input |
| `variance` | `variance(xs: list[float]) -> float` | population variance, mean of squared deviations |
| `binomial_pmf` | `binomial_pmf(n: int, p: float, k: int) -> float` | probability of exactly `k` successes |
| `normal_pdf` | `normal_pdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float` | density of the normal |
| `entropy` | `entropy(p: list[float]) -> float` | `-sum(q * ln(q))`, nats; terms with `q == 0` contribute 0 |
| `cross_entropy` | `cross_entropy(p: list[float], q: list[float]) -> float` | `-sum(p[i] * ln(q[i]))`; `ValueError` on length mismatch |
| `kl_divergence` | `kl_divergence(p: list[float], q: list[float]) -> float` | `sum(p[i] * ln(p[i] / q[i]))` |
| `log_sum_exp` | `log_sum_exp(xs: list[float]) -> float` | `ln(sum(exp(x)))`, computed stably |
| `softmax` | `softmax(logits: list[float], temperature: float = 1.0) -> list[float]` | stable softmax of `logits / temperature`; `ValueError` if `temperature <= 0` |
| `cross_entropy_from_logits` | `cross_entropy_from_logits(logits: list[float], target_index: int) -> float` | `-ln(softmax(logits)[target_index])`, computed stably |

## data.py - chapters 10, 11, 14, 15, 16

| Function | Signature | Behaviour |
|---|---|---|
| `rule_scores` | `rule_scores(features: list[list[float]], weights: list[float]) -> list[float]` | one score per example: `dot(features[i], weights)`; `ValueError` on any length mismatch |
| `accuracy` | `accuracy(preds: list[int], labels: list[int]) -> float` | fraction correct; `ValueError` if lengths differ or the input is empty (a score over zero examples is not a score) |
| `split` | `split(data: list, train_ratio: float = 0.8, seed: int = 0) -> tuple[list, list]` | deterministic split via `random.Random(seed)`; returns `(train, test)`; `ValueError` if `train_ratio` not in (0, 1) |
| `batches` | `batches(data: list, size: int) -> list[list]` | consecutive chunks of `size`; the last chunk may be shorter; `ValueError` if `size <= 0` |
| `polynomial_features` | `polynomial_features(x: float, degree: int) -> list[float]` | `[x, x^2, ..., x^degree]`; `ValueError` if `degree < 1` |
| `encode_labels` | `encode_labels(labels: list[str]) -> dict[str, int]` | labels to contiguous ids in first-seen order |
| `decode_labels` | `decode_labels(encoding: dict[str, int]) -> dict[int, str]` | the inverse map |
| `count_features` | `count_features(texts: list[str], vocab: list[str]) -> list[list[float]]` | per text, the count of each vocabulary word (case-insensitive, whole words) |

## optim.py - chapters 12, 13, 20

| Function | Signature | Behaviour |
|---|---|---|
| `squared_error` | `squared_error(pred: float, target: float) -> float` | `(pred - target) ** 2` |
| `mean_squared_error` | `mean_squared_error(preds: list[float], targets: list[float]) -> float` | mean of squared errors; `ValueError` if lengths differ or empty |
| `train_linear` | `train_linear(features: list[list[float]], targets: list[float], learning_rate: float = 0.01, steps: int = 1000) -> tuple[list[float], float]` | plain gradient descent on `w.x + b`; returns `(weights, bias)`; `ValueError` on length mismatch |
| `gradient_descent` | `gradient_descent(grad_fn, start: list[float], learning_rate: float, steps: int) -> list[float]` | generic loop: `x <- x - lr * grad_fn(x)`; `ValueError` if `steps < 0` |
| `momentum_step` | `momentum_step(velocity: list[float], grad: list[float], learning_rate: float, momentum: float = 0.9) -> list[float]` | `v = momentum * v + grad`, returns the new velocity. The learning rate is NOT applied inside this function - the caller moves the parameter by `learning_rate * v`, so the step size is applied in exactly one place. Note the effective step is `learning_rate / (1 - momentum)`: momentum 0.9 at lr 0.1 behaves like lr 1.0, which is why momentum usually needs a smaller learning rate |

## tensors.py - chapter 17

A tensor here is a nested Python list of floats. `shape` is a tuple of ints.

| Function | Signature | Behaviour |
|---|---|---|
| `shape` | `shape(x) -> tuple[int, ...]` | the shape of a nested list; `()` for a scalar |
| `flatten` | `flatten(x) -> list[float]` | all numbers, row-major |
| `reshape` | `reshape(x, dims: tuple[int, ...]) -> list` | same numbers, new shape; `ValueError` if the sizes do not match |
| `transpose` | `transpose(x) -> list[list[float]]` | 2D only; `ValueError` if not 2D |
| `broadcast_add` | `broadcast_add(x, y) -> list` | `(B, d) + (d,)`; `ValueError` on shape mismatch |

## autograd.py - chapter 19

| Class / Function | Signature | Behaviour |
|---|---|---|
| `Value` | `Value(data: float)` | holds `.data` (float), `.grad` (float, 0.0), `._backward` (callable); operators `+ - * **` and unary `-` build a graph; `backward()` fills `.grad` for every node in the graph; `backward()` seeds the output's gradient with 1.0, zeroes every `.grad` in the graph before walking, then accumulates into `.grad` with `+=` so a value used twice receives the sum of both paths |

## nn.py - chapters 18, 21, 22

| Function / Class | Signature | Behaviour |
|---|---|---|
| `relu` | `relu(x: list[float]) -> list[float]` | elementwise `max(0, v)` |
| `sigmoid` | `sigmoid(x: list[float]) -> list[float]` | elementwise `1 / (1 + exp(-v))`, computed stably |
| `forward` | `forward(x: list[float], W: list[list[float]], b: list[float]) -> list[float]` | one dense layer: `matvec(W, x) + b` |
| `MLP` | `MLP(sizes: list[int], seed: int = 0)` | sizes = `[in, hidden..., out]`; seeded random init so runs are reproducible; `.forward(x)`, `.train(data, steps, learning_rate)` |
| `MLP.forward` | `forward(self, x: list[float]) -> list[float]` | the network's output for one input |
| `MLP.train` | `train(self, data: list[tuple[list[float], float]], steps: int, learning_rate: float) -> list[float]` | trains on `(input, target)` pairs, returns the loss per step |
| `two_layer` | `two_layer(x: list[float], W1, b1, W2, b2) -> list[float]` | hidden layer then output layer, with ReLU between |
| `hidden_activations` | `hidden_activations(x: list[float], W1, b1) -> list[float]` | the hidden layer's output, so the learner can look at what the network built |

## tokenizer.py - chapter 23

| Function | Signature | Behaviour |
|---|---|---|
| `byte_tokens` | `byte_tokens(text: str) -> list[int]` | the UTF-8 bytes as ints, 0-255; never fails on any input |
| `word_tokens` | `word_tokens(text: str) -> list[str]` | lowercased, split on non-alphanumeric, empty pieces dropped |
| `build_vocab` | `build_vocab(texts: list[str]) -> dict[str, int]` | word -> id in first-seen order, ids starting at 0 |
| `encode` | `encode(text: str, vocab: dict[str, int]) -> list[int]` | word ids; unknown words are skipped (say so) |
| `decode` | `decode(ids: list[int], vocab: dict[str, int]) -> str` | ids back to text, joined by spaces; `ValueError` if an id is not in the vocabulary (a round trip must not silently drop content) |

## transformer.py - chapters 24-29

| Function | Signature | Behaviour |
|---|---|---|
| `embedding_lookup` | `embedding_lookup(ids: list[int], table: list[list[float]]) -> list[list[float]]` | one row of the embedding table per id |
| `cosine_similarity` | `cosine_similarity(a: list[float], b: list[float]) -> float` | `dot(a, b) / (norm(a) * norm(b))`; `ValueError` on a zero vector |
| `mean_pool` | `mean_pool(vectors: list[list[float]]) -> list[float]` | the component-wise mean |
| `attention_scores` | `attention_scores(q: list[float], k: list[list[float]], scale: float) -> list[float]` | one scaled dot product per key |
| `attention` | `attention(q: list[float], k: list[list[float]], v: list[list[float]]) -> list[float]` | softmax-weighted sum of the values |
| `causal_mask` | `causal_mask(n: int) -> list[list[float]]` | `n x n`, 0.0 below the diagonal and a large negative number above it |
| `split_heads` | `split_heads(x: list[list[float]], num_heads: int) -> list[list[list[float]]]` | split the last axis into `num_heads` heads |
| `merge_heads` | `merge_heads(heads: list[list[list[float]]]) -> list[list[float]]` | the inverse |
| `multi_head_attention` | `multi_head_attention(x: list[list[float]], Wq, Wk, Wv, Wo, num_heads: int) -> list[list[float]]` | one attention layer with `num_heads` heads |
| `layer_norm` | `layer_norm(x: list[float], gamma: list[float], beta: list[float]) -> list[float]` | zero mean, unit variance, then scale and shift |
| `feed_forward` | `feed_forward(x: list[float], W1, b1, W2, b2) -> list[float]` | two linear maps with a ReLU between |
| `transformer_block` | `transformer_block(x: list[list[float]], params: dict) -> list[list[float]]` | attention, residual, layer norm, feed-forward, residual, layer norm |
| `next_token_pairs` | `next_token_pairs(ids: list[int]) -> list[tuple[int, int]]` | every (input id, next id) pair from one sequence |
| `sequence_loss` | `sequence_loss(logits: list[list[float]], targets: list[int]) -> float` | mean cross entropy over the positions |
| `train_lm` | `train_lm(model: dict, data: list[list[int]], steps: int, learning_rate: float) -> list[float]` | next-token training; returns the loss per step |
| `sample_token` | `sample_token(logits: list[float], temperature: float = 1.0, top_p: float = 1.0, rng=None) -> int` | temperature, then top-p truncation, then a sample; `ValueError` if temperature < 0 or if top_p is not in (0, 1]; `temperature == 0` means greedy (return the argmax index, ties broken by the lowest index) |
| `generate` | `generate(model: dict, prompt_ids: list[int], steps: int, temperature: float = 1.0, top_p: float = 1.0, rng=None) -> list[int]` | feed the prompt, sample, append, repeat; same temperature and top-p rules as `sample_token` |

## decision.py - chapters 30, 32, 34

| Function | Signature | Behaviour |
|---|---|---|
| `decision_head` | `decision_head(logits: list[float]) -> list[float]` | softmax over the option set; the same math as Chapter 09 |
| `decide` | `decide(probabilities: list[float], options: list[str], threshold: float = 0.5) -> dict` | the top option if its probability clears the threshold, else abstain; returns `{"choice", "confidence", "abstained"}` |
| `state_to_features` | `state_to_features(state: dict, schema: list[str]) -> list[float]` | one feature per schema field, in schema order: 1.0 when the field is present and truthy, else 0.0 |

## metrics.py - chapters 31, 33

| Function | Signature | Behaviour |
|---|---|---|
| `brier_score` | `brier_score(probs: list[float], labels: list[int]) -> float` | mean squared error of the probabilities; `ValueError` on length mismatch |
| `ece` | `ece(probs: list[float], labels: list[int], bins: int = 10) -> float` | expected calibration error, weighted by bin count |
| `reliability_curve` | `reliability_curve(probs: list[float], labels: list[int], bins: int = 10) -> list[tuple[float, float, int]]` | per bin: (mean confidence, accuracy, count) |
| `agreement` | `agreement(preds_a: list[int], preds_b: list[int]) -> float` | fraction where the two providers agree; `ValueError` if lengths differ or the input is empty |

## Rules for every chapter

- Functions are pure, deterministic, and raise `ValueError` for shape mismatches.
- Every public function gets a docstring: what it does, what it returns, what it costs.
- Tests live in `labkit/tests/test_<module>.py` and use `unittest`.
- **Sampling convention (chapter 29).** Sort candidates by probability descending, ties broken by the lowest index. Draw `u = rng.random()`. Take the first candidate whose cumulative probability exceeds `u`. Renormalise the kept set. Fixing this convention is what makes seeded sample counts reproducible; an implementation that walks candidates in index order produces different counts from the same seed, which is a convention difference, not a bug.
