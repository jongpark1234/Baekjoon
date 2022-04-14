from sys import stdin
n = int(stdin.readline())
weight = [int(stdin.readline()) for _ in range(n)]
seq = sorted([i for i in range(n)], key = weight.__getitem__)
visited = [False for _ in range(n)]
result = 0
for i in range(n):
    if visited[i]:
        continue
    weights = []
    idx = i
    while not visited[idx]:
        visited[idx] = True
        weights.append(weight[idx])
        idx = seq[idx]
    result += min(sum(weights) + min(weights) * (len(weights) - 2), sum(weights) + min(weights) + min(weight) * (len(weights) + 1))
print(result)
