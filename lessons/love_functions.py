"""Some examples of tender, loving fucntion definitions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string"""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    i: int = 0
    love_note: str = ""
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note

    
