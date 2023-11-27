"""
file: bsttools.py
description: tool functions extracted from bst.py
language: python3
author: cs dept instructors
"""

from dataclasses import dataclass
from typing import Any, Union

############################################################
# structure definiton
############################################################

# note: this is repeated from bst.py for convenience.

@dataclass
class BinaryTree:
    '''Class to represent a Binary Tree'''
    left: Union[None, 'BinaryTree']
    value: Any
    right: Union[None, 'BinaryTree']

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

