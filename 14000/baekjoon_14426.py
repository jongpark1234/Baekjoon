from sys import stdin
from bisect import bisect
result = 0
n, m = map(int, stdin.readline().split())
s = sorted([stdin.readline().rstrip() for _ in range(n)])
for i in [stdin.readline().rstrip() for _ in range(m)]:
    idx = min(n - 1, bisect(s, i))
    if s[idx].startswith(i):
        result += 1
    elif s[idx - 1].startswith(i):
        result += 1
print(result)
