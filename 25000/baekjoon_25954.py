l1, l2 = map(lambda x: len(x), [s1 := input(), s2 := input()])
v1, v2 = [[[[0, j][i == 0] for j in range(l2 + 1)] for i in range(l1 + 1)] for _ in range(2)]
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        v1[i][j], v2[i][j] = (v2[i][j - 1], v1[i - 1][j]) if s1[i - 1] == s2[j - 1] else (max(v2[i][j - 1], v1[i - 1][j]), min(v2[i][j - 1], v1[i - 1][j]))
print(sum((j - v1[i][j]) * (l2 - j + 1) for j in range(1, l2 + 1) for i in range(1, l1 + 1)))
