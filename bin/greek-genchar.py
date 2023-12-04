#!/usr/bin/python3

import os,re,sys,unicodedata

def find_unicode_chars(u_name, start, stop):
    # Print the unicode values that match a name
    u_list = []

    for x in range(start,stop):
        c = chr(x)
        try:
            un = unicodedata.name(c)
            if un.find('LETTER ' + u_name) > 0 or un.find('LETTER FINAL ' + u_name) > 0:
                u_list.append(c)
                #print(un)
        except ValueError:
            continue

    return(u_list)

def gen_greek_chartable(fp):

    o_cnt = 0
    (start1, stop1, start2, stop2) = (0x370, 0x400, 0x1F00, 0x1FFF)

    # Open the file containing our table values
    if_name = fp + "/greek-base.csv"
    in_f = open(if_name, "r")

    # Open the file to write our unicode characters
    of_name = fp + "/greek-alphabet.csv"
    out_f = open(of_name, "w")

    # Header line
    out_f.write('GREEK CHARACTER SET\n')

    # Loop to build our unicode table for greek chars
    for line in in_f:
        m = re.match( r'(\w+)\s+(\d+)', line, flags=0)
        if m:
            char_name = m.group(1)
            char_val = m.group(2)
            l_main = find_unicode_chars(char_name, start1, stop1)
            l_ext  = find_unicode_chars(char_name, start2, stop2)
            ul = l_main + l_ext

            # Write a row to our output file
            o_line = '%-9s  %-5s ' % (char_name, char_val)
            for c in l_main:
                o_line += c + ' '
            for c in l_ext:
                o_line += c + ' '
            out_f.write(o_line + '\n')
            o_cnt += 1

    in_f.close()
    out_f.close()

    return(o_cnt)

if __name__ == "__main__":

    fp = os.path.expanduser('~') + "/Sync/Research/"
    f_count = gen_greek_chartable(fp)
    print('%d %s' % (f_count, 'output records written'))

    exit()
