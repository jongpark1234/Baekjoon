from sys import stdin
result = [0, 0]
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    if a == b:
        continue
    result[a < b] += 1
print(*result)
