"""tensors.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def shape(x):
    """the shape of a nested list; `()` for a scalar

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('shape')


def flatten(x):
    """all numbers, row-major

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('flatten')


def reshape(x, dims: tuple[int, ...]):
    """same numbers, new shape; `ValueError` if the sizes do not match

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('reshape')


def transpose(x):
    """2D only; `ValueError` if not 2D

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('transpose')


def broadcast_add(x, y):
    """`(B, d) + (d,)`; `ValueError` on shape mismatch

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('broadcast_add')

