#!/usr/bin/env python3
"""
N Queens Puzzle Solver
"""

import sys


def print_usage_and_exit():
    """ Print usage and exit with status 1 """
    print("Usage: nqueens N")
    sys.exit(1)


def is_integer(value):
    """ Check if value is an integer """
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_valid(board, row, col):
    """ Check if placing a queen at (row, col) is valid """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """ Solve the N queens problem and print all solutions """
    def backtrack(row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * N
    solutions = []
    backtrack(0)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()

    N = sys.argv[1]

    if not is_integer(N):
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
