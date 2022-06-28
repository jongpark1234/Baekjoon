from math import gcd
result = 0
n, l, r = map(int, input().split())
a = list(map(int, input().split()))
for i in range(1, 1 << n):
    cnt, temp = 0, 1
    for j in range(n):
        if (i >> j) & 1:
            cnt += 1
            temp = (temp * a[j]) // gcd(temp, a[j])
            if temp > r:
                temp = r + 1
    result += (r // temp - (l - 1) // temp) * [-1, 1][cnt & 1]
print(result)
