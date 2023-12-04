#!/usr/bin/python3

import sys

# Split a string of digits and sum them
lsum = 0
for line in sys.stdin:
    digits = list(line)
    digits.remove("\n")
    for i in digits:
        lsum += int(i)
print("I saw %d digits for a total sum of %d" % (len(digits),lsum))

exit()
