from fractions import Fraction
MAX = 10000
for tc in range(int(input())):
    inc, inct = {}, {}
    n, t = map(int, input().split())
    d = map(lambda x: [1] + x[1:], [list(map(int, input().split())) for _ in range(t)])
    seq = [0 for _ in range(t)]
    for i, j in enumerate(d):
        for k in j:
            if k not in inc:
                inc[k], inct[k] = 0, []
            inc[k] += 1
            inct[k].append(i)
    temp, s1, s2 = Fraction(0), Fraction(0), Fraction(0)
    for i in range(1, min(n, MAX) + 1):
        if i in inc:
            s1 += inc[i]
            s2 = 0
            for j in inct[i]:
                seq[j] += 1
            for j in range(t):
                for k in range(j + 1, t):
                    s2 += seq[j] * seq[k]
        acc = s1 / Fraction(n) + s2 / Fraction(n ** 2) * 2
        temp += acc
    if n > MAX:
        temp += (n - MAX) * acc
    a = int(temp)
    b = temp - a
    print(f'Case #{tc + 1}: {a}+{b.numerator}/{b.denominator}')
