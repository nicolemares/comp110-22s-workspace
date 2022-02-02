"""Exercise 03 - Wordle."""

__author__ = "730391824"


def contains_char(word: str, letter: str) -> bool:
    """if second string (letter) is found within first string (word)."""
    assert len(letter) == 1
    if (letter == word[0]) or (letter == word[1]) or (letter == word[2]) or (letter == word[3]) or (letter == word[4]):
        return True
    else:
        return False