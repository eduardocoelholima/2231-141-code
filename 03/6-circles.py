import math
import turtle


def circles(radius: int, depth: int) -> int:
    if depth <= 0:
        return 0
    if depth == 1:
        turtle.circle(radius)
        return math.pi * radius * 2

    total = math.pi * radius * 2
    for i in range(4):
        turtle.circle(radius, 90)
        total += circles(radius / 2, depth - 1)
    return total


def main():
    turtle.Screen().setup(width=1.0, height=1.0)
    turtle.tracer(True)
    radius = 300
    turtle.penup()
    turtle.setpos(0, -radius)
    turtle.pendown()
    turtle.pensize(2)
    turtle.speed(0)
    circumference = circles(radius, 3)
    print("circumference:", circumference)
    turtle.tracer(True)
    turtle.done()


if __name__ == "__main__":
    main()
