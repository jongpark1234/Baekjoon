def c(x, r):
    a = 1
    if (x < r):
        return 0
    elif (x == r):
        return 1
    for i in range(1, r + 1):
        a *= (x - i + 1)
        a //= i
    return a
n, k, m = map(int, input().split())
N = []
K = []
while (n != 0 or k != 0):
    N.append(n % m)
    K.append(k % m)
    n //= m
    k //= m
result = 1
for i in range(len(N)):
    result *= c(N[i], K[i])
    result %= m
print(result)
