#!/usr/bin/python3

import math
import sys


def semiprime(num):
    cnt = 0

    for n in range(2, int(math.sqrt(num)) + 1):
        while num % n == 0:
            num /= n
            cnt += 1  # Increment count of prime number

        # Break loop if count is greater than 2
        if cnt >= 2:
            break

    if num > 1:
        cnt += 1

    return cnt == 2


# Find semiprimes and print them
i = 0
print("Semi-prime numbers")
for line in sys.stdin:
    i += 1
    sp = int(line)
    if semiprime(sp) is True:
        print("%3d: %3d" % ((i+1), sp))

sys.exit()
