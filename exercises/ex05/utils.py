"""Exercise 05 - list functions."""

__author__ = "730382185"


def only_evens(a_list: list) -> list:
    new_list = []
    i = 0
    while i < len(a_list):
        if a_list[i] % 2 == 0:
            new_list.append(a_list[i])
            i = i + 1
        else:
            i = i + 1
    return(new_list)


list_a = [1, 2, 3]
list_b = [1, 5, 3]
list_c = [4, 4, 4]

print(only_evens(list_a))
print(only_evens(list_b))
print(only_evens(list_c))


def sub(a_list_2: list, start: int, end: int) -> list:
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


list_a_2 = [10, 20, 30, 40]
list_b_2 = [1, 5, 3, 8, 9, 10, 54]
list_c_2 = []

print(sub(list_a_2, 1, 3))
print(sub(list_b_2, 2, 5))
print(sub(list_c_2, 1, 3))
print(sub(list_b_2, 8, 10))
print(sub(list_b_2, 0, 0))


def concat(a_list_3: list, b_list: list) -> list:
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


list_a_3 = [1, 2, 3]
list_b_3 = [4, 5, 6]

print(concat(list_a_3, list_b_3))