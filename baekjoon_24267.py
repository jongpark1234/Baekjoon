n = int(input())
cnt = 0
for i in range(3, n + 1):
    cnt += (n - i + 2) * (abs(n - i) + 1) // 2
print(cnt, 3, sep = '\n')
