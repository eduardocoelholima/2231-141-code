from sorts import *
import random
import time
import sys


def sort_timer(sort_function, a_list):
    start = time.perf_counter()
    sort_function(a_list)
    end = time.perf_counter()
    return end - start


def main():
    # test all three on all types of data
    SIZE = 3000
    sys.setrecursionlimit(int(SIZE * 2))
    sorted = list(range(1, SIZE))
    reverse_sorted = list(range(SIZE, 1, -1))
    unsorted = sorted.copy()
    random.shuffle(unsorted)
    sorts = (insertion_sort, merge_sort, quick_sort)
    print('Size = ', SIZE)
    for sort in sorts:
        print(sort.__name__)
        data = {'Sorted': sorted.copy(), 'Reverse Sorted': reverse_sorted.copy(), 'Unsorted': unsorted.copy()}
        for item in data:
            print('\t' + str(item).ljust(20, '-') + '{:.4f}'.format(sort_timer(sort, data[item])))
        print()

    # face off just merge and quick on a  large set of unsorted data.
    SIZE = 40000
    sys.setrecursionlimit(int(SIZE * 1.1))
    sorted = list(range(1, SIZE))
    unsorted = sorted.copy()
    random.shuffle(unsorted)
    sorts = (merge_sort, quick_sort)
    print('Size = ', SIZE)
    for sort in sorts:
        print(sort.__name__)
        data = {'Unsorted': unsorted.copy()}
        for item in data:
            print('\t' + str(item).ljust(20, '-') + '{:.4f}'.format(sort_timer(sort, data[item])))
        print()

main()
