from sys import stdin
n = int(stdin.readline())
seq = sorted([int(stdin.readline()) for _ in range(n)])
score = 0
num = 0
if n == 1:
    print(seq[0])
    exit(0)
for i in range(0, n - 1, 2):
    if seq[i] < 0 and seq[i + 1] < 0:
        score += seq[i] * seq[i + 1]
    else:
        if seq[i] < 0 and seq[i + 1] > 0:
            score += seq[i]
        break
if i + 2 == n - 1:
    if seq[-1] < 0:
        score += seq[-1]
for i in range(n - 1, 0, -2):
    if seq[i] > 1 and seq[i - 1] > 1:
        score += seq[i] * seq[i - 1]
    else:
        num = i
        break
for i in range(num, -1, -1):
    if seq[i] > 0:
        score += seq[i]
    else:
        break
print(score)
