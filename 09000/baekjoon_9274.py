def solve(r, c):
    ret = 0
    for i in range(r, ar + tr, tr):
        for j in range(c, ac + tc, tc):
            if tilelist[i][j] > 0:
                ret += 1
    return ret
while True:
    try:
        Map = []
        templist = [[0 for _ in range(1111)] for _ in range(1111)]
        tilelist = [[0 for _ in range(1111)] for _ in range(1111)]
        ar, ac, tr, tc = map(int, input().split())
        for i in range(ar):
            Map.append(list(map(lambda x: x == 'X', list(input()))))
        for i in range(ar + tr):
            temp = 0
            for j in range(ac + tc):
                if i < ar and j < ac and Map[i][j]:
                    temp += 1
                if i < ar and j - tc >= 0 and Map[i][j - tc]:
                    temp -= 1
                templist[i][j] = temp
        for i in range(ac + tc):
            temp = 0
            for j in range(ar + tr):
                temp += templist[j][i]
                if j - tr >= 0:
                    temp -= templist[j - tr][i]
                tilelist[j][i] = temp
        result = float('inf')
        for i in range(tr):
            for j in range(tc):
                result = min(result, solve(i, j))
        print(result)
    except EOFError:
        break
