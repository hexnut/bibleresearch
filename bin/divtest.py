#!/usr/bin/python3
"""Division test """

import sys

if len(sys.argv) > 1:
    DIV = int(sys.argv[1])
else:
    DIV = 3

for line in sys.stdin:
    x = int(line)
    if x % DIV == 0:
        print(x)

sys.exit()
