from sys import stdin
stack = []
s = stdin.readline().rstrip()
e = stdin.readline().rstrip()
for i in s:
    stack.append(i)
    if ''.join(stack[-len(e):]) == e:
        del stack[-len(e):]
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
