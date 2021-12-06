from itertools import combinations
from sys import stdin
numlist = list(combinations(list(map(int, stdin.readline().split())), 2))
result = []
n = int(stdin.readline())
for i in numlist:
    if sum(i) == n:
        result.append(i)
result = list(set(result))
for i in result:
    print(*i)
print(len(result))
