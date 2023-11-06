'''
Immutable Linked List.
Non-Destructive Functions
Uses Recursion For Operations
'''
from typing import Union
from dataclasses import dataclass
from node_types import FrozenNode


@dataclass(frozen=False)
class LinkedListImmutable:
    head: Union[FrozenNode, None] = None
    size: int = 0


def make_empty_list():
    return LinkedListImmutable(None, 0)


def to_str(lst):
    head = lst.head
    result = "["
    result += _to_str_rec(head)
    result += " ]"
    return result


def _to_str_rec(head, acc=''):
    """
    to_str_acc_rec: FrozenNode, str -> str
    """
    if head is None:
        return acc
    else:
        suffix = ' ' + str(head.value)
        if head.next is not None:
            suffix += ","
        return _to_str_rec(head.next, acc + suffix)


def append(lst, new_value):
    newSize = lst.size + 1
    return LinkedListImmutable(_append(lst.head, new_value), newSize)


def _append(head, new_value):
    if head is None:
        return FrozenNode(new_value, None)
    else:
        return FrozenNode(head.value, _append(head.next, new_value))


def get_value(lst, index):
    head = lst.head
    return _get_value(head, index)


def _get_value(head, index):
    if head is None:
        raise IndexError("List is shorter than index " + str(index) + "!")
    elif index == 0:
        return head.value
    else:
        return _get_value(head.next, index - 1)


def set_value(lst, new_value, index):
    newSize = lst.size
    return LinkedListImmutable(_set_value(lst.head, new_value, index), newSize)


def _set_value(head, new_value, index):
    if head is None:  # index > 0
        raise IndexError("List is shorter than index " + str(index) + "!")
    elif index == 0:
        return FrozenNode(new_value, head.next)
    else:
        return FrozenNode(
            head.value,
            _set_value(head.next, new_value, index - 1)
        )


def contains(lst, target):
    return _contains(lst.head, target)


def _contains(head, target):
    if head == None:
        return False
    elif head.value == target:
        return True
    else:
        return _contains(head.next, target)



def index_of(lst, target):
    return _index_of(lst.head, target)


def _index_of(head, target, acc = 0):
    if head == None:
        return -1
    elif head.value == target:
        return acc
    else:
        return _index_of(head.next, target, acc + 1)

def remove_value(lst, value):
    newSize = lst.size - 1
    return LinkedListImmutable(_remove_value(lst.head, value), newSize)


def _remove_value(head, value):
    if head is None:
        raise ValueError("No such value " + str(value) + " in list!")
    elif head.value == value:
        return head.next
    else:
        return FrozenNode(head.value, _remove_value(head.next, value))


def insert_before_index(lst, new_value, index):
    newSize = lst.size + 1
    return LinkedListImmutable(_insert_before_index(lst.head, new_value, index), newSize)


def _insert_before_index(head, new_value, index):
    if index == 0:
        # Note: this case has two perspectives:
        # (1) We are past the end of the list; (2) We are given an empty list.
        return FrozenNode(new_value, head)
    elif head is None:  # index > 0
        raise IndexError("List is shorter than index " + str(index) + "!")
    else:
        return FrozenNode(
            head.value,
            _insert_before_index(head.next, new_value, index - 1)
        )


def concatenate(lst1, lst2):
    head1 = lst1.head
    head2 = lst2.head
    return LinkedListImmutable(_concatenate(head1, head2), lst1.size + lst2.size)


def _concatenate(head1, head2):
    if head1 is None:
        return head2
    else:
        return FrozenNode(head1.value, _concatenate(head1.next, head2))

