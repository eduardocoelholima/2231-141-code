""" 
description: Word Count Program for CSCI 141
file: word_count.py
language: python3.7
author: RIT CS Instructors
"""

from hashtable import *

def word_count( filename ):
    """Report on the frequency of different words in the
       file named by the argument.
    """
    hashtable = create_hash_table( hash , 1000 )

    # Read the words of the text file into the word count table.
    with open( filename ) as infile:
        for line in infile:
            for word in line.split():
                word = word.strip(",.\"\';:-!?").lower()
                if has( hashtable, word ):
                    count = get( hashtable, word )
                    put( hashtable, word, count + 1 )
                else:
                    put( hashtable, word, 1 )
    return hashtable

def print_summary( hashtable ):
    """
    print_summary : HashTable -> NoneType
    print_summary prints a summary of information about the table contents.
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

def print_table( hash_table ):
    """Print the contents of the given hash table.
       Each key/value pair is displayed in parentheses, tuple-style.
       All pairs appear on a single line.
    """
    answer = input( "Do you want to see the entire table?(y/n) " )
    if answer != "y":
        return
    print( "Word Count Data ---------------" )
    ltext = 0
    for key in keys( hash_table ):
        txt = "(" + key + "," + str( get( hash_table, key ) ) + ")"
        ltext += len( txt )
        if ltext > 51:
            print( txt )
            ltext = 0
        else:
            print( txt, end=" " )
    print()

def main():
    filename = input( "Enter filename: " )
    wordtable = word_count( filename )
    print_summary( wordtable )
    while True:
        print( "Commands: k[ey] <word> f[ind] <word> q[uit] ? ", end=" " )
        response = \
            input( ":- " )
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
    print_table( wordtable )

main()

