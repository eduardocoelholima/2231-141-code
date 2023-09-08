from turtle import *

def initialize():
    speed(1)
    up()
    left(90)

def draw_nose():
    right(90)
    bk(20)
    down()
    forward(40)
    left(120)
    forward(40)
    left(120)
    fd(40)
    left(120)
    up()
    fd(20)
    left(90)

def draw_outer():
    right(90)
    down()
    circle(100)
    up()
    left(90)

def draw_mouth():
    down()
    right(60)
    fd(40)
    bk(40)
    left(60+60)
    fd(40)
    bk(40)
    right(60)
    up()

def main():
    initialize()
    draw_outer()
    fd(20)
    draw_mouth()
    fd(20)
    draw_nose()
    # draw_eyes()
    done()

main()