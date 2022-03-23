"""Dictionary related utility functions."""

__author__ = "730391824"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file.
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read ech row of csv line by line.
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oreiented table to column-orientated table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce table with only first n rows of data for each column."""
    result: dict[str, list[str]] = {}
    for columns in column_table:
        list_of_columns: list[str] = []
        i: int = 0
        if n > len(column_table[columns]):
            n = len(column_table[columns])
        while i < n:
            list_of_columns.append(column_table[columns][i])
            i += 1
        result[columns] = list_of_columns
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce table with specfic subset of orginal columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        if column in column_table:
            result[column] = column_table[column]
    return result


def concat(column_table_one: dict[str, list[str]], column_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combining tables, making sure to not repeat keys.""" 
    result: dict[str, list[str]] = {}
    for columns in column_table_one:
        result[columns] = column_table_one[columns]
    for columns in column_table_two:
        if columns in result:
            result[columns] = column_table_one[columns] + column_table_two[columns]
        else:
            result[columns] = column_table_two[columns]
    return result


def count(values_list: list[str]) -> dict[str, int]:
    """Given a list, make dictionary counting amount of times it is in list."""
    result: dict[str, int] = {}
    for item in values_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result