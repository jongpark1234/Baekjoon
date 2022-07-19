def check(k: int, x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    if k == 0:
        return False
    if x == 1:
        return False
    if not x & 1:
        return True
    return k >= 2
def make(x: int) -> None:
    if x == 0:
        return
    while x > 3:
        result.append(1)
        x -= 2
    result.append((x == 3) + 1)
def solve(k: int, Min = float('inf'), Max = -float('inf')) -> None:
    for i in range(n):
        if m[i] == '#':
            Min, Max = min(Min, i), max(Max, i)
    if Min == float('inf'):
        print(0 if n == 1 else '1\n1')
        exit(0)
    if not check(k, Min - k) or not check(k, n - Max - k - 1):
        return
    temp = 0
    for i in range(Min, Max + 1):
        if m[i] == '_':
            temp += 1
        else:
            if temp:
                if not check(k, temp - k - 1):
                    return
            temp = 0
    make(Min - k)
    cur0 = cur1 = 0
    for i in range(Min, Max + 1):
        if m[i] == '_':
            cur0 += 1
            if cur1:
                result.append(cur1 + k)
                cur1 = 0
        else:
            cur1 += 1
            if cur0:
                make(cur0 - k - 1)
                cur0 = 0
    result.append(cur1 + k)
    make(n - Max - k - 1)
    print(len(result))
    print(*result)
    exit(0)
result = []
m = input()
n = len(m)
for i in range(4):
    solve(i)
print(-1)
