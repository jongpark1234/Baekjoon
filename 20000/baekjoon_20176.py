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
SIZE = 121212
result = 0
n = [[0 for _ in range(SIZE)] for _ in range(3)]
for i in range(3):
    input()
    for j in map(int, input().split()):
        n[i][j + 30000] += 1
c = multiply(n[0], n[2])
for i in range(60001):
    result += n[1][i] * c[i + i]
print(result)
