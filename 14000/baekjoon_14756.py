from decimal import Decimal, Context, setcontext, MAX_PREC, MAX_EMAX
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
    return [int(c[i:i + digit]) for i in range(0, total_digit, digit)]
n, l, m, w = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
t = [list(map(int, input().split()))[::-1] for _ in range(m)]
result = [multiply(s[i], t[i]) for i in range(m)]
print(sum(sum(result[j][i] for j in range(m)) > w for i in range(l - 1, n)))
