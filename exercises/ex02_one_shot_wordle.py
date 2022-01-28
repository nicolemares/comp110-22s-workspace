"""exercise 02 - one shot wordle."""

__author__ = "730391824"

secret: str = str("python")
guess: str = str(input("What is your 6-letter guess? "))
i: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# if guess is not 6 letters
while len(guess) != 6:
    guess = str(input("That was not 6 letters! Try again: "))
    i = i + 1
    if i == 4:
        print("Not quite. Play again soon!")
        exit()

n: int = 0
box: str = ""

# if guess is not correct
if guess != secret:
    while n <= 5:
        if guess[n] == secret[n]:
            box = box + str(GREEN_BOX)
            n = n + 1
        else:
            if (guess[n] == secret[0]) or (guess[n] == secret[1]) or (guess[n] == secret[2]) or (guess[n] == secret[3]) or (guess[n] == secret[4]) or (guess[n] == secret[5]):
                box = box + str(YELLOW_BOX)
                n = n + 1
            else:
                box = box + str(WHITE_BOX)
                n = n + 1
    print(box)
    print("Not quite. Play again soon!")

# if guess is correct
green = str(GREEN_BOX)
if guess == secret:
    print(green + green + green + green + green + green)
    print("Woo! You got it!")