# pypy3
from sys import stdin
string = []
count = 0
N, M = map(int, stdin.readline().split())
S = [stdin.readline().rstrip() for _ in range(int(N))]
string = [stdin.readline().rstrip() for _ in range(M)]
for i in string:
    for j in S:
        if j[:len(i)] == i:
            count += 1
            break
print(count)
