import sys
poslist = [0 for i in range(5)]
n = int(sys.stdin.readline())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 or y == 0:
        poslist[4] += 1
    elif x > 0 and y > 0:
        poslist[0] += 1
    elif x < 0 and y > 0:
        poslist[1] += 1
    elif x < 0 and y < 0:
        poslist[2] += 1
    elif x > 0 and y < 0:
        poslist[3] += 1
for i in range(4):
    print(f'Q{i + 1}: {poslist[i]}')
print(f'AXIS: {poslist[4]}')
