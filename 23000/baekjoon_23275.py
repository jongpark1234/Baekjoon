from sys import stdin
v = list(map(int, stdin.read().split()))
print(next(i for i in v[1:v[0] + 1] if i not in v[v[0] + 1:]))
