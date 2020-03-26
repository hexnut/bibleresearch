#!/bin/sh

tfile=$(mktemp /tmp/foo.XXX)

echo "Three digit numbers that resolve in one pass:"
seq 100 999 | ./narcgen.py | grep "^[0-9]* \[[0-9]\{3\}\]" | tee $tfile

echo

echo "Three digit narcissistic numbers:"
cat $tfile | cut -d' ' -f 2 | sort | uniq -c | awk '{ print $2, $1}'
