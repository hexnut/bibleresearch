#!/usr/bin/python3

import sys

n = 0
s = 0
for line in sys.stdin:
    for i in range( len(line) ):
        if line[i] not in (' ','\n'):
            d = int(line[i])
            n += 1
            p = (n * d)
            s += (n * d)
            print("%d x %d:\t%d" % (d,n,p))

    #print(n,p)
    print("Total:\t%d" % s)

exit()
