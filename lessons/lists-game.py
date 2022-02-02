"""Examples of using lists in a simple 'game'."""

from random import randint

rolls: list[int] = list()

while rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))


# rolls: list[int] = list()
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual item
# print(rolls[0])

# # Access length of list
# print(len(rolls))