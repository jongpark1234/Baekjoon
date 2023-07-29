w = h = 0
n = int(input())
room = [input() for _ in range(n)]
for i in range(n):
    cnt = 0
    for j in range(n):
        if room[i][j] == '.':
            cnt += 1
            if cnt == 2:
                w += 1
        else:
            cnt = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if room[j][i] == '.':
            cnt += 1
            if cnt == 2:
                h += 1
        else:
            cnt = 0
print(w, h)
