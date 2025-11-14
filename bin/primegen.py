#!/usr/bin/python3
import getopt
import sys

primeList = []

def is_prime(p):

    if p in (0, 1):
        return False
    if p in (2, 3):
        return True

    prime = True
    for j in range(2, int(p/2)+1):
        if p % j == 0:
            prime = False
            continue

    return prime


# Check command line args
try:
    opts, args = getopt.getopt(sys.argv[1:], "hcs")
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

(arg_c, arg_s) = (False, False)
for opt, arg in opts:
    if opt == "-h":
        print('usage: primegen.py [-hcs]')
        print('\t-h help')
        print('\t-c composite numbers')
        print('\t-s suppress indexes')
        sys.exit()
    elif opt == "-c":
        arg_c = True
    elif opt == "-s":
        arg_s = True

if arg_c:
    D = "Composite"
else:
    D = "Prime"

# Main loop to find primes
print("%s numbers" % D)
for line in sys.stdin:
    ls = line.split()
    for s in ls:
        i = int(s)
        if i == 1:
            continue
        if is_prime(i) != arg_c:
            primeList.append(i)

# Print a formatted list
for i in range(0, len(primeList)):
    p = primeList[i]
    if arg_s is False:
        print("%3d: %3d" % ((i+1), p), end='')
    else:
        print("%d" % (p), end='')
    print()
