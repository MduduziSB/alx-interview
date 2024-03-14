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


def primes_in_range(beg, end):
    """Returns a list of prime numbers in a range of [beg - end]."""
    primes = [i for i in range(beg, end+1) if is_prime(i)]
    return primes


def isWinner(x, nums):
    """Determines who the winner is between Maria and Ben"""
    maria_moves = 0
    ben_moves = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        if not primesSet:
            ben_moves += 1
            continue

        isMariaTurns = True

        while(True):
            if not primesSet:
                if isMariaTurns:
                    ben_moves += 1
                else:
                    maria_moves += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if maria_moves > ben_moves:
        return "Maria"

    if maria_moves < ben_moves:
        return "Ben"

    return None
