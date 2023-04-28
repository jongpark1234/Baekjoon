from math import log10
n, k = map(int, input().split())
result = 0
for i in range(1, n + 1):
    result = (result * 10 ** int(log10(i) + 1) + i) % k
print(result)
