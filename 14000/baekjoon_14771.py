def solve():
    d, p = [0], [0]
    ret = 0
    n, v = map(int, input().split())
    for _ in range(n):
        Input = list(map(int, input().split()))
        d.append(Input[0])
        p.append(Input[1])
    for _ in range(v):
        a, b, c = map(int, input().split())
        if d[a] == 1 or c == 1:
            ret += p[a]
        if d[b] == 1 or c == 2:
            ret += p[b]
    return ret
for i in range(int(input())):
    print(f'Data Set {i + 1}:\n{solve()}\n')
