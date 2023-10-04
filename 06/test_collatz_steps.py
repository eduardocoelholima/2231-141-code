from collatz_steps import collatz_steps as cs  # collatz_steps

"""
CSCI-141: Testing & Debugging
Author: RIT CS

Test unit for the collatz_steps module and its collatz_steps() function
for computing the number of steps for a Collatz number to converge at 1.
"""

def test_collatz_steps(name, n, expected):
    """
    Run a single test of collatz_steps.
    :param name: the name of the function being tested
    :param n: the starting N value
    :param expected: the expected result
    """
    result = cs(n)
    if result == expected:
        print(name, 'passed')
    else:
        print(name, 'failed; expected', expected, 'but got', result)

def run_tests():
    """
    Test cases for collatz_steps()
    """
    print('1 (expected)')
    test_collatz_steps('\ncollatz_steps(1)', 1, 1)
    print('2 1 (expected)')
    test_collatz_steps('\ncollatz_steps(2)', 2, 2)
    print('10 5 16 8 4 2 1 (expected)')
    test_collatz_steps('\ncollatz_steps(10)', 10, 7)
    print('21 64 32 16 8 4 2 1 (expected)')
    test_collatz_steps('\ncollatz_steps(21)', 21, 8)
    print('13 40 20 10 5 16 8 4 2 1 (expected)')
    test_collatz_steps('\ncollatz_steps(13)', 13, 10)

if __name__ == '__main__':
    run_tests()