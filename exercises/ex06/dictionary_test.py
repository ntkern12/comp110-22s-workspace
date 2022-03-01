"""Exercise 05 - list functions, test document."""

__author__ = "730382185"

from exercises.ex06.dictionary import invert, favorite_color, count
import pytest


def test_invert_1():
    """Test with letters."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_2():
    """Test with no elements."""
    assert invert({}) == {}


def test_invert_3():
    """Test with one element."""
    assert invert({'a': 'z'}) == {'z': 'a'}


with pytest.raises(KeyError):
    invert({'kris': 'jordan', 'michael': 'jordan'})


def test_favorite_color_1():
    """Test with 2 colors."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == 'blue'


def test_favorite_color_2():
    """Test with even numbers of colors."""
    assert favorite_color({'Al': 'green', 'Bill': 'red', 'Charlie': 'yellow', 'David': 'brown'}) == 'green'


def test_favorite_color_3():
    """Test with even numbers of colors."""
    assert favorite_color({'Al': 'green', 'Charlie': 'yellow'}) == 'green'


def test_favorite_color_4():
    """Test with empty dictionary."""
    assert favorite_color({}) == ''


def test_favorite_color_5():
    """Test with 2 colors."""
    assert favorite_color({"Marc": "green", "Mark": "green", "Marcy": "yellow", "Ezri": "green", "Kris": "green"}) == 'green'


def test_count_1():
    """Test with letters."""
    assert count(["a", "b", "c", "a", "a", "b"]) == {'a': 3, 'b': 2, 'c': 1}


def test_count_2():
    """Test with empty list."""
    assert count([]) == {}


def test_count_3():
    """Test with equal numbers, multiple unique."""
    assert count(["a", "b", "c", "a", "a", "b", "b", "c", "c"]) == {'a': 3, 'b': 3, 'c': 3}