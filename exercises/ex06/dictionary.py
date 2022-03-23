"""Ex06 - Dictionary Functions."""

__author__ = "730391824"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Invert the key and value."""
    result: dict[str, str] = {}
    for key in given:
        if given[key] in result:
            raise KeyError("Repeating Keys.")
        result[given[key]] = key
    return result


def favorite_color(given: dict[str, str]) -> str:
    """Return color that most often showed up."""
    count: dict[str, int] = {}
    result: str = ""
    i: int = 0
    for key in given:
        if given[key] in count:
            count[given[key]] += 1
        else:
            count[given[key]] = 1
    for key in count:
        if count[key] > i:
            i = count[key]
            result = key
    return result


def count(given: list[str]) -> dict[str, int]:
    """Return the str that was lsited the most."""
    result: dict[str, int] = {}
    for item in given:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
