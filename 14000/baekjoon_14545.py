for i in [*map(int, open(0))][1:]:
    print(i * (i + 1) * (i * 2 + 1) // 6)
