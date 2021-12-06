# pypy3
from sys import stdin
n = int(stdin.readline())
dots = sorted(list(map(int, stdin.readline().split())), reverse=True)
result = 0
for i in dots:
    for j in dots:
        result += abs(i - j)
print(result)
