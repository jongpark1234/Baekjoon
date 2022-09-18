def sieve(a: int, b: int = -1) -> list[int]:
    st, ed = (1, a + 1) if b < 0 else (min(a, b), max(a, b) + 1)
    if ed < 5:
        return [i for i in range(st, ed) if i in (2, 3)]
    n = ed + 6 - ed % 6
    sieve = [False] + [True for _ in range(n // 3 - 1)]
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            d, s, j = (k := 1 | 3 * i + 1) * 2, k * k, k * (k + 4 - 2 * (i & 1))
            sieve[s // 3::d] = [False for _ in range((n // 6 - s // 6 - 1) // k + 1)]
            sieve[j // 3::d] = [False for _ in range((n // 6 - j // 6 - 1) // k + 1)]
    b, e = (st | 1) // 3, n // 3 - 2 + (ed % 6 > 1)
    return ([i for i in (2, 3) if i >= st] + [1 | 3 * i + 1 for i in range(b, e) if sieve[i]])
def f(a, b):
    if not b:
        return 1
    if b == 1:
        return a
    if b & 1:
        return f(a, b - 1) * a % m
    return f(a ** 2 % m, b >> 1)
n, k, m = map(int, input().split())
result = 1
primeCounts = {}
primes = sieve(n)
for i in range(len(primes)):
    j = primes[i]
    while j <= n:
        temp = n // j - k // j - (n - k) // j
        if primes[i] in primeCounts:
            primeCounts[primes[i]] += temp
        else:
            primeCounts[primes[i]] = temp
        j *= primes[i]
for i in primeCounts:
    result = result * f(i, primeCounts[i]) % m
print(result)
