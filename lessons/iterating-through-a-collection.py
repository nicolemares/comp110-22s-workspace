""""example of looping through all characters in a string"""

user_str: str = input("Give me a string! ")

# the varible i is a common variable name 
# in programming. i is short for iteration.
i: int = 0

while i < len(user_str):
    print(user_str[i])
    i = i + 1

print("Done!")