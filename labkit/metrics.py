"""metrics.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def brier_score(probs: list[float], labels: list[int]):
    """mean squared error of the probabilities; `ValueError` on length mismatch

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('brier_score')


def ece(probs: list[float], labels: list[int], bins: int = 10):
    """expected calibration error, weighted by bin count

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('ece')


def reliability_curve(probs: list[float], labels: list[int], bins: int = 10):
    """per bin: (mean confidence, accuracy, count)

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('reliability_curve')


def agreement(preds_a: list[int], preds_b: list[int]):
    """fraction where the two providers agree

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('agreement')

