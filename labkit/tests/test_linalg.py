"""Checks for linalg.py. You write the assertions.

Each body raises NotImplementedError until you write it, so the suite fails
loudly instead of reporting a fake green.

Run: python -m unittest discover -s labkit/tests -v
"""

import unittest

from labkit import linalg


class TestLinalg(unittest.TestCase):
    def test_add(self):
        # TODO: add([1, 2], [3, 4]) == [4, 6]
        raise NotImplementedError("chapter 01, task 1")

    def test_add_length_mismatch(self):
        # TODO: add([1, 2], [3]) must raise ValueError
        raise NotImplementedError("chapter 01, task 1")

    def test_scale(self):
        # TODO: scale([1, 2, 3], 2) == [2, 4, 6]
        raise NotImplementedError("chapter 01, task 2")

    def test_dot(self):
        # TODO: dot([1, 2], [3, 4]) == 11
        raise NotImplementedError("chapter 01, task 3")

    def test_dot_length_mismatch(self):
        # TODO: dot([1, 2], [3]) must raise ValueError
        raise NotImplementedError("chapter 01, task 3")

    def test_norm(self):
        # TODO: norm([3, 4]) == 5
        raise NotImplementedError("chapter 01, task 4")


if __name__ == "__main__":
    unittest.main()
