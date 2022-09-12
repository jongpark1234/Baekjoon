n, m = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(0, m * 3, 3):
        intensity = image[i][j] * 2126 + image[i][j + 1] * 7152 + image[i][j + 2] * 722
        if intensity < 510000:
            print('#', end='')
        elif intensity < 1020000:
            print('o', end='')
        elif intensity < 1530000:
            print('+', end='')
        elif intensity < 2040000:
            print('-', end='')
        else:
            print('.', end='')
    print()
