from sys import stdin
while True:
    result = 0
    n, m = map(int, stdin.readline().split())
    if n == m == 0:
        break
    cdlist = set([int(stdin.readline()) for _ in range(n)])
    for _ in range(m):
        result += int(stdin.readline()) in cdlist
    print(result)
