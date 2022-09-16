for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if x < 24 and y < 60 else 'No', 'Yes' if (x == 2 and 0 < y < 30) or (x in [1, 3, 5, 7, 8, 10, 12] and 0 < y < 32) or (x in [4, 6, 9, 11] and 0 < y < 31) else 'No')
