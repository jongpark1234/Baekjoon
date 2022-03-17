from sys import stdin
lcs = 0
s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()
Map = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if (s1[i - 1] == s2[j - 1]):
            Map[i][j] = Map[i - 1][j - 1] + 1
            lcs = max(Map[i][j], lcs)
print(lcs)
