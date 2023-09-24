"""
file: semordnilap.py
language: python3
author: ben k steele, bks@cs.rit.edu
description: print the reverse of a word to see if it is another valid word.
date: 07/2017
purpose: strings lecture
"""

def reverse( st):
    """
    reverse: String -> String
    reverse returns the reverse of the string st.
    """
    result = ""
    for ch in st:
        result = ch + result
    return result

def reverse_by_index( st):
    """
    reverse_by_index: String -> String
    reverse_by_index returns the reverse of the string st using range().
    """
    result = ""
    for i in range( len(st) ):
        result = st[i] + result
    return result

def test_reverse( func):
    """
    test_reverse : (Function : String -> String) -> Void, IO
    test_reverse tests the passed-in function
    """
    # demonstrates the ability to pass a function in Python
    print( 'Begin testing', str( func))
    print( func( '') == "", end='\t')
    print( func( 'a') == "a", end='\t')
    print( func( 'ab') == "ba", end='\t')
    print( func( 'abc') == "cba", end='\t')
    print( func( 'ab d') == "d ba", end='\t')
    print( '\nEnd testing')

def main():
    """
    main prompts for a word and prints the reverse of the sequence.
    """
    word = input( "Enter a word to reverse: ")
    print( "word:", word)
    print( "reverse:", reverse( word))


if __name__ == "__main__":
    #test_reverse( reverse)
    #test_reverse( reverse_by_index)
    main()

