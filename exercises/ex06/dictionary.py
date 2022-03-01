"""Exercise 06 - dictionary functions."""

__author__ = "730382185"


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """Reverse the values and keys in a dictionary."""
    a_dict_values = a_dict.values()
    a_dict_values_list = list(a_dict_values)
    k = 0
    m = 0
    if len(a_dict_values_list) == 1:
        new_dict = {}
        for key in a_dict:
            new_dict[a_dict[key]] = key
    else:
        while k < len(a_dict_values_list):
            if k == m:
                m = m + 1
                if m == len(a_dict_values_list):
                    m = m - 2
                else:
                    m = m
            else:
                k = k
                m = m
            while m < len(a_dict_values_list):
                if a_dict_values_list[k] == a_dict_values_list[m]:
                    raise KeyError("identical keys not allowed")
                else:
                    m = m + 1
            k = k + 1
        new_dict = {}
        for key in a_dict:
            new_dict[a_dict[key]] = key
    return(new_dict)


def favorite_color(b_dict: dict[str, str]) -> str:
    """Return all items in a list between two indices."""
    new_dict = {}
    for key in b_dict:
        if b_dict[key] not in new_dict:
            new_dict[b_dict[key]] = 1
        else:
            new_dict[b_dict[key]] += 1
    fav_color_keys = new_dict.keys()
    fav_color_keys_list = list(fav_color_keys)
    fav_color_values = new_dict.values()
    fav_color_values_list = list(fav_color_values)
    i = 0
    j = 0
    if len(fav_color_keys_list) == 0:
        fav_color = ""
    else:
        while i < len(fav_color_values_list):
            if i == j:
                j = j + 1
                if j == len(fav_color_values_list):
                    j = j - 2
                else:
                    j = j
            else:
                i = i
                j = j
            while j < len(fav_color_values_list):
                if fav_color_values_list[i] == fav_color_values_list[j]:
                    return(fav_color_keys_list[0])
                else:
                    j = j + 1
            i = i + 1
        max_color_value = max(fav_color_values_list)
        fav_color = ""
        for key in new_dict:
            if new_dict[key] == max_color_value:
                fav_color = key
    return(fav_color)


def count(a_list: list[str]) -> dict[str, int]:
    """Combine a pair of lists sequentially."""
    new_dict = {}
    i = 0
    while i < len(a_list):
        if a_list[i] in new_dict:
            new_dict[a_list[i]] += 1
        else:
            new_dict[a_list[i]] = 1
        i = i + 1
    return(new_dict)