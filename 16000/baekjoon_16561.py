n = int(input())
result = 1
cnt = 2
for _ in range(9, n, 3):
    result += cnt
    cnt += 1
print(result)
