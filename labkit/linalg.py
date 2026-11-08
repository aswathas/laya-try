"""linalg.py - vectors and matrices.

Chapter 01. You write these. The docstrings say what each one must do;
the bodies are yours.

Convention: a vector is a plain Python list of floats. A column vector
is written (d, 1) in shape terms but stored as a list of d floats.
"""

from __future__ import annotations


def add(a, b):
    """Elementwise sum of two equal-length vectors.

    Returns: list[float] of the same length.
    Raises: ValueError if the lengths differ.
    """
    raise NotImplementedError("chapter 01, task 1")


def scale(a, k):
    """Multiply every element of a by the scalar k.

    Returns: list[float] of the same length.
    """
    raise NotImplementedError("chapter 01, task 2")


def dot(a, b):
    """Dot product of two equal-length vectors: sum(a[i] * b[i]).

    Returns: float.
    Raises: ValueError if the lengths differ.
    """
    raise NotImplementedError("chapter 01, task 3")


def norm(a):
    """Euclidean length of a vector: sqrt(sum(x * x for x in a)).

    Returns: float.
    """
    raise NotImplementedError("chapter 01, task 4")
