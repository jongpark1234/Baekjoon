from collections import deque
def eval(numlist, x):
    return numlist[0] * x + numlist[1]
def itr(numlist, l):
    return (numlist[1] - l[1]) // (l[0] - numlist[0])
n = int(input())
v1 = sorted([list(map(int, input().split())) for _ in range(n)])
v2 = [v1[-1]]
Deque = deque([])
Max = v1[-1][1]
for i in range(n - 1)[::-1]:
    temp = v1[i]
    if temp[1] > Max:
        Max = temp[1]
        v2.append(temp)
v2 = v2[::-1]
result = 0
Deque.append([v2[0][1], 0])
for i in range(len(v2)):
    while len(Deque) >= 2 and eval(Deque[0], v2[i][0]) >= eval(Deque[1], v2[i][0]):
        Deque.popleft()
    result = eval(Deque[0], v2[i][0])
    if i == len(v2) - 1:
        break
    cur = [v2[i + 1][1], result]
    while len(Deque) >= 2 and itr(cur, Deque[-1]) <= itr(Deque[-1], Deque[len(Deque) - 2]):
        Deque.pop()
    Deque.append(cur)
print(result)
