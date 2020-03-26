#!/usr/bin/python3

import sys

arg_o  = 'Simple hexagons'
arg_co = 'Centered hexagons'
arg_a  = 'Simple hexagrams'
arg_ca = 'Centered hexagrams'

if len(sys.argv) != 2:
    print("Usage: %s <arg>" % sys.argv[0])
    print(' -o: ', arg_o)
    print(' -co:', arg_co)
    print(' -a: ', arg_a)
    print(' -ca:', arg_ca)
    exit()

s = sys.argv[1]
# Use the cmd line arg to define a figurate function
if s == "-o":
    print(arg_o)
    f = 'int((2*n * (2*n - 1)) / 2)'
elif s == "-co":
    print(arg_co)
    f = 'int(1 + 6 * (0.5*n * (n - 1)))'
elif s == "-a":
    print(arg_a)
    f = 'int((12 * (n-1)))'
elif s == "-ca":
    print(arg_ca)
    f = 'int((6*n * (n-1) + 1))'
else :
    f = None

if (f is None):
    exit()

r = 0
for line in sys.stdin:
    n = int(line)
    r = eval(f)
    print(n,r)

exit()
