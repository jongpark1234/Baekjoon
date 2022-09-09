for i in [*map(int, open(0))][1:]:
    print(1 if i == 1 else pow(2, i - 2, 1000000007))
