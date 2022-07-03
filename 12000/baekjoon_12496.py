from collections import deque
from math import gcd, lcm, isqrt
def divisors(n):
    ret = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            ret.append(i)
            if i ** 2 != n:
                ret.append(n // i)
    return sorted(ret)
def solve(n, l, h, numlist):
    if numlist[0] != 1:
        numlist = [1] + numlist
        n += 1
    lcmlist = [numlist[0]]
    for i in range(1, n):
        lcmlist.append(lcm(lcmlist[-1], numlist[i]))
    gcdlist = deque([numlist[-1]])
    for i in range(n - 1)[::-1]:
        gcdlist.appendleft(gcd(gcdlist[0], numlist[i]))
    for i in range(n - 1):
        x, y = gcdlist[i + 1], lcmlist[i]
        if x < l or y > h:
            continue
        if y <= x and x % y == 0:
            for j in divisors(x):
                if j >= max(l, y) and j <= min(x, h) and j % y == 0:
                    return j
    ret = lcmlist[-1] * ((l - 1) // lcmlist[-1] + 1)
    return ret if ret <= h else -1
for i in range(int(input())):
    n, l, h = map(int, input().split())
    numlist = sorted(list(map(int, input().split())))
    result = solve(n, l, h, numlist)
    print(f'Case #{i + 1}:', 'NO' if result == -1 else result)
