from sys import stdin
from itertools import combinations
result = []
for i in range(int(stdin.readline())):
    numlist = []
    combilist = list(combinations(list(map(int, stdin.readline().split())), 3))
    for j in combilist:
        numlist.append(str(sum(j))[-1])
    result.append(max(numlist))
for i in reversed(range(len(result))):
    if result[i] == max(result):
        print(i + 1)
        break
