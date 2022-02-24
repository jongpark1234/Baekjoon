for _ in range(int(input())):
    s, k = map(int, input().split())
    if k % 2 == 0:
        s %= k + 1
        if s == k:
            print(k)
        elif s % 2 == 1:
            print(1)
        else:
            print(0)
    else:
        if s % 2 == 1:
            print(1)
        else:
            print(0)
