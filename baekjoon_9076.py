for _ in range(int(input())):
    n = sorted(list(map(int, input().split())))
    print('KIN' if n[3] - n[1] >= 4 else sum(n[1:4]))
