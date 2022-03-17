from sys import stdin
award = []
lan, eng, mat, sci = [], [], [], []
for _ in range(int(stdin.readline())):
    x, a, b, c, d = list(map(int, stdin.readline().split()))
    lan.append([x, a])
    eng.append([x, b])
    mat.append([x, c])
    sci.append([x, d])
lan.sort(key = lambda x : (-x[1], x[0]))
award.append(lan[0][0])
eng.sort(key = lambda x : (x[0] in award, -x[1], x[0]))
award.append(eng[0][0])
mat.sort(key = lambda x : (x[0] in award, -x[1], x[0]))
award.append(mat[0][0])
sci.sort(key = lambda x : (x[0] in award, -x[1], x[0]))
award.append(sci[0][0])
print(*award)
