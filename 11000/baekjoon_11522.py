for i in [*open(0)][1:]:
    k, n = map(int, i.split())
    print(k, sum(i for i in range(1, n + 1)), sum(i for i in range(1, n * 2 + 1, 2)), sum(i for i in range(2, n * 2 + 1, 2)))
