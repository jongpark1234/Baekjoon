from math import isqrt
def sieve(n):
    if n < 3: 
        return [2] if n == 2 else []
    size = (n - 3) // 2
    isp = [True for _ in range(size + 1)]
    for i in range(isqrt(n - 3) // 2 + 1):
        if isp[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            isp[s::p] = [False for _ in range((size - s) // p + 1)]
    return [2] + [i + i + 3 for i, v in enumerate(isp) if v]
print(sieve(104750)[int(input()) - 1])
