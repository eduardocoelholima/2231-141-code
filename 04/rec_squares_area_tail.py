import turtle
import random
import math

SIZE = 600

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
    draw_poly_rec(length, 4,90)
    turtle.end_fill()


def rec_squares(length, area):
    if length < 5:  # base case
        return area
    else:
        # unit of work
        draw_square(length)
        # prepare for recursion
        half = length / 2
        turtle.forward(half)
        turtle.left(45)
        next = math.sqrt(half**2*2)
        area += length * length
        # recursive call
        return rec_squares(next, area)


def main():
    turtle.speed(0)
    turtle.tracer(False)
    turtle.up()
    turtle.goto(-SIZE / 2, -SIZE / 2)
    total_area = rec_squares(SIZE, 0)
    print('Total area drawn: ', total_area)
    turtle.hideturtle()
    turtle.tracer(True)
    turtle.done()


if __name__ == '__main__':
    main()
