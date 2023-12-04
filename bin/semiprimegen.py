#!/usr/bin/python3
import math,sys

def semiprime(num):
    cnt = 0

    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num /= i
            cnt += 1 # Increment count of prime number

        # If count is greater than 2,
        # break loop
        if cnt >= 2:
            break
    # If number is greater than 1, add it to
    # the count variable as it indicates the
    # number remain is prime number
    if(num > 1):
        cnt += 1

    # Return '1' if count is equal to '2' else
    # return '0'
    return cnt == 2

spl=[];

# Main loop to find semi primes
print("Semi-prime numbers")
for line in sys.stdin:
    i = int(line)
    if semiprime(i) == True:
        spl.append(i)

# Print a formatted list
for i in range(0, len(spl)):
    p = spl[i]
    print("%3d: %3d" % ((i+1),p))
