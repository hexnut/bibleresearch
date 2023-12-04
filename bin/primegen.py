#!/usr/bin/python3
import sys

primeList=[];

def is_prime(p):

    if p in (0,1): return False;
    if p in (2,3): return True

    prime = True;
    for j in range(2, int(p/2)+1):
        if p % j == 0:
            prime=False;
            continue;

    return prime;

# Check command line args
arg_c = None
if len(sys.argv) > 1:
    arg_c = sys.argv[1]
    if arg_c != "-c":
        print("Usage: %s -c" % sys.argv[0])
        exit()

if arg_c:
    prime_flag = False
    desc = "Composite"
else:
    prime_flag = True
    desc = "Prime"

# Main loop to find primes
print("%s numbers" % desc)
for line in sys.stdin:
    ls = line.split()
    for s in ls:
        i = int(s)
        if i == 1:
            continue
        if is_prime(i) == prime_flag:
            primeList.append(i)

# Print a formatted list
for i in range(0, len(primeList)):
    p = primeList[i]
    print("%3d: %3d" % ((i+1),p), end='')
    print()
    #if (p + 6 in primeList):
        #print(" (s)")
    #else:
        #print()
