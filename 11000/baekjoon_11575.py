for _ in range(int(input())):
    a, b = map(int, input().split())
    print(''.join(map(lambda x: chr((a * (ord(x) - 65) + b) % 26 + 65), input())))
