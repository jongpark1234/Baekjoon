ret = 0
n = int(input())
for i in list(map(int, input().split())):
    ret ^= i
print('koosaga' if ret else 'cubelover')
