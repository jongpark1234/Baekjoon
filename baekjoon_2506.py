n = int(input())
score = 0
weight = 1
for i in list(map(int, input().split())):
    if i:
        score += weight
        weight += 1
    else:
        weight = 1
print(score)
