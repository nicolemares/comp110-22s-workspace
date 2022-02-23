"""Example of function that searches through a list"""

# define a fucntion named contains
# Two parameters
# 1. needle- the string we are starting for
# 2. haystack - the list we are searching through
# Algorithm:
#   for each item in the haystack
#       Test if it is equal to the needle
#           if so, return True
# after testing all items, return false beacuse not found
# returns true if needle is in haystack, false otherwise


def main() -> None:
    print(contains("one", ["one", "two", "three"]))


def contains(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False 


if __name__ == "__main__":
    main()
