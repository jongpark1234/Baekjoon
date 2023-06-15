result = 0
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    cnt = 1
    for j in range(i + 1, n):
        if a[j] < a[j - 1]:
            break
        cnt += 1
    result = max(result, cnt)
print(result)
