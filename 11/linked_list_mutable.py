'''
Mutable Linked List.
Destructive Functions
Uses Iteration For Operations
'''
from typing import Union
from dataclasses import dataclass
from node_types import MutableNode


@dataclass(frozen=False)
class LinkedListMutable:
    head: Union[MutableNode, None] = None
    size: int = 0


def make_empty_list():
    return LinkedListMutable(None, 0)


def to_str(lst):
    result = "["  # result is the accumulator
    node = lst.head
    while node is not None:
        result += " " + str(node.value)
        if node.next is not None:
            result += ","
        node = node.next
    result += " ]"
    return result


def append(lst, new_value):
    new_node = MutableNode(new_value, None)
    node = lst.head
    if node is None:
        lst.head = new_node
    else:
        successor = node.next
        while successor is not None:
            node = successor
            successor = node.next
        node.next = new_node
    lst.size += 1


def get_value(lst, index):
    node = lst.head
    while node != None and index > 0:
        node = node.next
        index -= 1
    if node is None:
        raise IndexError("List is shorter than index " + str(index) + "!")
    else:
        return node.value


def set_value(lst, new_value, index):
    node = lst.head
    while node != None and index > 0:
        node = node.next
        index -= 1
    if node is None:
        raise IndexError("List is shorter than index " + str(index) + "!")
    else:
        node.value = new_value


def contains(lst, target):
    node = lst.head
    while node != None and node.value != target:
        node = node.next
    if node is None:
        return False
    else:
        return True


def index_of(lst, target):
    node = lst.head
    index = 0
    result = -1
    while node != None and result == -1:
        if node.value == target:
            result = index
        node = node.next
        index += 1
    return result


def remove_value(lst, value):
    node = lst.head
    if node is None:
        raise ValueError("No such value " + str(value) + " in list!")
    elif node.value == value:
        lst.head = node.next
    else:
        successor = node.next
        while successor is not None and successor.value != value:
            node = successor
            successor = node.next
        if successor is None:
            raise ValueError("No such value " + str(value) + " in list!")
        else:
            node.next = successor.next
    lst.size -= 1


def insert_before_index(lst, new_value, index):
    new_node = MutableNode(new_value, None)
    current = lst.head
    if index == 0:  # We must modify the head of the LinkedList object.
        new_node.next = current
        lst.head = new_node
    elif current is None:
        raise IndexError("List is shorter than index " + str(index) + "!")
    else:
        successor = current.next
        loc = 1
        while successor is not None and loc < index:
            current = successor
            successor = current.next
            loc += 1
        if loc < index:  # The list ended prematurely.
            raise IndexError(
                "List is shorter than index " + str(index) + "!")
        else:
            new_node.next = successor
            current.next = new_node
    lst.size += 1


def concatenate(lst1, lst2):
    current = lst2.head
    while current != None:
        append(lst1, current.value)
        current = current.next

