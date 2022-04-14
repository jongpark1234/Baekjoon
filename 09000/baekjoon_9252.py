LCS1 = [[0 for _ in range(7001)] for _ in range(2)]
LCS2 = [[0 for _ in range(7001)] for _ in range(2)]
def Hirschburg(s1, s2, t1, t2):
    ret = ''
    Max = -1
    S = (s1 + s2) // 2
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
        LCS1[0][i] = 0
        LCS1[1][i] = 0
        LCS2[0][i] = 0
        LCS2[1][i] = 0
    for i in range(s1 + 1, S + 1):
        for j in range(t1 + 1, t2 + 1):
            LCS1[i % 2][j] = LCS1[(i + 1) % 2][j - 1] + 1 if s[i] == t[j] else max(LCS1[(i + 1) % 2][j], LCS1[i % 2][j - 1])
    for i in range(S, s2)[::-1]:
        for j in range(t1, t2)[::-1]:
            LCS2[i % 2][j] = LCS2[(i + 1) % 2][j + 1] + 1 if s[i + 1] == t[j + 1] else max(LCS2[(i + 1) % 2][j], LCS2[i % 2][j + 1])
    for i in range(t1, t2 + 1):
        if LCS1[S % 2][i] + LCS2[S % 2][i] > Max:
            Max = LCS1[S % 2][i] + LCS2[S % 2][i]
            T = i
    return Hirschburg(s1, S, t1, T) + Hirschburg(S, s2, T, t2)
s = '종' + input()
t = '박' + input()
LCS = Hirschburg(0, len(s) - 1, 0, len(t) - 1)
print(len(LCS), LCS, sep = '\n')
