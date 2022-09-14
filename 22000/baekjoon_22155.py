for _ in range(int(input())):
    i, f = map(int, input().split())
    if (i <= 1 and f <= 2) or (i <= 2 and f <= 1):
        print('Yes')
    else:
        print('No')
