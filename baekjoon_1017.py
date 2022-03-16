from sys import stdin
n = int(stdin.readline())
s = list(map(int, stdin.readline().split()))
sa = [0]
sb = [0]
sieve = [True for i in range(2000)]
result = []
sieve[1] = False
for i in range(2, 50):
    if sieve[i] == True:
        for j in range(i * 2, 2000, i):
            sieve[j] = False
def dfs(s):
    if visited[s] == True:
        return False
    visited[s] = True
    for i in numlist[s]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = s
            return True
    return False
for i in range(n):
    if s[0] % 2 == s[i] % 2:
        sa.append(s[i])
    else:
        sb.append(s[i])
numlist = [[] for _ in range(len(sa))]
for i in range(1, len(sa)):
    for j in range(1, len(sb)):
        if sieve[sa[i] + sb[j]]:
            numlist[i].append(j)
for i in numlist[1]:
    d = [0 for _ in range(len(sb))]
    d[i] = 1
    cnt = 1
    for j in range(1, len(sa)):
        visited = [0 for _ in range(len(sa))]
        visited[1] = True
        cnt += dfs(j)
    if cnt == n // 2:
        result.append(sb[i])
if result:
    print(*sorted(result))
else:
    print(-1)
