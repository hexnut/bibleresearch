#!/usr/bin/python3

import re,sys,unicodedata

def import_alphabet(fn, case='lower'):
    # Open the file containing the alphabet
    f = open(fn, "r")

    # Initialize dictionary for characters and numeric values
    d = {}

    # Loop to assign numeric values to each letter in the dictionary
    for line in f:
        m = re.match( r'(\w+)\s+(\d+)\s+(.) (.)', line, flags=0)
        if m:
            if case == "lower":
                k = m.group(4)
            else:
                k = m.group(3)
            val = m.group(2)
            d[k] = val

    # Clean up and quit
    f.close()

    return(d)

def parse_text(fn, d):
    # Parse a text and look for matches
    f = open(fn, "r")

    for line in f:
        for i in range(len(line)):
            c = line[i]
            if c in d.keys():
                print(d[c], ":", c)
            else:
                print(c)
    f.close()
    exit()


if __name__ == "__main__":

    if len(sys.argv) != 1:
        print("Usage: %s" % sys.argv[0])
        exit()

    base = "/home/stephen/Sync/Research/"

    #fn = base + "greek-alphabet.csv"
    fn = base + "hebrew-alephbet.csv"
    d = import_alphabet(fn,'lower')
    print(d.keys())

    fn = base + "gen1-1.txt"
    parse_text(fn,d)

    exit()
