"""
file: bst.py
description:
Demonstrates binary trees and binary search trees
Definition:
   An empty BinaryTree is represented as None.
   A non-empty BinaryTree structure has a left and right sub-tree
   which are both BinaryTrees, along with a slot to hold
   a value. 

language: python3
author: cs dept instructors
"""

from dataclasses import dataclass
from typing import Any, Union


############################################################
# structure definiton
############################################################

@dataclass
class BinaryTree:
    '''Class to represent a Binary Tree'''
    left: Union[None, 'BinaryTree'] = None
    value: Any = None
    right: Union[None, 'BinaryTree'] = None


@dataclass
class BinarySearchTree:
    '''Class to represent a Binary Search Tree'''
    root: Union[None, 'BinaryTree'] = None
    size: int = 0


############################################################
# add, size, height, imbalance, String Conversion and search
############################################################

def bt_add(tr, value):
    if tr is None:
        raise ValueError("Can't add to an empty tree")
    elif tr.value is None:
        tr.value = value
    else:
        q = list()
        x = tr
        while x is not None:
            if x.left is None:
                x.left = BinaryTree(None, value, None)
                break
            elif x.right is None:
                x.right = BinaryTree(None, value, None)
                break
            else:
                q.append(x.left)
                q.append(x.right)
            x = q.pop(0)

def bt_size(tr):
    if tr is None:
        return 0
    else:
        return 1 + bt_size(tr.left) + bt_size(tr.right)
def bt_height(tr, depth = 0):
    if tr is None and depth == 0:
        return 0
    elif tr is None:
        return - 1
    else:
        lHeight = bt_height(tr.left, depth + 1)
        rHeight = bt_height(tr.right, depth + 1)
        if lHeight > rHeight:
            return lHeight + 1
        else:
            return rHeight + 1


def bt_min_height(tr, minHeight=0, depth=1):
    if tr is None:
        return minHeight
    elif tr.left is None and tr.right is None:
        if depth < minHeight:
            minHeight = depth
        return minHeight
    else:
        minHeight = bt_min_height(tr.left, minHeight, depth + 1)
        minHeight = bt_min_height(tr.right, minHeight, depth + 1)
        return minHeight


def bt_imbalance(tr):
    if tr is None:
        return 0
    else:
        maxHeight = bt_height(tr) + 1
        if tr.left is None or tr.right is None:
            startMinHeight = 1
        else:
            startMinHeight = maxHeight
        minHeight = bt_min_height(tr, startMinHeight)
        return maxHeight - minHeight


def bt_to_string(tr):
    """
   Uses in-order by default.
   Can be changed to use the other orders instead
   """
    return bt_to_string_in_order(tr)


def bt_to_string_in_order(tr):
    """
   bt_to_string_in_order: BinaryTree -> String
   bt_to_string_in_order returns a string representing the
   in-order traversal of the given tree, tr.
   A single space delimits each item in the string.
   """
    if tr is None:
        return ''
    else:
        return bt_to_string(tr.left) + (str(tr.value) + ' ') + bt_to_string(tr.right)


def bt_to_string_pre_order(tr):
    """
   bt_to_string_pre_order: BinaryTree -> String
   bt_to_string_pre_order returns a string representing the
   pre-order traversal of the given tree, tr.
   A single space delimits each item in the string.
   """
    if tr is None:
        return ''
    else:
        return (str(tr.value) + ' ') + bt_to_string(tr.left) + bt_to_string(tr.right)


def bt_to_string_post_order(tr):
    """
   bt_to_string_post_order: BinaryTree -> String
   bt_to_string_post_order returns a string representing the
   post-order traversal of the given tree, tr.
   A single space delimits each item in the string.
   """
    if tr is None:
        return ''
    else:
        return (bt_to_string(tr.left) + bt_to_string(tr.right) + str(tr.value) + ' ')


def bt_search(tr, value):
    if tr is None:
        return False
    else:
        if value == tr.value:
            return True
        elif bt_search(tr.left, value):
            return True
        elif bt_search(tr.right, value):
            return True
        else:
            return False


############################################################
# bst add and search
############################################################

def bst_add_value(bst, value):
    if bst.root is None:
        bst.root = BinaryTree(None, value, None)
    else:
        _bst_add_value(bst.root, value)
    bst.size += 1


def _bst_add_value(node, value):
    if node is None:
        return BinaryTree(None, value, None)
    elif value < node.value:
        if node.left is None:
            node.left = _bst_add_value(None, value)
        else:
            _bst_add_value(node.left, value)
    else:
        if node.right is None:
            node.right = _bst_add_value(None, value)
        else:
            _bst_add_value(node.right, value)


def bst_search(bst, value):
    """
   bst_search: BinarySearchTree * Number -> Boolean
   bst_search returns True if the value is found in the
   binary search tree, tr.
   """
    if bst is None:
        return False
    else:
        if value == bst.value:
            return True
        elif value < bst.value:
            return bst_search(bst.left, value)
        elif value > bst.value:
            return bst_search(bst.right, value)


############################################################
# Sample trees
############################################################

exampleTree0 = None

exampleTree1 = BinaryTree(None, 1, None)

exampleTree2 = BinaryTree(BinaryTree(None, 1, None), 3, None)

exampleTree3 = BinaryTree(None, 3, BinaryTree(None, 4, None))

# t2 in lecture notes
exampleTree4 = BinaryTree(BinaryTree(None, 1, None), \
                          3, \
                          BinaryTree(None, 4, None))

exampleTree5 = BinaryTree(BinaryTree(None, 6, None), \
                          7, \
                          BinaryTree(None, 9, None))

exampleTree6 = BinaryTree(exampleTree4, 5, exampleTree5)

exampleBST = BinarySearchTree()
for value in [5, 6, 7, 3, 4, 2, 1, 8, 9]:
    bst_add_value(exampleBST, value)

def test_bt_to_string():
    """
    test_bt_to_string : Void -> None
    """
    print('Testing bt_to_string')
    print(bt_to_string(exampleTree0) == '', end=' ')
    print(bt_to_string(exampleTree1) == '1 ', end=' ')
    print(bt_to_string(exampleTree2) == '1 3 ', end=' ')
    print(bt_to_string(exampleTree3) == '3 4 ', end=' ')
    print(bt_to_string(exampleTree4) == '1 3 4 ', end=' ')
    print(bt_to_string(exampleTree6) == '1 3 4 5 6 7 9 ', end=' ')
    print(bt_to_string_pre_order(exampleTree6) == '5 1 3 4 6 7 9 ', end=' ')
    print(bt_to_string_post_order(exampleTree6) == '1 3 4 6 7 9 5 ', end=' ')
    print(bt_to_string(exampleBST.root) == '1 2 3 4 5 6 7 8 9 ', end=' ')
    print(bt_to_string_pre_order(exampleBST.root) == '5 1 2 3 4 6 7 8 9 ', end=' ')
    print(bt_to_string_post_order(exampleBST.root) == '1 2 3 4 6 7 8 9 5 ', end=' ')
    print(exampleBST.size == 9, end=' ')
    print(bt_height(exampleBST.root) == 4, end=' ')
    print(bt_imbalance(exampleBST.root) == 2)


# Tests
def test_bst_search():
    """
    test_bst_search : Void -> None
    """
    print('Testing bst_search')
    for i in range(1, 10):
        print(bst_search(exampleBST.root, i) == True, end=' ')
    print(bst_search(exampleBST.root, 11) == False)


# run tests

if __name__ == "__main__":
    test_bt_to_string()
    test_bst_search()
