#!/usr/bin/python3

import os,re,sys,unicodedata,getopt

def import_alphabet(fn):
    # Initialize our list of tuples data structure
    g_list = []
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
        g_list.append(row)
        linecnt += 1

    # Clean up and return
    f.close()
    return(g_list)

def numeric_lookup(g_table, c):
    oda = 0
    val = 0

    for li in g_table:
        if c in li:
            oda = int(li[0])
            val = int(li[2])
            break;

    return(oda,val)

def parse_chars(g_table):
    # Init local vars
    (gw, lc, wc) = ('', 0, 0)

    # Parse a text character by character via stdin
    for line in sys.stdin:
        if line[0] == "#":
            #print(line, end='')
            continue

        wordlist = line.split()
        wc = len(wordlist)

        for word in wordlist:
            for c in word:
                (o,v) = numeric_lookup(g_table, c)
                # Iota subscript adjustment
                try:
                    un = unicodedata.name(c)
                    if (un.find('YPOGEGRAMMENI') > 0):
                        lc += 1
                        o += 9
                        print("10 ", end="")
                except ValueError:
                    pass
                print("%d " % (v), end="")
            print()

    return()

def parse_words(g_table,arg_o,arg_n):
    # Init local vars
    (w_sum, wo_sum, l_sum, o_sum, lc, wc) = (0, 0, 0, 0, 0, 0)

    # Parse a text character by character via stdin
    for line in sys.stdin:
        if line[0] == "#":
            #print(line, end='')
            continue

        wordlist = line.split()
        wc = len(wordlist)

        for word in wordlist:
            for c in word:
                (o,v) = numeric_lookup(g_table, c)
                # Iota subscript adjustment
                try:
                    un = unicodedata.name(c)
                    if (un.find('YPOGEGRAMMENI') > 0):
                        lc += 1
                        o += 9
                        v += 10
                except ValueError:
                    pass
                w_sum += v
                wo_sum += o
                lc += 1
                o_sum += o
                l_sum += v

            if arg_o:
                if arg_n:
                    print("%d" % (wo_sum))
                else:
                    print("%-12s%7d" % (word, wo_sum))
            else:
                if arg_n:
                    print("%d" % (w_sum))
                else:
                    print("%-12s%7d" % (word, w_sum))
            (w_sum,wo_sum) = (0,0)

    return(lc, wc, l_sum, o_sum)

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hnol")
    except getopt.GetoptError as err:
        print (err)
        sys.exit(2)

    (arg_n, arg_o, arg_l) = (False, False, False)
    for opt, arg in opts:
        if opt == "-h":
            print ('usage: greek-parser.py [-hnol]')
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

    # Import a table for character lookups
    base = os.path.expanduser('~') + "/Sync/Research/"
    fn = base + "greek-alphabet.csv"
    g_table = import_alphabet(fn)

    if arg_l == True:
        # Parse hebrew chars from stdin
        parse_chars(g_table)
    else:
        # Parse hebrew words from stdin
        (l_cnt, w_cnt, t_sum, o_sum) = parse_words(g_table,arg_o,arg_n)
        if arg_n == False:
            if arg_o:
                print('Text contains %d words and %d letters for an ordinal value of %d' % (w_cnt, l_cnt, o_sum))
            else:
                print('Text contains %d words and %d letters for a total value of %d' % (w_cnt, l_cnt, t_sum))

    exit()
