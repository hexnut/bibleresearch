#!/usr/bin/python3

import os,re,sys,unicodedata,getopt

def import_alphabet(fn):       
    # Initialize our list of tuples data structure            
    h_list = []
    linecnt = 0

    # Open the file containing our table values     
    f = open(fn, "r")

    # Create a list of tuples containing our table of characters
    for line in f:
        # Skip over the first line
        if linecnt == 0:
            linecnt += 1
            continue

        row = [linecnt] + line.split()
        h_list.append(row)
        linecnt += 1

    # Clean up and return
    f.close()
    return(h_list)

def numeric_lookup(h_table, c):             
    oda = 0
    val = 0

    for li in h_table:
        if c in li:
            oda = int(li[0])
            val = int(li[2])
            break;

    return(oda,val)

def parse_chars(h_table):
    # Init local vars
    (gw, lc, wc) = ('', 0, 0)

    # Parse a text character by character via stdin
    for line in sys.stdin:
        if line[0] == "#":
            # print(line, end='')
            continue

        wordlist = line.split()
        wc = len(wordlist)

        for word in wordlist:
            for c in word:
                (o,v) = numeric_lookup(h_table, c)
                if v==0:
                    continue
                if arg_o:
                    print("%d " % (o), end="")
                else:
                    print("%d " % (v), end="")
            print()

    return()

def parse_words(ht,arg_n,arg_o):
    # Init local vars
    (w_sum, wo_sum, l_sum, o_sum, lc, wc) = (0, 0, 0, 0, 0, 0)

    # Parse a text via stdin
    for line in sys.stdin:
        if line[0] == "#":
            # print(line, end='')
            continue

        wordlist = line.split()
        wc = len(wordlist)

        for word in wordlist:
            for c in word:
                (o,v) = numeric_lookup(ht, c)
                if v == 0:
                    continue
                lc += 1
                o_sum += o
                l_sum += v
                w_sum += v
                wo_sum += o
            if arg_o:
                if arg_n:
                    print("%d" % (wo_sum))
                else:
                    print("%-10d %s" % (wo_sum, word))
            else:
               if arg_n:
                    print("%d" % (w_sum))
               else:
                    print("%-10d %s" % (w_sum, word))
            (w_sum,wo_sum) = (0,0)

        return(wc,lc,l_sum,o_sum)

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hnol")
    except getopt.GetoptError as err:
        print (err)
        sys.exit(2)

    (arg_n, arg_o, arg_l) = (False, False, False)
    for opt, arg in opts:
        if opt == "-h":
            print ('usage: hebrew-parser.py [-hnol]')
            print('\t-h help')
            print('\t-n numeric output only')
            print('\t-o calculate ordinal values')
            print('\t-l enumerate letter values')
            sys.exit()
        elif opt == "-n":
            arg_n = True
        elif opt == "-o":
            arg_o = True
        elif opt == "-l":
            arg_l = True

    # Create an array for character lookups
    base = os.path.expanduser('~') + "/Sync/Research/"
    fn = base + "hebrew-alephbet.csv"
    ht = import_alphabet(fn)

    if arg_l == True:
        # Parse hebrew chars from stdin
        parse_chars(ht)
    else:
        # Parse hebrew words from stdin
        (wc,lc,l_sum,o_sum) = parse_words(ht,arg_n,arg_o)
        if arg_n == False:
            if arg_o:
                print('Text contains',wc,'words and',lc,'letters for an ordinal value of',o_sum)
            else:
                print('Text contains',wc,'words and',lc,'letters for a total value of',l_sum)

    exit()
