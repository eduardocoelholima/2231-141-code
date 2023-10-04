"""
CSCI-141: Testing & Debugging
Author: RIT CS

Test unit for the collatz module and its collatz() function for computing
a Collatz number.
"""

import collatz     # collatz

def test_collatz(name, n, expected):
    """
    Run a single tests of collatz.
    :param name: the name of the function we are testing
    :param n: the starting N value
    :param expected: the expected result
    """
    result = collatz.collatz(n)
    if result == expected:
        print(name, 'passed')
    else:
        print(name, 'failed; expected', expected, 'but got', result)

def run_tests():
    """
    Test cases for collatz().
    """
    # test collatz() with N=1..11
    for i in range(1, 11):
        name = 'collatz(' + str(i) + ')'
        test_collatz(name, i, 1)

if __name__ == '__main__':
    run_tests()