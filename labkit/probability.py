"""probability.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def mean(xs: list[float]):
    """arithmetic mean; `ValueError` on empty input

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('mean')


def variance(xs: list[float]):
    """population variance, mean of squared deviations

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('variance')


def binomial_pmf(n: int, p: float, k: int):
    """probability of exactly `k` successes

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('binomial_pmf')


def normal_pdf(x: float, mu: float = 0.0, sigma: float = 1.0):
    """density of the normal

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('normal_pdf')


def entropy(p: list[float]):
    """`-sum(q * ln(q))`, nats; terms with `q == 0` contribute 0

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('entropy')


def cross_entropy(p: list[float], q: list[float]):
    """`-sum(p[i] * ln(q[i]))`; `ValueError` on length mismatch

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('cross_entropy')


def kl_divergence(p: list[float], q: list[float]):
    """`sum(p[i] * ln(p[i] / q[i]))`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('kl_divergence')


def log_sum_exp(xs: list[float]):
    """`ln(sum(exp(x)))`, computed stably

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('log_sum_exp')


def softmax(logits: list[float], temperature: float = 1.0):
    """stable softmax of `logits / temperature`; `ValueError` if `temperature <= 0`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('softmax')


def cross_entropy_from_logits(logits: list[float], target_index: int):
    """`-ln(softmax(logits)[target_index])`, computed stably

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('cross_entropy_from_logits')

