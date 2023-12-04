#!/usr/bin/python3
#
# Read input from stdin and echo the unicode name of each character
#

import os,sys,unicodedata

if __name__ == "__main__":

    if len(sys.argv) != 1:
        print("Usage: (echo|cat *) | %s" % sys.argv[0])
        exit()

    for line in sys.stdin:
        for i in range(len(line)):
            c = line[i]
            if (c == '\n'): continue
            print(c,':',unicodedata.name(c))

    exit()
