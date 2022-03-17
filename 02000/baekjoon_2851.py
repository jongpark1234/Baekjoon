score = 0
for i in [int(input()) for _ in range(10)]:
    score += i
    if score >= 100:
        break
print(sorted([score, score - i], key = lambda x: (abs(100 - x), -x))[0])
