#!/usr/bin/python3

import sys
from math import pow

def narcissist(num,loopcnt=12):

    tl = []
    ts = list(str(num))
    for j in range(1,loopcnt+1):
        tmp = 0
        for digit in ts:
            tmp += int(pow(int(digit),3))
        tl += [tmp]
        if (tmp in [1,153,370,371,407]):
            return(tl)
        ts = list(str(tmp))
    return tl

for line in sys.stdin:
    n = int(line)
    r = narcissist(n,15)
    print(n,r)

exit()
