from sys import stdin
n = int(stdin.readline())
cow = [int(stdin.readline()) for _ in range(n)]
seq = sorted([i for i in range(n)], key = cow.__getitem__)
visited = [False for _ in range(n)]
time = 0
for i in range(n):
    if visited[i]:
        continue
    cows = []
    idx = i
    while not visited[idx]:
        visited[idx] = True
        cows.append(cow[idx])
        idx = seq[idx]
    time += min(sum(cows) + min(cows) * (len(cows) - 2), sum(cows) + min(cows) + min(cow) * (len(cows) + 1))
print(time)
