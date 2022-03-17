import sys
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().rstrip()
    temp = s[0].upper()
    print(temp + s[1:])
