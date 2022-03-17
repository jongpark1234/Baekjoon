from sys import stdin
n = int(stdin.readline())
stack = []
result = []
error = False
cnt = 0
for _ in range(n):
    num = int(stdin.readline())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        error = True
        pass
if error:
    print('NO')
else:
    print('\n'.join(result))