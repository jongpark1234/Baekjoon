import sys
def Round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)
cut = []
n = int(sys.stdin.readline())
extreme = int(Round(n * 0.15))
scores = [int(sys.stdin.readline()) for _ in range(n)]
scores.sort()
for i in range(extreme, len(scores) - extreme):
    cut.append(scores[i])
if not n:
    print(0)
else:
    print(Round(sum(cut) / len(cut)))