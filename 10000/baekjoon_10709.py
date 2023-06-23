h, w = map(int, input().split())
for i in range(h):
    temp = -1
    for j in input():
        if j == 'c':
            temp = 0
        else:
            temp += temp != -1
        print(temp, end=' ')
    print()
