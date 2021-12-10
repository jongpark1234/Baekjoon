t, p = map(int, input().split())
if p > 20:
    a = t / (100 - p)
    print((p - 20) * a + 20 * 2 * a)
else:
    a = t / ((20 - p) * 2 + 80)
    print(p * 2 * a)
