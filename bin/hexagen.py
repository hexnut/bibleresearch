#!/usr/bin/python3

import sys

arg_o = 'Simple hexagons'
arg_co = 'Centered hexagons'
arg_a = 'Simple hexagrams'
arg_ca = 'Centered hexagrams'

if len(sys.argv) != 2:
    print("Usage: %s <arg>" % sys.argv[0])
    print(' -o: ', arg_o)
    print(' -co:', arg_co)
    print(' -a: ', arg_a)
    print(' -ca:', arg_ca)
    sys.exit()

s = sys.argv[1]
# Use the cmd line arg to define a figurate function
if s == "-o":
    print(arg_o)
    F = 'int((2*N * (2*N - 1)) / 2)'
elif s == "-co":
    print(arg_co)
    F = 'int(1 + 6 * (0.5*N * (N - 1)))'
elif s == "-a":
    print(arg_a)
    F = 'int((12 * (N-1)))'
elif s == "-ca":
    print(arg_ca)
    F = 'int((6*N * (N-1) + 1))'
else:
    F = None

if F is None:
    sys.exit()

R = 0
for line in sys.stdin:
    N = int(line)
    R = eval(F)
    print("%3d:%5d" % (N, R))

sys.exit()
