"""
CSCI-141: Testing & Debugging
Author: RIT CS

The Collatz conjecture defining a sequence for a positive integer N.
"""

def collatz(n):
    """
    Compute the collatz for N.
    :param n: positive integer N
    :return: its collatz number
    """
    if n == 1:
        return 1
    elif n % 2 == 0:  # N is even
        return collatz(n // 2)
    else:             # N is odd
        return collatz(3 * n + 1)

def main():
    """
    The main function prompts the user for an integer and computes
    its Collatz value.
    """
    n = int(input('Enter n: '))
    if n <= 0:
        print('N > 0')
    else:
        print('collatz(', n, ')=', collatz(n))

if __name__ == '__main__':
    main()