cnt = 0
n = int(input())
def isSquare(n):
    return int(n ** 0.5) ** 2 == n
for i in range(1, 501):
    if isSquare(i ** 2 + n):
        cnt += 1
print(cnt)
