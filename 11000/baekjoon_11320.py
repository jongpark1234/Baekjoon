for _ in range(int(input())):
    result = 0
    a, b = map(int, input().split())
    for i in range(1, a // b):
        result += i
    print(result * 2 + a // b)
