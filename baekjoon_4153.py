import sys
while True:
    a = list(map(int, sys.stdin.readline().split()))
    if sum(a) == 0:
        break
    temp = max(a)
    a.remove(temp)
    if ((a[0] ** 2) + (a[1] ** 2) == (temp ** 2)):
        print('right')
    else:
        print('wrong')