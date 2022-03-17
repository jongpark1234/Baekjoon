from math import factorial
from sys import stdin
while True:
    n = stdin.readline().rstrip()[::-1]
    result = 0
    if n == '0':
        break
    for i in reversed(range(len(n))):
        result += int(n[i]) * factorial(i + 1)
    print(result)
