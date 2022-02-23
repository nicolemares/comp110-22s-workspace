"""list test for ex05."""

__author__ = "730391824"

from utils import only_evens, sub, concat


def test_only_evens_many_items() -> None:
    """Test that only returns even values."""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]


def test_only_evens_many_negative_items() -> None:
    """Test that only returns even negative values."""
    assert only_evens([-8, -9, -3, -5, -6, -7]) == [-8, -6]


def test_only_evens_blank() -> None:
    """Test that returns balnk if given blank list."""
    assert only_evens([]) == []


def test_sub_within_len() -> None:
    """Test that returns correct start and end."""
    given: list[int] = [9, 8, 7, 6, 5, 4, 3]
    start: int = 2
    end: int = 5
    assert sub(given, start, end) == [7, 4]


def test_sub_negtive_start() -> None:
    """Test that returns index 0 when start is negative"""
    given: list[int] = [9, 8, 7, 6, 5, 4, 3]
    start: int = -2
    end: int = 4
    assert sub(given, start, end) == [9, 5]


def test_sub_too_high_end() -> None:
    """Test that returns second to last item when end is over len."""
    given: list[int] = [9, 8, 7, 6, 5, 4, 3]
    start: int = 2
    end: int = 8
    assert sub(given, start, end) == [7, 4]


def test_sub_empty() -> None:
    """Test that returns empty list when given empty."""
    given: list[int] = []
    start: int = 2
    end: int = 4
    assert sub(given, start, end) == []


def test_concat_one_empty_list() -> None:
    """Test that returns only not empty list."""
    list_one: list[int] = [6, 6, 6]
    list_two: list[int] = []
    assert concat(list_one, list_two) == [6, 6, 6]


def test_concat_two_empty_lists() -> None:
    """Test that returns black list."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_concat_mulitple_items() -> None:
    """Test that returns all items together."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_mulitple_items_two() -> None:
    """Test that returns all items together."""
    list_one: list[int] = [2, 4, 8, 9, 3]
    list_two: list[int] = [5, 6, 7]
    assert concat(list_one, list_two) == [2, 4, 8, 9, 3, 5, 6, 7]