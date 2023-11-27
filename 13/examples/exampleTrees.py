"""
file: exampleTrees.py
description:
Defines variables bound to different binary search trees.
Depends on bsttools.py classes and functions.

author: cs dept instructors
"""

from bsttools import *

############################################################
# Sample trees
############################################################

exampleTree0 = None

exampleTree1 = BinaryTree( None, 1, None )

exampleTree2 = BinaryTree( BinaryTree( None, 1, None ), 3, None )

exampleTree3 = BinaryTree( None, 3, BinaryTree( None, 4, None ) )

# t2 in lecture notes
exampleTree4 = BinaryTree( BinaryTree( None, 1, None ), \
                          3,                                   \
                          BinaryTree( None, 4, None ) )

exampleTree5 = BinaryTree( BinaryTree( None, 6, None ), \
                          7,                                   \
                          BinaryTree( None, 9, None ) )

exampleTree6 = BinaryTree( exampleTree4, 5, exampleTree5 )


