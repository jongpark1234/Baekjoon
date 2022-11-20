for _ in range(int(input())):
    y, m = map(int, input().split())
    if m == 1:
        print(y - 1, 12, 31)
    else:
        print(y, m - 1, 29 if m == 3 and ((y % 100 != 0 and y % 4 == 0) or y % 400 == 0) else [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
