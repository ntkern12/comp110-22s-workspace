"""Exercise 05 - list functions, test document."""

__author__ = "730382185"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_1():
    """Test with evens."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_2():
    """Test without evens."""
    assert only_evens([1, 5, 3]) == []


def test_only_evens_3():
    """Test with only evens."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_only_evens_4():
    """Test with empty list."""
    assert only_evens([]) == []


def test_sub_1():
    """Test with short list."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_2():
    """Test with long list."""
    assert sub([1, 5, 3, 8, 9, 10, 54], 2, 5) == [3, 8, 9]


def test_sub_3():
    """Test for inputting empty list."""
    assert sub([], 1, 3) == []


def test_sub_4():
    """Test for incorrect indices."""
    assert sub([1, 5, 3, 8, 9, 10, 54], 8, 10) == []


def test_sub_5():
    """Test for too small indices."""
    assert sub([1, 5, 3, 8, 9, 10, 54], 0, 0) == []


def test_sub_6():
    """Test for inputting empty list and incorrect indices."""
    assert sub([], 10, 0) == []


def test_concat_1():
    """Test with only numbers."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_2():
    """Test with numbers and letters."""
    assert concat(["a", "b", "c"], [1, 2, 3]) == ["a", "b", "c", 1, 2, 3]


def test_concat_3():
    """Test with empty lists."""
    assert concat([], []) == []