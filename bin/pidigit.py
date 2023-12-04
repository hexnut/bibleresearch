#!/usr/bin/env python3
# Find PI to the Nth Digit

import sys

def calcPi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    # yield digit
                    yield n
                    # insert period after first digit
                    if counter == 0:
                            yield '.'
                    # end
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: %s <integer>" % sys.argv[0])
        exit()

    l_flag=0
    if sys.argv[1] == "-l":
        l_flag = 1
        n = int(sys.argv[2])
    else:
        n = int(sys.argv[1])

    # Calls CalcPi with the given limit
    pi_digits = calcPi(n)
    i = 0

    # Prints the output of calcPi generator function
    l_pos = 1
    for d in pi_digits:
        if (l_flag):
            if l_pos < n + 2:
                print(d)
            else:
                print(d, end='')
            l_pos += 1
        else:
            print(d, end='')
