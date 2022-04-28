"""Tests for linked list utils."""

# from itsdangerous import NoneAlgorithm
import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730382185"


# Test Last Function
def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


# Test Value_At Function
def test_value_at_empty() -> None:
    """Value_at index 0 of an empty Linked List should raise a IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_0() -> None:
    """Value_at index 0 of an non-empty Linked List should return the first value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_value_at_1() -> None:
    """Value_at index 1 of an non-empty Linked List should return the second value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_value_at_2() -> None:
    """Value_at index 2 of an non-empty Linked List should return the third value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_value_at_3() -> None:
    """Value_at index 3 of an non-empty length-3 Linked List should return an IndexError."""
    linked_list = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 3)


def test_value_at_4() -> None:
    """Value_at index 3 of an non-empty length-3 Linked List should return an IndexError."""
    linked_list = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 4)


# Test Max Function
def test_max_empty() -> None:
    """Max of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_1() -> None:
    """Max of a non-empty list should return its maximum data value."""
    assert max(Node(10, Node(20, Node(30, None)))) == 30


def test_max_2() -> None:
    """Max of a non-empty list should return its maximum data value."""
    assert max(Node(10, Node(30, Node(20, None)))) == 30


def test_max_3() -> None:
    """Max of a non-empty list should return its maximum data value."""
    assert max(Node(30, Node(20, Node(10, None)))) == 30


# Test Linkify Function
def test_linkify_1() -> None:
    """Linkify should return a new linked list based off of a list[int]."""
    assert linkify([1, 2, 3])


def test_linkify_2() -> None:
    """Linkify should return a None from a empty list[int]."""
    assert linkify([]) is None


# Test Scale Function
def test_scale_1() -> None:
    """Scale of a non-empty list should return the scale version of the linked list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert scale(linked_list, 2) == Node(2, Node(4, Node(6, None)))


def test_scale_2() -> None:
    """Scale of a non-empty list should return the scale version of the linked list."""
    linked_list = Node(1, None)
    assert scale(linked_list, 2) == Node(2, None)