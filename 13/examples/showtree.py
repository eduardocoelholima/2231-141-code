"""
file: showtree.py
description:
Drawing binary trees using the turtle. 
Assumes definitions and examples from bst.py.
language: python3
author: R. Zanibbi
author: cs dept instructors
"""

from turtle import *
from bsttools import *
from bst import *

#########################################################
# More Sample trees
#########################################################

exampleTree7names = BinaryTree(           \
                        BinaryTree(       \
                            None,         \
                            'abra',       \
                            BinaryTree(   \
                                None,     \
                                'ca',     \
                                None)),   \
                        'dabra',          \
                        BinaryTree(       \
                            None,         \
                            'shaZAM!',    \
                            None))

exampleTree7 = BinaryTree(BinaryTree(None, 1, BinaryTree(None, 2, None)),  \
                          3,                                               \
                          BinaryTree(None, 4, None))

exampleTree8 = BinaryTree(BinaryTree(None, 6, None),              \
                          7,                                      \
                          BinaryTree(BinaryTree(None, 8, None),   \
                                     9,                           \
                                     BinaryTree(None, 10, None)))

exampleTree9 = BinaryTree(exampleTree7, 5, exampleTree8)

#########################################################
# Print the tree using a pre-order traversal
##########################################################

def btPrint(tr):
    """btPrint: BinaryTree -> NoneType
       Effect: Prints the tree using indentation.
    """
    ptree(tr, 0, '')

def ptree(tr, depth, arrow):
    """ptree: BinaryTree * Number * String -> NoneType
       Effect: Prints the tree using indentation.
    """
    if tr is None:
        pass
    else:
        ptree(tr.left, depth+1, '<')
        print(' '*depth, arrow, str(tr.value))
        ptree(tr.right, depth+1, '>')

############################################################
# Drawing trees using Turtle 
############################################################
DRAW_SCALE = .75
DRAW_ANGLE = 85
DRAW_ANGLE_MOD = .52
DRAW_DISTANCE = 330

def btDrawEasy(tr):
    btDraw(tr, DRAW_DISTANCE)
    done()

def btDraw(tr, distance):
    """btDraw: BinaryTree * Number -> NoneType
       Effect: The turtle draws the tree.
    """
    setheading(-90)
    speed(0)
    penup()
    goto(0, DRAW_DISTANCE)
    pendown()
    tracer(False)
    if tr is None:
        pass
    else:
        angle = DRAW_ANGLE
        dchild(tr.left, angle, distance)
        write(str(tr.value), False, 'left', ('Arial',18, 'bold'))
        node_circle()
        dchild(tr.right, -angle, distance)
    tracer(True)
    hideturtle()

def dchild(tr, angle, distance):
    """dchild: BinaryTree * Number * Number -> NoneType
       Effect: The turtle draws the child.
    """
    if tr is None:
        pass
    else:
        right(angle)
        forward(distance)
        right(-angle)
        dchild(tr.left, abs(angle * DRAW_ANGLE_MOD), distance * DRAW_SCALE)
        write(str(tr.value), False, 'left', ('Arial',18, 'bold'))
        node_circle()
        dchild(tr.right, -abs(angle * DRAW_ANGLE_MOD), distance * DRAW_SCALE)
        right(angle)
        back(distance)
        right(-angle)

def node_circle():
    x, y = pos()
    penup()
    goto(x - 15, y + 15)
    pendown()
    circle(30)
    penup()
    goto(x, y)
    pendown()


#######################################
# Testing function.
#######################################

def test():
    # for tree in [exampleTree0, exampleTree1, exampleTree2, exampleTree3, \
    #              exampleTree4, exampleTree5, exampleTree6, \
    #              exampleTree7names, exampleTree9]:
    for tree in [exampleBST]:
        # btPrint(tree)
        # btDraw(tree, 200)
        btPrint(tree.root)
        btDraw(tree.root, 200)
        # input("Hit enter to continue.\n")
        # clear()
        # setposition(0,0)

if __name__ == '__main__':
    # pass
    test()
    done()
