#!/usr/bin/python3

import sys,unicodedata

def print_unicode(fn):
    # Parse a text and look for matches
    f = open(fn, "r")

    for line in f:
        for i in range(len(line)):
            c = line[i]
            print(c, unicodedata.name(c))

    f.close()
    exit()


if __name__ == "__main__":

    if len(sys.argv) != 1:
        print("Usage: %s" % sys.argv[0])
        exit()

    base = "/home/stephen/Sync/Research/"

    #fn = base + "gen1-1.txt"
    fn = base + "john1-1.txt"
    d = print_unicode(fn)



