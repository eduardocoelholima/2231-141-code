# try to identify where the precondition and the postconditions do not hold in this code

import turtle as t

def draw_equilateral_triangle_bogus():
    '''
    draws an equilateral triangle with one of the sides facing down
         pre-conditions: turtle is facing East
         post-conditions: turtle is in the same state as at the start.
    '''
    t.fd(100)
    t.left(120)
    t.fd(100)
    t.left(120)
    t.fd(100)

def test_drawing_overlapping_tringles():
    draw_equilateral_triangle_bogus()
    draw_equilateral_triangle_bogus()

def test_drawing_tringle_facing_left():
    t.seth(180)
    draw_equilateral_triangle_bogus()

def main():
    test_drawing_overlapping_tringles()
    input("Press return to proceed")
    t.clear()
    test_drawing_tringle_facing_left()
    t.done()
main()