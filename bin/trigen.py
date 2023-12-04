#!/usr/bin/python3

import sys

arg_o = None
if len(sys.argv) > 1:
    arg_o = sys.argv[1]
    if arg_o != "-o":
        print("Usage: %s -o" % sys.argv[0])
        exit()

print ("Centered triangular numbers")
for line in sys.stdin:
    n = int(line)
    r = int((n * (n + 1)) / 2)
    o = (2 * (n - 1) + 1) + n-2
    if arg_o is None:
        print("%3d:%5d" % (n,r))
    else:
        print("%3d:%5d%4d" % (n,r,o))

exit()
