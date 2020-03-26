#!/usr/bin/python3

import sys

if len(sys.argv) > 1:
    divisor = int(sys.argv[1])
else:
    divisor = 3
 
for line in sys.stdin:
    x=int(line)
    if x % divisor == 0: print(x)

exit()
