n = int(input())
for i in range(n):
    score = 0
    temp = 0
    b = input()
    OXlist = list(map(str, b))
    for j in range(len(OXlist)):
        if (OXlist[j] == 'O'):
            temp += 1
            score += temp
        else:
            temp = 0
    print(score)
