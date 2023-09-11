""" 
tree_full_w_comments.py draws a recursive tree.

assignment: lecture
language: python3
author: mtf@cs.rit.edu, Matthew Fluet, James Heliotis
"""

import turtle

WIN_DIM = 600 # Window height and width, in pixels (not turtle's units)
PERCENTAGE = 0.7
TRACER = False
# function definitions

def init_world( window_size, boundary_width ):
    """
    init_world initializes the drawing by establishing its pre-conditions.

    window_size -- the length and height of the drawing area
    boundary_width -- the thickness of the window boundary

    pre-conditions: 
    post-conditions: coordinate system is as specified by the parameter values
                     turtle is at origin,
                     turtle is facing North,
                     turtle is pen-down.
    """
    
    turtle.setup( WIN_DIM, WIN_DIM )

    turtle.setworldcoordinates( -window_size - boundary_width,
                                -window_size - boundary_width,
                                window_size + boundary_width,
                                window_size + boundary_width )
    turtle.clear()
    turtle.home()  # turtle is at origin, facing east, pen-down
    turtle.left( 90 )  # turtle is facing North
    turtle.down()  # turtle is pen-down
    turtle.pensize( 2 )


def draw_tree0( size ):
    """
    draw_tree0 draws a 0-level tree (i.e., nothing).

    size -- PosNumber;
            length of tree "trunk" to draw should be (strictly) positive.

    pre-conditions: size > 0.
                    turtle is at base of tree,
                    turtle is facing along trunk of tree,
                    turtle is pen-down.
    post-conditions: a 0-level tree was drawn on the canvas,
                     turtle is at base of tree,
                     turtle is facing along trunk of tree,
                     turtle is pen-down.
    """
    # draw nothing
    pass


def draw_tree1( size ):
    """
    draw_tree1 draws a 1-level tree (i.e., a tree trunk)

    size -- PosNumber;
            length of tree "trunk" to draw should be (strictly) positive.

    pre-conditions: size > 0.
                    turtle is at base of tree,
                    turtle is facing along trunk of tree,
                    turtle is pen-down.
    post-conditions: a 1-level tree was drawn on the canvas,
                     turtle is at base of tree,
                     turtle is facing along trunk of tree,
                     turtle is pen-down.
    """
    # draw trunk (and two 0-level sub-trees)
    turtle.forward( size )
    turtle.forward( -size )


def draw_tree2( size ):
    """
    draw_tree2 draws a 2-level tree (i.e., a Y-tree)

    size -- PosNumber;
            length of tree "trunk" to draw should be (strictly) positive.

    pre-conditions: size > 0.
                    turtle is at base of tree,
                    turtle is facing along trunk of tree,
                    turtle is pen-down.
    post-conditions: a 2-level tree was drawn on the canvas,
                     turtle is at base of tree,
                     turtle is facing along trunk of tree,
                     turtle is pen-down.
    """
    # draw trunk and two sub-trees
    turtle.forward( size )
    turtle.left( 45 )
    draw_tree1( size / 2 )
    turtle.right( 90 )
    draw_tree1( size / 2 )
    turtle.left( 45 )
    turtle.forward( -size )


def draw_tree3( size ):
    """
    draw_tree3 draws a 3-level tree (i.e., a Y-trees on a Y-tree)

    size -- PosNumber;
            length of tree "trunk" to draw should be (strictly) positive.

    pre-conditions: size > 0.
                    turtle is at base of tree,
                    turtle is facing along trunk of tree,
                    turtle is pen-down.
    post-conditions: a 3-level tree was drawn on the canvas,
                     turtle is at base of tree,
                     turtle is facing along trunk of tree,
                     turtle is pen-down.
    """
    # draw trunk and two sub-trees
    turtle.forward( size )
    turtle.left( 45 )
    draw_tree2( size / 2 )
    turtle.right( 90 )
    draw_tree2( size / 2 )
    turtle.left( 45 )
    turtle.forward( -size )


def draw_tree( segments, size ):
    """
    draw_tree recursively draws the tree.

    segments -- NonNegInteger;
                number of line segments from the base of the tree to
                the end of any branch should be integral and non-negative.
    size -- PosNumber;
            length of tree "trunk" to draw should be (strictly) positive.

    pre-conditions: segments >= 0, size > 0.
                    turtle is at base of tree,
                    turtle is facing along trunk of tree,
                    turtle is pen-down.
    post-conditions: a segments-level tree was drawn on the canvas,
                     turtle is at base of tree,
                     turtle is facing along trunk of tree,
                     turtle is pen-down.
    """
    if segments == 0:
        # base case: draw nothing
        pass
    elif segments > 0:
        # recursive case: draw trunk and two sub-trees
        turtle.forward( size )
        turtle.left( 45 )
        draw_tree( segments - 1, size * PERCENTAGE )
        turtle.right( 90 )
        draw_tree( segments - 1, size * PERCENTAGE )
        turtle.left( 45 )
        turtle.forward( -size )


def init_world_and_draw_tree( segments, size ):
    """
    init_world_and_draw_tree prints a message, initializes the world,
    draws an instance of the recursive tree, and waits for ENTER.

    segments -- NonNegInteger;
                number of line segments from the base of the tree to
                the end of any branch should be integral and non-negative.
    size -- PosNumber;
            length of tree "trunk" to draw should be (strictly) positive.
    """
    print( "Drawing recursive tree with", (segments, size) )
    init_world( size * 4, 3 ) # The "2" is a "fudge factor" to try to keep
                             # the drawing from extending beyond the window.
    turtle.speed('fastest') # Remove if you want to follow execution better.
    draw_tree( segments, size )


def run_test_cases():
    """
    Run test cases from the writeup.
    """

    # test case 1: segments=0, size=100
    print( "(No image output)" )
    init_world_and_draw_tree( 0, 100 )

    # test case 2: segments=1, size=50
    print( "(single line; initial line length == 50)" )
    init_world_and_draw_tree( 1, 50 )

    # test case 3: segments=2, size=100
    print( "(Y-tree. initial line length == 100)" )
    init_world_and_draw_tree( 2, 100 )

    # test case 4: segments=3, size=100
    print( "(Y-trees on a Y-tree. initial line length == 100)" )
    init_world_and_draw_tree( 3, 100 )


def prompt_and_draw_tree():
    """
    prompt_and_draw_tree prompts for number of line segments from the
    base of the tree to the end of any branch and length of tree "trunk"
    and draws an instance of the recursive tree.
    """

    segments = int( input( "Enter 'segments' (a non-negative integer): " ) )
    size = int( input( "Enter 'size' (a positive integer): " ) )
    turtle.tracer(TRACER)
    init_world_and_draw_tree( segments, size )


# script execution/run

if __name__ == "__main__":
    prompt_and_draw_tree()
    turtle.tracer(True)
    print( "Close the window to quit." )
    turtle.done()

