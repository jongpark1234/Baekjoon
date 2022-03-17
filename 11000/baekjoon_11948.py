import sys
score1, score2 = [], []
for i in range(4):
    score1.append(int(sys.stdin.readline()))
for i in range(2):
    score2.append(int(sys.stdin.readline()))
print((sum(score1) - min(score1)) + sum(score2) - min(score2))
