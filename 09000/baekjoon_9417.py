from itertools import combinations
from sys import stdin
from math import gcd
for _ in range(int(stdin.readline())):
    total = 0
    numlist = list(map(int, stdin.readline().split()))
    for i in list(combinations(numlist, 2)):
        total = max(total, gcd(i[0], i[1]))
    print(total)
