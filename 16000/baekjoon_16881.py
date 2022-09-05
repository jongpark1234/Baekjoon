ret = 0
n, m = map(int, input().split())
for i in range(n):
    temp = 0
    matrix = list(map(int, input().split()))[::-1]
    for j in matrix:
        temp = j - (j <= temp)
    ret ^= temp
print('koosaga' if ret else 'cubelover')
