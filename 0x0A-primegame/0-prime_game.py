#!/usr/bin/python3
"""Prime number module"""


def sieve_of_eratosthenes(n):
    """This method finds all prime numbers up to n"""
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n+1) if primes[i]]


def isWinner(x, nums):
    """This function finds who the winner is"""
    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        num_primes = len(primes)

        if num_primes % 2 == 0:
            winners["Ben"] += 1
        else:
            winners["Maria"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return None
