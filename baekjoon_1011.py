for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x
    count = 0; length = 1; totalength = 0
    while totalength < distance:
        count += 1
        totalength += length
        if count % 2 == 0:
            length += 1
    print(count)
