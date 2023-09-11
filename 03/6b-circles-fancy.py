import math
import turtle

PAUSE_AND_PRINT = False
TRACER = True
DEPTH = 4
RADIUS = 300
SPEED = 0


def get_depth_color(depth):
    if depth == 1:
        return "red"
    elif depth == 2:
        return "green"
    elif depth == 3:
        return "blue"
    elif depth == 4:
        return "orange"
    elif depth == 5:
        return "purple"
    elif depth == 6:
        return "cyan"
    else:
        return "black"


def write_info_and_pause(msg):
    global PAUSE_AND_PRINT
    turtle.color('black')
    turtle.write(msg, font=("Arial", 19, "normal"))

    text = turtle.textinput("Pause", "Enter 'stop' to finish without pausing")
    print(text)
    if text.lower() == "stop":
        PAUSE_AND_PRINT = False

    turtle.undo()


def circles(radius, depth):
    if depth <= 0:
        return 0
    if depth == 1:
        if PAUSE_AND_PRINT:
            turtle.pencolor(get_depth_color(depth))
            write_info_and_pause("depth 1 - about to draw full circle r:" + str(radius))

        turtle.pencolor(get_depth_color(depth))
        turtle.circle(radius)

        return math.pi * radius * 2

    total = math.pi * radius * 2
    for i in range(4):
        if PAUSE_AND_PRINT:
            turtle.pencolor(get_depth_color(depth))
            write_info_and_pause("depth " + str(depth) + " - about to draw arc " + str(i) + " r:" + str(radius))

        turtle.pencolor(get_depth_color(depth))
        turtle.circle(radius, 90)
        total += circles(radius / 2, depth - 1)
    return total


def main():
    turtle.Screen().setup(width=1.0, height=1.0)
    turtle.tracer(TRACER)
    radius = RADIUS
    turtle.penup()
    turtle.setpos(0, -radius)
    turtle.pendown()
    turtle.pensize(2)
    turtle.speed(SPEED)
    circumference = circles(radius, DEPTH)
    print("circumference:", circumference)
    turtle.tracer(True)
    turtle.done()
    # input("Press enter to finish...")


if __name__ == "__main__":
    main()
