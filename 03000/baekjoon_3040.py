from sys import stdin
import itertools
dwarps = list(itertools.combinations(sorted([int(stdin.readline()) for i in range(9)]), 7))
for i in dwarps:
    if sum(i) == 100:
        for j in range(7):
            print(i[j])
        break
