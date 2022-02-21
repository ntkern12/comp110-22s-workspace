"""Exercise 05 - list functions."""

__author__ = "730382185"


def only_evens(a_list: list) -> list:
    """Return all items in a list that are even numbers."""
    new_list = []
    i = 0
    while i < len(a_list):
        if a_list[i] % 2 == 0:
            new_list.append(a_list[i])
            i = i + 1
        else:
            i = i + 1
    return(new_list)


def sub(a_list_2: list, start: int, end: int) -> list:
    """Return all items in a list between two indices."""
    new_list_2 = []
    j = 0
    while j < len(a_list_2):
        if len(a_list_2) == 0 or start > len(a_list_2) or end <= 0:
            return(new_list_2)
        elif j < end and j >= start:
            new_list_2.append(a_list_2[j])
            j = j + 1
        else:
            j = j + 1
    return(new_list_2)


def concat(a_list_3: list, b_list: list) -> list:
    """Combine a pair of lists sequentially."""
    new_list_3 = []
    k = 0
    while k < len(a_list_3):
        new_list_3.append(a_list_3[k])
        k = k + 1
    m = 0
    while m < len(b_list):
        new_list_3.append(b_list[m])
        m = m + 1
    return(new_list_3)