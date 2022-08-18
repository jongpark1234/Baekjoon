while True:
    distance, i = float('inf'), 1
    b, n = map(int, input().split())
    if b == n == 0:
        break
    while True:
        temp = abs(b - i ** n)
        if temp > distance:
            print(i - 1)
            break
        distance = temp
        i += 1
