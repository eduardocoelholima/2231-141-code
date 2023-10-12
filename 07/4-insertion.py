import random  # to use the shuffle function


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def insert(lst, mark):
    index = mark
    while index > -1 and lst[index] > lst[index + 1]:
        swap(lst, index, index + 1)
        index = index - 1


def insertion_sort(lst):
    for mark in range(len(lst) - 1):
        insert(lst, mark)


def main():
    # create shuffled data
    N = int(input("Number of elements: "))
    data = []
    for i in range(0, N):
        data = data + [i]
    random.shuffle(data)
    print("Shuffled data:", data)

    insertion_sort(data)
    print("Sorted data:", data)


if __name__ == "__main__":
    main()
