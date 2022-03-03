def conduct(n, q):
    rev_base = []
    while n > 0:
        n, mod = divmod(n, q)
        rev_base.append(mod)
    return rev_base
for i in range(1000, 10000):
    if sum(conduct(i, 10)) == sum(conduct(i, 12)) == sum(conduct(i, 16)):
        print(i)
