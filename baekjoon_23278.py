import sys
n, l, h = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))
for _ in range(l):
    del score[score.index(min(score))]
for _ in range(h):
    del score[score.index(max(score))]
print(sum(score) / len(score))