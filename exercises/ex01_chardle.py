"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730391824"

number_of_matching: int = int(0)
random_word: str = input("Enter a 5-character word: ")
if len(random_word) != int(5):
    print("Error: Word must contain 5 characters")
    exit()

single_letter: str = input("Enter a single character: ")
if len(single_letter) != int(1):
    print("Error: Character must be a single character")
    exit()

print("Searching for " + single_letter + " in " + random_word)

if random_word[0] == single_letter:
    print(single_letter + " found at index 0")
    number_of_matching = number_of_matching + 1
if random_word[1] == single_letter:
    print(single_letter + " found at index 1")
    number_of_matching = number_of_matching + 1
if random_word[2] == single_letter:
    print(single_letter + " found at index 2")  
    number_of_matching = number_of_matching + 1
if random_word[3] == single_letter:
    print(single_letter + " found at index 3") 
    number_of_matching = number_of_matching + 1
if random_word[4] == single_letter:
    print(single_letter + " found at index 4") 
    number_of_matching = number_of_matching + 1

if number_of_matching == 0:
    print("No instances of " + single_letter + " found in " + random_word)
else:
    if number_of_matching == 1:
        print(str(number_of_matching) + " instance of " + single_letter + " found in " + random_word)
    else: 
        print(str(number_of_matching) + " instances of " + single_letter + " found in " + random_word)