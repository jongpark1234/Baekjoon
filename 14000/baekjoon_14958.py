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
cycle = ['RP', 'PS', 'SR']
n, m = map(int, input().split())
a = input()
b = input()[::-1]
result = [0 for _ in range(n + m - 1)]
for i in range(3):
    w = multiply(list(map(lambda x: x == cycle[i][0], a)), list(map(lambda x: x == cycle[i][1], b)))
    for j in range(n + m - 1):
        result[j] += w[j]
print(max(result[m - 1:n + m - 1]))
