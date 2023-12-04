#!/usr/bin/python3

import sys

FibArray = [0,1]

def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<=len(FibArray):
        return FibArray[n-1]
    else:
        tmpfib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(tmpfib)
        return tmpfib

if len(sys.argv) == 2:
    n = int(sys.argv[1]) + 1

arg_s = 0
if len(sys.argv) == 3 and sys.argv[1] == "-s":
    arg_s = 1
    n = int(sys.argv[2]) + 1

f = fibonacci(n)
print("fib(%d) = " % (n-1),end="")
if arg_s:
    print(f)
else:
    print(FibArray)
