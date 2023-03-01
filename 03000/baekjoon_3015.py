from sys import stdin
result = 0
stack = []
n = int(stdin.readline())
for i in range(n):
    cnt = 1
    height = int(stdin.readline())
    while stack and stack[-1][0] <= height:
        if stack[-1][0] == height:
            result += stack[-1][1]
            cnt = stack[-1][1] + 1
        else:
            result += stack[-1][1]
            cnt = 1
        stack.pop()
    if stack:
        result += 1
    stack.append([height, cnt])
print(result)
