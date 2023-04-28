from math import log10
result = 0
n, k = map(int, input().split())
for i in range(1, n + 1):
    result = (result * 10 ** int(log10(i) + 1) + i) % k
print(result)
