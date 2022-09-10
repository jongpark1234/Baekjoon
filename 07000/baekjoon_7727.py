LCS1 = [[0 for _ in range(10001)] for _ in range(2)]
LCS2 = [[0 for _ in range(10001)] for _ in range(2)]
def Hirschburg(s1, s2, t1, t2):
    ret = ''
    Max = -1
    S = s1 + s2 >> 1
    T = 0
    if s1 == s2:
        return ''
    if s1 + 1 == s2:
        for i in range(t1 + 1, t2 + 1):
            if s[s2] == t[i]:
                ret += t[i]
                return ret
        return ''
    for i in range(t1, t2 + 1):
        LCS1[0][i] = LCS1[1][i] = LCS2[0][i] = LCS2[1][i] = 0
    for i in range(s1 + 1, S + 1):
        for j in range(t1 + 1, t2 + 1):
            LCS1[i & 1][j] = LCS1[i + 1 & 1][j - 1] + 1 if s[i] == t[j] else max(LCS1[i + 1 & 1][j], LCS1[i & 1][j - 1])
    for i in range(s2 - 1, S - 1, -1):
        for j in range(t2 - 1, t1 - 1, -1):
            LCS2[i & 1][j] = LCS2[i + 1 & 1][j + 1] + 1 if s[i + 1] == t[j + 1] else max(LCS2[i + 1 & 1][j], LCS2[i & 1][j + 1])
    for i in range(t1, t2 + 1):
        if LCS1[S & 1][i] + LCS2[S & 1][i] > Max:
            Max = LCS1[S & 1][i] + LCS2[S & 1][i]
            T = i
    return Hirschburg(s1, S, t1, T) + Hirschburg(S, s2, T, t2)
n1, n2 = map(int, input().split())
s = ' ' + input()
t = ' ' + input()
LCS = Hirschburg(0, n1, 0, n2)
print(len(LCS), LCS, sep = '\n')
