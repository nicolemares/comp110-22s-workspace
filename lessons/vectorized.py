from __future__ import annotations


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]):
        """Vectorized concatenation operator"""
        # Setup a result list of strings that is empy
        result: list[str] = []
        # Loop through each item in self.items
        if isinstance(rhs, str):
                for item in self.items:
                result.append(item + rhs)
        else:
            assert len(self.items) == len(rhs.items)
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
            # build up result list by concatenating each item in self.items with correponding item in rhs.items
            return StrArray(result)


        # Return a newly constructed StrArray whose items are result
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)
print(first + last)