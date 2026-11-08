"""optim.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def squared_error(pred: float, target: float):
    """`(pred - target) ** 2`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('squared_error')


def mean_squared_error(preds: list[float], targets: list[float]):
    """mean of squared errors; `ValueError` if lengths differ or empty

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('mean_squared_error')


def train_linear(features: list[list[float]], targets: list[float], learning_rate: float = 0.01, steps: int = 1000):
    """plain gradient descent on `w.x + b`; returns `(weights, bias)`; `ValueError` on length mismatch

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('train_linear')


def gradient_descent(grad_fn, start: list[float], learning_rate: float, steps: int):
    """generic loop: `x <- x - lr * grad_fn(x)`; `ValueError` if `steps < 0`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('gradient_descent')


def momentum_step(velocity: list[float], grad: list[float], learning_rate: float, momentum: float = 0.9):
    """`v = momentum * v + grad`, returns the new velocity

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('momentum_step')

