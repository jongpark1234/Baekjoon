a, b = map(lambda x: 100 - int(x), input().split())
c = 100 - a - b
d = a * b
q, r = divmod(d, 100)
print(a, b, c, d, q, r)
print(c + q, r)
