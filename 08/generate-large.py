"""
description: test file generator for big lists of integers
language: python3
author: sean strout
contributor: ben k steele
"""

from random import randint

NUM_VALUES = input( "enter size of file: " )
if NUM_VALUES == "":
    NUM_VALUES = 1000000
else:
    NUM_VALUES = int( NUM_VALUES)

MAX_NUMBER = 100000

fileName = input( "enter test case file name: (will append)" )

if fileName[1:] != '':
    inFile = open( fileName, "a" )
    for i in range(1, NUM_VALUES+1 ):
        numStr = str(i) # str( randint( -MAX_NUMBER, MAX_NUMBER ) )
        inFile.write( numStr + "\n")
    inFile.close()

