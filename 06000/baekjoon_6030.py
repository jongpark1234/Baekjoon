p, q = map(lambda x: [i for i in range(1, int(x) + 1) if int(x) % i == 0], input().split())
for i in p:
    for j in q:
        print(i, j)
