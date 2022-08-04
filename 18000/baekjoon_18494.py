result = 1
n = int(input())
a = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    result = max(result, a[i] - i + 1)
print(result)
