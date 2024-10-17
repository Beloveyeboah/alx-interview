#!/usr/bin/python3

"""
In a text file, there is a single character H.
"""


def minOperations(n):
    """Step 1: Check if n is less than or equal to 1
    # If yes, return 0 because it's impossible to have less than 1 'H'
    """

    if n <= 1:
        return 0

    # Step 2: Initialize the number of operations
    operations = 0
    # Step 3: Start with the smallest possible divisor
    divisor = 2
    # Step 4: Loop until n is reduced to 1
    while n > 1:
        # Step 5: Check if the current divisor can divide n completely
        while n % divisor == 0:
            # Step 6: Add the value of the divisor to the operations count
            operations += divisor
            # Step 7: Reduce n by dividing it by the divisor
            n = n // divisor
        # Step 8: Move on to the next possible divisor
        divisor += 1
    # Step 9: Return the total number of operations
    return operations
