from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
n = int(input())
star = [[' ' for i in range(n)] for j in range(n)]
def staring(num):
    if num == 3:
        star[0][:3] = star[2][:3] = ['*'] * 3
        star[1][:3] = ['*', ' ', '*']
        return
    num //= 3
    staring(num)
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            for k in range(num):
                star[num * i + k][num * j:num * (j + 1)] = star[k][:num]
staring(n)
for i in star:
    print(''.join(i))
