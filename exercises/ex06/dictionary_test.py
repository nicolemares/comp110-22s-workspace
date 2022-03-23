"""Tests for dictionary- ex06."""

__author__ = "730391824"

import pytest

from dictionary import favorite_color, count, invert


def test_invert_empty() -> None:
    """Empty dict."""
    assert invert({}) == {}


def test_invert_normal() -> None:
    """No repeating keys."""
    assert invert({"smile": "happy", "frown": "sad"}) == {"happy": "smile", "sad": "frown"}


def test_invert_repeating_keys() -> None:
    """Repeating keys."""
    with pytest.raises(KeyError):
        given = {'kris': 'jordan', 'michael': 'jordan'}
        invert(given)


def test_favorite_color_empty() -> None:
    """Empty dict."""
    assert favorite_color({}) == ""


def test_favorite_color_two_favorite() -> None:
    """More than 1 favorite color."""
    assert favorite_color({"leo": "blue", "tod": "yellow", "karen": "yellow", "nicole": "blue"}) == "yellow"


def test_favorite_color_one_favorite() -> None:
    """One favorite color."""
    assert favorite_color({"leo": "blue", "tod": "yellow", "nicole": "blue", "jared": "blue"}) == "blue"


def test_count_empty() -> None:
    """Empty dict."""
    assert count({}) == {}


def test_count_all_once() -> None:
    """All only once."""
    assert count(["michael", "erin", "kristin", "nicole", "jacob"]) == {"michael": 1, "erin": 1, "kristin": 1, "nicole": 1, "jacob": 1}


def test_count_multiple_times() -> None:
    """Some counted multiple times."""
    assert count(["michael", "erin", "erin", "kristin", "kristin", "kristin", "nicole", "nicole", "nicole", "nicole", "jacob", "jacob", "jacob", "jacob", "jacob", "jacob"]) == {"michael": 1, "erin": 2, "kristin": 3, "nicole": 4, "jacob": 5}