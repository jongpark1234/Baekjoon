from math import inf
def update(index, data):
    while index <= n:
        tree[index] = min(tree[index], data)
        index += (index & -index)
def getMin(end):
    ret = inf
    while end:
        ret = min(tree[end], ret)
        end -= (end & -end)
    return ret
n = int(input())
student = [[] for _ in range(n + 1)]
tree = [inf for _ in range(n + 1)]
student[0] = [0, 0, 0]
for _ in range(3):
    Input = list(map(int, input().split()))
    for i in range(n):
        student[Input[i]].append(i + 1)
student.sort()
result = 0
for i in range(1, n + 1):
    if getMin(student[i][1]) > student[i][2]:
        result += 1
    update(student[i][1], student[i][2])
print(result)
