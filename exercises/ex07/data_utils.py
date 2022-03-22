"""Dictionary related utility functions."""

__author__ = "730382185"

# Define your functions below

# read_csv_rows
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


# column_values


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


# columnar


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


# head


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Return values from first N rows of a table"""
    result: dict[str, list[str]] = {}
    for column in table:
        n_row: list[str] = []
        for i in range(N):
            col = table[column]
            n_row.append(col[i])
        result[column] = n_row
    return result


# select


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Return values of a certain column."""
    result: dict[str, list[str]] = {}
    for col in col_names:
        result[col] = table[col]
    return result


# concat
            

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Return values from first N rows of a table."""
    result: dict[str, list[str]] = {}
    for column1 in table1:
        result[column1] = table1[column1]
    for column2 in table2:
        if column2 in result:
            result[column2] += table2[column2]
        else:
            result[column2] = table2[column2]
    return result


# count


def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result