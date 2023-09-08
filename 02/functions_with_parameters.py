"""
   draws a square diamond
"""

import turtle as t


def draw_square_diamond(side_length):
    '''
    draws a square diamond

    -- side_length: the length of the diamond side

    -- post-condition: turtle will be at the position and orientation before the function call
    '''
    t.left(45)
    t.fd(side_length)
    t.left(90)
    t.fd(side_length)
    t.left(90)
    t.fd(side_length)
    t.left(90)
    t.fd(side_length)
    t.left(45)

def test_range_of_diamond_sizes():
    draw_square_diamond(30)
    draw_square_diamond(60)
    draw_square_diamond(90)
    draw_square_diamond(120)

if __name__ == "__main__":
    # side_length = input("Specify the diamong side length:")
    # draw_square_diamond(int(side_length))
    test_range_of_diamond_sizes()
    t.done()
