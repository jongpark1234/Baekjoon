for _ in range(int(input())):
    a, b = 1, 0
    for _ in range(int(input())):
        a, b = b, a + b
    print(a, b)
