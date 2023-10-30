""" 
file: node_types.py
description: type definitions for immutable linked sequences
author: RIT CS
"""

from typing import Any, Union
from dataclasses import dataclass


@dataclass(frozen=True)
class FrozenNode:
    """
    An immutable link node containing a value and a link to the next node
    """
    value: Any
    next: Union["FrozenNode", None]


@dataclass(frozen=False)
class MutableNode:
    """
    A mutable link node containing a value and a link to the next node
    """
    value: Any
    next: Union["MutableNode", None]


# ---------------------- Very Basic Test Code --------------------------------

# A list printer is defined here. It is redundant with the to-string
# functions found in immutable_list.py and mutable_list.py.
# But since we need something for basic testing and we don't want to
# introduce circular dependencies between modules, we put this
# quick-and-dirty function here.

def print_seq(head):
    print('[', end="")
    node = head
    while node is not None:
        print(" " + str(node.value), end="")
        node = node.next
    print(" ]")


def node_examples() -> None:
    """
    Let's make some node structures.
    """
    node_seq = FrozenNode(1, FrozenNode(2, FrozenNode(3, None)))
    #   Same as:
    #   tail = FrozenNode(3, None)
    #   middle = FrozenNode(2, tail)
    #   head = FrozenNode(1, middle)
    #   node_seq = head

    print_seq(node_seq)
    print("Above line should be [ 1 2 3 ].")

    print_seq(node_seq.next)
    print("Above line should be [ 2 3 ].")

    node_seq = None
    print_seq(node_seq)
    print("Above line should be [ ].")

    node_seq = MutableNode(1, MutableNode(2, MutableNode(3, None)))
    print_seq(node_seq)
    print("Above line should be [ 1 2 3 ].")

    node_seq.next = node_seq.next.next
    print_seq(node_seq)
    print("Above line should be [ 1 3 ].")


if __name__ == '__main__':
    node_examples()
