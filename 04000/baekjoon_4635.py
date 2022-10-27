while (n := int(input())) != -1:
    temp = result = 0
    for speed, time in [list(map(int, input().split())) for _ in range(n)]:
        temp, result = time, result + speed * (time - temp)
    print(f'{result} miles')
