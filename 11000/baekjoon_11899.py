from sys import stdin
s = stdin.readline().rstrip()
stack = []
cnt = 0
for i in s:
    if i == '(':
        stack.append(i)
    else:
        if len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        else:
            cnt += 1
print(cnt + len(stack))
