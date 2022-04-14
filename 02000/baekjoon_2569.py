from sys import stdin
n = int(stdin.readline())
burden = [int(stdin.readline()) for _ in range(n)]
seq = sorted([i for i in range(n)], key = burden.__getitem__)
visited = [False for _ in range(n)]
power = 0
for i in range(n):
    if visited[i]:
        continue
    burdens = []
    idx = i
    while not visited[idx]:
        visited[idx] = True
        burdens.append(burden[idx])
        idx = seq[idx]
    power += min(sum(burdens) + min(burdens) * (len(burdens) - 2), sum(burdens) + min(burdens) + min(burden) * (len(burdens) + 1))
print(power)
