#!/usr/bin/python3
"""Split a string of digits and sum them"""

import sys

LS = 0
for line in sys.stdin:
    digits = list(line)
    digits.remove("\n")
    for i in digits:
        LS += int(i)
print("I saw %d digits for a total sum of %d" % (len(digits), LS))

sys.exit()
