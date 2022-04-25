"""Tests for linked list utils."""

import pytest
from linked_list import Node, last, value_at, is_equal, max, linkify, scale

__author__ = "730391824"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_is_equal_equal() -> None:
    """Should return True."""
    linked_list = Node(1, Node(2, Node(3, None)))
    other_node = Node(1, Node(2, Node(3, None)))
    assert is_equal(linked_list, other_node) is True


def test_is_equal_not_equal() -> None:
    """Should return False."""
    linked_list = Node(1, Node(2, Node(3, None)))
    other_node = Node(1, Node(2, None))
    assert is_equal(linked_list, other_node) is False


def test_value_at_error() -> None:
    """Should be IndexError."""
    linked_list = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 4)


def test_value_at_within_len() -> None:
    """Should return correct index value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_max_mutiple_nodes() -> None:
    """Should return max node data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_max_one_node() -> None:
    """Should return only data value."""
    linked_list = Node(1, None)
    assert max(linked_list) == 1


def test_linkify_one_item() -> None:
    """Should return one Node from that index."""
    linked_list = [1]
    assert is_equal(linkify(linked_list), Node(1, None))


def test_linkify_multiple_items() -> None:
    """Should return nodes from each index."""
    # linked_list_2 = [1, 2, 3]
    assert is_equal(linkify([1, 2, 3]), Node(1, Node(2, Node(3, None))))


def test_scale_negative() -> None:
    """Should reuslt in negative data values in scaled correctly Nodes."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(scale(linked_list, -1), Node(-1, Node(-2, Node(-3, None))))


def test_scale_positive() -> None:
    """Should result in postive data values scaled correctly."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(scale(linked_list, 2), Node(2, Node(4, Node(6, None))))