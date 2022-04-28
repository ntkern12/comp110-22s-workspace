"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

# from pandas import NA

__author__ = "730382185"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head is not None and head.next is not None:
        return last(head.next)
    else: 
        return int(f"{head.data}")


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of a Linked List at a given index, or raises a ValueError if the index does not exist."""
    if head is not None and index != 0 and head.next is not None:
        return value_at(head.next, index - 1)
    elif head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return int(f"{head.data}")
    elif head.next is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        return int(f"{head.data}")


def max(head: Optional[Node]) -> int:
    """Returns the maximum data of a Linked List, or raises a ValueError if size None."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        return int(f"{head.data}")


def linkify(items: list[int]) -> Optional[Node]:
    """Returns a linked list from a list[int]."""
    if len(items) != 0:
        new_items = items
        link_items: Node = Node(0, None)
        link_items.data = new_items[(-len(new_items))]
        del new_items[(-len(new_items))]
        link_items.next = linkify(new_items)
        return link_items
    else:
        return None
    

def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scale a linked list by a value."""
    if head is not None:
        head.data = head.data * factor
        head.next = scale(head.next, factor)
        return head
    else:
        return head


print(scale(linkify([1, 2, 3]), 2))
print(scale(linkify([1]), 2))