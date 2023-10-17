"""
CSCI-141: Testing & Debugging
Author: RIT CS

Print the sequence and count the number of steps it takes the Collatz
conjecture to converge to N=1.
"""

def collatz_steps(n):
    """
    Count the number of steps for computing a Collatz number until
    it converges at 1.  Also print each number in the sequence.
    :param n: positive integer N
    :return: the number of steps
    """
    print(n, end=' ')
    if n == 1:
        return 1
    elif n % 2 == 0:  # N is even
        return 1 + collatz_steps(n // 2)
    else:             # N is odd
        return 1 + collatz_steps(3 * n + 1)

def main():
    """
    The main function prompts the user for an integer and prints the sequence
    while computing the number of steps it takes for it's Collatz number to
    converge at 1.
    """
    n = int(input('Enter N: '))
    if n <= 0:
        print('N > 0')
    else:
        print('\ncollatz(', n, ')=', collatz_steps(n))

if __name__ == '__main__':
    main()
