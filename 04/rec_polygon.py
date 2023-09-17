import turtle
import random
import math

BOUNDING_BOX = 600
SIDES = 16
SIZE = BOUNDING_BOX * math.sin(math.pi / SIDES)


def random_fill() -> None:
    R = random.random()
    G = random.random()
    B = random.random()
    turtle.fillcolor(R, G, B)


def draw_poly_rec(length: int, sides: int, angle: float) -> None:
    if sides == 0:
        return
    else:
        turtle.forward(length)
        turtle.left(angle)
        draw_poly_rec(length, sides - 1, angle)


def draw_square(length):
    random_fill()
    turtle.begin_fill()
    draw_poly_rec(length, SIDES, 360 / SIDES)
    turtle.end_fill()


def rec_squares(length):
    if length < 5:  # base case
        return 0
    else:
        # unit of work
        draw_square(length)
        area = length * length
        # prepare for recursion
        half = length / 2
        turtle.forward(half)
        turtle.left(360 / SIDES / 2)
        r = length / (2 * math.tan(math.pi / SIDES))
        next = 2 * r * math.sin(math.pi / SIDES)
        # recursive call
        total = area + rec_squares(next)
        return total


def main():
    turtle.speed(0)
    turtle.tracer(False)
    turtle.up()
    turtle.goto(-SIZE * SIDES / 8, -SIZE * SIDES / 8)
    total_area = rec_squares(SIZE)
    print('Total area drawn: ', total_area)
    turtle.hideturtle()
    turtle.tracer(True)
    turtle.done()


if __name__ == '__main__':
    main()
