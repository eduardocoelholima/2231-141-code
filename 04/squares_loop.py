import turtle
import random
import math

SIZE = 600

def random_fill() -> None:
    R = random.random()
    G = random.random()
    B = random.random()
    turtle.fillcolor(R, G, B)



def draw_square(length):
    random_fill()
    turtle.begin_fill()
    sides = 4
    while sides > 0:
        turtle.forward(length)
        turtle.left(90)
        sides = sides - 1
    turtle.end_fill()


def squares(length):
    area = 0
    while length >= 1:
        draw_square(length)
        half = length / 2
        turtle.forward(half)
        turtle.left(45)
        length = math.sqrt(half**2*2)
        area = area + length * length
    return area


def main():
    turtle.speed(0)
    turtle.tracer(False)
    turtle.up()
    turtle.goto(-SIZE / 2, -SIZE / 2)
    print(squares(SIZE))
    turtle.hideturtle()
    turtle.tracer(True)
    turtle.done()


if __name__ == '__main__':
    main()
