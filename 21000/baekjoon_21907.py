edges = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [4, 3], [5, 1], [6, 2], [7, 3], [8, 1], [9, 2], [10, 3], [11, 1]]
print(19, len(edges))
for i in edges:
    print(*i)
for i in range(1, 501):
    temp, idx = i, 12
    powers, edges = [], []
    while temp & 1 == 0:
        edges.append([idx, 1])
        temp //= 2
        idx += 1
    for i in range(9):
        if temp & (1 << i):
            powers.append(i)
    if len(powers) < 9:
        edges.append([len(powers) + 3, (len(powers) + 2) % 3 + 1])
    for i in range(1, len(powers)):
        for j in range(powers[i] - powers[i - 1]):
            edges += [[idx, i + 3], [idx, (i - 1) % 3 + 1]]
            idx += 1
    while idx < 20:
        edges += [[idx, 1], [idx, 2]]
        idx += 1
    print(len(edges))
    for i in edges:
        print(*i)
