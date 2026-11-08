"""tokenizer.py - built chapter by chapter in Book 1 - AI Foundations.

Every function here is written by the learner. The docstrings carry the
contract; the bodies are TODO. Stdlib only.
"""

from __future__ import annotations


def byte_tokens(text: str):
    """the UTF-8 bytes as ints, 0-255; never fails on any input

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('byte_tokens')


def word_tokens(text: str):
    """lowercased, split on non-alphanumeric, empty pieces dropped

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('word_tokens')


def build_vocab(texts: list[str]):
    """word -> id in first-seen order, ids starting at 0

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('build_vocab')


def encode(text: str, vocab: dict[str, int]):
    """word ids; unknown words are skipped (say so)

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('encode')


def decode(ids: list[int], vocab: dict[str, int]):
    """ids back to text, joined by spaces; `ValueError` if an id is not in the vocabulary (a round trip must not silently drop content)

    TODO: implement this. The behaviour above is the contract.
    """
    raise NotImplementedError('decode')

