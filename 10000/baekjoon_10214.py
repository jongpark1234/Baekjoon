import sys
t = int(sys.stdin.readline())
yonsei = 0
korea = 0
for i in range(t):
    korea, yonsei = 0, 0
    for j in range(9):
        y, k = map(int, sys.stdin.readline().split())
        yonsei += y
        korea += k
    if yonsei > korea:
        print("Yonsei")
    elif korea > yonsei:
        print("Korea")
    else:
        print("Draw")