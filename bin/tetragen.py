#!/usr/bin/python3

import sys

for line in sys.stdin:
    n = int(line)
    r = int((n * (n + 1) * (n + 2)) / 6)
    print(n,r)

exit()
