print(min(open(0).read().strip().split('\n'), key=lambda x: int(x.split()[1])).split()[0])
