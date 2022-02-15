"""Exercise 03 - Wordle."""

__author__ = "730391824"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# finding letter in word
def contains_char(secret: str, letter: str) -> bool:
    """If second string (letter) is found within first string (word)."""
    assert len(letter) == 1
    i: int = 0
    while i < len(secret):
        if secret[i] == letter:
            return True
        i = i + 1 
    return False


# correct boxes for each letter
def emojified(word: str, secret: str) -> str:
    """Returning correct color for coreect letter."""
    assert len(word) == len(secret)
    n: int = 0
    box: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while n < len(secret):
        if word[n] == secret[n]:
            box = box + str(GREEN_BOX)
        else:
            if contains_char(secret, word[n]) is True:
                box = box + str(YELLOW_BOX)
            else:
                box = box + str(WHITE_BOX)
        n = n + 1
    return box


# correct amount of letters in guess
def input_guess(length: int) -> str:
    """Checking to see if guess is correct length."""
    guess: str = str(input("Enter a " + str(length) + " character word: "))
    while len(guess) != length:
        guess = str(input("That wasn't " + str(length) + " chars! Try again: "))
    return guess


# game loop
def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    turn: int = 1
    lose: bool = False
    while turn <= 6 and not lose:
        print(f"=== Turn {turn}/6 ===")
        word = (input_guess(5))
        secret: str = "codes"
        print(emojified(word, secret))
        if word == secret:
            print(f"You won in {turn}/6 turns!")
            lose = True
        else:
            turn = turn + 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


# converting to module
if __name__ == "__main__":
    main()