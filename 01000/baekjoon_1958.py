from sys import stdin
s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()
s3 = stdin.readline().rstrip()
Map = [[[0] * (len(s3) + 1) for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        for k in range(1, len(s3) + 1):
            if (s1[i - 1] == s2[j - 1] == s3[k - 1]):
                Map[i][j][k] = Map[i - 1][j - 1][k - 1] + 1
            else:
                Map[i][j][k] = max(Map[i - 1][j][k], Map[i][j - 1][k], Map[i][j][k - 1])
print(Map[-1][-1][-1])
