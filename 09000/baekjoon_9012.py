import sys
t = int(sys.stdin.readline())
stack = []
for i in range(t):
    temp = 0
    stack.clear()
    s = sys.stdin.readline().rstrip()
    for j in range(len(s)):
        stack.append(s[j])
    for j in range(len(stack)):
        if temp < 0:
            break
        elif stack[j] == '(':
            temp += 1
        else:
            temp -= 1
    if temp == 0:
        print('YES')
    else:
        print('NO')
