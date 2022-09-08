from math import isqrt
def solve(n):
    ret = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            ret.append(i)
            if i ** 2 != n:
                ret.append(n // i)
    return len(ret)
for _ in range(int(input())):
    n = int(input())
    print(n, solve(n))
