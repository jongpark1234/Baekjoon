def primetest(n):
    def verify(a, n, s):
        if a >= n:
            a %= n
        if a < 2:
            return True
        d = n >> s
        x = pow(a, d, n)
        if x == n - 1:
            return True
        if x == 1: 
            return True
        for _ in range(s):
            x = x * x % n
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False
    if n == 2:
        return True
    if n < 2 or not n & 1:
        return False
    d = n >> 1
    r = 1
    while not d & 1:
        d >>= 1
        r += 1
    return all(verify(i, n, r) for i in ([2, 7, 61] if n < 4759123141 else [2, 325, 9375, 28178, 450775, 9780504, 1795265022]))
def palindromical(n):
    ret = n
    n //= 10
    while n > 0:
        ret = ret * 10 + n % 10
        n //= 10
    return ret
result = 0
candidates = [2, 3, 5, 7, 11]
l, h = map(int, input().split())
for i in range(10, 1000000):
    if (int(str(i)[0]) == 5) or (~int(str(i)[0]) & 1):
        continue
    temp = palindromical(i)
    if primetest(temp):
        candidates.append(temp)
for i in candidates:
    if l <= i <= h:
        result += 1
print(result)
print(candidates)