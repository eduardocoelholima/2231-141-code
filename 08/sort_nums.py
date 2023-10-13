"""
file: sort_nums.py
author: bksteele
description:
    demonstrate sorting of large file of numbers
"""

import time

from insertion_sort import insertion_sort as isort_in_place

def test_sort( data ):
    result = data[:]
    isort_in_place( result )
    return result

# uncomment either of these to override test_sort
from merge_sort import merge_sort as test_sort
#from quick_sort import quick_sort as test_sort

def main():
    """
    pre-condition: sort function returns the sorted list
    """

    fname = input( "Enter a file of numbers to sort: " )
    if fname == "":
        return

    print( "processing", fname )
    with open( fname ) as fd:
        lst = [ int( line.strip()) for line in fd ]
        start = time.process_time()
        result = test_sort( lst)
        end = time.process_time()
        print( "list of length", len(lst)
             , "sorted in", end-start, "seconds")
        print( "front", result[:40])
        print()
        print( "rear", result[-40:])


if __name__ == "__main__":
    main()


