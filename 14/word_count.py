"""
file: word_count.py
description: Word Count Program for CSCI 141
language: python3.7
author: RIT CS Instructors
"""

# import the functions needed from the hashtable.py module.

from hashtable import *


def word_count( hashtable, filename ):
    """
        Record the frequency of all words in the named file in the hashtable.
        word_count : HashTable String -> HashTable
    """

    # Read the words of the text file into the word count table.
    fd = open( filename )
    for line in fd:
        for word in line.split():
            # using a regular expression argument to strip(),
            # strip out punctuation and convert token to lower-case.
            word = word.strip(",.\"\';:-!?").lower()
            if has( hashtable, word ):
                count = get( hashtable, word )
                put( hashtable, word, count + 1 )
            else:
                put( hashtable, word, 1 )

    fd.close()          # closing the file is a 'good practice'.
    return hashtable

def print_summary( hashtable ):
    """
    print_summary prints a summary of information about the table contents.
    print_summary : HashTable -> NoneType
    """

    # Find the most common word in the text file.
    total = 0
    maxword = ""
    maxcount = 0
    for key in keys( hashtable ):
        thiscount = get( hashtable, key )
        total += thiscount
        if thiscount > maxcount:
            maxcount = thiscount
            maxword = key

    print( "There are " + str( len( keys( hashtable ) ) ) + " unique words." )
    print( "Total words:", total )
    print( '"' + maxword + "\" appeared ", str( maxcount ),
           " times, more than any other word." )

def print_table( hashtable ):
    """
        print_table : HashTable -> NoneType
        Print the contents of the given hash table.
        Each key/value pair is displayed in parentheses, tuple-style.
        All pairs appear on a single line.
    """
    print( "Word Count Data ---------------" )
    ltext = 0
    for key in keys( hashtable ):
        txt = "(" + key + "," + str( get( hashtable, key ) ) + ")"
        ltext += len( txt )
        if ltext > 51:
            print( txt )
            ltext = 0
        else:
            print( txt, end=" " )
    print()


def main():
    capacity = int( input( "Enter capacity (-1 for default): " ) )
    hashtable = create_hash_table( hash, capacity )
    filename = input( "Enter filename: " )

    wordtable = word_count( hashtable, filename )
    print_summary( wordtable )

    while True:

        print( "Commands: k[ey] <word> f[ind] <word> q[uit] ? ", end=" " )
        response = input( ":- " )   # the displayed prompt
        query = response.split()

        if len( response ) == 0 or not response[0] in "fkq":
            print( response + " invalid. Please enter a command and a word." )
            response = ""
            continue

        if query[0] == "k":
            print( "( " + query[1] + " in text ) is " \
                   + str( has( wordtable, query[1] ) ) + "." )

        if query[0] == "f":
            if has( wordtable, query[1] ):
                print( query[1] + " appears " \
                       + str( get( wordtable, query[1] ) ) + " times." )
            else:
                print( query[1] + " in not in the text." )

        if query[0] == "q":
            break
    #
    answer = input( "Do you want to see the entire table?(y/n) " )
    if answer != "y":
        return
    print_table( wordtable )

# run the main program
main()
