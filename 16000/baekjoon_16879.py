from sys import stdin
palace = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
ret = 0
for i in palace:
    ret ^= ((i[0] // 3) ^ (i[1] // 3)) * 3 + (i[0] + i[1]) % 3
print('koosaga' if ret else 'cubelover')
