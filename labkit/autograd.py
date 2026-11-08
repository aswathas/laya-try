"""autograd.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


class Value:
    """holds `.data` (float), `.grad` (float, 0.0), `._backward` (callable); operators `+ - * **` and unary `-` build a graph; `backward()` fills `.grad` for every node in the graph; `backward()` seeds the output's gradient with 1.0, zeroes every `.grad` in the graph before walking, then accumulates into `.grad` with `+=` so a value used twice receives the sum of both paths

    TODO: implement this class.
    """

    # TODO: attributes, methods and their behaviour come from the contract.
    raise NotImplementedError('Value')
