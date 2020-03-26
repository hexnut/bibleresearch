#!/usr/bin/python3

import sys

for line in sys.stdin:
    n = int(line)
    r = int((n * (n + 1)) / 2)
    print(n,r)

exit()
