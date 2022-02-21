"""Exercise 05 - list functions, test document."""

__author__ = "730382185"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_1():
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_2():
    assert only_evens([1, 5, 3]) == []


def test_only_evens_3():
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_sub_1():
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_2():
    assert sub([1, 5, 3, 8, 9, 10, 54], 2, 5) == [3, 8, 9]


def test_sub_3():
    assert sub([], 1, 3) == []


def test_sub_4():
    assert sub([1, 5, 3, 8, 9, 10, 54], 8, 10) == []


def test_sub_5():
    assert sub([1, 5, 3, 8, 9, 10, 54], 0, 0) == []


def test_concat_1():
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]