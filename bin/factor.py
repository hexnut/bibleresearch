#!/usr/bin/python

import sys
import math

def prime_factorize(n):
    factors = []
    number = math.fabs(n)

    while number > 1:
        factor = get_next_prime_factor(number)
        factors.append(factor)
        number /= factor

    if n < -1: # If we'd check for < 0, -1 would give us trouble
        factors[0] = -factors[0]

    s = ", ".join(str(x) for x in factors)
    return s

def get_next_prime_factor(n):
    if n % 2 == 0:
        return 2

    for x in range(3, int(math.ceil(math.sqrt(n)) + 1), 2):
        if n % x == 0:
            return x

    return int(n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: %s <integer>" % sys.argv[0])
        exit()

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("'%s' is not an integer!" % sys.argv[1])
    else:
        print("%s" % (prime_factorize(number)))
