for idx, i in enumerate([*open(0)][:-1]):
    n, *numlist = map(int, i.split())
    print(f'Case {idx + 1}:', float(numlist[n >> 1]) if n & 1 else sum(numlist[(n >> 1) - 1:(n >> 1) + 1]) / 2)
