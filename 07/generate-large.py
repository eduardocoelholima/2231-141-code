"""
description: test file generator for Store Locator problems
language: python3
author: sean strout
contributor: ben k steele
"""
# Generate the large test data file for the k-select problem.

from random import randint

MAX_VALUES = 10000
MAX_DISTANCE = 100000

fileName = input( "enter test case file name: (will append)" )

if fileName[1:] != '':
    inFile = open( fileName, "a" )
    for i in range(1, MAX_VALUES+1 ):
        numStr = str( randint( 0, MAX_DISTANCE ) )
        inFile.write( "Location_" + str(i) + " " + numStr + "\n")
    inFile.close()

