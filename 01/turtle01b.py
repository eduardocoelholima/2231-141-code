import turtle

# initialization step
def init():
    turtle.up()
    turtle.left(90)
    turtle.speed(100)

def draw_square():
    turtle.down()
    turtle.right(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)

init()
draw_square()
turtle.fd(200)
# turtle.left(90)
draw_square()

turtle.done()
