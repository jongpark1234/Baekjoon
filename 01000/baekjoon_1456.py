def sieve(a: int, b: int = -1) -> list[int]:
    st, ed = (1, a + 1) if b < 0 else (min(a, b), max(a, b) + 1)
    if ed < 5:
        return [i for i in range(st, ed) if i in (2, 3)]
    n = ed + 6 - ed % 6
    sieve = [False] + [True for _ in range(n // 3 - 1)]
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            d, s, j = (k := 1 | i * 3 + 1) << 1, k ** 2, k * (k - ((i & 1) << 1) + 4)
            sieve[s // 3::d] = [False for _ in range((n // 6 - s // 6 - 1) // k + 1)]
            sieve[j // 3::d] = [False for _ in range((n // 6 - j // 6 - 1) // k + 1)]
    b, e = (st | 1) // 3, n // 3 - 2 + (ed % 6 > 1)
    return ([i for i in (2, 3) if i >= st] + [1 | 3 * i + 1 for i in range(b, e) if sieve[i]])
result = 0
primes = sieve(10000000)
a, b = map(int, input().split())
for i in primes:
    temp = i
    while temp * i <= b:
        temp *= i
        if temp >= a:
            result += 1
print(result)
