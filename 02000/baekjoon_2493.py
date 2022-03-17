from sys import stdin
n = int(stdin.readline())
top = list(map(int, stdin.readline().split()))
result = [0] * n
stack = []
for i in range(n - 1, -1, -1):
    if len(stack):
        while stack[-1][1] < top[i]:
            tower = stack.pop()
            result[tower[0]] = i + 1
            if len(stack) == 0:
                break
    stack.append([i, top[i]])
print(*result)
