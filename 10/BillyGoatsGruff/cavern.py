"""
file: cavern.py
author: Arthur Nunes-Harwitt
author: RIT CS Department

This module is part of a lecture on the stack and queue datatypes.
It introduces Stack and Queue data structures implemented using a
mutable linked Node structure is in node.py.

The data structure modules are cs_stack.py and cs_queue.py.
"""

from cs_stack import pop, push, size, is_empty
from random import randint

def get_troll_damage():
    """
    generate a random amount for what pain the troll can cause a goat. 
    """
    return randint(100, 200)
    
def get_goat_damage():
    """
    generate a random amount for what pain a goat can cause the troll. 
    """
    return randint(0, 100)

def survive_the_cavern(troll, cavern):
    """
    Returns the surviving goats in the cavern (stack), if any.
    """
    
    print("STAGE 1: BATTLE WITH THE TROLL...")
        
    # push the goats into the cavern
    print("The troll blocks the cavern exit!")
    print("The goats must fight their way out in order to survive...")
    while not is_empty(cavern) and troll.hit_points > 0:
        goat = pop(cavern)
        print(goat.name, "prepares to do battle with the troll...")
        while troll.hit_points > 0 and goat.hit_points > 0:
            # goat strikes damage first
            print("\tTroll hit points:", troll.hit_points, 
                ",", goat.name, "hit points:", goat.hit_points)
            dmg_to_troll = get_goat_damage()
            troll.hit_points -= dmg_to_troll
            print("\t" + goat.name, "does", dmg_to_troll, "to troll")
            if (troll.hit_points > 0):
                dmg_to_goat = get_troll_damage()
                goat.hit_points -= dmg_to_goat 
                print("\tTroll does", dmg_to_goat, "to goat")
                
        if troll.hit_points <= 0:
            print(goat.name, "has defeated the Troll!")
            # put them back on the stack
            push(cavern, goat)
        else:
            print(goat.name, "has fallen!")
                
    # did anyone survive?
    print(str(size(cavern)), "goat/s survived the dark cavern...")

