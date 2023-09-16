t = int(input())
scores = list(map(int, input().split())) + [0 for _ in range(5 - t)]
print((abs(scores[0] - scores[2]) * (508 if scores[0] > scores[2] else 108) + abs(scores[1] - scores[3]) * (212 if scores[1] > scores[3] else 305) + scores[4] * 707) * 4763)
