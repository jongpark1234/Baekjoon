for _ in range(int(input())):
    l = r = 0
    n = int(input())
    for i in map(int, input().split()):
        if i < 0:
            l -= i
        else:
            r += i
    print('Left' if l > r else 'Right' if r > l else 'Equilibrium')
