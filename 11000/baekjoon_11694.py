ret = 0
x = 0
n = int(input())
for i in list(map(int, input().split())):
    x ^= i
    ret |= x > 1
print('cubelover' if (not x if ret else x) else 'koosaga')
