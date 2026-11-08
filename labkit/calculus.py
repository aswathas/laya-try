"""calculus.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def derivative(f, x: float, h: float = 1e-7):
    """central difference `(f(x+h) - f(x-h)) / (2h)`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('derivative')


def square(x: float):
    """`x * x`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('square')


def cube(x: float):
    """`x * x * x`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('cube')


def numeric_gradient(f, xs: list[float], h: float = 1e-7):
    """one partial derivative per entry of `xs`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('numeric_gradient')


def compose(f, g):
    """returns `lambda x: f(g(x))`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('compose')


def chain_grad(f, g, x: float, h: float = 1e-7):
    """numeric derivative of `f(g(x))`

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('chain_grad')

