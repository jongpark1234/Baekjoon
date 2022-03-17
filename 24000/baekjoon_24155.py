# pypy3
from sys import stdin
numlist = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
rank = sorted(numlist, reverse=True)
for i in numlist:
    print(rank.index(i) + 1)
