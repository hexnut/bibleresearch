#!/usr/bin/python3

import sys
import math

def prime_factorize(n):
    factors = []
    number = math.fabs(n)

    if number == 1:
        return("1")

    while number > 1:
        factor = get_next_prime_factor(number)
        factors.append(factor)
        number /= factor

    # Need one negative factor for n < 0
    if n < -1:
        factors[0] = -factors[0]

    s = " ".join(str(x) for x in factors)
    return s

def get_next_prime_factor(n):
    if n % 2 == 0:
        return 2

    # Only need to check odd values up to sqrt(n) for primality
    for x in range(3, int(math.ceil(math.sqrt(n)) + 1), 2):
        if n % x == 0:
            return x

    return int(n)

if __name__ == "__main__":
    s_arg = 0

    try:
        s_arg = sys.argv.index("-s")
    except ValueError:
        pass

    if len(sys.argv) == 3:
        n = int(sys.argv[2])
        print("%s" % prime_factorize(n))
    elif len(sys.argv) == 2 and s_arg == 0:
        n = int(sys.argv[1])
        print("%d: %s" % (n,prime_factorize(n)))
    else:
        for line in sys.stdin:
            for n in line.split():
                n = int(n)
                if (s_arg):
                    print("%s" % prime_factorize(n))
                else:
                    print("%d: %s" % (n,prime_factorize(n)))

