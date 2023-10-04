"""
file: lengths.py
language: python3
author: ben k steele, bks@cs.rit.edu
description: functions computing lengths of string values.
date: 07/2017
purpose: introduction to strings
"""

def length( st):
    """
    length: String -> Integer
    length returns the length of the string st.
    """
    # duplicates functionality of Python's len() function to show iteration.
    size = 0
    for ch in st:
        size = size + 1
    return size

def longest( st):
    """
    longest: String -> Integer
    longest returns the length of longest sequence of non-whitespace symbols.
    longest recognizes only space, tab and newline characters as whitespace.
    """
    size = 0
    cursize = 0
    for ch in st:
        if ch == ' ' or ch == '\n' or ch == '\t':
            cursize = 0
        else:
            cursize += 1
        if cursize > size:
            size = cursize
    return size



# Run tests only if run as the main program

if __name__ == "__main__": # run tests in this case
    import test_lengths as tester
    tester.test_lengths()

