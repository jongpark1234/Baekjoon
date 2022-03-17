from sys import stdin
cnt = 0
vip = []
n, k, l = map(int, stdin.readline().split())
for _ in range(n):
    scores = list(map(int, stdin.readline().split()))
    if min(scores) >= l and sum(scores) >= k:
        cnt += 1
        vip.extend(scores)
print(cnt)
print(*vip)
