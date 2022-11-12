for i in [*open(0)]:
    for j in list(map(int, i.split())):
        if j == 0:
            exit(0)
        temp = sum(k for k in range(1, j) if j % k == 0)
        print(j, 'ABUNDANT' if temp > j else 'PERFECT' if temp == j else 'DEFICIENT')
