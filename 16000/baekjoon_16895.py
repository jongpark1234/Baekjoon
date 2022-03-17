result = 0
n = int(input())
stoneList = list(map(int, input().split()))
for i in range(n):
    ret = 0
    for j in range(n):
        if i == j:
            continue
        ret ^= stoneList[j]
    for j in range(stoneList[i]):
        if ret ^ j == 0:
            result += 1
print(result)
