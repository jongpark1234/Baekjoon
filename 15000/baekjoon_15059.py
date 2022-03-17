a = list(map(int, input().split()))
r = list(map(int, input().split()))
result = 0
for i in range(3):
    if a[i] < r[i]:
        result += r[i] - a[i]
print(result)
