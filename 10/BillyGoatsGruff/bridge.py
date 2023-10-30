"""
file: bridge.py
author: CS @ rit.edu

This module is part of a lecture on the stack and queue datatypes.
It introduces Stack and Queue data structures implemented using a
linked node sequence data structure, an alternative to Python lists.

The data structure modules are cs_stack.py and cs_queue.py.
The mutable linked Node structure is in node.py.
"""

from cs_queue import make_empty_queue, front, enqueue, dequeue
from cs_stack import top, pop
import cs_queue, cs_stack # used to disambiguate is_empty
from random import randint

MAX_WEIGHT = randint(800, 1000)
MAX_GOATS = randint(3, 5)

def cross_the_bridge( cavern, meadow ):
    """
    Goats leave the cavern and enter the bridge for stage 2 of the adventure.
    """
    bridge = make_empty_queue()
    
    print("STAGE 2: SKILL CHALLENGE...")
    print("The goats make it to a perilous gorge...")
    print("There is an old and rotting wooden bridge that spans the gorge...")
    print("The berries are on the other side of the bridge!")
    print("The goats decide to cross it together...")
    
    print("The maximum weight supported by the bridge is", MAX_WEIGHT)
    
    print("The bridge can hold a maximum of", MAX_GOATS, "goats")
    
    # loop by adding goats to the bridge until either it breaks or 
    # they all make it on
    total_weight = 0
    broken_bridge = False
    while not broken_bridge and not cs_stack.is_empty(cavern):
        # if the bridge holds the max goats, remove the front goat from it
        if bridge.size == MAX_GOATS:
            goat = front(bridge)
            print("The bridge is full.", goat.name, "finishes crossing it...")
            enqueue( meadow, front( bridge ) )
            dequeue(bridge)
            total_weight -= goat.weight
            
        # process the next goat in the cavern
        goat = pop(cavern)
        print(goat.name, "of weight", goat.weight,
            "steps carefully onto the bridge...")
        enqueue(bridge, goat)
        total_weight += goat.weight
        print("Total weight on bridge:", total_weight)
        print("Number of goats on the bridge:", bridge.size)
        if total_weight > MAX_WEIGHT:
            print("OH NO! The bridge collapses under the massive weight!")
            broken_bridge = True
    
    # if the bridge breaks, separate those who fall from those 
    # who are stranded
    if broken_bridge:
        while not cs_queue.is_empty(bridge):
            # the goats on the bridge are in trouble
            print(front(bridge).name, "falls into the gorge!")
            dequeue(bridge)
        while not cs_stack.is_empty(cavern):
            goat = top(cavern)
            pop(cavern)
            print(goat.name, "is left stranded in the fields!")
    else:
        while not cs_queue.is_empty(bridge):
            goat = front(bridge)
            print(goat.name, "finishes crossing the bridge...")
            enqueue( meadow, front( bridge ) )
            dequeue(bridge)
        
    print( str( meadow.size ), "goat/s survived the bridge crossing..." )
