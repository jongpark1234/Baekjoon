checked = [False for _ in range(3000001)]
def solve1(numlist, p):
    global ret
    ret = [-1, 1]
    def F(x, y):
        global ret
        x += Sum
        y += Sum
        x %= p * 2 + 1
        y %= p * 2 + 1
        if checked[x] and checked[y]:
            ret = [x, y]
    Sum = 0
    for i in numlist:
        checked[i] = True
        Sum += i
        Sum %= p * 2 + 1
    if p & 1:
        for i in range(1, p):
            F(i, p * 2 + 1 - i)
    else:
        for i in range(1, p):
            F(p * 2 + 1 - i, i)
    F(0, p * 2)
    F(0, 1)
    F(p, 2)
    F(p, p * 2 - 1)
    F(4, p + 1)
    F(p * 2 - 3, p + 1)
    for i in numlist:
        checked[i] = False
    return ret
def solve2(x, y, p):
    global ret
    ret = -1
    def F(a, b):
        global ret
        if (x + b) % (p * 2 + 1) == (a + y) % (p * 2 + 1):
            ret = x - a + p * 2 + 1
            ret %= p * 2 + 1
    if p & 1:
        for i in range(1, p):
            F(i, p * 2 + 1 - i)
    else:
        for i in range(1, p):
            F(p * 2 + 1 - i, i)
    F(0, p * 2)
    F(0, 1)
    F(p, 2)
    F(p, p * 2 - 1)
    F(4, p + 1)
    F(p * 2 - 3, p + 1)
    return ret
t = int(input())
r = int(input())
for _ in range(t):
    n = int(input())
    if r < 3:
        print(*solve1(list(map(int, input().split())), n))
    else:
        print(((n * 4 + 2) - (solve2((Input := list(map(int, input().split())))[0], Input[1], n) + solve2(Input[2], Input[3], n))) % (n * 2 + 1))
