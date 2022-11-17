n = int(input())
runners = [0 for _ in range(n)]
for i in map(int, input().split()):
    runners[i - 1] = 1
print(runners.index(0) + 1)
