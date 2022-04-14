from sys import stdin
n = int(stdin.readline())
dumbbell = list(map(int, stdin.readline().split()))
seq = sorted([i for i in range(n)], key = dumbbell.__getitem__)
visited = [False for _ in range(n)]
result = 0
for i in range(n):
    if visited[i]:
        continue
    dumbbells = []
    idx = i
    while not visited[idx]:
        visited[idx] = True
        dumbbells.append(dumbbell[idx])
        idx = seq[idx]
    result += min(sum(dumbbells) + min(dumbbells) * (len(dumbbells) - 2), sum(dumbbells) + min(dumbbells) + min(dumbbell) * (len(dumbbells) + 1))
print(result)
