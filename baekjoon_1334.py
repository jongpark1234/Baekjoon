from sys import stdin
from math import *
def isprime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True
n = stdin.readline().rstrip()
while True:
    palindrome = True
    for i in range(len(n) // 2):
        if n[i] != n[-(i + 1)]:
            palindrome = False
            break
    if palindrome and isprime(int(n)):
        print(n)
        break
    n = str(int(n) + 1)