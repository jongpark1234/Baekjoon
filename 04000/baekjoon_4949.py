from sys import stdin
while True:
    balanced = True
    stack = []
    s = stdin.readline().rstrip()
    if s == '.':
        break
    for i in s:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) == 0:
                balanced = False
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                balanced = False
                break
        elif i == ')':
            if len(stack) == 0:
                balanced = False
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                balanced = False
                break
    if balanced and not len(stack):
        print('yes')
    else:
        print('no')
