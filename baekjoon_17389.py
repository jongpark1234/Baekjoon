bonus = 0
score = 0
n = int(input())
ox = input()
for i in range(1, n + 1):
    if ox[i - 1] == 'O':
        score += i + bonus
        bonus += 1
    else:
        bonus = 0
print(score)
