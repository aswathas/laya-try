"""data.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def rule_scores(features: list[list[float]], weights: list[float]):
    """one score per example: `dot(features[i], weights)`; `ValueError` on any length mismatch

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('rule_scores')


def accuracy(preds: list[int], labels: list[int]):
    """fraction correct; `ValueError` if lengths differ or the input is empty (a score over zero examples is not a score)

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('accuracy')


def split(data: list, train_ratio: float = 0.8, seed: int = 0):
    """deterministic split via `random.Random(seed)`; returns `(train, test)`; `ValueError` if `train_ratio` not in (0, 1)

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('split')


def batches(data: list, size: int):
    """consecutive chunks of `size`; the last chunk may be shorter; `ValueError` if `size <= 0`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('batches')


def polynomial_features(x: float, degree: int):
    """`[x, x^2, ..., x^degree]`; `ValueError` if `degree < 1`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('polynomial_features')


def encode_labels(labels: list[str]):
    """labels to contiguous ids in first-seen order

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('encode_labels')


def decode_labels(encoding: dict[str, int]):
    """the inverse map

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('decode_labels')


def count_features(texts: list[str], vocab: list[str]):
    """per text, the count of each vocabulary word (case-insensitive, whole words)

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('count_features')

