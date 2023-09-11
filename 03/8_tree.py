import turtle

SPEED = 0
TRACER = False
SIZE = 200
SEGMENTS = 16
PERCENTAGE = 0.7


def init_turtle():
    turtle.speed(SPEED)
    turtle.tracer(TRACER)
    turtle.left(90)
    turtle.penup()
    turtle.backward(SIZE * 1.5)
    turtle.pendown()



def draw_tree0( size ):
    pass


def draw_tree1( size ):
    turtle.forward( size )
    turtle.forward( -size )


def draw_tree2( size ):
    turtle.forward( size )
    turtle.left( 45 )
    draw_tree1( size / 2 )
    turtle.right( 90 )
    draw_tree1( size / 2 )
    turtle.left( 45 )
    turtle.forward( -size )


def draw_tree3( size ):
    turtle.forward( size )
    turtle.left( 45 )
    draw_tree2( size / 2 )
    turtle.right( 90 )
    draw_tree2( size / 2 )
    turtle.left( 45 )
    turtle.forward( -size )


def draw_tree( segments, size ):
    """
    Recursive solution
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


if __name__ == "__main__":
    init_turtle()
    # draw_tree0(SIZE)
    draw_tree(SEGMENTS, SIZE)
    turtle.tracer(True)
    turtle.done()

