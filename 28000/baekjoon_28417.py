from sys import stdin
results = []
for _ in range(int(input())):
    scores = list(map(int, stdin.readline().split()))
    results.append(max(scores[:2]) + sum(sorted(scores[2:])[-2:]))
print(max(results))
