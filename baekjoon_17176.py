from sys import stdin
n = int(input())
tf = ['n', 'y']
numlist = list(map(int, stdin.readline().split()))
charlist = list(map(ord, input()))
for i in range(len(charlist)):
    if charlist[i] == 32:
        charlist[i] = 0
    elif charlist[i] > 96:
        charlist[i] -= 70
    else:
        charlist[i] -= 64
numlist.sort(), charlist.sort()
print(tf[int(numlist == charlist)])
