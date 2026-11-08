"""decision.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def decision_head(logits: list[float]):
    """softmax over the option set; the same math as Chapter 09

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('decision_head')


def decide(probabilities: list[float], options: list[str], threshold: float = 0.5):
    """the top option if its probability clears the threshold, else abstain; returns `{"choice", "confidence", "abstained"}`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('decide')


def state_to_features(state: dict, schema: list[str]):
    """one feature per schema field, in schema order: 1.0 when the field is present and truthy, else 0.0

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('state_to_features')

