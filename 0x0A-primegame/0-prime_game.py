#!/usr/bin/python3
"""Prime number module"""


def is_prime(num):
    """This module computes all the prime numbers up num"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determines who the winner is between Maria and Ben"""
    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        maria_moves = 0
        ben_moves = 0

        for i in range(2, n + 1):
            if is_prime(i):
                if maria_moves == ben_moves:
                    maria_moves += 1
                else:
                    ben_moves += 1

        if maria_moves > ben_moves:
            winners["Maria"] += 1
        elif ben_moves > maria_moves:
            winners["Ben"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    if winners["Ben"] > winners["Maria"]:
        return "Ben"

    return None
