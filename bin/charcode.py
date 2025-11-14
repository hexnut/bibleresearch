#!/usr/bin/python3
"""Read from stdin and echo the unicode name of each character"""

import sys
import unicodedata

if __name__ == "__main__":

    if len(sys.argv) != 1:
        print("Usage: (echo|cat *) | %s" % sys.argv[0])
        sys.exit()

    for line in sys.stdin:
        for i, char in enumerate(line):
            if char == '\n':
                continue
            print(char, ':', unicodedata.name(char))

    sys.exit()
