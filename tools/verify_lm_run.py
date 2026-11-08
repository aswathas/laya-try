"""Reproduce the Chapter 28 tiny language-model training run.

The chapter states a setup but leaves the update rule and the gradient-averaging
convention implicit, and two different curves were produced from it. This script
runs the setup under each plausible convention so the chapter can state the one
that is actually reproducible.

    python tools/verify_lm_run.py
"""
from __future__ import annotations

import math
import random

VOCAB = 2
DIM = 2
SEQ = [0, 1, 0, 1, 0, 1]
LR = 0.5
STEPS = 200
CHECK = [0, 20, 25, 50, 100, 199]


def init():
    rng = random.Random(0)
    embed = [[rng.gauss(0.0, 0.01) for _ in range(DIM)] for _ in range(VOCAB)]
    unembed = [[rng.gauss(0.0, 0.01) for _ in range(DIM)] for _ in range(VOCAB)]
    bias = [rng.gauss(0.0, 0.01) for _ in range(VOCAB)]
    return embed, unembed, bias


def softmax(z):
    m = max(z)
    e = [math.exp(v - m) for v in z]
    s = sum(e)
    return [v / s for v in e]


def loss_of(embed, unembed, bias):
    total = 0.0
    for x, y in zip(SEQ, SEQ[1:]):
        logits = [sum(unembed[j][k] * embed[x][k] for k in range(DIM)) + bias[j] for j in range(VOCAB)]
        p = softmax(logits)
        total += -math.log(p[y])
    return total / (len(SEQ) - 1)


def train(divide_by_positions: bool, record_after_update: bool):
    embed, unembed, bias = init()
    losses = []
    for _ in range(STEPS):
        if not record_after_update:
            losses.append(loss_of(embed, unembed, bias))
        g_embed = [[0.0] * DIM for _ in range(VOCAB)]
        g_unembed = [[0.0] * DIM for _ in range(VOCAB)]
        g_bias = [0.0] * VOCAB
        scale = 1.0 / (len(SEQ) - 1) if divide_by_positions else 1.0
        for x, y in zip(SEQ, SEQ[1:]):
            logits = [sum(unembed[j][k] * embed[x][k] for k in range(DIM)) + bias[j] for j in range(VOCAB)]
            p = softmax(logits)
            delta = [p[j] - (1.0 if j == y else 0.0) for j in range(VOCAB)]
            for j in range(VOCAB):
                for k in range(DIM):
                    g_unembed[j][k] += scale * delta[j] * embed[x][k]
                g_bias[j] += scale * delta[j]
            for k in range(DIM):
                g_embed[x][k] += scale * sum(unembed[j][k] * delta[j] for j in range(VOCAB))
        for t in range(VOCAB):
            for k in range(DIM):
                embed[t][k] -= LR * g_embed[t][k]
                unembed[t][k] -= LR * g_unembed[t][k]
        for j in range(VOCAB):
            bias[j] -= LR * g_bias[j]
        if record_after_update:
            losses.append(loss_of(embed, unembed, bias))
    return losses


def main() -> int:
    variants = [
        ("mean gradient over positions, loss recorded before update", True, False),
        ("sum gradient over positions, loss recorded before update", False, False),
        ("mean gradient over positions, loss recorded after update", True, True),
        ("sum gradient over positions, loss recorded after update", False, True),
    ]
    print(f"chapter table claims: {[0.6916, 0.3688, 0.1107, 0.0097, 0.0027, 0.0010]} at {CHECK}\n")
    for label, div, after in variants:
        losses = train(div, after)
        vals = [round(losses[i], 4) for i in CHECK]
        print(f"{label}\n    -> {vals}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
