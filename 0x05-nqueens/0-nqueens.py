#!/usr/bin/python3
""" N queens puzzle module """
import sys


def is_safe(board, row, col):
    """ Traces the queen """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens_util(N, row, board, solutions):
    """ Appends the board """
    if row == N:
        solutions.append(list(enumerate(board)))
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(N, row + 1, board, solutions)


def solve_nqueens(N):
    """ solves nqueens' puzzle """
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens_util(N, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_nqueens(sys.argv[1])
