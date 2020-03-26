#!/usr/bin/python3
import sys

primeList=[];

def is_prime(p):

    if (p <= 0 or p == 1 or p == 4): return False;

    prime = True;
    for j in range(2, int(p/2)):
        if p % j == 0:
            prime=False;
            continue;

    return prime;

# Main loop to find primes
for line in sys.stdin:
    i = int(line)
    if is_prime(i) == True:
        primeList.append(i)

# Print a formatted list
for i in range(0, len(primeList)):
    p = primeList[i]
    print(str(i+1) + ": " + str(p), end='')
    if (p+6 in primeList):
        #print "s(" + str(p) + "," + str(p+6) + ")"
        print("(s)")
    else:
        print()
