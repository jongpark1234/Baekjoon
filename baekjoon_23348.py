A, B, C = map(int, input().split())
result = 0
for _ in range(int(input())):
    score = 0
    for i in range(3):
        a, b, c = map(int, input().split())
        score += a * A + b * B + c * C
    result = max(score, result)
print(result)
