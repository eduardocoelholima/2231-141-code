"""
file: gruff.py
author: CS @ rit.edu

Billy Goats Gruff is an adventure of a herd of goats trying to 
escape a cave blocked by an evil troll. If there are enough goats, 
and they are strong enough to defeat the troll, then the goats
leave the cave to cross a bridge to a paradise of berries.
The bridge, however, may fall down if too many trolls get on at once.
As long as the bridge lasts, the goats cross to the berry field.
Any goats on the bridge fall into a gorge if the bridge breaks,
and any goats stuck waiting to cross are stranded.

This module is part of a lecture on the stack and queue datatypes.
It introduces Stack and Queue data structures implemented using a
mutable linked node sequence data structure, an alternative to Python lists.

Data Types:
    Troll
    Goat
"""

from random import randint
from dataclasses import dataclass
from cavern import survive_the_cavern
from bridge import cross_the_bridge
from cs_queue import make_empty_queue, front, dequeue, is_empty
from cs_stack import make_empty_stack, push, size


"""
generate a random hitpoint strength of the troll in one game.
"""
TROLL_HITPOINTS = randint(1000, 2000)

@dataclass
class Troll:
    hit_points: int
       
def make_troll():
    """
    Create and return a troll with random strength.
    """
    return Troll(TROLL_HITPOINTS)
    
def get_goat_hit_points():
    """
    generate a random hitpoint strength of one goat in one game.
    """
    return randint(100, 200)
    
def get_goat_weight():
    """
    generate a random weight of one goat in one game.
    """
    return randint(50, 300)

# define the Goat data type.
@dataclass
class Goat:
    name: str
    hit_points: int
    weight: int
    
def mkGoat(id):
    """
    Create and return a goat with random strength.
    """
    return Goat("Goat #" + str(id), get_goat_hit_points(), get_goat_weight())
    
def welcome():
    """
    print the welcome banner to the adventure.
    """
    print("Billy Goats Gruff v1.0")
    print("-------------")
    print("Welcome to the field.  Goats yearn for the berries on the hills.")

def endingCredits(troll, goats):
    """
    print the information on the end of the adventure.
    """
    if troll.hit_points > 0:
        print("The troll, with", troll.hit_points,
            "hit points remaining, claims victory!")
    elif goats.size > 0:
        print(str(goats.size), "goats reach the berries and eat their fill!")
        while not is_empty(goats):
            goat = front(goats)
            dequeue(goats)
            print(goat.name, ", with", goat.hit_points,
                "hit points remaining, eats berries!")
        print("The goats live happily ever after!")
    print("THE END.")
    
def main():
    """
    play the adventure game.
    """

    welcome()
    # spawn the troll!
    troll = make_troll()
    print("The troll spawns somewhere in front of the bridge with", 
        troll.hit_points, "hit points...")
        
    # create the goats and push them into the cavern
    numGoats = int(input("How many goats? "))
    cavern = make_empty_stack()
    for id in range(1, numGoats+1):
        goat = mkGoat(id)
        print("Goat", goat.name, "with", goat.hit_points,
            "hit points and", goat.weight, "weight, enters the cavern...")
        push(cavern, goat)
        
    # get the berries!
    survive_the_cavern(troll, cavern)
    meadow = make_empty_queue()
    if size( cavern ) > 0:
        input("Hit enter to continue...")
        cross_the_bridge(cavern, meadow)

    endingCredits(troll, meadow)
   
# run the game
main()

