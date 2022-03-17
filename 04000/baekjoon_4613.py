import sys
while True:
    quicksum = 0
    s = sys.stdin.readline().rstrip()
    if s == '#':
        break
    else:
        for i in range(len(s)):
            if s[i] == ' ':
                pass
            else:
                quicksum += (i + 1) * (ord(s[i]) - 64)
    print(quicksum)
