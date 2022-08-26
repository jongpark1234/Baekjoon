from sys import setrecursionlimit, stdin
from decimal import Decimal, Context, setcontext, MAX_PREC, MAX_EMAX
MOD = 100003
setrecursionlimit(10 ** 5)
def multiply(a, b, digit = 0):
    setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX))
    if digit == 0:
        digit = len(str(min(len(a), len(b)) * max(a) * max(b)))
    f = f'0{digit}d'
    a_dec = Decimal(''.join(format(x, f) for x in a))
    b_dec = Decimal(''.join(format(x, f) for x in b))
    c_dec = a_dec * b_dec
    total_digit = digit * (len(a) + len(b) - 1)
    c = format(c_dec, f'0{total_digit}f')
    return [int(c[i:i + digit]) % MOD for i in range(0, total_digit, digit)]
def solve(l, r):
    if l == r:
        return v[l]
    return multiply(solve(l, l + r >> 1), solve((l + r >> 1) + 1, r))
n = int(stdin.readline())
v = list(map(lambda x: [int(x), 1], stdin.readline().split()))
result = solve(0, n - 1)
for _ in range(int(stdin.readline())):
    print(result[-(int(stdin.readline()) + 1)])
