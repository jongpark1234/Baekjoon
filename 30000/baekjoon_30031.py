print(sum([1000, 5000, 10000, 50000][(int(i.split()[0]) - 136) // 6] for i in [*open(0)][1:]))
