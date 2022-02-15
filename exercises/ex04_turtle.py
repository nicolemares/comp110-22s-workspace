"""Scene: Ocean with sailboats of various size and color."""

__author__ = "730391824"

from random import randint
from turtle import Turtle, colormode, done
import random

colormode(255)


def main() -> None:
    """The entrypoint of my scene"""
    jim: Turtle = Turtle()
    jim.speed(2000)
    background_color(jim, -400, 400)

    # repeating line of waves
    i: float = 325.0
    while i >= -325:
        waves(jim, -360, i)
        i = i - 50

    # reapeating sailboats of various size and location
    horizontal: float = -325
    vertical: float = 325
    width: float = 30
    n: int = 0
    while horizontal <= 360 and vertical >= -360:
        # repeating at various locations
        n = 0
        while n < 8:
            # repeating at various sailboat size
            sailboats(jim, horizontal, vertical, width)
            horizontal = horizontal + randint(50, 150)
            width = randint(25, 75)
            n = n + 1
        horizontal = -325
        vertical = vertical - randint(75, 150)
    done()


def sailboats(jim: Turtle, x: float, y: float, width: float) -> None:
    """Drawing Sailboats"""
    jim.penup()
    jim.goto(x, y)
    jim.setheading(0.0)
    jim.pendown()

    # Sail of boat
    i: int = 0
    r = random.randint(0, 255)
    jim.color(r, r, r)
    jim.begin_fill()
    while i < 3:
        jim.forward(width)
        jim.left(120)
        i = i + 1
    jim.end_fill()

    # boat part
    jim.color(225, 255, 255)
    jim.penup()
    jim.goto((x + (.5 * width)), y)
    jim.pendown()
    jim.right(90)
    jim.forward(.25 * width)
    jim.left(90)
    jim.forward(.5 * width)
    jim.left(180)
    jim.begin_fill()
    jim.forward(width)
    jim.left(90)
    jim.forward(.25 * width)
    jim.left(90)
    jim.forward(width)
    jim.left(90)
    jim.forward(.25 * width)
    jim.end_fill()


def waves(jim: Turtle, x: float, y: float) -> None:
    """Drawing waves"""
    jim.penup()
    jim.goto(x, y)
    jim.setheading(0.0)
    jim.pendown()
    jim.color(17, 111, 247)

    # one line of waves
    i: float = -350.00
    while i <= 350.00:
        jim.left(45)
        jim.forward(10)
        jim.right(35)
        jim.forward(2.5)
        jim.right(55)
        jim.forward(7)
        jim.left(190)
        jim.forward(5)
        jim.left(90)
        jim.forward(8)
        jim.setheading(0.0)
        jim.forward(25)
        i = i + 25
    i = 0

    
def background_color(jim: Turtle, x: float, y: float) -> None:
    """background color"""
    jim.penup()
    jim.goto(x, y)
    jim.setheading(0.0)
    jim.pendown()
    jim.color(10, 177, 244)

    jim.begin_fill()
    i: int = 0
    while i < 4:
        jim.forward((0 - x) + y)
        jim.right(90)
        i = i + 1
    jim.end_fill()


if __name__ == "__main__":
    main()