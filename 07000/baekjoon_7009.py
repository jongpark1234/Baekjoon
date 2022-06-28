for i in range(int(input())):
    p, t, s, b = map(int, input().split())
    b -= 1
    v = [0 for _ in range(p)]
    while s > 0:
        v[b % p] += 1
        s -= 1
        b += t
    p1 = p2 = p
    v.append(-1)
    for j in range(p):
        if v[j] >= v[p1]:
            p2 = p1
            p1 = j
        elif v[j] >= v[p2]:
            p2 = j
    print(f'Data Set {i + 1}:\n{[p2, p1][v[p1] == v[p2]] + 1}', end = '\n\n')
