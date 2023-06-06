from sys import stdin
n, c = map(int, input().split())
fireworks = [0 for _ in range(c + 1)]
for _ in range(n):
    cycle = int(stdin.readline())
    for i in range(cycle, c + 1, cycle):
        fireworks[i] = 1
print(sum(fireworks))
