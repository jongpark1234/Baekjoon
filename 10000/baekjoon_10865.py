from sys import stdin
n, m = map(int, input().split())
setlist = [set() for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    setlist[a].add(b)
    setlist[b].add(a)
print('\n'.join(map(lambda x: str(len(x)), setlist[1:])))
