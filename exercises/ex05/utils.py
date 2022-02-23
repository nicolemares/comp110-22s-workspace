"""EX05- 'list' utility functions."""

__author__ = "730391824"


def only_evens(given: list[int]) -> list[int]:
    """Function that returns only even numbers from a list."""
    i: int = 0
    evens: list[int] = []
    while len(given) > i:
        if given[i] % 2 == 0:
            evens.append(given[i])
        i = i + 1
    return evens


def sub(given: list[int], start: int, end: int) -> list[int]:
    """Fucntion that returns the index indicated (start and end) of list."""
    a_list: list[int] = []
    if len(given) == 0 or len(given) < start or len(given) >= end:
        return a_list
    if start < 0:
        a_list.append(given[0])
    else:
        a_list.append(given[start])
    if end >= len(given):
        end = len(given) - 2
        a_list.append(given[end])
    else:
        a_list.append(given[end])
    return a_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Function that return a list comprised on list one and list two."""
    i: int = 0
    together: list[int] = []
    together = list_one
    while len(list_two) > i:
        together.append(list_two[i])
        i += 1
    return together