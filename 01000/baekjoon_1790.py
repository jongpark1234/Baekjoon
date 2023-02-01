n, k = map(int, input().split())
temp, idx = 0, 0
while (temp := 9 * (10 ** idx) * (idx + 1)) <= k:
    k -= temp
    idx += 1
num = (10 ** idx) + (k + idx) // (idx + 1) - 1
try:
    print(-1 if num > n else str(num)[(k + idx) % (idx + 1)])
except IndexError:
    print(num)
